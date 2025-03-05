from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return {"message": "01001000 01100101 01101100 01101100 01101111 00101100 00100000 01010111 01101111 01110010 01101100 01100100 00100001 long long long longlon long long long long"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000, debug=True)
