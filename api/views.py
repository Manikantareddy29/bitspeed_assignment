from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Contact
from django.db.models import Q

@api_view(['POST'])
def identify(request):
    email = request.data.get('email')
    phone_number = request.data.get('phoneNumber')

    if not email and not phone_number:
        return Response({"error": "Email or phone number is required"}, status=status.HTTP_400_BAD_REQUEST)

    contacts = Contact.objects.filter(Q(email=email) | Q(phone_number=phone_number))

    if contacts.exists():
        primary_contact = min(contacts, key=lambda contact: contact.created_at)
        secondary_contacts = [contact for contact in contacts if contact.id != primary_contact.id]

        if (email and not primary_contact.email) or (phone_number and not primary_contact.phone_number):
            new_secondary = Contact(
                email=email,
                phone_number=phone_number,
                linked_id=primary_contact.id,
                link_precedence="secondary"
            )
            new_secondary.save()
            secondary_contacts.append(new_secondary)

        response = {
            "contact": {
                "primaryContactId": primary_contact.id,
                "emails": [primary_contact.email] + [contact.email for contact in secondary_contacts if contact.email],
                "phoneNumbers": [primary_contact.phone_number] + [contact.phone_number for contact in secondary_contacts if contact.phone_number],
                "secondaryContactIds": [contact.id for contact in secondary_contacts],
            }
        }
    else:
        primary_contact = Contact(
            email=email,
            phone_number=phone_number,
            link_precedence="primary"
        )
        primary_contact.save()
        response = {
            "contact": {
                "primaryContactId": primary_contact.id,
                "emails": [primary_contact.email],
                "phoneNumbers": [primary_contact.phone_number],
                "secondaryContactIds": [],
            }
        }

    return Response(response, status=status.HTTP_200_OK)
