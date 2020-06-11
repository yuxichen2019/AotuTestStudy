*** Settings ***
Resource          基础关键字.robot
Resource          业务关键字.robot

*** Keywords ***
登陆
    [Arguments]    ${username}    ${password}
    输入文本    id=name    ${username}
    输入密码    id=password    ${password}
    点击元素    id=loginsub

创建客户
    [Arguments]    ${curstomerName}
    Click Element    xpath=//span[text()='客户管理']
    Click Element    id=customer-index
    Click Element    xpath=//a[@class="btn btn-primary btn-sm pull-left"]
    输入文本    id=name    ${curstomerName}
    Click Element    xpath=//*[@id="origin"]/option[2]
    Click Element    id=save_submit

创建商机
    [Arguments]    ${curstomerName}
    Click Element    xpath=//span[contains(text(),'商机管理') and contains(@class,'nav-label')]
    Click Element    id=business-index
    Click Element    xpath=//a[contains(@href,'/index.php?m=business&a=add')]
    ${curDate}    获取当前时间
    输入文本    id=name    business${curDate}
    Click Element    id=customer_name
    Click Element    xpath=//td[contains(text(),'${curstomerName}')]
    Click Element    xpath=//span[contains(text(),'确认')]
    Click Element    xpath=//select[@name="status_id"]/option[4]
    输入文本    id=business_price    999999
    Click Element    id=save_submit

创建合同
    [Arguments]    ${customerName}
    Click Element    xpath=//a[contains(@title,'合同订单')]
    Click Element    id=contract-index
    Click Element    xpath=//a[contains(@class,'btn btn-primary btn-sm pull-left')]
    ${curDate}    获取当前时间
    输入文本    name=contract_name    contract${curDate}    #输入合同名称
    Click Element    id=customer_name    #客户来源
    Click Element    xpath=//td[contains(text(),'${customerName}')]    #选择客户
    Click Element    xpath=(//span[@class='ui-button-text' and text()='确定'])[3]
    Click Element    id=business_name    #商机来源
    Click Element    xpath=//td[contains(text(),'${customerName}')]
    Click Element    xpath=(//span[@class='ui-button-text' and text()='确定'])[2]
    输入文本    id=contract_price    100    #合同金额
    ${dateTime1}    获取当前日期和时间
    输入文本    id=due_time    ${dateTime1}    #签约时间
    ${dateTime2}    获取当前日期和时间
    输入文本    id=end_date    ${dateTime2}    #合同到期时间
    Click Element    id=examine_role    #合同审批人
    Click Element    xpath=//td[contains(text(),'超级管理员')]
    Click Element    xpath=//span[contains(text(),'确定')]
    Click Element    id=save_submit

客户商机合同数据驱动
    [Arguments]    ${username}    ${password}
    登录系统驱动    ${username}    ${password}
    ${customerName}    随机获取中文名
    创建客户    ${customerName}
    创建商机    ${customerName}
    创建合同    ${customerName}

登录系统驱动
    [Arguments]    ${username}    ${password}
    打开浏览器    https://my.crm.cc/index.php?m=user&a=login    chrome
    最大化浏览器
    登陆    ${username}    ${password}
