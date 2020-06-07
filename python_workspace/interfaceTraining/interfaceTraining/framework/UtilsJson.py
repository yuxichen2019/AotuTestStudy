# from __future__ import print_function

import json

from framework.BlueRose import BlueRose


class UtilsJson(object):
    # 存放接口返回变量的全局变量字典
    variables = {}
    requests = BlueRose()

    # 递归遍历json
    @staticmethod
    def dict_generator(indict, pre=None):
        pre = pre[:] if pre else []
        if isinstance(indict, dict):
            for key, value in indict.items():
                if isinstance(value, dict):
                    if len(value) == 0:
                        yield pre + [key, '{}']
                    else:
                        for d in UtilsJson.dict_generator(value, pre + [key]):
                            yield d
                elif isinstance(value, list):
                    if len(value) == 0:
                        yield pre + [key, '[]']
                    else:
                        for v in value:
                            for d in UtilsJson.dict_generator(v, pre + [key]):
                                yield d
                elif isinstance(value, tuple):
                    if len(value) == 0:
                        yield pre + [key, '()']
                    else:
                        for v in value:
                            for d in UtilsJson.dict_generator(v, pre + [key]):
                                yield d
                else:
                    yield pre + [key, value]
        else:
            yield indict

    # 组装Testcase
    @staticmethod
    def assembleTestcase(json):
        url = ""
        method = ""
        headers = []
        bodys = []
        extracts = []
        validates = []
        headersData = None
        bodysData = None

        for i in UtilsJson.dict_generator(json):
            key = '.'.join(i[0:-1])
            value = i[-1]
            if "url" in key:
                url = value
            elif "method" in key:
                method = value
            elif "headers" in key:
                headers.append({key.split(".")[2]: value})
            elif "json" in key:
                bodys.append({key.split(".")[2]: value})
            elif "extract" in key:
                extracts.append({value.split(".")[0]: value.split(".")[1]})
            elif "validate" in key:
                validates.append({key.split(".")[3]: value})
            elif "variables" in key:
                # variables[key.split(".")[2]] = value
                UtilsJson.variables["phpsessid"] = ""

        if len(headers) > 0:
            headersStr = str(headers).replace("{'", "'").replace("'}", "'").replace("[", "{").replace("]", "}")
            if "$phpsessid" in headersStr:
                headersData = eval(headersStr.replace("$phpsessid", str(UtilsJson.variables.get("phpsessid"))))

        if len(bodys) > 0:
            bodysData = eval(str(bodys).replace("{'", "'").replace("'}", "'").replace("[", "{").replace("]", "}"))

        # 方法不等于空的时候才执行发送请求
        if method != "":
            reponse = UtilsJson.requests.sendRequests(url=url, method=method, headers=headersData, data=bodysData)
        # 判断是不是有返回值要获取
        if len(extracts) > 0:
            for extract in extracts:
                for key in extract.keys():
                    if key == "cookies":
                        UtilsJson.variables["phpsessid"] = UtilsJson.requests.getCookiesValue(reponse,
                                                                                              extract.get("cookies"))
        # 判断是否有断言
        if len(validates) > 0:
            for validate in validates:
                for key in validate.keys():
                    # 断言HTTP状态码
                    if key == "status_code":
                        if str(reponse.status_code) == validate.get("status_code"):
                            print("断言成功")
                    #  断言json返回值
                    if key == "info":
                        if UtilsJson.requests.getJsonFilesValue(reponse, "info") == validate.get("info"):
                            print("断言成功")

    @staticmethod
    def outPutJson(json):
        for i in UtilsJson.dict_generator(json):
            print('.'.join(i[0:-1]), ':', i[-1])


if __name__ == "__main__":
    jsonFile = open("../data/testCase_refreshPhpsessid.json", encoding='utf-8')
    # 加载完整用例的json数组
    jsonArray = json.load(jsonFile, encoding='utf-8')
    for json in jsonArray:
        UtilsJson.assembleTestcase(json)
