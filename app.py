# app.py
from flask import Flask
import os

from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, mundo! Este es mi primer servidor con Flask.'

if __name__ == '__main__':
    app.run(debug=False, port=os.getenv('PORT', 5000))
