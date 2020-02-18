http_responses = {
    'UserCreated': {
        'message': 'User created successfully',
        'code': '201'
    },
    'WrongRequest': {
        'message': 'Wrong parameters in the request',
        'code': '400'
    },
    'UnexpectedError': {
        'message': 'There is a problem with the data base. Please try later',
        'code': '500'
    }
}

class WrongRequest(Exception):
    pass