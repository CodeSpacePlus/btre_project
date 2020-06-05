from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from btre.settings import EMAIL_USER
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing = request.POST['listing_title']
        listing_id = request.POST['listing_id']
        realtor_email = request.POST['realtor_email']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        # User has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contact = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contact:
                messages.error(request, 'Inquiry already submitted.')
                return redirect('/listings/' + listing_id)

        new_contact = Contact.objects.create(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        new_contact.save()

        send_mail(
            'Porperty Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into admin panel for more info.',
            EMAIL_USER,
            [realtor_email, 'AllInquiries@btrealtors.co'],
            fail_silently=True
        )

        messages.success(request, "Your inquiry has been successfully submitted.")
        return redirect('/listings/' + listing_id)
    return redirect('listings')
