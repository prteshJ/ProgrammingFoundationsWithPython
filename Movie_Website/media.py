import webbrowser

""" Superclass """
class Video():

    """ Video class constructor """
    def __init__(self, video_title, youtube_url):
        print("Video Constructor invoked")
        self.title = video_title
        self.trailer_youtube_url = youtube_url

    def show_trailer(self):
               webbrowser.open(self.trailer_youtube_url)

""" Child of Video class """
class Movie(Video):
    """ This class provides a way to store movie related information"""

    """ Movie class constructor """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, movie_title, trailer_youtube)
        print("Movie Constructor Invoked")
        self.storyline = movie_storyline
        self.poster_image_url = poster_image        

""" Child of Video class """
class TVShow(Video):
    """ This class provides a way to store information related to television shows"""

    """ TVShow class constructor """
    def __init__(self, show_title, show_image, show_trailer):        
        Video.__init__(self, show_title, show_trailer)
        print("TV Show Constructor Invoked")
        self.poster_image_url = show_image
