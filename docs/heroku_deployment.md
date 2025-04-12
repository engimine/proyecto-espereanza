# Despliegue en Heroku

Este documento proporciona instrucciones detalladas para desplegar el Proyecto Esperanza en Heroku, permitiendo que la aplicación funcione con el modelo completo para predicciones reales.

## Requisitos previos

1. Crear una cuenta en [Heroku](https://signup.heroku.com/)
2. Instalar [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
3. Tener [Git](https://git-scm.com/downloads) instalado en tu ordenador

## Instrucciones de despliegue

### 1. Preparar el entorno local

Primero, clona el repositorio y navega al directorio del proyecto:

```bash
git clone https://github.com/engimine/proyecto-esperanza.git
cd proyecto-esperanza
```

### 2. Iniciar sesión en Heroku

Abre una terminal o línea de comandos y ejecuta:

```bash
heroku login
```

Sigue las instrucciones para completar el inicio de sesión.

### 3. Crear una nueva aplicación en Heroku

```bash
heroku create proyecto-esperanza
```

Si el nombre "proyecto-esperanza" no está disponible, elige otro nombre.

### 4. Configurar el buildpack de Python

```bash
heroku buildpacks:set heroku/python
```

### 5. Desplegar la aplicación

```bash
git push heroku main
```

Si tu rama principal se llama "master" en lugar de "main", usa:

```bash
git push heroku master
```

### 6. Abrir la aplicación

Una vez completado el despliegue, abre la aplicación en tu navegador:

```bash
heroku open
```

## Solución de problemas comunes

### Error: "No web process running"

Si recibes este error, necesitas configurar un dyno web:

```bash
heroku ps:scale web=1
```

### Error al cargar el modelo

Si la aplicación se despliega pero no puede cargar el modelo, verifica que el archivo del modelo esté correctamente incluido en el repositorio y que la ruta en `app.py` sea correcta.

### Límites de memoria

Heroku tiene límites de memoria para las aplicaciones gratuitas. Si la aplicación falla debido a límites de memoria, considera:

1. Usar un modelo más ligero
2. Actualizar a un plan de Heroku con más recursos
3. Optimizar el código para reducir el uso de memoria

## Monitoreo y mantenimiento

### Ver logs

Para ver los logs de la aplicación:

```bash
heroku logs --tail
```

### Reiniciar la aplicación

Si necesitas reiniciar la aplicación:

```bash
heroku restart
```

### Actualizar la aplicación

Para actualizar la aplicación después de realizar cambios:

1. Haz commit de tus cambios locales
2. Ejecuta `git push heroku main` (o `master`)

## Consideraciones adicionales

### Dyno sleeping

En el plan gratuito de Heroku, los dynos "duermen" después de 30 minutos de inactividad. La primera solicitud después de este período puede ser lenta mientras el dyno se "despierta".

### Almacenamiento de archivos

Heroku tiene un sistema de archivos efímero, lo que significa que los archivos subidos a la aplicación no persistirán después de un reinicio. Para almacenamiento permanente, considera usar servicios como AWS S3 o Cloudinary.

### Variables de entorno

Para configurar variables de entorno (como claves API o configuraciones):

```bash
heroku config:set NOMBRE_VARIABLE=valor
```

## Recursos adicionales

- [Documentación oficial de Heroku para Python](https://devcenter.heroku.com/categories/python-support)
- [Guía de despliegue de Flask en Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)
- [Solución de problemas en Heroku](https://devcenter.heroku.com/categories/troubleshooting)
