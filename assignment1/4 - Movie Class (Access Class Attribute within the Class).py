"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


class Movie:

    id_counter = 1
    movie_counter = 0
    titles = set()

    latest_title = None

    def __init__(self, title: str, rating: float):
        self.id = Movie.id_counter
        self.title = title
        self.rating = rating

        Movie.id_counter += 1
        self.titles.add(title)
        Movie.latest_title = title
        Movie.movie_counter += 1

        # def f():
        #     print(f"THE Movie title is: {self.title}")
        # self.print_title_2 = f

    def print_title(self):
        print(f"Movie title is: {self.title}")

    # @staticmethod
    # def restart():
    #     Movie.id_counter = 1
    #
    # @classmethod
    # def restart_cls(cls):
    #     # cls is Movie
    #     cls.id_counter = 1


def restart():
    Movie.id_counter = 1


my_movie = Movie("Sense and Sensibility", "4.5")
your_movie = Movie("Legends of the Fall", 4.7)
their_movie = Movie("aFGDSFGSDFGSD", 4.7)


print(my_movie.id)
print(your_movie.id)
print(their_movie.id)
print(Movie.id_counter)

my_movie.print_title()

restart()

# my_movie.print_title_2()


# func = (x, y) => {print(x, y)}
func = lambda x, y: print(x, y)
# def func(x, y):
#     print(x, y)


print(Movie.latest_title)
print(Movie.movie_counter)
