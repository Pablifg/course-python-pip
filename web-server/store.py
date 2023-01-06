import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    # Verify type of data
    print(type(r.text))
    # Transformar str a formato python
    categories = r.json()
    for category in categories:
        print(category['name'])