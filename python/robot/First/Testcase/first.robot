*** Test Cases ***
Hello Robot Framework
    [Documentation]
    Log To Console     this is a message for the console
    Log     this is a message for the log
    Log Variables
    Should Be Equal     ${TEST_NAME}    Hello Robot Framework

