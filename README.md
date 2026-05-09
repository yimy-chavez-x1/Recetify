### Recetify API Rest - Full Stack

API REST desarrollada con Flask que permite gestionar recetas mediante operaciones CRUD, con autenticación basada en JWT.
Incluye backend modularizado y frontend en HTML, CSS y JavaScript.

### CARACTERISTICAS
```
- CRUD completo de recetas
- Autenticación con JWT
- Base de datos SQLite
- Arquitectura modular 
- Historial de cambios 
- Frontend HTML, JS, CSS
```
### TECNOLOGIAS
```
Backend: Python con flask,SQLite y JWT
Frontend: HTML, CSS y JS
Otros: Cors, Fetch API
```
## Estructura del proyecto
```
git 
RECETIFY/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── auth.py
│   │   └── recetas.py
│   ├── auth.py
│   ├── models.py
│   └── utils.py
├── data/
│   └── historial.json
├── static/
│   ├── crear.js
│   ├── crear.css
│   ├── editar.js
│   ├── editar.css
│   ├── eliminar.js
│   ├── eliminar.css
│   ├── ver.js
│   ├── ver.css
│   ├── home.js
│   ├── home.css
│   ├── index.js
│   └── index.css
├── templates/
│   ├── crear_receta.html
│   ├── editar_receta.html
│   ├── eliminar_receta.html
│   ├── ver_receta.html
│   ├── home.html
│   └── index.html
├── assets/
│   ├── png_crear.png
│   ├── png_editar.png
│   ├── png_eliminar.png
│   ├── png_home.png
│   ├── png_register.png
│   └── png_ver.png
├── recetas.db
├── requirements.txt
├── run.py
├── README.md
└── .gitignore
```
### Deploy web
```
en render (https://recetify-urcf.onrender.com/)
```
###  Metodo de instalación

Clonar Repositorio
```bash
git clone https://github.com/yimy-chavez-x1/Recetify
cd Recetify
```
Crear un entorno virtual
```bash
  python -m venv .venv
```

Activar entorno virtual
  Linux/Mac:  
  ```bash
    source .venv/bin/activate
  ```
  windows:
  ```bash
    .venv\Scripts\activate
  ```

Instalar dependencias
  ```bash
  pip install -r requirements.txt
  ```

Levantar el server
  ```bash
  python run.py
  ```
La aplicación estará disponible en http://127.0.0.1:5000


### Capturas de pantalla

### Registro de usuario
![Registro](assets/png_register.png)

### Página principal
![Home](assets/png_home.png)

### Crear receta
![Crear receta](assets/png_crear.png)

### Editar receta
![Editar receta](assets/png_editar.png)

### Eliminar receta
![Eliminar receta](assets/png_eliminar.png)

### Ver recetas
![Ver recetas](assets/png_ver.png)
