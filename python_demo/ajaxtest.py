import requests
from urllib.parse import urlencode

def get_page(offset):
    params = {
        'aid': 24,
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': 1,
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': 1555838377163
    }
    url = 'http://www.toutiao.com/api/search/content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None
    except Exception as e:
        print(str(e))
        return None

def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            image_url = item.get('image_url')
            # for image in images:
            yield {
                'image': image_url,
                'title': title
            }

import os
from hashlib import md5

def save_image(folder, item):
    # if not os.path.exists(folder):
    #     os.makedirs(folder)
    if not os.path.exists(folder + '/' + item.get('title')):
        os.mkdir(folder + '/' + item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}/{2}.{3}'.format(folder, item.get('title'), md5(response.content).hexdigest(), 'jpg')
            print('file-path: ' + file_path)
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')
    except Exception as e:
        print(str(e))


from multiprocessing.pool import Pool

def main(offset):
    json = get_page(offset)
    print(json)
    for item in get_images(json):
        print(item)
        save_image('ajaxtest', item)

GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()


