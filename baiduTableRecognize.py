import requests
import base64
from exception import *
def getAccessToken(api_key,secret_key):
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}".format(api_key,secret_key)
    
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    if response:
        return response.json()
    else:
        return ""

def baiduTableRecognize(api_key,secret_key,model:str,*arg) -> dict:
    """
    调用百度API识别表格
    :param model:识别方式 image,url or pdf_file
    :param arg:文件地址或者url地址
    :return: 识别结果
    """
    #基本参数
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/table"
    header = {"Content-Type":"application/x-www-form-urlencoded"}
    body = {
        #url,image,pdf_file三选一
        #要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/jpeg/png/bmp格式
        # "image": "",
        # "url" : "",
        # "pdf_file" : "",
        # #识别的页数
        # "pdf_file_num": "",

        #是否输出单元格文字位置信息
        #- false： 默认值，仅输出单元格行列信息及四角点坐标，不输出单元格内文字位置信息；
        #- true： 输出单元格内文字的外接四边形四角点坐标，若文字折行，则分行分别输出
        "cell_contents": "false"
    }
    
    #识别方式
    if model not in ("image,url,pdf_file"):
        raise ValueError("you must choose one of image,url or pdf_file")
    elif model == "image":
        f = open(arg[0],"rb")
        img = base64.b64encode(f.read())
        body[model] = img
    elif model == "url":
        body[model] = arg[0]
    elif model == "pdf_file":
        if(len(arg[0]) < 2):
            raise ValueError("check your parameters.pdf mode need pages number")
        body[model] = arg[0][0]
        body["pdf_file_num"] = arg[0][1]

    #获取access_token

    #post请求
    request_url = url + "?access_token=" + getAccessToken(api_key=api_key,secret_key=secret_key)["access_token"]
    response = requests.post(request_url, data=body, headers=header)
    if response:
        return response.json()
    else:
        return {"no return."}

