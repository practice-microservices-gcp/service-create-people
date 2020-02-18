
class PersonFacade():

    def _valuesValidation(self, value):
        return (value is not None) and (len(value) > 0)

    def personValidation(self, name, surname, email):
        nameValidation = self._valuesValidation(name)
        surnameValidation = self._valuesValidation(surname)
        emailValidation = self._valuesValidation(email)

        return nameValidation and surnameValidation and emailValidation


personFacade = PersonFacade()

    