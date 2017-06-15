import pritesh_cinema
import media

""" MOVIES """

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

#midnight_in_paris = media.Movie("Midnight in Paris",
#                                "Going back in time to meet authors",
#                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
#                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

#hunger_games = media.Movie("Hunger Games",
#                           "A really real reality show",
#                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
#                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

#One of my favorite movies
doctor_strange = media.Movie("Doctor Strange",
                             "The story of the talented neurosurgeon Doctor Stephen Strange who, after a tragic car accident, must put ego aside and learn the secrets of a hidden world of mysticism and alternate dimensions.",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                             "https://www.youtube.com/watch?v=HSzx-zryEgM")

guardians_of_galaxy_vol_2 = media.Movie("Guardians of the Galaxy Vol. 2",
                                        "A team of superheroes fight to unravel their leader's true parentage",
                                        "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",
                                        "https://www.youtube.com/watch?v=2cv2ueYnKjg")

""" Load Movie data into an array """
movies = [toy_story, avatar, school_of_rock, ratatouille, doctor_strange, guardians_of_galaxy_vol_2]

""" TV SHOWS """

big_bang_theory = media.TVShow("The Big Bang Theory",
                                "http://3.bp.blogspot.com/-jZpzpfIjPfQ/UM9zOWkoHOI/AAAAAAACLaE/P9NDFqKftJk/s1600/Big_bang_theory_poster11.jpg",
                                "https://www.youtube.com/watch?v=WBb3fojgW0Q")

game_of_thrones = media.TVShow("Game of Thrones",
                               "https://s-media-cache-ak0.pinimg.com/564x/98/f9/40/98f94074e68655e84d54350a5a2a1e97.jpg",
                               "https://www.youtube.com/watch?v=LNGW6mmemz8")

breaking_bad = media.TVShow("Breaking Bad",
                            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxgboX6JbWB3YT4uFASl2ip_383Jf4NEMlWUNkR2Qlgm05pf8H",
                            "https://www.youtube.com/watch?v=5NpEA2yaWVQ")

""" Load TV Show data into an array """
tv_shows = [big_bang_theory, game_of_thrones, breaking_bad]

""" Merge arrays using '+' and utilize python code to create a movie website """
pritesh_cinema.open_movies_page(movies+tv_shows)




