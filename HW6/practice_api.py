import requests, json

app_id = "be77c0cb"
app_key = "bf29b57815ffe51f465ca7069db9135c"
base_url="https://od-api.oxforddictionaries.com/api/v1/entries/en/"

def oxford_dict_request(app_id, app_key, base_url, word_id):
    base_url = base_url + word_id.lower()
    data = requests.get(base_url, headers={'app_id': app_id, 'app_key':app_key})
    return data.json()['results'][0]

#sample word queries
programming_dict = oxford_dict_request(app_id, app_key, base_url, "programming")
cool_dict = oxford_dict_request(app_id, app_key, base_url, "cool")
bark_dict = oxford_dict_request(app_id, app_key, base_url, "bark")

#ex, programming_dict:
word = programming_dict['word']
language = programming_dict['language']
print(word, language, programming_dict)

#TODO: invoke the fxn a couple of times to show how i will use it in the final assignment
