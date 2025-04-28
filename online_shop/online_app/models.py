from django.db import models

# Create your models here.

from django.contrib.auth.models import User # To know WHO is selling

class Item(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE) # Link to the user selling it
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2) # Like $9.99
    image = models.ImageField(upload_to='item_images/') # Where to save the picture!
    created_at = models.DateTimeField(auto_now_add=True) # When it was added

    def __str__(self):
        return self.name

# online_app/models.py (Add this class)
class Comment(models.Model):
    item = models.ForeignKey(Item, related_name='comments', on_delete=models.CASCADE) # Which item?
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Who wrote it?
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.item}'
