*** Settings ***
Library           SeleniumLibrary
Library           RandomLibrary
Library           DateLibrary

*** Keywords ***
打开浏览器
    [Arguments]    ${url}    ${browser}
    Open Browser    ${url}    ${browser}

关闭浏览器
    close Browser

最大化浏览器
    Maximize Browser Window

输入文本
    [Arguments]    ${locator}    ${text}
    Input Text    ${locator}    ${text}

输入密码
    [Arguments]    ${locator}    ${content}
    Input Password    ${locator}    ${content}

点击元素
    [Arguments]    ${locator}
    Click Element    ${locator}

随机获取中文名
    ${chineseName}    Get Chinese Name
    [Return]    ${chineseName}

获取当前时间
    ${curTime}    Get Current Time
    [Return]    ${curTime}

获取当前日期和时间
    ${dateTime}    Get Current Date And Time
    [Return]    ${dateTime}

获取当前日期
    ${curDate}    Get Current Date
    [Return]    ${curDate}
