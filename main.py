from controllers.create_person_controller import createPerson
from response_decorator.response_decorator import http_response

@http_response
def create_person(request):
    name = None
    surname = None
    email = None

    body = request.get_json()

    if body and 'name' in body:
        name = body['name']

    if body and 'surname' in body:
        surname = body['surname']

    if body and 'email' in body:
        email = body['email']

    return createPerson(name, surname, email)