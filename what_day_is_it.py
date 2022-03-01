import datetime

class Solution:
    
    def run(self, birthday_date):
        
        future_dates = []
        
        weekends = {
            4: "Fry",
            5: "Sat",
            6: "Sun"
        }
                        
        d, m = birthday_date.split("-")    
        
        for y in range(2016, 2016+50):
            
            try:
                day = datetime.date(y, int(m), int(d)).weekday()
            except:
                continue
            
            if day in [4, 5, 6]:
                future_dates.append(f"{weekends[day]}-{y}")
            
        future_dates = " ".join(future_dates)
        print(future_dates)
    

solution = Solution()
solution.run("29-02")


'''
Wouldn't it be neat if every year, your birthday would fall on a Friday, Saturday or Sunday? Given a certain date, return a string with the day of the week and the year it will fall in a weekend, starting with the year (2016). Do this for 50 years in the future.

INPUT
string dateofbirth ^ with this format: dd-mm

OUTPUT
string future_dates
^ wday-yyyy wday-yyyy … (where wday can be any of this three values: Fry, Sat, Sun)
Every date should be separated by one space

EXAMPLE
Input
"23-10"

Output
"Sun-2016 Fri-2020 Sat-2021 Sun-2022 Fri-2026 Sat-2027 Sat-2032 Sun-2033 Fri-2037 Sat-2038 Sun-2039 Fri-2043 Sun-2044 Fri-2048 Sat-2049 Sun-2050 Fri-2054 Sat-2055 Sat-2060 Sun-2061 Fri-2065"
'''