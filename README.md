# Movie Trailer Webpage
Contains source code to creates an **HTML page of movie list** with its title, 
posters and trailers.

## Install 
*Download and extract* the zip folder into the python library

## Command Line 
Check example for the Movie Trailer webpage 
```
import entertainment_center
```

These modules are already available in the zip folder extracted
```
import fresh_tomatoes
import media
```
Create you favorite movie tile by creating an object by calling a class Movie
from the media module which has been imported. 
Create six instances of your six favorite movies. An example is shown below 
of an instance created.
```
fire_in_the_blood = media.Movie(
    'Fire in the Blood',
    'Fight against high-priced medicines',
    'https://upload.wikimedia.org/wikipedia/en/thumb/1/15/Movie_Poster%2C_%22Fire_in_the_Blood%22.jpg/220px-Movie_Poster%2C_%22Fire_in_the_Blood%22.jpg',
    'https://www.youtube.com/watch?v=eVf2UUu_w4o')
```
Create a **_list_** that contains the instances of the six favourtie movie you 
have *created as shown in the previous step*
```
movies = [fire_in_the_blood, inception, amelie, tzp, hours_127, schmidt]
```
Now call the **open_movies_page** function from the imported **fresh_tomatoes**
module to generate the HTML
```
fresh_tomatoes.open_movies_page(movies)
```
## Issues 
Some youtube links may not work because permissions are required.

## Attribution
One module was forked from Udacity [here](https://github.com/udacity/ud036_StarterCode.git)
The code for other two modules were sourced and developed with guidance from 
the Udacity FNSD course.




