from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    description = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title
    
