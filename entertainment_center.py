import movies_website
import media

dhadak = media.Movie("Dhadak",
                     "The story of lover",
                     "https://images.inuth.com/2017/11/1Janhvi-Kapoor-and-Ishaan-Khatter-look-beautiful-in-new-Dhadak-poster.jpg",
                     "https://www.youtube.com/watch?v=b-vv-ijGAdA")
satyamev_jayate = media.Movie("Satyamev Jayate",
                              "A petriotic movie",
                              "http://www.bollywoodlife.com/wp-content/uploads/2018/06/satyamev-jayate.jpg",
                              "https://www.youtube.com/watch?v=Pcv0aoOlsLM&t=37s")

gold = media.Movie("Gold",
                   "A petirotic movie",
                   "http://s3.india.com/wp-content/uploads/2018/06/Gold.jpg",
                   "https://www.youtube.com/watch?v=Pcv0aoOlsLM&t=37s")
stree = media.Movie("Stree",
                    "Something like horror movie",
                    "https://www.comingtrailer.com/images/poster/285Xheight-Stree5.jpg",
                    "https://www.youtube.com/watch?v=gzeaGcLLl_A")
qarib_qarib_single = media.Movie("Qarib Qarib Single",
                                    "Story of every single man",
                                    "https://i2.cinestaan.com/image-bank/1500-1500/102001-103000/102194.jpg",
                                    "https://www.youtube.com/watch?v=MU4QL-VwDlc")
three_idiots = media.Movie("3 Idiots",
                      "Story of students life and their choises",
                      "https://cdn.shopify.com/s/files/1/0747/3829/products/mNS0669_1024x1024.jpg",
                      "https://www.youtube.com/watch?v=K0eDlFX9GMc&t=2s")


#print(dhadak.storyline)

avatar = media.Movie("Avatar",
                     "The story of avatar",
                     "https://images-na.ssl-images-amazon.com/images/I/61OUGpUfAyL._SY679_.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")
#print(avatar.storyline)

#avatar.show_trailer()

hunger_games = media.Movie("Hunger Games",
                           "The real story of reality",
                           "https://images-na.ssl-images-amazon.com/images/I/51OGv-AnD6L.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

dead_poets_society = media.Movie("Dead Poets Society",
                                 "Very interesting story",
                                 "http://www.kinomuza.pl/uploads/muza_film/image/1720/A70-1607.jpg",
                                 "https://www.youtube.com/watch?v=4lj185DaZ_o")

spectacular = media.Movie("The Spectacular Now",
                          "This is awesome movie",
                          "https://images-na.ssl-images-amazon.com/images/I/51VPVEGmiGL.jpg",
                          "https://www.youtube.com/watch?v=XDTBLSkUmYk")
war_for_the_planet = media.Movie("War For The Planet of The Apes",
                                 "An interesting story",
                                 "http://vintageposterdesigns.com/wp-content/uploads/2018/04/movie-poster-war-for-the-planet-of-the-apes-war-for-the-planet-of-the-apes.jpg",
                                 "https://www.youtube.com/watch?v=qxjPjPzQ1iU")
angry_men = media.Movie("Twelve Angry men",
                        "Story of 12 angry men",
                        "https://images-na.ssl-images-amazon.com/images/I/81LX%2BJlavLL._SY550_.jpg",
                        "https://www.youtube.com/watch?v=A7CBKT0PWFA")


movies = [dhadak, satyamev_jayate, gold, stree, qarib_qarib_single,three_idiots, avatar, hunger_games, dead_poets_society, spectacular, war_for_the_planet, angry_men]

movies_website.open_movies_page(movies)







