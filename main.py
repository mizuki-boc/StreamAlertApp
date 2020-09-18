from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "stream alert app!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8888, threaded=True)