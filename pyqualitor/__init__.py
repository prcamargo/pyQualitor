import logging
from zeep import Client
'''
url = 'https://qltapi.vantix.com.br/qualitor/ws/services/service.php?wsdl=WSTicket'

client = Client(url)

token = client.service.login('ws.vantix', 'qlt@1!@#', '1')
print(totken)
'''

class QualitorAPI(object):
    def __init__(self, url=''):
        self.url = url

    def Token(self, login,password, empresa):
        self.login = login
        self.password = password
        self.empresa = empresa

        client = Client(self.url)
        return client.service.login(login, password, empresa)


class Ticket(object):
    def __init__(self,)

    

