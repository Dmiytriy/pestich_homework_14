from flask import Flask, jsonify
from utils import search_title, search_by_period, search_new_by_genre, search_by_rating

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/movie/<title>', methods=['GET'])
def get_by_title(title):
    movie = search_title(title)
    return jsonify(movie)


@app.route('/movie/<year_one>/to/<year_two>', methods=['GET'])
def get_by_period(year_one, year_two):
    movies = search_by_period(year_one, year_two)
    return jsonify(movies)


@app.route('/movies/<rating>', methods=['GET'])
def get_by_rating(rating):
    movies = search_by_rating(rating)
    return jsonify(movies)


@app.route('/genre/<genre>', methods=['GET'])
def get_new_by_genre(genre):
    movies = search_new_by_genre(genre)
    return jsonify(movies)


if __name__ == '__main__':
    app.run()
