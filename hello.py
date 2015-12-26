from flask import Flask
app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_PORT','localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT','5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
