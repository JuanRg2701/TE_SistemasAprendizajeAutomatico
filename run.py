from waitress import serve
from back import app

print("Iniciando el servidor...")

serve(app, host="0.0.0.0", port=5000)