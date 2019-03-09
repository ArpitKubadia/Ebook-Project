from flask import Flask, render_template, flash, redirect, request, session, abort
import libgensearch

app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True

@app.route("/")
def hello():
    return render_template('input.html')


@app.route('/search/<name>', methods=['GET'])
def api_id(name):
	out=libgensearch.findMirrors(name)

if __name__ == "__main__":
    app.run()