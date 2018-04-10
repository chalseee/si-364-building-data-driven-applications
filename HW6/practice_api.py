import requests, json

app_id = "be77c0cb"
app_key = "bf29b57815ffe51f465ca7069db9135c"
base_url="https://od-api.oxforddictionaries.com/api/v1/entries/en/programming"

data = requests.get(base_url, headers={'app_id': app_id, 'app_key':app_key}).json()

print(data)
