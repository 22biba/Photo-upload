from django.apps import AppConfig

class PhotosConfig(AppConfig):
    # Define the configuration for the "photos" app
    
    # Specify the default auto-generated field for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Specify the name of the app
    name = 'photos'
