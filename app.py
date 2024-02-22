import requests
import os

def get_ip_info(ip_address):
    url = f"https://api.bgpview.io/ip/{ip_address}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['status'] == "ok":
            return data
        else:
            print("Query was successful but returned an unexpected status:", data['status_message'])
            return None
    else:
        print("Failed to retrieve data, HTTP status code:", response.status_code)
        return None

def print_ip_info(ip_info):
    if ip_info and 'data' in ip_info:
        data = ip_info['data']
        
        print("Prefixes:")
        for prefix in data['prefixes']:
            ip = prefix['ip']
            cidr = prefix['cidr']
            asn = prefix['asn']
            print(f"  Prefix: {prefix['prefix']}")
            print(f"  IP: {ip}")
            print(f"  CIDR: {cidr}")
            print(f"  ASN: {asn['asn']}")
            print(f"  ASN Name: {asn['name']}")
            print(f"  ASN Description: {asn['description']}")
            print(f"  Country Code: {prefix['country_code']}")
            print("")

        print("RIR Allocation:")
        rir_allocation = data['rir_allocation']
        print(f"  RIR Name: {rir_allocation['rir_name']}")
        print(f"  Country Code: {rir_allocation['country_code']}")
        print(f"  IP: {rir_allocation['ip']}")
        print(f"  CIDR: {rir_allocation['cidr']}")
        print(f"  Prefix: {rir_allocation['prefix']}")
        print(f"  Date Allocated: {rir_allocation['date_allocated']}")
        print("")

        print("MaxMind GeoIP:")
        maxmind = data['maxmind']
        print(f"  Country Code: {maxmind['country_code']}")
        city = maxmind.get('city', 'N/A')  # Handling possible null value for city
        print(f"  City: {city}")
    else:
        print("No information available for the given IP address.")

if __name__ == "__main__":
    ip_address = os.environ.get('IP_ADDRESS', '8.8.8.8')  # Default to '8.8.8.8' if not set
    ip_info = get_ip_info(ip_address)
    print_ip_info(ip_info)
