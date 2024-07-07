from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_cors import CORS
from libro import Libro
from libro import DB_CONFIG

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/form')
def principal():
    return render_template("form.html")

@app.route('/libros', methods=["GET", "POST"])
def libros_endpoint():
    """Recupera o añade libros"""
    
    if request.method == "GET":
        libros = Libro.get_all()
        libros_list = []
        for libro in libros:
            libro_dict = {
                "id_libros": libro["id_libros"],
                "nombre_libro": libro["nombre_libro"],
                "autor": libro["autor"],
                "precio": libro["precio"],
                "genero": libro["genero"],
                "imagen": libro["imagen"],
            }
            libros_list.append(libro_dict)
        
        return jsonify(libros_list)
    elif  request.method == "POST": 
        data = request.get_json()
        print("Datos recibidos:", data)
        new_libro = Libro(
            nombre_libro=data.get("nombre_libro"),
            autor=data.get("autor"),
            precio=data.get("precio"),
            genero=data.get("genero"),
            imagen=data.get("imagen")
        )
        new_libro.save()
        new_libro_dict = {
            "id_libros": new_libro.id_libros,
            "nombre_libro": new_libro.nombre_libro,
            "autor": new_libro.autor,
            "precio": new_libro.precio,
            "genero": new_libro.genero,
            "imagen": new_libro.imagen,
        }
        
        return jsonify(new_libro_dict), 201
    else:
        return jsonify({"Error": "no se ha podido realizar la acción"}), 404
    
@app.route('/libros/<int:id_libros>', methods=["GET", "PUT", "PATCH", "DELETE"])
def id_libros_endpoint(id_libros):
    if request.method == "GET":
        libro = Libro.get_by_id(id_libros)
        if libro:
            libro_dict = {
                "id_libros": libro.id_libros,
                "nombre_libro": libro.nombre_libro,
                "autor": libro.autor,
                "precio": libro.precio,
                "genero": libro.genero,
                "imagen": libro.imagen
            }
            return jsonify(libro_dict)
        else:
            return jsonify({"error": "Libro no encontrado"}), 404
    
    if request.method == "PUT":
        data = request.get_json()
        libro = Libro.get_by_id(id_libros)
        if libro:
            libro.nombre_libro = data.get("nombre_libro", libro.nombre_libro)
            libro.autor = data.get("autor", libro.autor)
            libro.precio = data.get("precio", libro.precio)
            libro.genero = data.get("genero", libro.genero)
            libro.imagen = data.get("imagen", libro.imagen)
            libro.save()
            
            libro_dict = {
                "id_libros": libro.id_libros,
                "nombre_libro": libro.nombre_libro,
                "autor": libro.autor,
                "precio": libro.precio,
                "genero": libro.genero,
                "imagen": libro.imagen
            }
            return jsonify(libro_dict)
        else:
            return jsonify({"error": "Libro no encontrado"}), 404
        
    if request.method == "PATCH":
        data = request.get_json()
        libro = Libro.get_by_id(id_libros)
        if libro:
            if "nombre_libro" in data:
                libro.nombre_libro = data["nombre_libro"]
            if "autor" in data:
                libro.autor = data["autor"]
            if "precio" in data:
                libro.precio = data["precio"]
            if "genero" in data:
                libro.genero = data["genero"]
            if "imagen" in data:
                libro.imagen = data["imagen"]
            libro.save()
            return jsonify({"message": "Libro actualizado correctamente"})
        return jsonify({"error": "Libro no encontrado"}), 404         
    
    if request.method == "DELETE":
        libro = Libro.get_by_id(id_libros)
        if libro:
            libro.delete(id_libros)
            return jsonify({"message": "Libro eliminado"}), 200
        else:
            return jsonify({"error": "Libro no encontrado"}), 404
        
        
if __name__ == '__main__':
    app.run(debug=True)
