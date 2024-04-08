# Dynamic DNS Updater

This repository contains a Python scipt that checks your current public IP address and updates a DNS record on DigitalOcean if you IP has changed. This allows you to maintain a consistent domain name or subdomain that always points to your current public IP, even if it changes frequently.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)
- DigitalOcean account and API token

## Setup

1. Clone the repostiory or download the script.
2. Install the required Python dependencies: `pip install requests`
3. Set the following Environment Variables
    - `DO_API_TOKEN`: Your DigitialOcean API token
    - `DOMAIN_NAME`: Your domain name (eg. `example.com`)
    - `RECORD_NAME`: The subdomain name (eg. `subdomain` for `subdomain.example.com`)

## Usage

1. Run the script manually to update the DNS record with your current public IP:
```
python dynamic_dns_updater.py
```

2. To automatically update the DNS record perodically, set up a cron job or task scheduler to run the script at desired intervals (eg. every hour or every day).

The script will retrieve your current public IP address via ipify.org, check if it has changed from the previously stored IP, and update the specified DNS record on DigitalOcean with the new IP if necessary.

License

This project is licensed under the Apache License.


