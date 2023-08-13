# activate environment using the command:
#   myenv\Scripts\activate
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Serve the Angular static files
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.root_path + '/static', filename)

# Serve the Angular app template
@app.route('/')
def index():
    return render_template('angular_template.html')

if __name__ == '__main__':
    app.run()
