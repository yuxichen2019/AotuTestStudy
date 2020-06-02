*** Settings ***
Library           SeleniumLibrary
Resource          业务关键字.txt

*** Test Cases ***
百度搜索
    [Tags]    baidu
    [Template]    百度搜索数据驱动
    [Timeout]    1 minute
    java
    selenium
    python
    ruby
    [Teardown]    关闭浏览器

163-EmailHome-发送邮件
    [Tags]    163
    [Setup]    打开浏览器    http://mail.163.com    chrome    # 打开网易邮箱
    [Timeout]    10 minutes
    最大化浏览器
    Comment    Comment    Click Element    xpath=//div[@class="new-loginFuncNormal account-163-icon"]
    Select Frame    xpath=//iframe[starts-with(@id,'x-URS-iframe')]
    Input Text    name=email    15112342277
    Input Password    name=password    yxc253676
    Click Link    id=dologin
    Comment    Wait Until Element Is Enabled    xpath=//span[contains(text(), '写 信')]    50s
    Click Element    xpath=//span[contains(text(), '写 信')]
    Comment    Wait Until Element Is Enabled    css=.nui-editableAddr-ipt    50s
    Input Text    css=.nui-editableAddr-ipt    gavintraining@163.com
    Input Text    xpath=//input[contains(@class,'nui-ipt-input') and contains(@maxlength,'256') and contains(@type,'text')]    selenium training email
    Select Frame    css=.APP-editor-iframe
    Input Text    css=.nui-scroll    please tell me content
    Unselect Frame
    Click Element    css=.nui-toolbar-item
    Sleep    20s
    Page Should Contain    发送成功
    [Teardown]    关闭浏览器

163-EmailHome-发送邮件分层实现
    [Tags]    163
    [Setup]    打开浏览器    http://mail.163.com    chrome    # 打开网易邮箱
    [Timeout]    10 minutes
    最大化浏览器
    登录网易邮箱    15112342277    yxc253676
    发送邮件
    [Teardown]    关闭浏览器
