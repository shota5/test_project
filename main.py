import json, config #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み

# APIの秘密鍵
CK = 'YOUR_CONSUMER_KEY'
CS = 'YOUR_CONSUMER_SECRET_KEY'
AT = 'YOUR_ACCESS_TOKEN'
ATS = 'YOUR_ACCESS_TOKEN_SECRET'

class Twitter():
    def __init__(self, ck, cs, at, ats):
        self.twitter = OAuth1Session(ck, cs, at, ats) #認証処理

    def get_timeline(self):
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json' #タイムライン取得エンドポイント

        params = {'count' : 5} #取得数
        res = self.twitter.get(url, params=params)

        if res.status_code == 200: #正常通信出来た場合
            timelines = json.loads(res.text) #レスポンスからタイムラインリストを取得
            for line in timelines: #タイムラインリストをループ処理
                print(line['user']['name']+'::'+line['text'])
                print(line['created_at'])
                print('*******************************************')
        else: #正常通信出来なかった場合
            print(f'Failed. : {%res.status_code}')

    def post_tweet(self, tweet):
        url = 'https://api.twitter.com/1.1/statuses/update.json' #ツイートポストエンドポイント

        params = {'status' : tweet}

        res = self.twitter.post(url, params=params) #post送信

        if res.status_code == 200: #正常投稿出来た場合
            print('Success.')
        else: #正常投稿出来なかった場合
            print(f'Failed. : {%res.status_code}')

if __name__ == '__main__':
    print('success')