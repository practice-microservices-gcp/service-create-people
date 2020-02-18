from datasources.mysql_datasource import mysqlDataSource
from string import Template

class PeopleRepository:

    def createPerson(self, name, surname, email):
        insertQuery = Template("""
        INSERT INTO people.people (name, surname, email)
        VALUES ("$name", "$surname", "$email")
        """).safe_substitute({
            'name': name,
            'surname': surname,
            'email': email
        })

        connection = mysqlDataSource.getConnection()
        cursor = mysqlDataSource.getCursor()

        cursor.execute(insertQuery)
        connection.commit()

        mysqlDataSource.closeConnection()

peopleRepository = PeopleRepository()