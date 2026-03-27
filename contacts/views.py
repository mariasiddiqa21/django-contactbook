from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.db.models import Q


def contact_list(request):
    
    query = request.GET.get('q')

    if query:
        contacts = Contact.objects.filter(
            Q(name__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query)
        )
    else:
        contacts = Contact.objects.all()

    return render(request, 'contacts/contact_list.html', {'contacts': contacts})


def add_contact(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            


            return redirect('contact_list')
        else:
            print(form.errors)
        
    else:
        form = ContactForm()


    return render(request, 'contacts/add_contact.html', {'form': form})


def contact_detail(request, id):
    contact = Contact.objects.get(id=id)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})


def delete_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('contact_list')


def update_contact(request, id):
    contact = Contact.objects.get(id=id)

    if request.method == 'POST':
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')

        contact.save()

        return redirect('contact_list')

    return render(request, 'contacts/update_contact.html', {'contact': contact})
