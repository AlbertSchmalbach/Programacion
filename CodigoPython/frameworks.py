from flask import Flask, render_template

# Crear una instancia del aplicacion.
app = Flask(__name__)

# Definir una ruta y una funcion de vista.
@app.route('/')
def index():
    return 'Hola Mundo desde flask'

# Iniciar la aplicacion.
if __name__ == '__main__':
    app.run()