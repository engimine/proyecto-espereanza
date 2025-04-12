# Proyecto Esperanza

Detección de Cáncer de Mama mediante Imágenes Histopatológicas utilizando técnicas de análisis de patrones inspiradas en la ingeniería de minas.

## Descripción

El Proyecto Esperanza es una aplicación web que utiliza inteligencia artificial para detectar cáncer de mama a partir de imágenes histopatológicas. El proyecto nace de la experiencia personal de una ingeniera de minas que aplicó sus conocimientos de mapeo y análisis de minerales al campo médico.

El modelo Esperanza Ultra-Ligero está optimizado para funcionar en entornos con recursos computacionales limitados, alcanzando una precisión del 82.17% y un AUC de 90.35% en la clasificación de imágenes histopatológicas.

## Características

- **Detección Precisa**: El modelo alcanza una precisión del 82.17% y un AUC de 90.35%.
- **Recursos Limitados**: Diseñado para funcionar en entornos con recursos computacionales limitados.
- **Accesibilidad**: Interfaz web intuitiva para médicos sin conocimientos técnicos avanzados.
- **Transferencia de Conocimiento**: Inspirado en técnicas de mapeo de minerales aplicadas al análisis de imágenes médicas.

## Instalación

### Requisitos

- Python 3.10 o superior
- Flask
- TensorFlow 2.8.0
- NumPy
- Matplotlib
- Pillow

### Instalación local

1. Clonar el repositorio:
```
git clone https://github.com/engimine/proyecto-esperanza.git
cd proyecto-esperanza
```

2. Instalar dependencias:
```
pip install -r requirements.txt
```

3. Ejecutar la aplicación:
```
python src/app.py
```

4. Abrir en el navegador:
```
http://localhost:5000
```

### Despliegue en Heroku

Ver instrucciones detalladas en [docs/heroku_deployment.md](docs/heroku_deployment.md).

## Uso

1. Acceder a la aplicación web
2. Subir una imagen histopatológica de tejido mamario
3. Recibir una predicción sobre si el tejido es benigno o maligno
4. Revisar el nivel de confianza y la visualización de resultados

## Estructura del Proyecto

```
proyecto-esperanza/
├── src/                    # Código fuente
│   ├── app.py              # Aplicación Flask principal
│   ├── templates/          # Plantillas HTML
│   └── static/             # Archivos estáticos (CSS, JS, imágenes)
├── models/                 # Modelos entrenados
│   └── esperanza_ultralight_model.h5
├── data/                   # Datos para entrenamiento y pruebas
├── docs/                   # Documentación
│   ├── paper_tecnico.md    # Paper técnico detallado
│   └── historia_personal.md # Historia personal de la autora
├── examples/               # Ejemplos de uso
└── tests/                  # Pruebas unitarias
```

## Historia Personal

Este proyecto nace de la experiencia personal de una ingeniera de minas que aplicó sus conocimientos de mapeo y análisis de minerales al campo médico tras ser diagnosticada con cáncer de mama.

Durante el tratamiento, observó que los patrones en las imágenes histopatológicas no eran tan diferentes de los que había analizado durante años en muestras de minerales. Las estructuras celulares, la distribución de tejidos y las anomalías podían ser "mapeadas" de manera similar a las formaciones geológicas.

Para más detalles, consulte [docs/historia_personal.md](docs/historia_personal.md).

## Detalles Técnicos

El modelo Esperanza Ultra-Ligero utiliza una arquitectura de red neuronal convolucional (CNN) optimizada para funcionar en entornos con recursos limitados. La arquitectura refleja el proceso de análisis de minerales:

1. **Primera capa**: Identificación de patrones básicos (texturas y bordes)
2. **Segunda capa**: Reconocimiento de estructuras más complejas
3. **Tercera capa**: Análisis de regiones completas
4. **Capa densa**: Integración de todas las características
5. **Capa de salida**: Decisión final sobre malignidad

Para más detalles técnicos, consulte [docs/paper_tecnico.md](docs/paper_tecnico.md).

## Contribuir

Las contribuciones son bienvenidas. Por favor, siga estos pasos:

1. Fork del repositorio
2. Crear una rama para su característica (`git checkout -b feature/amazing-feature`)
3. Commit de sus cambios (`git commit -m 'Add some amazing feature'`)
4. Push a la rama (`git push origin feature/amazing-feature`)
5. Abrir un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - vea el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

María Jesús Puerta Angulo - [@engimine](https://github.com/engimine)
mjpaupc@gmail.com
URL del Proyecto: [https://github.com/engimine/proyecto-esperanza](https://github.com/engimine/proyecto-esperanza)


