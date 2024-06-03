
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articles.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    publication_date = db.Column(db.Date, nullable=False)
    text = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    articles = Article.query.filter(Article.title.like(f'%{query}%')).all()
    return render_template('index.html', articles=articles)

@app.route('/article/<int:id>')
def article(id):
    article = Article.query.get(id)
    return render_template('article.html', article=article)

@app.route('/add-article', methods=['GET', 'POST'])
def add_article():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        publication_date = request.form.get('publication_date')
        text = request.form.get('text')
        article = Article(title=title, author=author, publication_date=publication_date, text=text)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add-article.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
