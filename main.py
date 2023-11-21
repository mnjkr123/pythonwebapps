import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    try:
        weight = float(request.form['weight'])
        height = float(request.form['height']) / 100  # Convert height to meters
        bmi = weight / (height ** 2)
        result = f'BMI: {bmi:.2f}'
    except ValueError:
        result = 'Invalid input. Please enter valid numbers.'

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
