from __future__ import unicode_literals
from django.db import models
from ..users.models import User

# Create your models here.
class MessageManager(models.Manager):
    def message_validator(self, postData, u_id, c_id):
        errors = []
        if len(postData['message']) < 1:
            errors.append("Please enter a message")

        if not errors:
            new_message = Message.objects.create(
                message=postData['message'],
                user_id=u_id,
                commenter_id=c_id
            )
            return new_message
        return errors

class CommentManager(models.Manager):
    def comment_validator(self, postData, u_id, c_id, msg_id):
        errors = []
        if len(postData['comment']) < 1:
            errors.append("Please enter a comment")

        if not errors:
            new_comment = Comment.objects.create(
                comment=postData['comment'],
                message_id=msg_id,
                user_id=u_id,
                commenter_id=c_id
            )
            return new_comment
        return errors

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="messages")
    commenter = models.ForeignKey(User, related_name="messagefroms")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class Comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Message, related_name="comments")
    user = models.ForeignKey(User, related_name="comments")
    commenter = models.ForeignKey(User, related_name="commentfroms")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
