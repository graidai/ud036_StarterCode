import webbrowser

class Movies():
	""" THis is a clear class to store movies related to informatinos"""
	#all caps for constant valiable - me still learning
	VALID_RATINGS = ["G","PG","PG-13","R","MA"]
	def __init__(self, movie_title, movie_storyline, poster, trailer):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster
		self.trailer_youtube_url= trailer


	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

