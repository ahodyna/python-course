class Book:
    def __init__(self, title, author, pages):
      self.title = title
      self.author = author
      self.pages = pages
      self._reviews = []

    def get_summary(self):
         return f'Title: {self.title}, Author: {self.author},Pages: {self.pages}'

    def __str__(self):
        return self.get_summary()

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __len__(self):
        return self.pages

    @classmethod
    def from_string(cls, book_value):
        try:
            title, author, pages = book_value.split(" - ")
            return cls(title, author, int(pages))
        except ValueError:
            raise ValueError("Invalid format.")

    def add_review(self, number):
        if not (0 <= number <= 5):
            raise ValueError("Error")
        self._reviews.append(number)

    @property
    def rating(self):
        if not self._reviews:
            return "No reviews"
        return sum(self._reviews) / len(self._reviews)

class Comic(Book):
    def get_summary(self):
        original_summary = super().get_summary()
        return f"Genre: Comic, {original_summary}"
