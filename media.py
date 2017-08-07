import webbrowser


class Movies():
    # info of the movie class
    """ THis is a clear class to store movies related to informatinos"""

    def __init__(self, movie_title, movie_storyline, poster, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
