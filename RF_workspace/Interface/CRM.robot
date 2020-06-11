*** Settings ***
Library           requests
Library           Collections
Resource          业务关键字.txt
Resource          基础关键字.txt
Library           RandomLibrary
Library           RequestsLibrary

*** Test Cases ***
创建CRM客户
    #登录前刷新PHPSESSID
    ${phpsessid}    刷新PHPSESSID
    #登录CRM系统
    ${loginInfo}    登录CRM    15112342277    e10adc3949ba59abbe56e057f20f883e    ${phpsessid}
    should contain    ${loginInfo}    登录成功
    #创建客户
    ${chineseName}    随机获取中文姓名
    log    创建的客户是：${chineseName}
    ${actualResult}    创建客户    ${phpsessid}    ${chineseName}
    #断言结果
    ${expectResult}    Convert To Integer    200
    should be equal    ${actualResult}    ${expectResult}

创建CRM工单
    #登录前刷新PHPSESSID
    ${phpsessid}    刷新PHPSESSID
    #登录CRM系统
    ${loginInfo}    登录CRM    19926451606    900e0313b981caa9f83ed5d0a01e9c58    ${phpsessid}
    should contain    ${loginInfo}    登录成功
    #创建客户
    ${chineseName}    随机获取中文姓名
    log    创建的工单是：${chineseName}
    ${actualResult}    创建工单    ${phpsessid}    ${chineseName}
    #断言结果
    ${expectResult}    Convert To Integer    200
    should be equal    ${actualResult}    ${expectResult}

数据驱动创建工单
    [Template]    创建CRM工单
    19926451606    900e0313b981caa9f83ed5d0a01e9c58
    13316998731    d720540930356de133676796ae328894
