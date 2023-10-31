from django.shortcuts import render
from apps.geeks.models import Settings, Contact,Gallery
# Create your views here.
def index(request):
    settings = Settings.objects.latest("id")
    gallery  = Gallery.objects.all()
    return render(request, "index_2.html", locals())

def contact(request):
    contact = Contact.objects.latest("id")
    return render(request, "contact.html", locals()) 
