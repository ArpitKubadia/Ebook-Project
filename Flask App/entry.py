from flask import Flask, render_template, flash, redirect, request, session, abort

app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True

@app.route("/")
def hello():
    return render_template('input.html')


if __name__ == "__main__":
    app.run()