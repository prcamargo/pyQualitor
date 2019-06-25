
# PyQualitor #

**PyQualitor** é um modulo em Python para utilizar o Web Service do Central de Serviço [Qualitor](https://www.qualitor.com.br).

Modulo expirado no [pyzabbix](https://github.com/lukecyca/pyzabbix)

## Requerimentos
* Qualitor 8
* Python 3.7.3

### Instalação

Instalar PyQabbix usando pip:

```bash
$ pip install pyQualitor
```

### Exemplo:
#####Iniciar um chamado:

```python
import pyQualitor

qapi = pyQualitor(url='https://qualitor.com.br/qualitor/WSTicket.wsdl',
                    user='login', 
                    password='password', 
                    empresa='1')
                    
qapi.startTichek(cdchamado='22222')

```

Return xml:
````bash



````
