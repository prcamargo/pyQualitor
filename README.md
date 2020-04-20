
# PyQualitor #

**pyQualitor** é um modulo em Python para utilizar o Web Service do Central de Serviço [Qualitor](https://www.qualitor.com.br).

Modulo inspirado no [pyzabbix](https://github.com/lukecyca/pyzabbix)

## Requerimentos
* Qualitor 8
* Python 3.7.3

### Instalação

Instalar PyQabbix usando pip:

```bash
$ pip install pyQualitor
```

### Exemplo:

* Iniciar um chamado:

```python
from pyQualitor import QualitorWS

qws = QualitorWS('https://qualitor.com.br/qualitor/WSTicket.wsdl')

qws.login(login='login', password='password')
        
qws.startTicket(cdchamado='22222')


```

Return xml:
````bash



````
