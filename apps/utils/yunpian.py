# -*- coding: utf-8 -*-

import requests
import json


class YunPian(object):
    """
    等待审批，这里只是一个测试逻辑
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        params = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "xxxxxxxxxxxxxxxx{code}xxxxxxxxxxxxxxxxxxxxxx".format(code=code)
        }

        response = requests.post(self.single_send_url, data=params)
        re_dict = json.loads(response.text)
        # print(re_dict)
        return re_dict


if __name__ == "__main__":
    yun_pian = YunPian("")
    yun_pian.send_sms("2017", "13168693629")
