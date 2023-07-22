from django.db import models

class Category(models.Model):
    # Model for the category of a photo
    
    name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.name

class Photo(models.Model):
    # Model for a photo
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    # ForeignKey relationship with the Category model. A photo can belong to a category.
    # If the category is deleted, the photos associated with it will be set to null.
    # The category can be blank for a photo, allowing it to be added without a category.
    
    image = models.ImageField(null=False, blank=False)
    # ImageField for storing the photo image. It cannot be null or blank.
    
    description = models.TextField()
    # TextField for storing the description of the photo.
    
    def __str__(self):
        return self.description
