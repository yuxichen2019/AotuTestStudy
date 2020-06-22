*** Settings ***
Test Teardown     关闭APP
Resource          业务关键字.txt
Library           AppiumLibrary

*** Test Cases ***
微信发送消息
    Open Application    http://127.0.0.1:4723/wd/hub    platformName=Android    platformVersion=7.0    deviceName=K6T6R17124002359    appPackage=com.tencent.mm    appActivity=com.tencent.mm.ui.LauncherUI    unicodeKeyboard=true    resetKeyboard=true    noReset=true
    Input Text    id=bfl    yb092226
    Click Element    id=d2y    #登录
    Click Element    id=f4u
    Input Text    id=bfl    yu
    Click Element    id=g8b    #点击好友名称
    FOR    ${n}    IN RANGE    1
        Wait Until Element Is Visible    id=ak7    30s
        Input Text    id=ak7    快点了，等你很久了，到底来不来啊！！！${n}
        Click Element    id=amr    #发送
        Wait Until Element Is Visible    id=amv
        Click Element    id=amv    #表情
        Click ElementsByIndex    id=rq    3
        Click ElementsByIndex    id=rq    4
        Click Element    xpath=//android.widget.Button[@text=\"发送\"]
        Click Element    id=am9
        Long Press    id=gms    4000
        Click Element    id=am9    #切换键盘
        log    ${n}
    END
    log    outside loop
    Click Element    id=rn
    Click Element    id=aai
    Comment    Click Element    id=rn
    [Teardown]    退出微信

微信发送信息分层实现
    [Tags]    A
    [Setup]    打开APP
    登陆微信    ujm159yhn753
    通讯录搜索好友    yu    name=高焰-Gavin
    FOR    ${n}    IN RANGE    1    3
    发送文字与语音信息    快点了，等你很久了，到底来不来啊！！！
    发送表情
    log    ${n}
    log    结束循环
    退出微信
    [Teardown]    关闭APP
