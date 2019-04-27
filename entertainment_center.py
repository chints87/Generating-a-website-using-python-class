import fresh_tomatoes
import media

# Over here an instance fire_in the_blood is created. From the media file the
# class Movie is called that takes arguments in the following order of movie
# name, short description for the movie, poster image of the movie and a
# youtube link for the movie trailer.
fire_in_the_blood = media.Movie(
    'Fire in the Blood',
    'Fight against high-priced medicines',
    'https://upload.wikimedia.org/wikipedia/en/thumb/1/15/Movie_Poster%2C_%22Fire_in_the_Blood%22.jpg/220px-Movie_Poster%2C_%22Fire_in_the_Blood%22.jpg',
    'https://www.youtube.com/watch?v=eVf2UUu_w4o')
# Over here an instance inception is created. From the media file the
# class Movie is called that takes arguments in the following order of movie
# name, short description for the movie, poster image of the movie and a
# youtube link for the movie trailer.
inception = media.Movie(
    'Inception',
    'N/A',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMZ9rLZoIigTrTpDfdfnINSemIj7znCeR3WwDDCrdVubw_QD13K052rw',
    'https://www.youtube.com/watch?v=xitHF0IPJSQ')
# Over here an instance amelie is created. From the media file the
# class Movie is called that takes arguments in the following order of movie
# name, short description for the movie, poster image of the movie and a
# youtube link for the movie trailer.
amelie = media.Movie(
    'Amelie',
    'Shy lady who find its hard to confess her love',
    'https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Amelie_poster.jpg/220px-Amelie_poster.jpg',
    ' https://www.youtube.com/watch?v=HUECWi5pX7o')
# Over here an instance tzp is created. From the media file the
# class Movie is called that takes arguments in the following order of movie
# name, short description for the movie, poster image of the movie and a
# youtube link for the movie trailer.
tzp = media.Movie(
    'Taare Zameen Par',
    'Teacher comes to the rescue of the student suffering from dyslexia',
    'https://upload.wikimedia.org/wikipedia/en/thumb/b/b4/Taare_Zameen_Par_Like_Stars_on_Earth_poster.png/220px-Taare_Zameen_Par_Like_Stars_on_Earth_poster.png',
    'https://www.youtube.com/watch?v=tn_2Ie_jtX8')
# Over here an instance hours_127 is created. From the media file the
# class Movie is called that takes arguments in the following order of movie
# name, short description for the movie, poster image of the movie and a
# youtube link for the movie trailer.
hours_127 = media.Movie(
    '127 Hours',
    'N/A',
    'https://upload.wikimedia.org/wikipedia/en/b/b3/127_Hours_Poster.jpg',
    'https://www.youtube.com/watch?v=OlhLOWTnVoQ')
# Over here an instance schmidt is created. From the media file the
# class Movie is called that takes arguments in the following order of movie
# name, short description for the movie, poster image of the movie and a
# youtube link for the movie trailer.
schmidt = media.Movie(
    'About Schmidt',
    'N/A',
    'https://upload.wikimedia.org/wikipedia/en/thumb/4/4c/About_Schmidt_poster.jpg/220px-About_Schmidt_poster.jpg',
    'https://www.youtube.com/watch?v=M9OHT6EErbY')

# A list is created that stores all instances that we created
movies = [fire_in_the_blood, inception, amelie, tzp, hours_127, schmidt]
# The movies list is an argument for the open_movies_page function that
# has been imported from the fresh tomatoes file.
fresh_tomatoes.open_movies_page(movies)
