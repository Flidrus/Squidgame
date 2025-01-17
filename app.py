from flask import Flask, request

from functions import solve


app = Flask(__name__)


@app.route('/')
def index():
    return "<h1 style='color:blue'> Gomelskiy Semen </h1>"


@app.route('/solve')
def get_result():
    
    a = request.args.get('a', None)
    b = request.args.get('b', None)
    c = request.args.get('c', None)

    if a is None:
        return "<p style='color:red'> Parameter 'a' is required </p>"
    else:
        a = float(a)

    if b is None:
        return "<p style='color:red'> Parameter 'b' is required </p>"
    else:
        b = float(b)

    if c is None:
        return "<p style='color:red'> Parameter 'c' is required </p>"
    else:
        c = float(c)

    result = solve(a, b, c)

    if not result:
        return "<p style='color:green'> No roots </p>"
    elif result == ['all']:
        return "<p style='color:green'> Any number </p>"
    else:
        return f"<p style='color:green'> Roots: {result[0]}, {result[1]}. </p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
