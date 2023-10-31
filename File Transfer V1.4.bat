@ECHO off
SETLOCAL EnableDelayedExpansion
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do     rem"') do (
  set "DEL=%%a"
)
cls
:start
@TITLE File Transfer V1.4
color 07
cls
echo *********************************************************************************************************
echo.
call :colorEcho 0e "                                       Encrypted File Transfer"
call :colorEcho 0A " V1.4"
echo.
call :colorEcho 0e "                                       Copyrighted"				
call :colorEcho 0f " Oct-30-2023"
echo.
echo.
call :colorEcho 0b "                                       Created by " 
call :colorEcho 0c " TrojanX12388"
call :colorEcho 0b " and"
call :colorEcho 06 " Team SFTP"  
echo.
echo.
echo *********************************************************************************************************
echo.
echo.	Options [1] Send File - Send File to the client (receiver)
echo.
echo 		[2] Receive File - Listen and Receive file from server (sender)
echo.
echo 		[3] Encrypt Upload - Upload File to cloud in Encryted mode (Public Key)
echo. 
echo 		[4] Decrypt Download - Download uploaded file in cloud and decrypt (Private Key)
echo.
echo 		[5] RSA Key Generator - Generate Public and Private RSA Key (Stored in Generated key folder)
echo.
echo.
echo 		[e] Exit
echo.
echo *********************************************************************************************************
ECHO.
set choice=
set /p choice=Select option:

if not '%choice%'=='' set choice=%choice:~0,1%

if '%choice%'=='1' goto send
if '%choice%'=='2' goto receive
if '%choice%'=='3' goto encrypt
if '%choice%'=='4' goto decrypt
if '%choice%'=='5' goto generate
if '%choice%'=='e' goto exit

ECHO "%choice%" is not valid, try again
ECHO.

goto start


:send
cls
@TITLE File Sender
echo ***************************************************************
echo.
echo 			File Sender 
echo.
echo ***************************************************************
ECHO.
set key=
set salt=
set file=
set filename=

ECHO Enter Password:
set /p key=
ECHO Enter Salt Key:
set /p salt=
ECHO.
ECHO Generating Hash code...
cls
ECHO.
ECHO List of files (In the File folder):
ECHO.
echo ***************************************************************
ECHO.
dir file /b
ECHO.
ECHO.
echo ***************************************************************
ECHO.
ECHO Select file to send:
set /p file=
ECHO.
ECHO File Output Name:
set /p filename=

ECHO.
call :colorEcho 0c "Sending File to the client..."
Echo (127.0.0.1:9999)
ECHO. 
ECHO.
python.exe -u sender.py --key %key% --salt %salt% --file %file% --filename %filename%
ECHO.
pause
goto start

:receive
cls
@TITLE File Receiver
set key=
set salt=
echo ***************************************************************
echo.
echo 			File Receiver
echo.
echo ***************************************************************

ECHO.
ECHO Enter Password:
set /p key=
ECHO Enter Salt Key:
set /p salt=
ECHO.
ECHO.
ECHO Generating Hash code...
cls
ECHO. 
ECHO (Listening to 127.0.0.1:9999)
ECHO.
call :colorEcho 0c "Waiting for the sender..."
ECHO.

python.exe -u receiver.py --key %key% --salt %salt%
ECHO.
ECHO. 
pause
goto start

:encrypt
cls
@TITLE Encrypted File Upload
set file=
set filename=
echo ***************************************************************
echo.
echo 			Encrypted File Upload
echo.
echo ***************************************************************
ECHO.
ECHO List of files (In the File folder):
ECHO.
echo ***************************************************************
ECHO.
dir file /b
ECHO.
ECHO.
echo ***************************************************************
ECHO.
ECHO Select file to upload in cloud:
set /p file=
ECHO.
ECHO Select output filename:
set /p filename=

python.exe -u encrypt_upload.py --file %file% --filename %filename%

pause

:decrypt
@TITLE Decrypt File Download
set key=
set salt=
echo ***************************************************************
echo.
echo 			Decrypt File Download
echo.
echo ***************************************************************


pause

:generate
cls
@TITLE RSA Key Generator
echo ***************************************************************
echo.
call :colorEcho 0A "              RSA Key Generator"
echo.
echo.
echo ***************************************************************

python.exe -u RSA_keygen.py
echo.
call :colorEcho 0c "Key has been successfully generated!"
echo.
call :colorEcho 0e "Key is located at generated_key folder."
echo.
echo.
echo.
pause

goto start


:end
pause

:exit
cls
echo ***************************************************************
echo.
echo Thank You for using Encrypted File Transfer!
echo.
echo ***************************************************************
pause
exit


:colorEcho
echo off
<nul set /p ".=%DEL%" > "%~2"
findstr /v /a:%1 /R "^$" "%~2" nul
del "%~2" > nul 2>&1i
