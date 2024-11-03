# Usa una imagen base con Python
FROM python:3.13-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /poc-bokeh-auth

# Copia el archivo de requerimientos a la imagen
COPY requirements.txt /poc-bokeh-auth

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación a la imagen
COPY ./ /poc-bokeh-auth

# Expone el puerto que va a utilizar Bokeh
EXPOSE 5006

# Comando para ejecutar el servidor de Bokeh
CMD ["python", "bootstrap.py"]