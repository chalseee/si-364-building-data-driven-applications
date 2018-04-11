import requests, json

app_id = "be77c0cb"
app_key = "bf29b57815ffe51f465ca7069db9135c"
base_url="https://od-api.oxforddictionaries.com/api/v1/entries/en/"
word_id=str(input("enter word to search: \n"))

def oxford_dict_request(app_id, app_key, base_url, word_id):
    base_url = base_url + word_id.lower()
    data = requests.get(base_url, headers={'app_id': app_id, 'app_key':app_key})
    return data.json()['results']

print(oxford_dict_request(app_id, app_key, base_url, word_id))
