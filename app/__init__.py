import sqlite3
from flask import Flask, render_template, request, redirect, url_for, abort
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    def get_db_connection():
        conn = sqlite3.connect(app.config['DATABASE_URL'])
        conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por su nombre
        return conn


    # RUTAS 

    # Listar usuarios (GET /users)
    @app.route('/')
    @app.route('/users', methods=['GET'])
    def list_users():
        conn = get_db_connection()
        users = conn.execute('SELECT * FROM users').fetchall()
        conn.close()
        return render_template('users/list.html', users=users)

    # Formulario para nuevo usuario (GET /users/new)
    @app.route('/users/new', methods=['GET'])
    def new_user():
        return render_template('users/create.html')

    # Guardar usuario (POST /users)
    @app.route('/users', methods=['POST'])
    def create_user():
        dni = request.form['dni']
        given_name = request.form['given_name']
        family_name = request.form['family_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        address = request.form['address']

        conn = get_db_connection()
        conn.execute('''
            INSERT INTO users (dni, given_name, family_name, email, phone_number, address)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (dni, given_name, family_name, email, phone_number, address))
        conn.commit()
        conn.close()

        return redirect(url_for('list_users'))

    # Ver un usuario por ID (GET /users/<id>)
    @app.route('/users/<int:id>', methods=['GET'])
    def get_user(id):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchone()
        conn.close()

        if user is None:
            abort(404)

        return render_template('users/detail.html', user=user)

    # Formulario para editar usuario (GET /users/<id>/edit)
    @app.route('/users/<int:id>/edit', methods=['GET'])
    def edit_user(id):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchone()
        conn.close()

        if user is None:
            abort(404)

        return render_template('users/edit.html', user=user)

    # Actualizar usuario (POST /users/<id>)
    @app.route('/users/<int:id>', methods=['POST'])
    def update_user(id):
        dni = request.form['dni']
        given_name = request.form['given_name']
        family_name = request.form['family_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        address = request.form['address']

        conn = get_db_connection()
        conn.execute('''
            UPDATE users
            SET dni = ?, given_name = ?, family_name = ?, email = ?, phone_number = ?, address = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (dni, given_name, family_name, email, phone_number, address, id))
        conn.commit()
        conn.close()

        return redirect(url_for('list_users'))

    # Eliminar usuario (POST /users/<id>/delete)
    @app.route('/users/<int:id>/delete', methods=['POST'])
    def delete_user(id):
        conn = get_db_connection()
        conn.execute('DELETE FROM users WHERE id = ?', (id,))
        conn.commit()
        conn.close()

        return redirect(url_for('list_users'))

    # ENDPOINTS API (JSON) 

    # Endpoint 1: Retorna todos los usuarios en formato JSON
    @app.route('/api/users', methods=['GET'])
    def api_list_users():
        conn = get_db_connection()
        users = conn.execute('SELECT * FROM users').fetchall()
        conn.close()
        return [dict(u) for u in users]

    # Endpoint 2: Buscar usuarios por nombre en JSON (/api/users/search?given_name=Javier)
    @app.route('/api/users/search', methods=['GET'])
    def api_search_users():
        name = request.args.get('given_name', '')
        conn = get_db_connection()
        users = conn.execute('SELECT * FROM users WHERE given_name LIKE ?', (f'%{name}%',)).fetchall()
        conn.close()
        return [dict(u) for u in users]

    # Endpoint 3: Retorna un usuario por ID en JSON
    @app.route('/api/users/<int:id>', methods=['GET'])
    def api_get_user(id):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchone()
        conn.close()
        if user is None:
            return {"error": "Usuario no encontrado"}, 404
        return dict(user)

    # VISTA PARA HTMX 

    @app.route('/search', methods=['GET'])
    def search_page():
        return render_template('search.html')

    return app