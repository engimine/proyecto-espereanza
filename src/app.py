"""
Aplicación web para el Proyecto Esperanza
Detección de Cáncer de Mama mediante Imágenes Histopatológicas
Autora: María Jesús Puerta Angulo
"""

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from flask import Flask, render_template, request, jsonify, url_for, redirect, flash
from werkzeug.utils import secure_filename
import uuid
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
from PIL import Image

# Configuración de la aplicación
app = Flask(__name__)
app.secret_key = 'esperanza_project_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Asegurar que el directorio de uploads existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configuración del modelo
MODEL_PATH = 'model/esperanza_ultralight_model.h5'
IMG_SIZE = 64  # Tamaño de imagen que espera el modelo

# Cargar el modelo si existe
model = None
if os.path.exists(MODEL_PATH):
    try:
        model = load_model(MODEL_PATH)
        print("Modelo cargado exitosamente")
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
else:
    print(f"Modelo no encontrado en {MODEL_PATH}")
    print("La aplicación funcionará en modo demo")

def allowed_file(filename):
    """Verifica si el archivo tiene una extensión permitida"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def preprocess_image(image_path):
    """Preprocesa la imagen para el modelo"""
    img = load_img(image_path, target_size=(IMG_SIZE, IMG_SIZE))
    img_array = img_to_array(img)
    img_array = img_array / 255.0  # Normalización
    img_array = np.expand_dims(img_array, axis=0)  # Añadir dimensión de lote
    return img_array

def generate_prediction_visualization(image_path, prediction, probability):
    """Genera visualización de la predicción"""
    # Cargar imagen original
    img = Image.open(image_path)
    img = img.resize((300, 300))
    
    # Crear figura
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Mostrar imagen
    ax.imshow(img)
    ax.axis('off')
    
    # Añadir título con predicción
    result_text = "MALIGNO" if prediction > 0.5 else "BENIGNO"
    confidence = probability if prediction > 0.5 else 1 - probability
    title = f"Predicción: {result_text} (Confianza: {confidence:.2%})"
    ax.set_title(title, fontsize=14, color='red' if prediction > 0.5 else 'green')
    
    # Guardar figura en memoria
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Convertir a base64 para mostrar en HTML
    img_str = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    
    return img_str

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html', model_loaded=(model is not None))

@app.route('/about')
def about():
    """Página sobre el proyecto"""
    return render_template('about.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Maneja la subida de archivos y realiza predicciones"""
    if 'file' not in request.files:
        flash('No se seleccionó ningún archivo')
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No se seleccionó ningún archivo')
        return redirect(url_for('index'))
    
    if file and allowed_file(file.filename):
        # Generar nombre único para el archivo
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        
        # Guardar archivo
        file.save(file_path)
        
        # Realizar predicción si el modelo está cargado
        if model is not None:
            try:
                # Preprocesar imagen
                processed_img = preprocess_image(file_path)
                
                # Realizar predicción
                prediction = model.predict(processed_img)[0][0]
                
                # Generar visualización
                img_b64 = generate_prediction_visualization(file_path, prediction, prediction)
                
                # Determinar resultado
                result = "Maligno" if prediction > 0.5 else "Benigno"
                confidence = prediction if prediction > 0.5 else 1 - prediction
                
                return render_template('result.html', 
                                      result=result,
                                      confidence=confidence * 100,
                                      image_b64=img_b64,
                                      is_malignant=(prediction > 0.5))
            except Exception as e:
                flash(f'Error al procesar la imagen: {str(e)}')
                return redirect(url_for('index'))
        else:
            # Modo demo - generar resultado aleatorio
            import random
            prediction = random.random()
            result = "Maligno" if prediction > 0.5 else "Benigno"
            confidence = prediction if prediction > 0.5 else 1 - prediction
            
            # Generar visualización demo
            img_b64 = generate_prediction_visualization(file_path, prediction, prediction)
            
            flash('Modo demo: El modelo no está cargado. Mostrando resultado aleatorio.')
            return render_template('result.html', 
                                  result=result,
                                  confidence=confidence * 100,
                                  image_b64=img_b64,
                                  is_malignant=(prediction > 0.5),
                                  demo_mode=True)
    
    flash('Tipo de archivo no permitido')
    return redirect(url_for('index'))

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API para predicciones (para integración con otros sistemas)"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        # Generar nombre único para el archivo
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        
        # Guardar archivo
        file.save(file_path)
        
        # Realizar predicción si el modelo está cargado
        if model is not None:
            try:
                # Preprocesar imagen
                processed_img = preprocess_image(file_path)
                
                # Realizar predicción
                prediction = float(model.predict(processed_img)[0][0])
                
                # Determinar resultado
                result = "malignant" if prediction > 0.5 else "benign"
                confidence = prediction if prediction > 0.5 else 1 - prediction
                
                return jsonify({
                    'prediction': result,
                    'confidence': float(confidence),
                    'raw_score': float(prediction)
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        else:
            # Modo demo
            import random
            prediction = random.random()
            result = "malignant" if prediction > 0.5 else "benign"
            confidence = prediction if prediction > 0.5 else 1 - prediction
            
            return jsonify({
                'prediction': result,
                'confidence': float(confidence),
                'raw_score': float(prediction),
                'demo_mode': True
            })
    
    return jsonify({'error': 'File type not allowed'}), 400

# Configuración para Heroku
port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    # Crear directorio para el modelo si no existe
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    
    # Iniciar la aplicación
    app.run(host='0.0.0.0', port=port, debug=False)
