from flask import Flask, render_template
from flaskwebgui import FlaskUI
app = Flask(__name__)
ui = FlaskUI(app, width=500, height=500)
@app.route('/')
def index_page():
    return render_template('index1.html')

if __name__ == "__main__":
    ui.run()
