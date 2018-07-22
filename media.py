import webbrowser

# Creating a Movie Class


class Movie:
    """The Movie class initializes a Movie object.
    Attributes:
        title: Movie Title (string)
        poster: URL of the Movie Poster
        trailer: URL of the Movie Trailer"""
    def __init__(self, movie_title, movie_poster_url, movie_trailer_url):
        self.title = movie_title
        self.poster = movie_poster_url
        self.trailer = movie_trailer_url
