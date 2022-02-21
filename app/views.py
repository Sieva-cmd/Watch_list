
from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    message ='coding is awosome'
    title ='Home - Welcome to the best movie review website obline'
    return render_template("index.html",title =title)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    """
    View movie page function that returns the movie page and data
    """
    return render_template('movie.html', id =movie_id)

