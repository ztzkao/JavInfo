import requests
import json
def _1pondo_init(id):
    r = requests.get('https://www.1pondo.tv/dyn/phpauto/movie_details/movie_id/' + id + '.json')
    data = json.loads(r.text)
    diction = {
        'id': id,
        'coverLink': data['ThumbHigh'],
        'title': data['Title'],
        'description': data['Desc'].strip(),
        'actor': data['Actor'],
        'releaseTime': data['Release'],
        'duration': getDuration(data['Duration']),
        'tags': getTags(data['UCNAME'])
    }
    return diction
def getDuration(sec):
    HH = str(sec // 3600).zfill(2)
    MM = str(sec % 3600 // 60).zfill(2)
    SS = str(sec % 60).zfill(2)
    duration = HH + ':' + MM + ':' + SS
    return duration

def getTags(tags):
    date = ''
    for num in range(len(tags)):
        date += tags[num] + ' '
    return date[:-1]

if __name__ == '__main__':
    id = input('输入id:\n')
    print(_1pondo_init(id))


