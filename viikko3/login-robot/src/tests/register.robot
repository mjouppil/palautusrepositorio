*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pekka  pekka123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  vellu  pekka123
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  pe  pekka123
    Output Should Contain  Username too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  64113  pekka123
    Output Should Contain  Username not valid

Register With Valid Username And Too Short Password
    Input Credentials  pekka  pekka69
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pekka  pekkaiso
    Output Should Contain  Password not valid

*** Keywords ***
Input New Command And Create User
    Create User  vellu  vellu123
    Input New Command