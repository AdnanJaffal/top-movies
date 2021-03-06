# Import packages and modules
import webbrowser


# Movie class
class Movie():
    # Initializes object with title, storyline, cast, rating, poster url,
    # youtube url
    def __init__(self, movie_title, movie_storyline, stars, imdb_rating,
                 poster_image, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.cast = stars
        self.rating = imdb_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
