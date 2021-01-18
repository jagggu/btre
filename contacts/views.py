from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail




def contact(request):
    if request.method == 'POST':
        listing = request.POST.get('listing')
        listing_id = request.POST.get('listing_id')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(user_id=user_id, listing_id=listing_id)
            if has_contacted:
                messages.error(request, "You have already made an inquiry on this property")
                return redirect('/listings/'+listing_id)


        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, user_id=user_id, message=message)
        contact.save()

        send_mail(
            'Property Listing Inquiry',
            'There has been a inquiry for the ' + listing + '. Please sign in to admin panel for more info.',
            'jagadeesh.vedas@gmail.com',
            [realtor_email,'chandragiriumareddy@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been to the realtor, he/she will get back to you soon')

        return redirect('/listings/'+ listing_id)
    else:
        return redirect('listings')