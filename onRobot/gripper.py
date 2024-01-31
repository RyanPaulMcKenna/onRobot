import requests
import xmlrpc.client

class RG2:
    def __init__(self, rg_id: int = 0) -> None:
        self.rg_id = rg_id

    def get_rg_width(self) -> float:
        xml_request = f"""<?xml version="1.0"?>
    <methodCall>
        <methodName>rg_get_width</methodName>
            <params>
                <param>
                    <value><int>{self.rg_id}</int></value>
                </param>
            </params>
    </methodCall>"""

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = xml_request.replace('\r\n','').encode()
        try:
            response = requests.post('http://192.168.0.99:41414', headers=headers, data=data)

            if (response.status_code==200):
                #print(response.text)
                xml_response = xmlrpc.client.loads(response.text)
                rg_width = float(xml_response[0][0])
                #print(rg_width)
                return rg_width
        except requests.HTTPError as e:
            # should actually write this to ros logs, I think?
            print("XMLRPC-HTTP Error: ",e)

    def rg_grip(self, target_width: float = 100, target_force: float= 10) -> bool:
        #assert target_width <= 100 and target_width >= 0, 'Target Width must be within the range [0,100]'
        #assert target_force <= 40 or target_force >= 0, 'Target force must be within the range [0,40]'

        # WARNING: params will be sent straight to electrical system with no error checking on robot!
        if (target_width > 100):
            target_width = 100
        if(target_width < 0):
            target_width = 0
        if(target_force > 40):
            target_force = 40
        if(target_force < 0):
            target_force = 0

        xml_request = f"""<?xml version="1.0"?>
    <methodCall>
    <methodName>rg_grip</methodName>
        <params>
            <param>
                <value><int>{self.rg_id}</int></value>
            </param>
            <param>
                <value><double>{target_width}</double></value>
            </param>
            <param>
                <value><double>{target_force}</double></value>
            </param>
        </params>
    </methodCall>"""

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = xml_request.replace('\r\n','').encode()
        try:
            response = requests.post('http://192.168.0.99:41414', headers=headers, data=data)

            if (response.status_code==200):
                #print(response.text)
                #xml_response = xmlrpc.client.loads(response.text)
                return True
            else:
                return False
                
        except requests.HTTPError as e:
            # should actually write this to ros logs, I think?
            print("XMLRPC-HTTP Error: ",e)

