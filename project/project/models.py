from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    category = models.TextField()
    
    def __str__(self):
        return self.name
    
class Tag (models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Post (models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title
    

class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Commented by {self.name} on {self.post}'
    
class Profile (models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    # profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
    def __str__(self):
        return 'Admin Profile'
    
    