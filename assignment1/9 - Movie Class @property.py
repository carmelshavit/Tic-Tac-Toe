"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating: float | int = rating

    @property
    def rating(self) -> int | float:
        print("Calling the getter...")
        return self._rating
    
    @rating.setter
    def rating(self, new_rating: float | int):
        """
        raises ValueError if new rating it now between 1-5
        :param new_rating: must be value between 1 and 5
        :return:
        """
        # if isinstance(new_rating, (float, int)):
        if 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            raise ValueError("new_rating must be between 1 and 5")




favorite_movie = Movie("Titanic", 4.3)
# print(favorite_movie.rating)

favorite_movie.rating = 4.5
# print(favorite_movie.rating)

new_rating = 10
while True:
    try:
        favorite_movie.rating = new_rating  # Invalid value.
        break
    except ValueError:
        print(f"Invalid rating {new_rating}, decreasing value by 1")
        new_rating -= 1

print(favorite_movie.rating)

