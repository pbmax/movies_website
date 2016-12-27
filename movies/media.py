import webbrowser

class Movie():
    """ This class provides a way to store information related to on movies """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title,movie_storyline,poster_image,trailer_youtube,movie_director, year_released, movie_genre):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = movie_director
        self.year_released = year_released
        self.genre = movie_genre

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
