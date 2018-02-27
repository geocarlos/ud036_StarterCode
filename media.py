class Movie():
    """This class provides a way to store movies info and trailers"""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        '''
        :param movie_title: string
        :param movie_storyline: string
        :param poster_image: string
        :param trailer_youtube: string
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
