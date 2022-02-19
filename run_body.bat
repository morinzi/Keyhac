copy /Y %AppData%\Keyhac\config_body.py %AppData%\Keyhac\config.py
taskkill /F /IM keyhac.exe
Start "" "%USERPROFILE%\Documents\keyhac_182\keyhac\keyhac.exe"