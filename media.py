import webbrowser


class Movie():
    """Store movie information provided by the user"""

    def __init__(
            self,
            movie_name,
            movie_description,
            movie_poster,
            movie_trailer):
        self.title = movie_name
        self.storyline = movie_description
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    # Will open the youtube link for trailer of the movie object.
    def open_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
