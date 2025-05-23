from django.db import models

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True, primary_key=True) 
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"

    def to_dict(self):
        """Converte o objeto Book para um dicionário."""
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'year': self.year,
        }
