# Proyecto Django APP

## 📁 Repositorio de GitHub  
https://github.com/MarcMarTG/examen_cloud_computing.git

## 👥 Integrantes  
- Marcos Alejandro Martínez Gaona  
- Dieter Ariel Pastoriza Marecos  

## 🌐 Enlace de Acceso al Sistema  
https://examen-cloud-computing.onrender.com/

---

## ✅ Tareas Realizadas  

| Integrantes        | Tareas Realizadas |
|--------------------|-------------------|
| **Marcos Martínez** | Levantamiento del proyecto base a GitHub, modificaciones funcionales en los módulos: crear proyecto, proyecto, crear tareas y tareas. Encargado del Tablero de Trello. |
| **Dieter Pastoriza** | Modificaciones visuales a todos los módulos del proyecto, creación de archivo `DockerCompose` y `DockerFile`, despliegue del sistema en hosting Render.com. |

---

## 📌 Enlace a Trello  
https://trello.com/invite/b/68746d7a27fa929fd9d869da/ATTI77aeec143f6827702d409e7e90bdc0abE1A743B4/examen-cloud-computing

## 🎥 Enlace al video de Presentación del Sistema  
https://drive.google.com/file/d/1L2Y5Yt1wFcjOpY5hOzuHYKugnnXSxGER/view?usp=sharing

---

## 📝 Descripción del Proyecto  

Se trata de un proyecto web desarrollado para gestionar eficientemente tareas y proyectos, permitiendo a los usuarios crear, editar, eliminar y visualizar tanto proyectos como sus tareas asociadas. La aplicación ofrece una interfaz intuitiva que facilita el seguimiento del progreso, la organización de actividades y el control de fechas importantes, mejorando así la productividad y la planificación del trabajo.

---

## ⚙️ Tecnologías Utilizadas  

- Python – Django  
- HTML  
- CSS  
- Bootstrap  
- Docker  

---

## 🛠️ Requerimientos, Instalación Local y Configuración

### • Instalación de Visual Studio Code y la extensión de Python  
Es necesario contar con el editor de código Visual Studio Code (VSCode) y la extensión de Python instalada para facilitar el desarrollo.

### • Instalación de Python  
Descarga e instala la última versión de Python desde su sitio oficial. Para verificar que la instalación fue exitosa, abre la terminal o consola (CMD) y ejecuta el siguiente comando:

```bash
python --version
```

### • Verificación o instalación de pip  
Asegúrate de tener instalado pip, el gestor de paquetes de Python. Puedes verificarlo con:

```bash
pip --version
```

Si no está instalado, puedes instalarlo con:

```bash
python -m ensurepip --upgrade
```

### • Instalación de Django  
Una vez tengas pip, instala Django con el siguiente comando:

```bash
pip install django
```

Para comprobar que Django se instaló correctamente, ejecuta:

```bash
django-admin --version
```

### • Ejecución del proyecto localmente  
Clonar el Repositorio git seleccionando la ruta donde desees que se guarde el proyecto

```bash
git clone https://github.com/MarcMarTG/examen_cloud_computing.git
```

Para correr el servidor de desarrollo de Django y visualizar el proyecto en tu navegador, ejecuta el siguiente comando dentro del directorio raíz del proyecto:

```bash
python manage.py runserver
```

Y luego seleccionas el link del localhost que te proveera en la terminal 

### • Solución de posibles incompatibilidades  
Si el proyecto fue clonado desde un repositorio y presenta errores relacionados con la base de datos, se recomienda eliminar el archivo de la base de datos SQLite existente y luego regenerar las migraciones con los siguientes comandos:

```bash
python manage.py makemigrations  
python manage.py migrate
```

### • Visualización de la base de datos  
Si deseas explorar visualmente la base de datos SQLite, puedes utilizar **DB Browser for SQLite**. El instalador se encuentra incluido en el repositorio o también puedes descargarlo desde su sitio oficial.

---

## 🗂️ Estructura del Proyecto  

- `myapp/`: Controladores, modelos, formularios, vistas y lógica de negocio de la aplicación principal.  
- `myapp/migrations/`: Migraciones de la base de datos, encargadas de reflejar los cambios en los modelos.  
- `myapp/templates/`: Vistas HTML utilizadas por Django para renderizar el contenido al usuario.  
- `myapp/templates/layouts/`: Plantillas base que estructuran el diseño común entre vistas.  
- `myapp/templates/projects/`: Vistas específicas para la gestión de proyectos (crear, editar, listar, etc.).  
- `myapp/templates/tasks/`: Vistas específicas para la gestión de tareas.  
- `myapp/static/`: Archivos públicos como imágenes, hojas de estilo o scripts (equivalente a la carpeta `public/`).  
- `mysite/`: Archivos de configuración general del proyecto Django (equivalente a `config/`).  
- `myapp/urls.py`: Archivo donde se definen las rutas web de la aplicación (equivalente a `routes/web.php`).  
- `manage.py`: Script principal para ejecutar comandos del proyecto, como iniciar el servidor o aplicar migraciones.  
- `requirements.txt`: Archivo que define las dependencias del proyecto.  
- `Dockerfile / docker-compose.yml`: Archivos de configuración para el despliegue y contenedorización del proyecto.  

---

## 🚀 Despliegue  

El proyecto está desplegado en **Render** usando **Docker**.  
Cada commit en la rama `main` ejecuta un despliegue automatizado.

---

## 🖥️ Capturas del Despliegue 

- Build Logs  
  ![1](https://github.com/user-attachments/assets/ca0ad1d7-3ee8-4bf8-9d74-db3b2a1890ba)

- Application Logs  
  ![2](https://github.com/user-attachments/assets/63d0bf60-b879-4e01-86e1-803f43a2fd88)

- Historial de Despliegue  
  ![3](https://github.com/user-attachments/assets/0b003f8c-f58c-4239-ac6a-36f3baccc8e5)

