import requests
def validCity(url, city):
    r = requests.get(url + city)
    return (r.status_code);
