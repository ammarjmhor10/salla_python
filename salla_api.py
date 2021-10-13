import json
import requests



class Salla:
    def __init__(self,token,url='https://api.salla.dev/admin/v2/'):
        self.token = token
        self.url = url
        self.headers = {'authorization': 'Bearer ' + token}
    

    def get(self,part:str = ''):
        if 'https://api.salla.dev/admin/v2/' in part:
            url = part
            header = self.headers
            r = requests.get(url,headers=header).json()
            if r['success'] != True:
                raise Exception('error')
            else:
                return r
        else:
            url = self.url + part
            header = self.headers
            r = requests.get(url,headers=header).json()
            if r['success'] != True:
                raise Exception('error')
            else:
                return r
    

    def get_id(self,part:str = ''):
        url = self.url + part
        header = self.headers
        r = requests.get(url,headers=header).json()
        if r['status'] != 200:
            raise Exception('error')
        else:
            return r['pagination']

    def post(self,json:dict,part:str=''):
        url = self.url + part
        header = self.headers
        r = requests.post(url,headers=header,json=json).json()
        if r['success'] != True:
            raise Exception('error')
        else:
            return r['data']
        
    
    def put(self,json:dict,part:str=''):
        url = self.url + part  
        header = self.headers
        r = requests.put(url,headers=header,json=json).json()
        if r['status'] != 200:
            raise Exception('error')
        else:
            return r['data']

    def delet(self,part:str):
        url = self.url + part
        header = self.headers
        r = requests.delete(url,headers=header).json()
        if r['status'] != 200:
            raise Exception('error')
        else:
            return r['data']

    def create_products(self,shcema:dict):
        url ='products'
        add = self.post(shcema,url)

        return add



   













