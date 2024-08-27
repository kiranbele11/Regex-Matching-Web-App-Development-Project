import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/regex_matcher', methods=['GET', 'POST'])
def regex_matcher():
    matches = None
    if request.method == 'POST':
        test_string = request.form['test_string']
        regex_pattern = request.form['regex']
        matches = re.findall(regex_pattern, test_string)
    return render_template('results.html', matches=matches)

@app.route('/email_validator', methods=['GET', 'POST'])
def email_validator():
    email_result = None
    if request.method == 'POST':
        email = request.form['email']
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(regex, email):
            email_result = f"'{email}' is a valid email address."
        else:
            email_result = f"'{email}' is not a valid email address."
    return render_template('validate_email.html', email_result=email_result)

if __name__ == '__main__':
    app.run(debug=True)
