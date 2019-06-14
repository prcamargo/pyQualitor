from zeep import Client
import xml.etree.ElementTree as ET

class QualitorAPI:

    def __init__(self,
                 url='',
                 user='',
                 password='',
                 empresa=1
    ):

        if not url:
            raise ValueError ('No URL given for the wsdl')

        self.url = url
        self.user = user
        self.password = password
        self.empresa = empresa

        self.client = Client(self.url)

        self.token = self.client.service.login(self.user, self.password, self.empresa)

    def request(self,method,xml):

        return self.client.service.__getitem__(method)(self.token, xml)


    def __getattr__(self, attr):

        return QualitorAPIObjectClass(attr, self)


class QualitorAPIObjectClass(object):

        def __init__(self, method, parent):
            self.method = method
            self.parent = parent

        def __getattr__(self, attr):

            def fn(**kwargs):
                wsqualitor = ET.Element('wsqualitor')
                contents = ET.SubElement(wsqualitor, 'contents')
                data = ET.SubElement(contents, 'data')
                for key, value in kwargs.items():
                    key = ET.SubElement(data, key)
                    key.text = value

                    #create var XML
                    cxml = ET.tostring(wsqualitor)

                return self.parent.request(self.method,cxml)

            return fn
