# Concert Memories

## Descripción del Proyecto

Concert Memories es una plataforma web dedicada a compartir recuerdos de conciertos musicales. Este proyecto fue creado como parte de la entrega final del curso de Python y nació de mi pasión por la música.

## Funcionalidades

### Crear, Actualizar y Eliminar Posts

Concert Memories permite a los usuarios compartir sus recuerdos de conciertos mediante la creación, actualización y eliminación de posts. Cada post contiene información detallada sobre el concierto, incluyendo:

- **Artista:** Nombre del artista del concierto.
- **Tour:** Nombre del tour o evento.
- **Fecha:** Fecha del concierto.
- **Descripción:** Una rica descripción del recuerdo del concierto.
- **Adjunto:** Posibilidad de adjuntar imágenes relacionadas al concierto.

### Creación y Edición de Usuarios

Los usuarios de Concert Memories pueden registrarse y editar su perfil con la siguiente información:

- **Correo:** Dirección de correo electrónico del usuario.
- **Nombre:** Nombre del usuario.
- **Apellido:** Apellido del usuario.
- **Biografía:** Una breve biografía o descripción del usuario.
- **Avatar:** Imagen de perfil del usuario.

Estos detalles permiten a los usuarios personalizar su experiencia en la plataforma y compartir sus recuerdos de conciertos de manera única.

**Nota:** Para obtener instrucciones detalladas sobre cómo instalar y ejecutar Concert Memories, consulta la sección de [Instalación](#instalación) en este README.

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tuusuario/concert-memories.git
    cd concert-memories
    ```

2. Configura el entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # o venv\Scripts\activate en Windows
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones:

    ```bash
    python manage.py migrate
    ```

5. Ejecuta el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

6. Abre tu navegador y accede a [http://localhost:8000/](http://localhost:8000/).

## Contribuciones

¡Las contribuciones son bienvenidas! Si quieres mejorar Concert Memories, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama: `git checkout -b feature/nueva-caracteristica`.
3. Realiza tus cambios y haz commit: `git commit -m 'Añade nueva característica'`.
4. Haz push a la rama: `git push origin feature/nueva-caracteristica`.
5. Abre un pull request.
