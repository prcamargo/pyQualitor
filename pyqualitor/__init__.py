from zeep import Client
from zeep.transports import Transport
from requests import Session
import xml.etree.ElementTree as ET


class QualitorWS(object):

    def __init__(self,wsdl):

        self.wsdl = wsdl

        if not wsdl:
            raise ValueError ('No URL given for the wsdl')

    def login(self, login='', password='', company='1', verify=False):

        self.login = login
        self.password = password
        self.company = company
        self.verify = verify

        if verify == False:

            import warnings
            warnings.filterwarnings('ignore', message='Unverified HTTPS request')

            session = Session()
            session.verify = False
            transport = Transport(session=session)

            '''Gerando token'''
            self.client = Client(self.wsdl, transport=transport)

        self.token = self.client.service.login(self.login, self.password, self.company)

    def request(self,method,xml):

        return self.client.service.__getitem__(method)(self.token,xml)

    def __getattr__(self, attr):

        def fn(*args, **kwargs):

            wsqualitor = ET.Element('wsqualitor')
            contents = ET.SubElement(wsqualitor, 'contents')
            data = ET.SubElement(contents, 'data')
            for key, value in kwargs.items():
                key = ET.SubElement(data, key)
                key.text = value

            cxml = ET.tostring(wsqualitor)

            return self.request(attr,cxml)

        return fn