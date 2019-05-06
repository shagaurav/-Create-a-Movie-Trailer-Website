import fresh_tomatoes # makes a connection with the fresh_tomatoes file
import media          # makes a connection with media file
"""stores details of movie trailer and displays the video"""

forrest_gump = media.Movie("Forrest Gump",
                           "Comedy, Drama, Romance",
                           "The story of a lifetime.",
                           "2h 22min",
                           "PG-13",
                           "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")


silver_linings_Playbook = media.Movie("Silver Linings Playbook",
                                      "Comedy, Drama, Romance",
                                      "Watch for the signs.",
                                      "2h 2min",
                                      "R",
                                      "https://upload.wikimedia.org/wikipedia/en/9/9a/Silver_Linings_Playbook_Poster.jpg",
                                      "https://www.youtube.com/watch?v=EI_3ywJLQio")



the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "Crime, Drama",
                                       "Fear can hold you prisoner. Hope can set you free.",
                                       "2h 22min",
                                       "R",
                                       "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                       "https://www.youtube.com/watch?v=NmzuHjWmXOc")


jerry_maguire = media.Movie("Jerry Maguire",
                            "Comedy, Drama, Romance",
                            "Everybody loved him... Everybody disappeared.",
                            "2h 19min",
                            "R",
                            "https://upload.wikimedia.org/wikipedia/en/e/ea/Jerry_Maguire_movie_poster.jpg",
                            "https://www.youtube.com/watch?v=rCCaTPY-z4Q")

inception = media.Movie("Inception",
                        "Action, Adventure, Sci-Fi",
                        "The dream is real.",
                        "2h 28min", "PG-13",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

interstellar = media.Movie("Interstellar",
                           "Adventure, Drama, Sci-Fi",
                           "Mankind was born on Earth. It was never meant to die here.",
                           "2h 49min",
                           "PG-13",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=2LqzF5WauAw")

hunger_games = media.Movie("Hunger Games",
                           "Adventure, Sci-Fi, Thriller",
                           "The World Will Be Watching.",
                           "2h 22min",
                           "PG-13",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

Queen = media.Movie("Queen",
                    "Adventure, Comedy, Drama",
                    "Everything in life happens for the good.",
                    "2h 26min",
                    "R",
                    "https://upload.wikimedia.org/wikipedia/en/4/45/QueenMoviePoster7thMarch.jpg",
                    "https://www.youtube.com/watch?v=KGC6vl3lzf0")

fight_club = media.Movie("Fight Club",
                         "Drama",
                         "Losing all hope is freedom.",
                         "2h 19min",
                         "R",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=BdJKm16Co6M")

movies = [forrest_gump, silver_linings_Playbook, the_shawshank_redemption,
         jerry_maguire, inception, interstellar, hunger_games, Queen, fight_club]
# Stores the movie object in a list

# print (media.Movie.VALID_RATINGS)

fresh_tomatoes.open_movies_page(movies) # Creates the output which is a website
