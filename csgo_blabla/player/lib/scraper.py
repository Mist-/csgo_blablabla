#coding=UTF-8
from pip._vendor.requests.packages import chardet
from pyquery import PyQuery as pyq
import httplib


def getHtml(host, url):
    httpClient = None
    htmlText = ''
    try:
        httpClient = httplib.HTTPConnection(host, 80, timeout=30)
        httpClient.request('GET', url)
        response = httpClient.getresponse()
        htmlText = response.read()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
    return htmlText

def getPlayerInfo(playerid):
    html = getHtml('www.csgola.com', '/player/' + playerid)
    q = pyq(html)
    avatar = q('img.avatar.center-block.img-responsive').attr('src')
    playername = q('.personaname').text()
    statTit = q('.col-md-10 .title').text().encode('utf-8')
    statVal = q('.col-md-10 .datala')
    chartVal = q('.polar-detail .datala')
    statiscsName = q('.list-group .list-group-item span.stats-title')
    staticsData = q('.list-group .list-group-item span.stats-count.pull-right')
    print pyq(statiscsName[0]).text()
    print(chardet.detect(pyq(statiscsName[0]).text().encode('utf-8')))
    json = {
        'error': 0,
        'playerinfo': {
            'avatar': avatar,
            'name': playername,
        },
        'stats': {
            'jishashu':       pyq(statVal[0]).text().encode('utf-8'),
            'baotoulv':       pyq(statVal[1]).text().encode('utf-8'),
            'kd':             pyq(statVal[2]).text().encode('utf-8'),
            'shenglv':        pyq(statVal[3]).text().encode('utf-8'),
            'zhengwangshu':   pyq(statVal[4]).text().encode('utf-8'),
            'mingzhonglv':    pyq(statVal[5]).text().encode('utf-8'),
            'juanzengwuqi':   pyq(statVal[6]).text().encode('utf-8'),
            'mvpcishu':       pyq(statVal[7]).text().encode('utf-8'),
        },
        'chart': {
            'zonghe':          pyq(chartVal[0]).text().encode('utf-8'),
            'kd':              pyq(chartVal[1]).text().encode('utf-8'),
            'mingzhonglv':     pyq(chartVal[2]).text().encode('utf-8'),
            'baotoulv':        pyq(chartVal[3]).text().encode('utf-8'),
            'shenglv':         pyq(chartVal[4]).text().encode('utf-8'),
        },
        'staData': {
            pyq(statiscsName[0]).text(): pyq(staticsData[0]).text(),
            pyq(statiscsName[1]).text(): pyq(staticsData[1]).text(),
            pyq(statiscsName[2]).text(): pyq(staticsData[2]).text(),
            pyq(statiscsName[3]).text(): pyq(staticsData[3]).text(),
            pyq(statiscsName[4]).text(): pyq(staticsData[4]).text(),
            pyq(statiscsName[5]).text(): pyq(staticsData[5]).text(),
            pyq(statiscsName[6]).text(): pyq(staticsData[6]).text(),
            pyq(statiscsName[7]).text(): pyq(staticsData[7]).text(),
            pyq(statiscsName[8]).text(): pyq(staticsData[8]).text(),
            pyq(statiscsName[9]).text(): pyq(staticsData[9]).text(),
            pyq(statiscsName[10]).text(): pyq(staticsData[10]).text(),
            pyq(statiscsName[11]).text(): pyq(staticsData[11]).text(),
            pyq(statiscsName[12]).text(): pyq(staticsData[12]).text(),
            pyq(statiscsName[13]).text(): pyq(staticsData[13]).text(),
            pyq(statiscsName[14]).text(): pyq(staticsData[14]).text(),
            pyq(statiscsName[15]).text(): pyq(staticsData[15]).text(),
            pyq(statiscsName[16]).text(): pyq(staticsData[16]).text(),
            pyq(statiscsName[17]).text(): pyq(staticsData[17]).text(),
            pyq(statiscsName[18]).text(): pyq(staticsData[18]).text(),
        }
    }
    return json

if __name__ == '__main__':
    a = getPlayerInfo('76561198275804672')
    print a
    print a['staData']['击杀'.decode('utf-8')]
