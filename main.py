from flask import Flask, request
from flask.scaffold import F
from flask_cors import CORS
import Login



app = Flask(__name__)
CORS(app)

@app.route("/logar", methods=['POST'])
def logar_repository():
    try:
        usuario = request.json
        resultado = Login.verificacao(usuario['EMAIL'],usuario['SENHA'])

        return resultado
    except Exception as e:
       return str(e)

@app.route("/deluser", methods=['POST'])
def del_user_repository():
    try:
        usuario = request.json
        resultado = Login.deletar(usuario['EMAIL'],usuario['SENHA'])

        return resultado
    except Exception as e:
       return str(e)

@app.route("/salvaruser", methods=['POST'])
def salvar_user_repository():
    try:
        usuario = request.json
        resultado = Login.salvar(usuario['EMAIL'],usuario['SENHA'])

        return resultado
    except Exception as e:
        return str(e)

if __name__=="__main__":
    app.run()