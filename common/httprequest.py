#	-*-	coding:	utf-8	-*
"""封装https的get和post请求
"""
import requests

class HttpRequest():
    def send_get(self, url, data, cookies):
        result = requests.get(url=url,params=data, cookies=cookies)
        return  result

    def send_post(self, url, data, cookies):
        result = requests.post(url=url,data=data, cookies=cookies)
        return result

    def send_request(self,method,url=None,data=None,cookies=None):
        if method == 'get':
            result = self.send_get(url,data,cookies)
        elif method == 'post':
            result = self.send_post(url, data, cookies)
        else:
            print('暂时不支持{}该方法'.format(method))
        return  result.json()


if __name__ == '__main__':
    r = HttpRequest()
    url= 'http://apitopic.che168.com/lottery818/user/getmyprize'
    data ={'_appid' : '2scapp.ios'}
    cookies = {'pcpopclub':'c080e8c219824be985b5d5156b85010601a71231'}
    t =r.send_request('get',url,data,cookies)
    print(t)