# Import packages and modules
import media
import fresh_tomatoes

# Call media.Movie to create movie objects with data
toy_story = media.Movie("Toy Story", "A group of toys come to life and try to find their way back home before their owner, Andy, moves away.", "Tom Hanks, Tim Allen, Don Rickles", "8.3/10", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")
pirates_caribbean = media.Movie("Pirates of the Caribbean: At World's End", "The pirates band together in an attempt to protect their way of life from those that wish them eradicated.", "Johnny Depp, Orlando Bloom, Keira Knightley", "7.1/10", "https://upload.wikimedia.org/wikipedia/en/5/5a/Pirates_AWE_Poster.jpg", "https://www.youtube.com/watch?v=HKSZtp_OGHY")
ratatouille = media.Movie("Ratatouille", "An untalented chef gets help from a rat who knows how to cook.", "Brad Garrett, Lou Romano, Patton Oswalt", "8.0/10", "http://images.fanpop.com/images/image_uploads/Ratatouille-poster-ratatouille-324474_1215_1800.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk")
transformers = media.Movie("Transformers: Age of Extinction", "The creators of the transformers return in full force to retrieve their inventions.", "Mark Wahlberg, Nicola Peltz, Jack Reynor", "5.8/10", "https://upload.wikimedia.org/wikipedia/en/9/94/Transformers_Age_of_Extinction_Poster.jpeg", "https://www.youtube.com/watch?v=pbI980iUb78")
lord_of_the_rings = media.Movie("Lord of the Rings: Return of the King", "The ring bearer and his team take their final stand to save their land from evil.", "Elijah Wood, Viggo Mortensen, Ian McKellen", "8.9/10", "http://ia.media-imdb.com/images/M/MV5BMjE4MjA1NTAyMV5BMl5BanBnXkFtZTcwNzM1NDQyMQ@@._V1_SX640_SY720_.jpg", "https://www.youtube.com/watch?v=r5X-hFf6Bwo")
land_before_time = media.Movie("The Land Before Time", "The tale of 5 baby dinosaurs making their journey to find the Great Valley.", "Pat Hingle, Gabriel Damon, Judith Barsi", "7.3/10", "http://ia.media-imdb.com/images/M/MV5BOTkyNjQ0MDA1OV5BMl5BanBnXkFtZTcwMDkyMTYyMQ@@._V1_SX640_SY720_.jpg", "https://www.youtube.com/watch?v=lpnwK2NGxIo")

# Create list of movie objects
movies = [toy_story, land_before_time, pirates_caribbean, ratatouille, transformers, lord_of_the_rings]

# Call fresh_tomatoes package to create HTML file
fresh_tomatoes.open_movies_page(movies)

