import media
import fresh_tomatoes

#construct objects for the movie
toy_story = media.Movies("Toy Story",
	"A story about a boytoy",
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movies("Avatar",
	"a marine's psychedelic journey where real and CGI people die",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")

stand_by_me = media.Movies("Stand By Me",
	"four kids and a dead body",
	"https://upload.wikimedia.org/wikipedia/en/7/74/Stand_By_Me_1986_American_Theatrical_Release_Poster.jpg",
	"https://www.youtube.com/watch?v=oYTfYsODWQo")

sea_of_love = media.Movies("Sea of Love",
	"killer working girl or is she",
	"https://upload.wikimedia.org/wikipedia/en/9/9c/Sea_of_love_1989.jpg",
	"https://www.youtube.com/watch?v=hoQPFMWteQ4")

the_lover = media.Movies("The Lover",
	"poor French girl, rich Vietnamese businessman, an affair, lost love, an eternal poster in every asian room",
	"https://upload.wikimedia.org/wikipedia/en/b/b8/The-Lover-poster.jpg",
	"https://www.youtube.com/watch?v=ObXJvC49_4k")

double_impact = media.Movies("Double Impact",
	"classical sakespearian twin entanglement with lots of kicking and love makeing",
	"https://upload.wikimedia.org/wikipedia/en/2/24/Double_impact.jpg",
	"https://www.youtube.com/watch?v=xyUqIuwOEzI")

movies = [toy_story, avatar, stand_by_me, sea_of_love, the_lover, double_impact]

#generate a webpage using a method in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)



