from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/for_employers')
def for_employers():
    return render_template('for_employers.html')

if __name__ == '__main__':
    app.run(debug=True)
