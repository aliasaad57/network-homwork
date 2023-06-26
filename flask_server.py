from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def info():
    return render_template('about.html')

@app.route('/signup')
def login():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)