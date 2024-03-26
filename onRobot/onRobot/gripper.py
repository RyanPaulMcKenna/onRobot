import pycurl
import xmlrpc.client
from io import BytesIO

# https://onrobot.com/sites/default/files/documents/VG10_Vacuun_Gripper_User_Manual_V1.1.1.pdf
class VG10:
    def __init__(self, robot_ip, vg_id):
        self.vg_id = vg_id
        self.robot_ip = robot_ip

    def vg10_release(self, channelA: bool = True, channelB: bool = True):
        
        self.channelA = channelA # True/False
        self.channelB = channelB # True/False
  
        xml_request = f"""<?xml version="1.0"?>
        <methodCall>
        <methodName>vg10_release</methodName>
            <params>
                    <param>
                    <value><int>{self.vg_id}</int></value>
                    </param>
                    <param>
                    <value><boolean>{self.channelA}</boolean></value>
                    </param>
                    <param>
                    <value><boolean>{self.channelB}</boolean></value>
                    </param>
            </params>
        </methodCall>"""

        headers = ["Content-Type: application/x-www-form-urlencoded"]

        # headers = ["User-Agent: Python-PycURL", "Accept: application/json"]
        data = xml_request.replace('\r\n','').encode()
        # Create a new cURL object
        curl = pycurl.Curl()

        # Set the URL to fetch
        curl.setopt(curl.URL, f'http://{self.robot_ip}:41414')
        curl.setopt(curl.HTTPHEADER, headers)
        curl.setopt(curl.POSTFIELDS, data)
        # Create a BytesIO object to store the response
        buffer = BytesIO()
        curl.setopt(curl.WRITEDATA, buffer)

        # Perform the request
        curl.perform()

        # Get the response body
        response = buffer.getvalue()

        # Print the response
        print(response.decode('utf-8'))

        # Close the cURL object
        curl.close()

    def vg10_grip(self, channel, vacuum_percent):
        
        self.channel = channel # 0,1,2
        self.vacuum_percent = vacuum_percent # softgrip => 30 = 30%, firm grip => 60 = 60%

        xml_request = f"""<?xml version="1.0"?>
        <methodCall>
        <methodName>vg10_grip</methodName>
            <params>
                <param>
                    <value><int>{self.vg_id}</int></value>
                </param>
                <param>
                    <value><int>{self.channel}</int></value>
                </param>
                <param>
                    <value><double>{self.vacuum_percent}</double></value>
                </param>
            </params>
        </methodCall>
        """

        headers = ["Content-Type: application/x-www-form-urlencoded"]

        # headers = ["User-Agent: Python-PycURL", "Accept: application/json"]
        data = xml_request.replace('\r\n','').encode()
        # Create a new cURL object
        curl = pycurl.Curl()

        # Set the URL to fetch
        curl.setopt(curl.URL, f'http://{self.robot_ip}:41414')
        curl.setopt(curl.HTTPHEADER, headers)
        curl.setopt(curl.POSTFIELDS, data)
        # Create a BytesIO object to store the response
        buffer = BytesIO()
        curl.setopt(curl.WRITEDATA, buffer)

        # Perform the request
        curl.perform()

        # Get the response body
        response = buffer.getvalue()

        # Print the response
        print(response.decode('utf-8'))

        # Close the cURL object
        curl.close()


class RG2:
    def __init__(self, robot_ip, rg_id):
        self.rg_id = rg_id
        self.robot_ip = robot_ip

    def get_rg_width(self):
        xml_request = f"""<?xml version="1.0"?>
    <methodCall>
        <methodName>rg_get_width</methodName>
            <params>
                <param>
                    <value><int>{self.rg_id}</int></value>
                </param>
            </params>
    </methodCall>"""

        headers = ["Content-Type: application/x-www-form-urlencoded"]

        data = xml_request.replace('\r\n','').encode()

        # Create a new cURL object
        curl = pycurl.Curl()

        # Set the URL to fetch
        curl.setopt(curl.URL, f'http://{self.robot_ip}:41414')
        curl.setopt(curl.HTTPHEADER, headers)
        curl.setopt(curl.POSTFIELDS, data)
        # Create a BytesIO object to store the response
        buffer = BytesIO()
        curl.setopt(curl.WRITEDATA, buffer)

        # Perform the request
        curl.perform()

        # Get the response body
        response = buffer.getvalue()

        # Print the response
        print(response.decode('utf-8'))

        # Close the cURL object
        curl.close()

        xml_response = xmlrpc.client.loads(response.decode('utf-8'))
        rg_width = float(xml_response[0][0])
        #print(rg_width)
        return rg_width


    def rg_grip(self, target_width: float = 100, target_force: float= 10) -> bool:
        #assert target_width <= 100 and target_width >= 0, 'Target Width must be within the range [0,100]'
        #assert target_force <= 40 or target_force >= 0, 'Target force must be within the range [0,40]'

        # WARNING: params will be sent straight to electrical system with no error checking on robot!
        # if (target_width > 100):
        #     target_width = 100
        # if(target_width < 0):
        #     target_width = 0
        # if(target_force > 40):
        #     target_force = 40
        # if(target_force < 0):
        #     target_force = 0

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

        headers = ["Content-Type: application/x-www-form-urlencoded"]

        # headers = ["User-Agent: Python-PycURL", "Accept: application/json"]
        data = xml_request.replace('\r\n','').encode()
        # Create a new cURL object
        curl = pycurl.Curl()

        # Set the URL to fetch
        curl.setopt(curl.URL, f'http://{self.robot_ip}:41414')
        curl.setopt(curl.HTTPHEADER, headers)
        curl.setopt(curl.POSTFIELDS, data)
        # Create a BytesIO object to store the response
        buffer = BytesIO()
        curl.setopt(curl.WRITEDATA, buffer)

        # Perform the request
        curl.perform()

        # Get the response body
        response = buffer.getvalue()

        # Print the response
        print(response.decode('utf-8'))

        # Close the cURL object
        curl.close()

def main():

    # Default id is zero, if you have multiple grippers, 
    # see logs in UR Teach Pendant to know which is which :)
    print("Main")
    rg_id = 0
    ip = "192.168.56.101"
    rg_gripper = RG2(ip,rg_id)

    rg_width = rg_gripper.get_rg_width()
    print("rg_width: ",rg_width)
    
    target_force = 40.00

    rg_gripper.rg_grip(100.0, target_force)



if __name__ == "__main__":
    main()