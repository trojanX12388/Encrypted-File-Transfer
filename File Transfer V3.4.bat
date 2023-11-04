@ECHO off
SETLOCAL EnableDelayedExpansion
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do     rem"') do (
  set "DEL=%%a"
)
cls
:start
@TITLE File Transfer V3.4
color 07
cls
echo *********************************************************************************************************
echo.
call :colorEcho 0e "                                       Encrypted File Transfer"
call :colorEcho 0A " V3.4"
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
echo.	Options [1] Send File - Send File to the client (Sender)
echo.
echo 		[2] Receive File - Listen and Receive file from server (Receiver)
echo.
echo 		[3] Encrypt Upload - Upload File to cloud in Encrypted mode.
echo. 
echo 		[4] Decrypt Download - Download uploaded file in Cloud and Decrypt.
echo.
echo 		[5] Key Generator - Generate File Encryption and Decryption Key (Stored in Generated key folder)
echo.
echo.
echo 		[6] Unsecured File Transfer - Transfer file to client without encryption.
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
if '%choice%'=='6' goto unsecured
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
python.exe -u bin/sender.py --key %key% --salt %salt% --file %file% --filename %filename%
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

python.exe -u bin/receiver.py --key %key% --salt %salt%
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
ECHO Enter upload filename:
set /p filename=
ECHO.

python.exe -u bin/encrypt_upload.py --file %file% --filename %filename%

pause
goto start

:decrypt
@TITLE Decrypt File Download
cls
set id=
echo ***************************************************************
echo.
echo 			Decrypt File Download
echo.
echo ***************************************************************
call :colorEcho 0A "Retrieving files from cloud..."
echo.
echo.


python.exe -u bin/retrieve_file.py
echo.
echo.
ECHO Enter file id to download:
set /p id=

python.exe -u bin/decrypt_download.py --id %id%
ECHO.

pause
goto start


:unsecured
cls
@TITLE Unsecured File Transfer
echo ***********************************************************************
echo.
echo 			Unsecured File Transfer
echo.
echo.
echo.	Options [1] Send File - Send File to the client (Sender)
echo.
echo 		[2] Receive File - Listen and Receive file (receiver)
echo.
echo 		[3] Back - Go back to main menu.
echo.
echo ***********************************************************************
ECHO.
set select=


ECHO Select Option:
set /p select=

if not '%select%'=='' set choice=%choice:~0,1%

if '%select%'=='1' goto unsec_send
if '%select%'=='2' goto unsec_receive
if '%select%'=='3' goto start

pause
goto start

:unsec_send
cls
@TITLE Unsecured File Sender
echo ***************************************************************
echo.
echo 			Unsecured File Sender 
echo.
echo ***************************************************************
ECHO.
set file=
set filename=
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
python.exe -u unsecured_FTP/send.py --file %file% --filename %filename%
ECHO.
pause
goto start

:unsec_receive
cls
@TITLE Unsecured File Receiver
echo ***************************************************************
echo.
echo 			Unsecured File Receiver
echo.
echo ***************************************************************
cls
ECHO. 
ECHO (Listening to 127.0.0.1:9999)
ECHO.
call :colorEcho 0c "Waiting for the sender..."
ECHO.

python.exe -u unsecured_FTP/receive.py 
ECHO.
ECHO. 
pause
goto start


:generate
cls
@TITLE RSA Key Generator
echo ***************************************************************
echo.
call :colorEcho 0A "              Key Generator"
echo.
echo.
echo ***************************************************************

python.exe -u bin/RSA_keygen.py
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

