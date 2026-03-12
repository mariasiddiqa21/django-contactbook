from django.shortcuts import render, redirect
from .models import Contact


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})


def add_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone
        )

        return redirect('contact_list')

    return render(request, 'contacts/add_contact.html')


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
