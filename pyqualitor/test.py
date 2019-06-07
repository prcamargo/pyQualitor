from __init__ import QualitorAPI

qapi = QualitorAPI('https://qltapi.vantix.com.br/qualitor/ws/services/service.php?wsdl=WSTicket')

print(qapi.Token('ws.vantix', 'qlt@1!@#', 1))

#qapi.Ticket.closeTicket(cdchamado='', idfecharrelacionados='Y')