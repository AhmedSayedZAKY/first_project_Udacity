

# Import the web browser model to open project output in browser
import webbrowser

#declaring class movie 
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    #declaring function of open trailer url in the web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
#########################
#i had declared the class here because i was working on jupyter notebook
#and that causing a problem in importing the class file.
#########################

# the first instance(object) of the movie class #the movie of TOY STORY

toy_story = Movie("Toy Story",
                        "A story of a boy and his toys that came to life",
                        "https://static.comicvine.com/uploads/original/12/126071/2427139-toy_story_1995.jpeg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio"
                       )
#print(toy_story.storyline)



# the second instance(object) of the movie class #the movie of AVATAR

avatar = Movie("AVATAR",
                        "A MARINE landed on an alien planet",
                        "https://images-na.ssl-images-amazon.com/images/I/71rj1RPn4iL._SL1425_.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                       )

# the third instance(object) of the movie class #the movie of Ratatuillie
ratatuil = Movie("Ratatuillie",
                        "a rat meets a cooker and help him",
                        "https://images-na.ssl-images-amazon.com/images/I/71VDlRubWtL._SL1000_.jpg",
                        "https://www.youtube.com/watch?v=e8GBfNo3IHY"
                       )

# the fourth instance(object) of the movie class #the movie of School of Rock
school = Movie("school of rock",
                        "A teacher and rock students",
                        "https://images-na.ssl-images-amazon.com/images/I/51XB8K6WPEL._SY445_.jpg",
                        "https://www.youtube.com/watch?v=5afGGGsxvEA"
                       )

# the fifth instance(object) of the movie class #the movie of Deadpol
Deadpol = Movie("DeadPol",
                        "A fighter of the night movie",
                        "https://images-na.ssl-images-amazon.com/images/I/519eLr--nIL.jpg",
                        "https://www.youtube.com/watch?v=20bpjtCbCz0"
                       )
#print(avatar.storyline)

# the Sixth instance(object) of the movie class #the movie of Infinity war
infinity_war = Movie("Infinity War",
                        "A film for all marvell avengers",
                        "https://www.hindustantimes.com/rf/image_size_960x540/HT/p2/2018/04/30/Pictures/_de62c026-4c6f-11e8-bd65-8f9614bffbbb.jpg",
                        "https://www.youtube.com/watch?v=6ZfuNTqbHE8"
                       )
#print(infinity_war.storyline)
#infinity_war.show_trailer()


# Import the fresh tomatoes file 

import fresh_tomatoes
movies = [toy_story, avatar, ratatuil, school, Deadpol, infinity_war]
fresh_tomatoes.open_movies_page(movies)


# end of the code



