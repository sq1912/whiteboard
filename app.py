# activate environment using the command:
#   myenv\Scripts\activate

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hellp():
    return render_template('index.html')