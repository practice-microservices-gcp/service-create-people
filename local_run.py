from controllers.create_person_controller import createPerson

response = createPerson('Silvia', 'Arnaiz', 'silvia@mail.com') 
print ("Code: {}".format(response.code))
print ("Body: {}".format(response.body.to_json()))


