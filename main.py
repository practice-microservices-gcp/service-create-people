import flask

from controllers.create_person_controller import createPerson

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

    response = createPerson(name, surname, email)

    web_response = flask.Response(
        response.body.to_json(),
        status=response.code
    )

    web_response.headers['Content-Type'] = 'application/json'

    return web_response