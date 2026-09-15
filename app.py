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

        <style>
            body {
                text-align: center;
                font-family: Arial, sans-serif;
                padding-top: 100px;
            }

            button {
                font-size: 20px;
                padding: 15px 30px;
                cursor: pointer;
                border-radius: 10px;
                border: none;
            }

            #thanks {
                display: none;
                margin-top: 40px;
            }

            .heart {
                font-size: 180px;
            }

            .text {
                font-size: 50px;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <h1>Привет всем моим друзьям и родителям! ❤️</h1>

        <p>Рад видеть вас на моём сайте!</p>

        <button onclick="showThanks()">Нажми меня</button>

        <div id="thanks">
            <div class="heart">❤️</div>
            <div class="text">Спасибо!</div>
        </div>

        <script>
            function showThanks() {
                document.getElementById("thanks").style.display = "block";
            }
        </script>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)