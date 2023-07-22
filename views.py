from sre_parse import CATEGORIES  # Importing CATEGORIES from sre_parse module
from django.shortcuts import render, redirect
from .models import Category, Photo
from django.shortcuts import render, get_object_or_404
from .models import Photo

def gallery(request):
    category_name = request.GET.get('category')  # Retrieve the category name from the URL query parameters
    if category_name is None:  # Check if no category is specified
        photos = Photo.objects.all()  # Retrieve all photos
    else:
        photos = Photo.objects.filter(category__name=category_name)  # Filter photos based on the specified category

    categories = Category.objects.all()  # Retrieve all categories

    context = {'categories': categories, 'photos': photos}  # Create context data to pass to the template
    return render(request, 'photos/gallery.html', context)  # Render the gallery template with the context data

def viewPhoto(request, pk):
    photo = get_object_or_404(Photo, id=pk)  # Retrieve the specific photo based on the provided primary key
    return render(request, 'photos/photo.html', {'photo': photo})  # Render the photo template with the photo data

def addPhoto(request):
    categories = Category.objects.all()  # Retrieve all categories

    if request.method == 'POST':
        data = request.POST  # Retrieve the submitted form data
        image = request.FILES.get('image')  # Retrieve the uploaded image file

        if data['category'] != 'none':
            selected_category = Category.objects.get(id=data['category'])  # Retrieve the selected category from the form
        elif data['category_new'] != '':
            selected_category, created = Category.objects.get_or_create(name=data['category_new'])  # Create a new category if specified
        else:
            selected_category = None

        photo = Photo.objects.create(
            category=selected_category,
            description=data['description'],
            image=image,
        )  # Create a new photo object with the provided data
        return redirect('gallery')  # Redirect to the gallery page after successfully adding the photo

    context = {'categories': categories}  # Create context data to pass to the template
    return render(request, 'photos/add.html', context)  # Render the add photo template with the context data
