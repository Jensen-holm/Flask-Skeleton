from flask import Flask, render_template
from datetime import datetime


app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/")
@app.route("/index")
def main() -> str:
    return render_template(
        "index.html",
        date=datetime.now()
    )


if __name__ == "__main__":
    app.run(debug=True)
