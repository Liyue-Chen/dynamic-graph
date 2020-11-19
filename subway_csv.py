import requests
from pyquery import PyQuery

#数据在http://sh.bendibao.com/ditie/time.shtml爬取

template = 'http://sh.bendibao.com/ditie/shike_{param}.shtml'
file = open('d:/vscode/code file/timetable.txt', 'a', encoding='utf-8') #储存文件
for page in range(1,18):
    url = template.format(param = (page + 222))
    resp = requests.get(url = url ,  headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.97 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;'
                  'q=0.9,image/webp,image/apng,*/*;'
                  'q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    })
    if resp.status_code == 200:
        print('test ' + str(page) + ' success')
    if page <= 13:
        file.write(str(page) +'号地铁时刻表\n\n')
    elif page == 14:
        file.write('磁悬浮地铁时刻表\n\n')
    elif page == 15:
        file.write('10号线支线地铁时刻表\n\n')
    elif page == 16:
        file.write('11号线支线地铁时刻表\n\n')
    elif page == 17:
        file.write('16号线支线地铁时刻表\n\n')
    item0 = PyQuery(resp.text)
    item1 = item0('table tbody tr').items()
    for it1 in item1:
        item2 = it1('td').items()
        for it2 in item2:
            string = it2.text()
            file.write(str(string).replace('\n', '') + '    ')
        file.write('\n')
    file.write('\n\n')
url = template.format(param = 242)
resp = requests.get(url = url ,  headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/83.0.4103.97 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;'
              'q=0.9,image/webp,image/apng,*/*;'
              'q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    })
if resp.status_code == 200:
    print('test 18 success')
file.write('17号地铁时刻表\n\n')
item00 = PyQuery(resp.text)
item01 = item00('.table tr').items()
for it01 in item01:
    item02 = it01('td').items()
    for it02 in item02:
        string = it02.text()
        file.write(str(string).replace('\n', '') + '    ')
    file.write('\n')
file.write('\n\n')
url = template.format(param = 554)
resp = requests.get(url = url ,  headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/83.0.4103.97 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;'
              'q=0.9,image/webp,image/apng,*/*;'
              'q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    })
if resp.status_code == 200:
    print('test 19 success')
file.write('浦江线地铁时刻表\n\n')
item10 = PyQuery(resp.text)
item11 = item10('.table tr').items()
for it11 in item11:
    item12 = it11('td').items()
    for it12 in item12:
        string = it12.text()
        file.write(str(string).replace('\n', '') + '    ')
    file.write('\n')
file.write('\n\n')
url = template.format(param = 587)
resp = requests.get(url = url ,  headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/83.0.4103.97 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;'
              'q=0.9,image/webp,image/apng,*/*;'
              'q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    })
if resp.status_code == 200:
    print('test 20 success')
file.write('5号线支线地铁时刻表\n\n')
item20 = PyQuery(resp.text)
item21 = item20('.table tr').items()
for it21 in item21:
    item22 = it21('td').items()
    for it22 in item22:
        string = it22.text()
        file.write(str(string).replace('\n', '') + '    ')
    file.write('\n')
file.write('\n\n')
file.close()

    
 


    
