import re, requests

url = "https://knowunity.fr/app/knows/8d067f62-099a-4204-9ab3-faaeec5dd582?referrerScreen=search&query=Gargantua+chapitre+57"
url2 = "https://knowunity.fr/app/knows/9cb6b17c-16ab-4609-bafc-52563de6d70a?referrerScreen=search&query=math*"
url3 = "https://knowunity.fr/app/knows/9cb6b17c-16ab-4609-bafc-52563de6d70a?referrerScreen=search&query=math*"

pattern = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"

def extract_know_id(input_url):
    match = re.search(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", input_url)
    return match.group(0) if match else None

know_id = extract_know_id(url)

api_url = f'https://apiedge-eu-central-1.knowunity.com/knows/{know_id}'
response = requests.get(api_url)

json_data = response.json()

a = json_data['documents'][0]['contentUrl']


print(a)
