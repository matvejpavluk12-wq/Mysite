from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Мой сайт</title>
    </head>

    <body>

        <h1>Привет всем моим друзьям и родителям! ❤️</h1>

        <p>Рад видеть вас на моём сайте!</p>

        <button>Нажми меня</button>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)