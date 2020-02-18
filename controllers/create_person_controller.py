from repositories.people_repository import peopleRepository
from entities.response_entity import ResponseEntity
from entities.message_entity import MessageEntity
from facades.person_facade import personFacade
from responses import responses

import traceback

def createPerson(name, surname, email):

    try:

        if (not personFacade.personValidation(name, surname, email)):
            raise responses.WrongRequest
        
        peopleRepository.createPerson(name, surname, email)
        message = MessageEntity(responses.http_responses['UserCreated']['message'])
        return ResponseEntity(responses.http_responses['UserCreated']['code'], message)
    except responses.WrongRequest:
        message = MessageEntity(responses.http_responses['WrongRequest']['message'])
        return ResponseEntity(responses.http_responses['WrongRequest']['code'], message)
    except Exception:
        print(traceback.format_exc())
        message = MessageEntity(responses.http_responses['UnexpectedError']['message'])
        return ResponseEntity(responses.http_responses['UnexpectedError']['code'], message)
