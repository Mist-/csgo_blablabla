#coding=utf-8
import urllib
import urllib2
import json
import chardet

def getPlayerUrl(steamID):
	url = 'http://www.csgola.com/player/'
	values = {
		'playerid': steamID
	}
	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	res = urllib2.urlopen(req)
	result = str(res.read()).decode('UTF-8-SIG').encode('UTF-8')
	result_message = json.loads(result, encoding='UTF-8')
	return url + result_message['msg']
