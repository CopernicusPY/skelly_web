import flask
import flask_cors
app = flask.Flask(__name__, static_folder=".")
flask_cors.CORS(app)

@app.route('/')
def home():
    return flask.send_from_directory(".", "index.html")

@app.route('/<path:path>')
def static_file(path):
    return flask.send_from_directory(".", path)
    
if __name__ == "__main__":
    app.run(port=8080)