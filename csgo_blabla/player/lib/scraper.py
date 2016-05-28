#coding=UTF-8
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
    statVal = q('.col-md-10 .datala').text().encode('utf-8')
    chartVal = q('.polar-detail .datala').text().encode('utf-8')
    json = {
        'error': 0,
        'playerinfo': {
            'avatar': avatar,
            'name': playername,
        },
        'stats': {
            'jishashu':       statVal[0],
            'baotoulv':       statVal[1],
            'kd':             statVal[2],
            'shenglv':        statVal[3],
            'zhengwangshu':   statVal[4],
            'mingzhonglv':    statVal[5],
            'juanzengwuqi':   statVal[6],
            'mvpcishu':       statVal[7],
        },
        'chart': {
            'zonghe':         chartVal[0],
            'kd':             chartVal[1],
            'mingzhonglv':    chartVal[2],
            'baotoulv':       chartVal[3],
            'shenglv':        chartVal[4],
        },
    }
    return json

if __name__ == '__main__':
    print getPlayerInfo('76561198275804672')
