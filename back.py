from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

usuarios = [
    {"id": 1, "nombre": "Carlos", "cursos": ["Matemáticas Básicas", "Álgebra", "Cálculo I", "Estadística", "Geometría", "Matemáticas Financieras"]},
    {"id": 2, "nombre": "Ana", "cursos": ["Historia Moderna", "Filosofía", "Historia del Arte", "Lógica Formal", "Antropología", "Economía Política"]}
]

cursos_disponibles = [
    {"nombre": "Matemáticas Avanzadas", "categoria": "Matemáticas"},
    {"nombre": "Álgebra Lineal", "categoria": "Matemáticas"},
    {"nombre": "Historia del Arte", "categoria": "Historia"},
    {"nombre": "Lógica y Argumentación", "categoria": "Filosofía"},
    {"nombre": "Cálculo II", "categoria": "Matemáticas"},
    {"nombre": "Ciencias Sociales", "categoria": "Historia"},
    {"nombre": "Filosofía Contemporánea", "categoria": "Filosofía"},
    {"nombre": "Física General", "categoria": "Ciencias"},
    {"nombre": "Introducción a la Psicología", "categoria": "Ciencias Sociales"},
    {"nombre": "Estrategias de Aprendizaje", "categoria": "Educación"},
    {"nombre": "Economía", "categoria": "Ciencias Sociales"},
    {"nombre": "Estudios Literarios", "categoria": "Literatura"},
    {"nombre": "Geometría Analítica", "categoria": "Matemáticas"},
    {"nombre": "Geografía Humana", "categoria": "Historia"},
    {"nombre": "Introducción a la Sociología", "categoria": "Ciencias Sociales"},
    {"nombre": "Inteligencia Artificial", "categoria": "Informática"},
    {"nombre": "Programación Avanzada", "categoria": "Informática"},
    {"nombre": "Estudios de Género", "categoria": "Ciencias Sociales"},
    {"nombre": "Mecánica Cuántica", "categoria": "Ciencias"},
    {"nombre": "Economía Global", "categoria": "Ciencias Sociales"},
    {"nombre": "Teoría de Juegos", "categoria": "Matemáticas"},
    {"nombre": "Algebra Abstracta", "categoria": "Matemáticas"},
    {"nombre": "Cultura Contemporánea", "categoria": "Historia"},
    {"nombre": "Sociología Urbana", "categoria": "Ciencias Sociales"},
    {"nombre": "Matemáticas Financieras", "categoria": "Matemáticas"}
]

cursosApuntados = {
    "Matemáticas Básicas": "Matemáticas",
    "Álgebra": "Matemáticas",
    "Cálculo I": "Matemáticas",
    "Estadística": "Matemáticas",
    "Geometría": "Matemáticas",
    "Historia Moderna": "Historia",
    "Filosofía": "Filosofía",
    "Historia del Arte": "Historia",
    "Lógica Formal": "Filosofía",
    "Antropología": "Ciencias Sociales",
    "Matemáticas Financieras": "Matemáticas",
    "Economía Política": "Ciencias Sociales"
}

def recomendar_cursos(usuario_id):
    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)
    if not usuario:
        return []
    
    cursosApuntados_usuario = {cursosApuntados[curso] for curso in usuario["cursos"] if curso in cursosApuntados}
    recomendaciones = [curso for curso in cursos_disponibles if curso["categoria"] in cursosApuntados_usuario]
    
    return recomendaciones[:6]

@app.route('/recomendaciones/<int:usuario_id>', methods=['GET'])
def obtener_recomendaciones(usuario_id):
    recomendaciones = recomendar_cursos(usuario_id)
    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)
    return render_template("recomendaciones.html", usuario_id=usuario_id, recomendaciones=recomendaciones, cursos_apuntados=usuario["cursos"])

if __name__ == '__main__':
    app.run(debug=True)