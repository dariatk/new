from flask import Flask, request

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return 'Error: Division by zero is not allowed', 400
        result = num1 / num2
    else:
        return 'Error: Invalid operation', 400

    return 'Result: {}'.format(result)

if __name__ == '__main__':
    app.run(debug=True)
