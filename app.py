from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/listar_archivos', methods=['GET', 'POST'])
def listar_archivos():
    if request.method == 'POST':
        directorio = request.form.get('directorio', '')

        if os.path.exists(directorio):
            archivos = obtener_archivos_texto(directorio)
            print(f"Archivos encontrados: {archivos}")  # Imprime la lista en la consola para depurar
            return render_template('listar_archivos.html', archivos=archivos)

    return render_template('listar_archivos.html')

def obtener_archivos_texto(directorio):
    archivos = [archivo for archivo in os.listdir(directorio) if archivo.endswith('.docx')]
    return archivos

if __name__ == '__main__':
    app.run(debug=True, port=8080)
