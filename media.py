import webbrowser

# Creating a Movie Class


class Movie:
    def __init__(self, movie_title, movie_poster_url, movie_trailer_url):
        self.title = movie_title
        self.poster = movie_poster_url
        self.trailer = movie_trailer_url
