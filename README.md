# ud036_StarterCode
Source code for a Movie Trailer website.

This project is a continuation of the above repo # ud036_StarterCode aka Movie Trailer Project.

media.py contains the constructer for the indiviual movies. 
entertainment_center.py if the main python file which generates the html page for the trailer website using the pre-written code in fresh_tomatoes.py


To add new movies
- open entertainment_center.py to input movies you want in the trailer website
- create a movie object in entertainment_center.py with [title, info, poster_url, trailer_url]
	* [title] = name of the movie
	* [info] = a short description of the movie
	* [poster_url] = link to the offical/or not release poster of the movie
	* [trailer_url] = link to the trailer of the movie

- create a movie object using the above 4 parameters like
	toy_story = media.Movies(
          "Toy Story",
          "A story about a boytoy",
          "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
          "https://www.youtube.com/watch?v=KYz2wyBy3kc")

- create an array of all the movies objects you created like
	movies = [toy_story, avatar, stand_by_me,
          sea_of_love, the_lover, double_impact]


- initate open_movies_page(movie_array) method from fresh_tomatoes.py
	fresh_tomatoes.open_movies_page(movies)

- run entertainment_center.py in python. An html page will be created in the same folder which will include all the movie-objects that have been created and run thru open_movies methond



