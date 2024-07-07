from flask import Flask, jsonify, request, send_file
from psycopg2 import connect, extras
import os

app = Flask(__name__)


def get_connection():

    if os.environ.get("DATABASE_URL", None):
        print(os.environ.get("DATABASE_URL"))
        return connect(os.environ.get("DATABASE_URL"))

    return connect(
        host=os.environ.get("DB_HOST", "localhost"),
        port=int(os.environ.get("DB_PORT", "5432")),
        database=os.environ.get("DB_NAME", "cac_app"),
        user=os.environ.get("DB_USER", "cac_app"),
        password=os.environ.get("DB_PASSWORD", "password"),
    )


@app.get("/api/books")
def get_books():

    # conectar a la bbdd
    conn = get_connection()
    # crear un cursor -- se encarga de ejecutar las queries
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)

    # ejecutar la query para obtener registros
    cursor.execute("SELECT * FROM libros")
    books = cursor.fetchall()

    # cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    # retornar los resultados
    return jsonify(books)


@app.post("/api/books")
def create_book():

    book_data = request.get_json()

    # conectar a la bbdd
    conn = get_connection()
    # crear un cursor -- se encarga de ejecutar las queries
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)

    # ejecutar la query para obtener registros
    # OJO CON ESTO, CREO QUE TIENE QUE COINCIDIR CON LO DE JS, OJOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    query = """
    INSERT INTO libros (author_id, description, language, name, rating, release_date)
    VALUES (%s, %s, %s, %s, %s, %s)
    RETURNING *
    """
    cursor.execute(
        query=query,
        vars=(
            book_data["author_id"],
            book_data["description"],
            book_data["language"],
            book_data["name"],
            book_data["rating"],
            book_data["release_date"],
        ),
    )
    book = cursor.fetchone()
    conn.commit()

    # cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    if book is None:
        return jsonify({"message": "Libro no creado"}), 400

    # retornar los resultados
    return jsonify(book), 201


@app.get("/api/books/<book_id>")
def get_book(book_id):
    # conectar a la bbdd
    conn = get_connection()
    # crear un cursor -- se encarga de ejecutar las queries
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)

    # ejecutar la query para obtener registros
    cursor.execute(
        query="SELECT * FROM libros WHERE book_id = %s", vars=(book_id,)
    )
    book = cursor.fetchone()
    # cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    if book is None:
        return jsonify({"message": "Libro no encontrado"}), 404

    # retornar los resultados
    return jsonify(book)


@app.delete("/api/books/<book_id>")
def delete_book(book_id):
    # conectar a la bbdd
    conn = get_connection()
    # crear un cursor -- se encarga de ejecutar las queries
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)

    # ejecutar la query para obtener registros
    cursor.execute(
        query="DELETE FROM books WHERE book_id = %s RETURNING *",
        vars=(book_id,),
    )
    book = cursor.fetchone()
    conn.commit()
    # cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    if book is None:
        return jsonify({"message": "Libro no encontrado"}), 404

    # retornar los resultados
    return jsonify(book)


# OJO ACAAAA VEEEEEER ESTE PATCH. BORRAR ESTA LÍNEA PERO NO EL ESPACIO, O SEA, DOS RENGLONES. VER ESTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# PUT / PATCH
@app.patch("/api/books/<book_id>")
def update_book(book_id):
    return {"title": "Spiderman 2", "year": 2002, "id": book_id}


@app.put("/api/books/<book_id>")
def update_book_put(book_id):

    book_data = request.get_json()

    # conectar a la bbdd
    conn = get_connection()
    # crear un cursor -- se encarga de ejecutar las queries
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)

    # ejecutar la query para obtener registros
    query = """
    UPDATE books
    SET
        author_id = %s,
        description = %s,
        language = %s,
        name = %s,
        rating = %s,
        release_date = %s
    WHERE book_id = %s
    RETURNING *
    """
    cursor.execute(
        query=query,
        vars=(
            book_data["author_id"],
            book_data["description"],
            book_data["language"],
            book_data["name"],
            book_data["rating"],
            book_data["release_date"],
            book_id,
        ),
    )
    book = cursor.fetchone()
    conn.commit()

    # cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    if book is None:
        return jsonify({"message": "Libro no encontrado"}), 404

    # retornar los resultados
    return jsonify(book)


@app.get("/")
def home():
    return send_file("static/productos-responsive.html")

@app.get("/nosotros")
def nosotros():
    return send_file("static/nosotros-responsive.html")

# TODO: ver esto!
# VER ESTO QUE SIGUE TAMBIEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEN
@app.route("/images", methods=["GET", "POST"])
def images():

    if request.method == "GET":
        return send_file("static/images.html")

    if request.method == "POST":
        # file = request.files["image"]
        # request.form.get("name")
        # file.save(f'static/uploads/{file.name}.{file.filename.split(".")[-1]}')
        # return jsonify({"message": "ok"}), 200

        data = request.form.get("image")
        return {"image": data}


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
