from flask import Flask, request
import os

app = Flask(__name__)
port = int(os.getenv("PORT", 5000))

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/goodbye")
def goodbye():
    return "Goodbye!"

@app.route("/echo")
def echo():
    return request.args.get('data', '')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
