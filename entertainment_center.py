from media import Movie
from fresh_tomatoes import open_movies_page

# Prefix for Wikimedia images
wikiUrl = "https://upload.wikimedia.org/wikipedia/en/"

"""
List of movies.
Please check Movie class in media.py file for clarification on how the Movie
objects are constructed.
"""

movies = [

    Movie("Interstellar",
          '''A team of explorers travel through a wormhole in space in an
          attempt to ensure humanity's survival.''',
          wikiUrl + "b/bc/Interstellar_film_poster.jpg",
          "https://youtu.be/zSWdZVtXT7E"),

    Movie("The Matrix",
          '''A computer hacker learns from mysterious rebels about the true nature
          of his reality and his role in the war against its controllers. ''',
          wikiUrl + "c/c1/The_Matrix_Poster.jpg",
          "https://youtu.be/m8e-FF8MsqU"),

    Movie("The Terminator",
          '''A seemingly indestructible humanoid cyborg is sent
          from 2029 to 1984 to assassinate a waitress, whose unborn son
          will lead humanity in a war against the machines, while a soldier
          from that war is sent to protect her at all costs.''',
          wikiUrl + "7/70/Terminator1984movieposter.jpg",
          "https://youtu.be/rBlT3eXrXZU"),

    Movie("Pink Floyd - The Wall",
          '''A confined but troubled rock star descends into madness in the midst
          of his physical and social isolation from everyone.''',
          wikiUrl + "9/94/Pink_Floyd_The_Wall.jpg",
          "https://youtu.be/5CJRnRyA4wA"),

    Movie("Abre Los Ojos",
          '''A very handsome man finds the love of his life, but he suffers an
          accident and needs to have his face rebuilt by surgery after it is
          severely disfigured..''',
          wikiUrl + "/a/a6/Abre_los_ojos_movie.jpg",
          "https://youtu.be/PBtnPuB0x3U"),

    Movie("Transcendence",
          '''A scientist's drive for artificial intelligence,
          takes on dangerous implications when his consciousness is
          uploaded into one such program.''',
          wikiUrl + "e/ef/Transcendence2014Poster.jpg",
          "https://youtu.be/QheoYw1BKJ4"),

    Movie("Resident Evil",
          '''A special military unit fights a powerful, out-of-control
          supercomputer and hundreds of scientists who have mutated
          into flesh-eating creatures after a laboratory accident.''',
          wikiUrl + "thumb/a/a1/Resident_evil_ver4.jpg/220px-Resident_evil_ver4.jpg",
          "https://youtu.be/PWUT4CXWcwQ"),

    Movie("Non Ti Muovere",
          '''Gaetano and Delia, a separated couple, try to pick up the pieces
          of their broken love, recalling all the faults and the mistakes which
          led them to where they are now.''',
          wikiUrl + "5/5d/Don%27t_Move%282004%29.jpg",
          "https://youtu.be/Wn4V8BXzjNI"),

    Movie("Tropa de Elite",
          ''' Captain Nascimento has to find a substitute for his occupation
          while trying to take down drug dealers and criminals before the
          Pope comes to Rio de Janeiro, Brazil.''',
          wikiUrl + "2/2a/TropaDeElitePoster.jpg",
          "https://youtu.be/ELlkWtNWyKY")
]

open_movies_page(movies)
