# use the class we defined in the media file
# keep class definitions in their own file

import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

batman = media.Movie("The Dark Knight",
                     "A crime fighter protects Gotham City.",
                     "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY")

nemo = media.Movie("Finding Nemo",
                   "A fathers search for his son through the ocean.",
                   "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
                   "https://www.youtube.com/watch?v=wZdpNglLbt8")


movies = [toy_story,avatar,batman,nemo]
#fresh_tomatoes.open_movies_page(movies)