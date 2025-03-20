from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    msg = f'Hola, Docker pipeline funcionando 🚀, se hace CI automático?'
    new_info = f'Automatic testing deployment'
    return msg + new_info

@app.route('/info')
def info():
    msg = f'Hola, Docker pipeline funcionando 🚀, se hace CI automático'
    return msg
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
