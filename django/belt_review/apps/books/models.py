from __future__ import unicode_literals
from django.db import models
from ..users.models import User

# Create your models here.
class BookManager(models.Manager):
    def book_validator(self, postData, u_id):
        errors = []
        if len(postData['title']) < 1:
            errors.append("You must enter a book name")
        if postData['author'] == 'none' and len(postData['new_author']) < 1:
            errors.append("You must enter an author")
        if len(postData['review']) < 1:
            errors.append("Your review cannot be blank")
        if len(postData['rating']) < 1:
            errors.append("Your rating cannot be blank")

        if not errors:
            if postData['author'] == 'none':
                author = postData['new_author']
                new_author = Author.objects.create(
                    name = author
                )
            else:
                author = postData['author']

            auth = Author.objects.get(name=author)

            new_book = self.create(
                title=postData['title'],
                author_id=auth.id,
            )

            bk = self.get(title=postData['title'])

            new_review = Review.objects.create(
                review=postData['review'],
                rating=postData['rating'],
                book_id=bk.id,
                user_id=u_id
            )
            return new_book
        return errors

    def review_validator(self, postData, u_id, book_id):
        errors = []
        if len(postData['review']) < 1:
            errors.append("Your review cannot be blank")
        if len(postData['rating']) < 1:
            errors.append("Your rating cannot be blank")

        if not errors:
            new_review = Review.objects.create(
                review=postData['review'],
                rating=postData['rating'],
                book_id=book_id,
                user_id=u_id
            )
            return new_review
        return errors

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name="reviews")
    user = models.ForeignKey(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
