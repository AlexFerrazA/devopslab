from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "MBA IMPACTA FULL DEVOPS NA VEIA"

if __name__ == '__main__':
    app.run(debug=True)
