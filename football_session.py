import urllib.request, json

class Solution:
    
    def run(self, teamKey):
        
        response = urllib.request.urlopen("https://s3.eu-west-1.amazonaws.com/hackajob-assets1.p.hackajob/challenges/football_session/football.json")
        data = json.loads(response.read())
        
        goals = 0
        
        for round in data["rounds"]:
            for match in round["matches"]:
                
                if match["team1"]["key"] == teamKey:
                    goals += match["score1"]
                elif match["team2"]["key"] == teamKey:
                    goals += match["score2"]
        print(goals)
        return goals
    
s = Solution()
s.run("manutd")