from flask_app import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5000,debug=True)

    if __name__ == '__main__':
        app.run(port=5000, debug=True)

@app.route('/')
def home():
    return"Welkom op mijn eerste Website met framework Flask ;)"