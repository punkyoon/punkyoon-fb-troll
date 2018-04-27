# DEPRECATED

**"Publishing comments through the API is only available for page access tokens"**

Facebook has disabled likes and comments through graph API. So It cannot work now.

## 소개

[하지윤](http://www.facebook.com/jiyoon96)이 페이스북에 글을 쓸 때마다 힘내서 열심히 일을 하라는 격려의 댓글을 달아줘요!

[shlee322-fb-troll](https://github.com/devxoul/shlee322-fb-troll) 코드를 python3, facebook-sdk의 최신버전에 맞게 고쳤습니다.

## 사용법

1. `troll.py`를 열어 `token = 'YOUR_ACCESS_TOKEN_HERE'` 부분을 본인의 페이스북 액세스 토큰으로 저장한다.
2. `$ python troll.py` 혹은 `$ python3 troll.py` 하거나 `crontab`을 돌리거나 `celery`를 붙이거나 알아서 잘 쓴다.

## 주의사항

1. 중복검사를 위해 최신 글의 아이디만 저장하기 때문에 혹시 지윤이가 글을 지우면 이전 글에 또 일하라는 격려 댓글을 남기게 됩니다.
2. 액세스토큰을 연장하는 로직이 없습니다. 조금 돌리다보면 `GraphAPIError`를 마구 뿜을겁니다.

## Thanks to..

[shlee322-fb-troll](https://github.com/devxoul/shlee322-fb-troll)
