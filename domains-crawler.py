import requests

# URLs to fetch the latest files
domains_url = "https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/main/data/domains.txt"
wildcards_url = "https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/main/data/wildcards.txt"

# Local files to store domains and wildcards
domains_file = "domains.txt"
wildcards_file = "wildcards.txt"

# Telegram bot settings
bot_token = "<bot_token>"
chat_id = "<chat_id>"

# Fetch the contents of the domains URL
domains_response = requests.get(domains_url)

# Parse the response for the domains
domains = set()
for line in domains_response.text.splitlines():
    line = line.strip()
    if line and not line.startswith("#"):
        domains.add(line.lower())

# Open the domains local file for reading
with open(domains_file, "r") as f:
    existing_domains = set(line.strip().lower() for line in f)

# Add new domains to the local file
new_domains = domains - existing_domains
if new_domains:
    with open(domains_file, "a") as f:
        for domain in new_domains:
            f.write(domain + "\n")
    # Send new domains to Telegram channel using bot
    message = f"{len(new_domains)} new domains added to {domains_file}:\n" + "\n".join(sorted(new_domains))
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    telegram_params = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(telegram_url, data=telegram_params)
else:
    print(f"No new domains found in {domains_url}.")

# Fetch the contents of the wildcards URL
wildcards_response = requests.get(wildcards_url)

# Parse the response for the wildcards
wildcards = set()
for line in wildcards_response.text.splitlines():
    line = line.strip()
    if line and not line.startswith("#"):
        wildcards.add(line.lower())

# Open the wildcards local file for reading
with open(wildcards_file, "r") as f:
    existing_wildcards = set(line.strip().lower() for line in f)

# Add new wildcards to the local file
new_wildcards = wildcards - existing_wildcards
if new_wildcards:
    with open(wildcards_file, "a") as f:
        for wildcard in new_wildcards:
            f.write(wildcard + "\n")
    # Send new wildcards to Telegram channel using bot
    message = f"{len(new_wildcards)} new wildcards added to {wildcards_file}:\n" + "\n".join(sorted(new_wildcards))
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    telegram_params = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(telegram_url, data=telegram_params)
else:
    print(f"No new wildcards found in {wildcards_url}.")