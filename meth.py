from flask import send_file
from requests import get

def getIp():
    ip = get('https://api.ipify.org?format=js').text

    location_URL = f'http://ip-api.com/json/{ip}'

    return ip

#TODO
def download():
        path = 'C:\Code\IPPuller\command.cmd'

        return send_file(path, as_attachment=False)

