# -*- coding: utf-8 -*-

from facebook import GraphAPI
from facebook import GraphAPIError
from json import loads as _parse_json
import urllib

token = 'YOUR_ACCESS_TOKEN_HERE'

def troll():
    # 최근 실행에서 저장된 feed id
    fid = None
    try:
        f = open('fid.txt', 'r')
        fid = f.read().strip()
        f.close()
    except IOError:
        pass
    print('* Last feed id:', fid)

    graph = GraphAPI(access_token=token)

    print('* Retrieving feeds...')
    feeds = graph.get_connections(id='674366342659988', connection_name='feed', fields='message,id')['data']
    print('Done')

    # 받아온 피드 중 가장 최신 피드의 id
    lastest_feed_id = None
    for feed in feeds:
        feed_id = feed['id']
        feed_id=str(feed_id)

        # 받아온 피드 중 가장 최신의 피드 id 저장
        if lastest_feed_id is None:
            lastest_feed_id = feed_id

        # 최근 실행에서 처리한 피드일 경우 종료
        if fid == feed_id:
            break

        print('* Publishing comment on %s...' % feed_id)
        try:
            graph.put_comment(object_id=feed_id, message='일 안함? ㅡㅡ')
        except GraphAPIError as e:
            print(e)
            print('Failed')
            continue
        print('Done')

    # 중복검사를 위해 가장 최신 피드 id 저장
    f = open('fid.txt', 'w')
    f.write(lastest_feed_id)
    f.close()
    print('* Finished.')

if __name__ == '__main__':
    troll()
