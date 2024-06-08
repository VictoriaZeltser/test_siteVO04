from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/mesotherapy')
def mesotherapy():
    return render_template('mesotherapy.html')

@app.route('/hair_removal')
def hair_removal():
    return render_template('hair_removal.html')

@app.route('/body_sculpting')
def body_sculpting():
    return render_template('body_sculpting.html')

if __name__ == '__main__':
    app.run(debug=True)
