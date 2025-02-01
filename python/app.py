from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data['operation']
    num1 = data['num1']
    num2 = data['num2']
    result = subprocess.run(['python', 'calculator.py', operation, str(num1), str(num2)], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)