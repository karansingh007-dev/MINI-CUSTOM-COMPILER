from flask import Flask, request, jsonify
import sys
import io
from compiler import run  # 👈 Import your custom run function

app = Flask(__name__)

@app.route('/')
def index():
    with open("index.html", "r") as file:
        return file.read()

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json['code']

    # Use the run function from your PLY-based compiler and capture its output
    output = run(code)

    return jsonify({'output': output})


if __name__ == "__main__":
    app.run(debug=True)
