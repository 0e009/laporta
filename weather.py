import urllib2, urllib, json
baseurl = "https://query.yahooapis.com/v1/public/yql?"
yqlQuery = "select wind from weather.forecast where woeid=2460286"
yqlUrl = baseurl + urllib.urlencode({'q':yqlQuery}) + "&format=json"
data = json.loads(urllib2.urlopen(yqlUrl).read())
print(data['query']['results'])
