*** Settings ***
Library           SeleniumLibrary
Resource          基础关键字.robot
Resource          业务关键字.robot

*** Test Cases ***
CrmFlow
    [Tags]    创建客户-添加商机-添加合同
    [Setup]    打开浏览器    http://my.crm.cc/index.php?m=user&a=login    chrome    # 谷歌谷歌~~打开CRM登陆页面
    [Template]
    [Timeout]
    最大化浏览器
    登陆    15112342277    123456
    ${customerName}    随机获取中文名
    创建客户    ${customerName}
    创建商机    ${customerName}
    创建合同    ${customerName}
    [Teardown]    关闭浏览器

CrmFlowUsers
    [Template]    客户商机合同数据驱动
    [Timeout]
    15112342277    123456
    19926451606    ujm159yhn753
    [Teardown]    关闭浏览器
