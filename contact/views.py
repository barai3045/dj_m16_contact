from django.shortcuts import get_object_or_404, render, redirect

from .forms import ContactForm
from .models import Contact

# Create your views here.
def home(request):
    contacts = Contact.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, "contact/home.html", context)


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            employee = form.save()
            
            
            return redirect('home')
    else:
        form = ContactForm()
    context = {
        'form': form
    }

    return render(request, "contact/add.html", context)



def view_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    

    context = {
        'contact': contact
    }

    return render(request, "contact/view.html", context)


def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('view_contact', pk)
    else:
        form = ContactForm(instance=contact)

    context = {
        'form': form, 
        'contact': contact
    }

    return render(request, "contact/update.html", context)


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('home')
    
    context = {
        'contact': contact
    }
    return render(request, 'contact/delete.html', context )