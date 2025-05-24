# Custom exception handler for Django REST Framework (DRF).
# Ensures all error responses follow a consistent JSON format.
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Standardizes API error responses.
    response = exception_handler(exc, context)
    
    if response is not None:
        custom_response_data = {
            'error': 'An error occurred',
            'details': response.data
        }
        response.data = custom_response_data
    return response
