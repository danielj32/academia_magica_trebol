# La  Academia de  Trébol Mágica

## Descripción
Este proyecto es una API para gestionar solicitudes de estudiantes y la asignación de Grimorios en la academia de magia del Reino del Trébol.
utiliza Flask, sqlite,

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd academia_magica_trebol
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python3.9 -m venv venv
    source venv/bin/activate  # En Windows usa: venv\Scripts\activate
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Crea la base de datos:
    ```sh
    python
    >>> from app import db
    >>> db.create_all()
    >>> exit()
    ```

## Uso

Para iniciar el servidor:
```sh
flask run

