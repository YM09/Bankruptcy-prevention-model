
from flask import Flask, request, render_template, jsonify
import project_code  # Import your modularized project code

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Renders the web page

@app.route('/process', methods=['POST'])
def process():
    input_data = request.form.get("user_input")  # Retrieve user input from the form
    result = project_code.process(input_data)  # Call the function from project_code.py
    return jsonify({"result": result})  # Return the result as JSON

if __name__ == '__main__':
    app.run(debug=True)
