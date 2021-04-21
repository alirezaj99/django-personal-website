from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import Contact


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            full_name = contact_form.cleaned_data.get("full_name")
            email = contact_form.cleaned_data.get("email")
            message = contact_form.cleaned_data.get("message")
            Contact.objects.create(full_name=full_name, email=email, message=message)
            contact_form = Contact()
            return redirect('/success-send-message')
    else:
        contact_form = ContactForm()

    context = {
        "contact_form": contact_form
    }
    return render(request, "contact/contact.html", context)


def success_contact(request):
    context = {

    }
    return render(request, "contact/success_send_message.html", context)
