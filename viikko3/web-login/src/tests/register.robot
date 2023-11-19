*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Confirm
Test Teardown  Reset Test

*** Test Cases ***
Register With Valid Username And Password
    Set Username  erkki
    Set Password  erkki123
    Set Password Confirmation  erkki123
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  er
    Set Password  erkki123
    Set Password Confirmation  erkki123
    Submit Register Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  jorma
    Set Password  jormaiso
    Set Password Confirmation  jormaiso
    Submit Register Credentials
    Register Should Fail With Message  Password not valid

Register With Nonmatching Password And Password Confirmation
    Set Username  jorma
    Set Password  jorma123
    Set Password Confirmation  jorma456
    Submit Register Credentials
    Register Should Fail With Message  Password and password confirmation do not match

Login After Successful Registration
    Set Username  ${USER1}
    Set Password  ${PASS1}
    Set Password Confirmation  ${PASS1}
    Submit Register Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  ${USER1}
    Set Password  ${PASS1}
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  ${USER2}
    Set Password  ${PASS2}
    Set Password Confirmation  ${PASS1}
    Submit Register Credentials
    Register Should Fail With Message  Password and password confirmation do not match
    Go To Login Page
    Set Username  ${USER2}
    Set Password  ${PASS2}
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Go To Register Page And Confirm
    Go To Register Page
    Register Page Should Be Open

Reset Test
    Reset Application

Register Should Succeed
    Register Success Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Register Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}