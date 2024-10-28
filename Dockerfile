# Usa una imagen base con Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos a la imagen
COPY requirements.txt /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación a la imagen
COPY ./ /app/poc-bokeh-auth

# authentication cookie secret
ENV BOKEH_COOKIE_SECRET 'avib'

# Expone el puerto que va a utilizar Bokeh
EXPOSE 5006

# Comando para ejecutar el servidor de Bokeh
CMD ["bokeh", "serve", "--auth-module=./poc-bokeh-auth/auth/auth.py", "--allow-websocket-origin=*", "--port", "5006", "--show", "poc-bokeh-auth"]