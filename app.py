ffrom flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    show_thanks = False

    if __import__("flask").request.method == "POST":
        show_thanks = True

    return f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Мой сайт</title>

        <style>
            body {{
                text-align: center;
                font-family: Arial, sans-serif;
                padding-top: 80px;
            }}

            button {{
                font-size: 20px;
                padding: 15px 30px;
                cursor: pointer;
                border-radius: 10px;
                border: none;
            }}

            .heart {{
                font-size: 180px;
                margin-top: 30px;
            }}

            .text {{
                font-size: 50px;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>

        <h1>Привет всем моим друзьям и родителям! ❤️</h1>

        <p>Рад видеть вас на моём сайте!</p>

        <form method="POST">
            <button type="submit">Нажми меня</button>
        </form>

        {"<div class='heart'>❤️</div><div class='text'>Спасибо!</div>" if show_thanks else ""}

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)