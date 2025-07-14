# Imagen base
FROM python:3.10

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expone el puerto
EXPOSE 8000

# Comando por defecto
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
