"""Movie entities module."""


class Movie:

    def __init__(self, title: str, year: int, director: str):
        self.title = title
        self.year = year
        self.director = director

    def __repr__(self):
        return "{0}(title={1}, year={2}, director={3})".format(
            self.__class__.__name__,
            repr(self.title),
            repr(self.year),
            repr(self.director),
        )
