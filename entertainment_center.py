import media
import fresh_tomatoes

# Creating variables for each movie
the_count_of_monte_cristo = media.Movie("The Count of Monte Cristo",
                                        "https://m.media-amazon.com/images/M/MV5BMDM0ZWRjZDgtZWI0MS00ZTIzLTg4MWYtZjU5MDEyMDU0ODBjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                                        "https://www.youtube.com/watch?v=gzRSVl8UewM")  # NOQA

the_skin_i_live_in = media.Movie("The Skin I Live In",
                                 "https://m.media-amazon.com/images/M/MV5BMjMwOTYyNDY4NV5BMl5BanBnXkFtZTcwNDI1ODk0Ng@@._V1_SY1000_CR0,0,669,1000_AL_.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=BOto6S0Rz64&t=28s")  # NOQA

inception = media.Movie("Inception",
                        "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

donnie_darko = media.Movie("Donnie Darko",
                           "https://m.media-amazon.com/images/M/MV5BZjZlZDlkYTktMmU1My00ZDBiLWFlNjEtYTBhNjVhOTM4ZjJjXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=bzLn8sYeM9o")

fight_club = media.Movie("Fight Club",
                         "https://m.media-amazon.com/images/M/MV5BNGM2NjQxZTAtMmU5My00YTk5LWFmOWMtYjZlYzk4YzMwNjFlXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,666,1000_AL_.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

eternal_sunshine_of_the_spotless_mind = media.Movie("""Eternal Sunshine of the
                                                    Spotless Mind""",
                                                    "https://m.media-amazon.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                                                    "https://www.youtube.com/watch?v=hj7Wgd_Yn94")  # NOQA

vanilla_sky = media.Movie("Vanilla Sky",
                          "https://m.media-amazon.com/images/M/MV5BYzFlMTJjYzUtMWFjYy00NjkyLTg1Y2EtYmZkMjdlOGQ1ZGYwL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=9jUX3xfWH-U")

source_code = media.Movie("Source Code",
                          "https://m.media-amazon.com/images/M/MV5BMTY0MTc3MzMzNV5BMl5BanBnXkFtZTcwNDE4MjE0NA@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=t5roJgHV_lA")

memento = media.Movie("Memento",
                      "https://m.media-amazon.com/images/M/MV5BZTcyNjk1MjgtOWI3Mi00YzQwLWI5MTktMzY4ZmI2NDAyNzYzXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,681,1000_AL_.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=E77LfnMI-34")

filth = media.Movie("Filth",
                    "https://m.media-amazon.com/images/M/MV5BMjE2NTgyMzM0NV5BMl5BanBnXkFtZTgwNzkwNDE1MzE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=uWGhCLu0fZg")

fear_and_loathing_in_las_vegas = media.Movie("Fear and Loathing in Las Vegas",
                                             "https://m.media-amazon.com/images/M/MV5BNjA2ZDY3ZjYtZmNiMC00MDU5LTgxMWEtNzk1YmI3NzdkMTU0XkEyXkFqcGdeQXVyNjQyMjcwNDM@._V1_.jpg",  # NOQA
                                             "https://www.youtube.com/watch?v=4iOslycQDwQ")  # NOQA

silence_of_the_lambs = media.Movie("The Silence of the lambs",
                                   "https://m.media-amazon.com/images/M/MV5BNjNhZTk0ZmEtNjJhMi00YzFlLWE1MmEtYzM1M2ZmMGMwMTU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,677,1000_AL_.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=RuX2MQeb8UM")  # NOQA

mr_nobody = media.Movie("Mr. Nobody",
                        "https://m.media-amazon.com/images/M/MV5BMTg4ODkzMDQ3Nl5BMl5BanBnXkFtZTgwNTEwMTkxMDE@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=uH5BgJbbGuE")

eyes_wide_shut = media.Movie("Eyes Wide Shut",
                             "https://images-na.ssl-images-amazon.com/images/I/41c9Qi%2BYuBL.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=gUBETbMtaN8")

ex_machina = media.Movie("Ex Machina",
                         "https://m.media-amazon.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=EoQuVnKhxaM")

the_shinning = media.Movie("The Shinning",
                           "https://m.media-amazon.com/images/M/MV5BZWFlYmY2MGEtZjVkYS00YzU4LTg0YjQtYzY1ZGE3NTA5NGQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=S014oGZiSdI")

# Creating a list with the movies variables
movies_list = [the_count_of_monte_cristo, the_skin_i_live_in, inception,
               donnie_darko, fight_club, eternal_sunshine_of_the_spotless_mind,
               vanilla_sky, source_code, memento,
               fear_and_loathing_in_las_vegas, silence_of_the_lambs,
               mr_nobody, eyes_wide_shut, ex_machina, the_shinning]

# Parsing the list of movies to fres_tomatoes.py to generate the HTML file.
fresh_tomatoes.open_movies_page(movies_list)
