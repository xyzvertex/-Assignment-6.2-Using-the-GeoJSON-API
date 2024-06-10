import urllib.request, urllib.parse
import json, ssl
import re

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
        print()

    except:
        js = None

    if not js or 'plus_code' not in js:
        print()
    line = data

    pattern = r'"plus_code":"([^"]+)"'

    match = re.search(pattern, line)

    if match:
        plus_code_short = match.group(1)
        print("Plus Code :", plus_code_short)
    else:
        print("Plus Code Short not found.")
    break
