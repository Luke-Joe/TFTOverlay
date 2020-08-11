try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

import json

myAPI = "I DONT KNOW HOW TO HIDE MY CODE

rankURL = "https://na1.api.riotgames.com/tft/league/v1/entries/by-summoner/" \
          "DfaD_-zgTcHJydv9BdaXWvG55OShTP8CkbeXtLqcSElHQqU?" \
          "api_key=" + myAPI

rankJson = urllib2.urlopen(rankURL)

rankData = json.load(rankJson)

username = ""
for item in rankData:
    username = item['summonerName']

rank = ""
for item in rankData:
    rank = item['tier'] + " " + item['rank'] + " " + str(item["leaguePoints"]) + "LP"

accURL = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/" + username + "?" \
         "api_key=" + myAPI

accJson = urllib2.urlopen(accURL)

accData = json.load(accJson)


def getRank():
    return rank


def getUsername():
    return username



