# BackendAssignment 


## Requirements

- Python 3.11.6
- Django 4.2.5
- Django REST Framework


## Installation

### After cloning the repository, it is advisable to create a virtual environment to ensure a clean Python installation. This can be done by running the following command:

```
python -m venv env
```

### After creating the virtual environment, it is necessary to activate it. You can find more information about this process
### You can install all the required dependencies by running the following command:

```
pip install -r requirements.txt
```


## API Usage
Identify or Create Contact
This endpoint is used to identify or create a contact based on provided email and phone number. If the contact already exists, it returns the contact details including primary and secondary contact IDs, emails, and phone numbers. If the contact is new, it creates a new contact with the provided information.

Endpoint: `/api/identify/`

## Test URL
`http://127.0.0.1:8000/api/identify/`