from flask import Flask, request
app = Flask(__name__)

@app.route('/status')
def status():
    return {'status': 'ok'}

@app.route('/sum')
def sum_numbers():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return {'sum': a + b}

if __name__ == '__main__':
    app.run(debug=True)
