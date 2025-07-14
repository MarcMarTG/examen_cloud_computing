# Imagen base
FROM python:3.10

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos al contenedor
COPY . /app

# Instala dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expone el puerto dinámico (Render asigna el puerto en runtime)
EXPOSE 8000

# Comando que hace makemigrations, migrate y runserver
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT"]
