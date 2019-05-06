import webbrowser


class Movie():

    # VALID_RATINGS = ["G", "PG", "PG-13", "R"] for movies

    """This class provides a way to store movie related information.

       Attributes:
       title - title of the movie,
       genre - genre of the movie,
       tagline - tagline of the movie,
       duration - duration of the movie,
       rating - rating of the movie,
       poster_image_url - title of the movie,
       trailer_youtube_url - title of the movie.
    """

    def __init__(self, movie_title, movie_genre, movie_tagline, movie_duration, movie_rating, poster_image, trailer_youtube):
        self.title = movie_title
        self.genre = movie_genre
        self.tagline = movie_tagline
        self.duration = movie_duration
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube



    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    """This function plays the movie trailer"""
