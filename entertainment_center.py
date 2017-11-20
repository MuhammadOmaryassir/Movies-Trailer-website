import fresh_tomatoes
import media


fight_club = media.Movie(movie_title = "Fight Club",
					     movie_storyline = "An insomniac office worker looking for a way to change his life crosses paths with a devil-may-care soap maker and they form an underground fight club that evolves into something much, much more...",
					     poster_image = "http://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
					     trailer_youtube = "www.youtube.com/watch?v=SUXWAEX2jlg")




Justice_League = media.Movie("Justice League",
                             "Fueled by his restored faith in humanity and inspired by Superman's selfless act",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BNDgwNjMwNjM1OV5BMl5BanBnXkFtZTgwNjA2Njk5MzI@._V1_.jpg",
                             "https://www.youtube.com/watch?v=r9-DM9uBtVI")


Avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a unique mission",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

matrix = media.Movie("The Matrix",
					 "Neo searches for the truth about the Matrix and discovers his place in it.",
					 "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
					 "https://www.youtube.com/watch?v=_Ls19O-9p3s")

point_break = media.Movie("Point Break",
					      "Reeves stars as rookie FBI agent Johnny Utah, who is investigating a string of bank robberies possibly being committed by surfers. Johnny goes undercover to infiltrate the surfing community and develops a complex friendship with Bodhi (Swayze), the charismatic leader of a gang of surfers.",
					      "http://upload.wikimedia.org/wikipedia/en/7/7e/Pointbreaktheatrical.jpg",
					      "https://www.youtube.com/watch?v=AVk3mR2UhgI")

usual_suspects = media.Movie(movie_title = "The Usual Suspects",
						     movie_storyline = "A sole survivor tells of the twisty events leading up to a horrific gun battle on a boat, which begin when five criminals meet at a seemingly random police lineup.",
						     poster_image = "http://upload.wikimedia.org/wikipedia/en/9/9c/Usual_suspects_ver1.jpg",
						     trailer_youtube = "https://www.youtube.com/watch?v=oiXdPolca5w")

movies = [fight_club,Justice_League,Avatar,matrix,point_break,usual_suspects]
fresh_tomatoes.open_movies_page(movies)
