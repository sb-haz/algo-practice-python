import urllib.request
from requests.utils import requote_uri
import json

class Solution:
    
    def run(self, film, character):

        filmsAllCharacters = []
        charactersFilmAppearances = []
        
        # Get film data
        film_response = urllib.request.urlopen(
            requote_uri(f"https://challenges.hackajob.co/swapi/api/films/?search={film}"))
        film_data = json.loads(film_response.read())
        
        
        # Get character data
        character_response = urllib.request.urlopen(
            requote_uri(f"https://challenges.hackajob.co/swapi/api/people/?search={character}"))
        character_data = json.loads(character_response.read())
        
        # Get characters in film
        for i in range(0, len(film_data["results"][0]["characters"])):
            char_response = urllib.request.urlopen(
                requote_uri(film_data["results"][0]["characters"][i]))
            char_data = json.loads(char_response.read())
            
            filmsAllCharacters.append(char_data["name"])
                                
        filmsAllCharacters = ', '.join(sorted(filmsAllCharacters))
        
        # Get films character appears in
        if character_data["results"] != []:
            for i in range(0, len(character_data["results"][0]["films"])):
                film_response = urllib.request.urlopen(
                    requote_uri(character_data["results"][0]["films"][i]))
                film_data = json.loads(film_response.read())
                
                charactersFilmAppearances.append(film_data["title"])
                                
            charactersFilmAppearances = ', '.join(sorted(charactersFilmAppearances))
            
        else:
            charactersFilmAppearances = "none"
                
        filmsAndCharacters = f"{film}: {filmsAllCharacters}; {character}: {charactersFilmAppearances}"
        return filmsAndCharacters
    
s1 = Solution()
print(s1.run("The Force Awakens", "Walter White"))