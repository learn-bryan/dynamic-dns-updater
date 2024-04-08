import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# DigitalOcean API credentials
DO_API_TOKEN = os.getenv('DO_API_TOKEN')
DOMAIN_NAME = os.getenv('DOMAIN_NAME')
RECORD_NAME = os.getenv('RECORD_NAME')

# Read previously stored IP address from a file
try:
    with open('previous_ip.txt', 'r') as f:
        previous_ip = f.read().strip()
except FileNotFoundError:
    previous_ip = ''

# Get current public IP
public_ip = requests.get('https://api.ipify.org').text

# If the IP has changed, update the DNS record
if public_ip != previous_ip:
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {DO_API_TOKEN}',
    }

    # Get the record ID for the specific DNS record
    records = requests.get(f'https://api.digitalocean.com/v2/domains/{DOMAIN_NAME}/records', headers=headers).json()['domain_records']


    # Find the record ID for the specific DNS record
    record_id = None
    for record in records:
        if record['type'] == 'A' and record['name'] == f'{RECORD_NAME}':
            record_id = record['id']
            break

    # If the record is found, update it with the new IP
    if record_id:
        data = {'data': public_ip}
        requests.put(f'https://api.digitalocean.com/v2/domains/{DOMAIN_NAME}/records/{record_id}', headers=headers, json=data)
        # Store the new IP address for future comparisons
        with open('previous_ip.txt', 'w') as f:
            f.write(public_ip)
        print(f"DNS record '{RECORD_NAME}.{DOMAIN_NAME}' was updated to {public_ip}.")
    else:
        print(f"DNS record '{RECORD_NAME}.{DOMAIN_NAME}' not found.")

else:
    print(f'IP has not changed: {public_ip}')
