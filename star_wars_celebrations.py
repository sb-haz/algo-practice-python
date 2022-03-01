import urllib.request
from requests.utils import requote_uri
import json

class Solution:

    def run(self, character):

        response = urllib.request.urlopen(
            requote_uri(f"https://challenges.hackajob.co/swapi/api/people/?search={character}")
        )
        data = json.loads(response.read())

        numberOfFilms = len(data["results"][0]["films"])
        return numberOfFilms
    
    #print(json.dumps(film_data["results"][0]["characters"], indent=2, sort_keys=True))

sol = Solution()
sol.run("Luke Skywalker")
