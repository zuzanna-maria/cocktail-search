from pprint import pprint
import requests




url = "https://the-cocktail-db.p.rapidapi.com/filter.php"

base_alcohol: str = input("what is your favourite cocktail base? choose one from below: \n vodka \n gin \n rum \n tequila \n Scotch \n Brandy")
mixer: str = input("what is your favourite mixer? choose one from below: \n apple juice \n orange juice \n cranberry juice \n carbonated water \n lemonade ")


querystring= {"i": base_alcohol, "i": mixer}




headers = {
    'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
    'x-rapidapi-key': "03c6b07284msh3f82f773dc8f43dp1bfb0bjsn55c1eaa21f05"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

pprint("Cocktails you might like are listed below: {}".format(response.text))
