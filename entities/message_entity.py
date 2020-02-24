from entity_decorator.entity_decorator import serializable

@serializable
class MessageEntity():

    def __init__(self,message):
        self.message = message