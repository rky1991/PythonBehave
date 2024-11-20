Python - Behave Development

Python Imp Commnads for Virtual Env Setup :

Activate Virtual Env Command :
venv\Scripts\activate

Note:-if Virtual Env is restricted
to Check the Resctriction Command  :-->
get-ExecutionPolicy

********************************
According to Microsoft Tech Support it might be a problem with Execution Policy Settings.

To fix it, you should try executing below Conmmand
Set-ExecutionPolicy Unrestricted -Scope Process
(as mentioned in the comment section by @wtsiamruk) in your PowerShell window. This would allow running virtualenv in the current PowerShell session.

There is also another approach that is more unsafe, but recommended by MS Tech Support.

This approach would be to use below command:-
Set-ExecutionPolicy Unrestricted -Force

(which do unleash powers to screw Your system up).
However, before you use this unsafe way, be sure to check what your current ExecutionPolicy setting is by using below Command :-->
get-ExecutionPolicy.
Then, when you are done, you can revert back to this ExecutionPolicy by using
Set-ExecutionPolicy %the value the get-ExecutionPolicy command gave you% -Force.


**********************************************************

To check all the packeage installed :-->>
pip freeze

C:\PythonWorkSpace\pythonProject\BehaveProject\drivers\chromedriver.exe


Allure Report -->
allure-behave  --> installed in env only

pip uninstall allure-behave --> To uninstall

Command for generate Allure report :-->
Json Report will generate in report folder :-
behave -f allure_behave.formatter:AllureFormatter -o reports/ features

For Specific Feature File -->
behave -f allure_behave.formatter:AllureFormatter -o "reports" features/LoginHRM.feature

Command for convert all Json reports to  in single html report :--
allure serve reports/


To Add/install Allure Scoop--->>

Run these 2 commands in Powershell to install scoop
Command 1 ->
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Command 2 ->
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
now once that is done run other command which installs allure
Command -->
scoop install allure
now check version of allure using  --> allure --version

