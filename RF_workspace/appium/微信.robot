*** Settings ***
Test Teardown     关闭APP
Library           AppiumLibrary
Resource          业务关键字.txt

*** Test Cases ***
微信发送消息
    Open Application    http://127.0.0.1:4723/wd/hub    platformName=Android    platformVersion=7.0    deviceName=K6T6R17124002359    appPackage=com.tencent.mm    appActivity=com.tencent.mm.ui.LauncherUI    unicodeKeyboard=true    resetKeyboard=true    noReset=true
    Wait Until Element Is Visible    id=com.tencent.mm:id/bfl     60s
    Input Text    id=com.tencent.mm:id/bfl     yb092226
    Click Element    id=com.tencent.mm:id/d2y     #登录
    Wait Until Element Is Visible    id=com.tencent.mm:id/f4u    30s    #放大镜
    Click Element    id=com.tencent.mm:id/f4u
    Input Text    id=com.tencent.mm:id/bfl     yu
    Wait Until Element Is Visible    id=com.tencent.mm:id/g8b    60s
    Click Element    id=com.tencent.mm:id/g8b    	#点击好友名称
    FOR    ${n}    IN RANGE    1    2
        Wait Until Element Is Visible    id=com.tencent.mm:id/ak7    30s
        Input Text    id=com.tencent.mm:id/ak7    快点了，等你很久了，到底来不来啊！！！${n}
        Click Element    id=com.tencent.mm:id/amr
        Click Element    des=表情
        Click Element    des=[得意]
        Click Element    xpath=//android.widget.Button[@text=\"发送\"]
        Click Element    des=切换到按住说话
        Long Press    des=按住说话    4
        Click Element    accessibility_id=切换到键盘
        log    ${n}
    log    outside loop
    Wait Until Element Is Visible    accessibility_id=返回    20
    Click Element    accessibility_id=返回
    Click Element    accessibility_id=返回

微信发送信息分层实现
    [Tags]    A
    [Setup]    打开APP
    登陆微信    ujm159yhn753
    通讯录搜索好友    gavin    name=高焰-Gavin
    FOR    ${n}    IN RANGE    1    3
        发送文字与语音信息    快点了，等你很久了，到底来不来啊！！！
        发送表情
        log    ${n}
    log    结束循环
    退出微信
    [Teardown]    关闭APP
