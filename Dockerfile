# Imagen base
FROM python:3.10

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos al contenedor
COPY . /app

# Instala dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expone el puerto dinámico (aunque Render no lo use directamente)
EXPOSE 8000

# Comando que Render puede usar
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:$PORT"]
