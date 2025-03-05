from flask import Flask, render_template, jsonify
app = Flask(__name__)

def read_file():
    try:
        with open("output.txt", 'r', encoding='utf-8') as out:
            return out.read()
    except FileNotFoundError:
        print("no output file found")
        return "no message"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify({"message": read_file()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000, debug=True)
