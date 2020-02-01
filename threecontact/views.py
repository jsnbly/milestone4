from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Contact
from .forms import ContactForm

# Create your views here.

def contact_detail(request, pk):
    #view to return a single post based on post id

    contact = get_object_or_404(Contact, pk=pk)
    contact.save()
    return render(request, "success.html", {'contact':contact})

def create_contact(request,pk=None):
    #view to take contact form into database
    contact = get_object_or_404(Contact, pk=pk) if pk else None
    if request.method == "POST":
            form = ContactForm(request.POST, request.FILES, instance=contact)
            if form.is_valid():
                contact = form.save()
                return redirect(contact_detail, contact.pk)
                #return redirect(request, 'success.html')
    else:
            form = ContactForm(instance=contact)
    return render(request, 'contact.html', {'form':form})