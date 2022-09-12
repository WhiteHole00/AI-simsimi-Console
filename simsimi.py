import requests


def simsimi_header():
    headers=  {
                "Accept": "application/json, text/plain, */*",
                "Authkey": "NTQwNzQwMTc2YzM5OTlhNmZkYThkNTAxNGUxMmM5NzlmOGY2MWU0ZTU1ODYxOTIxMThhY2QwYjM4ZTE2M2I5Ng",
                "Os": "a",
                "Av": "8.2.5",
                "Content-Type": "application/json",
                "Host": "beta-bumcoming.simsimi.com",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.9.1"
            }
    return headers


def simsimi_(msg):
    try:
        data_json = {"av": "8.2.5","os": "a","lc": "ko","cc": "KR","tz": "Asia/Seoul","message": msg,"free_level": 15}
        si = requests.post("https://beta-bumcoming.simsimi.com/simtalk/get_talk_set",json=data_json,headers=simsimi_header()).json()

        result = f'[심심이 AI] : {si["origin_sentence"]}'
        return result
    except Exception as e:
        result_ = f'[심심이 AI] : {si["detail"]}'
        return result_


def main():
    while True:
        try:
            qu = input("질문 : ")
            re = simsimi_(qu)
            print(re)
        except Exception as e:
            print("Error!" + e)
            break
         



main()
