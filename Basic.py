import os, platform, time, sys
print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mChecking For Update...')
os.system('git pull --quiet 2>/dev/null')
os.system('xdg-open https://chat.whatsapp.com/KThLuumIszgD0UCJz3T33C')
mrkoja = platform.architecture()[0]
if mrkoja == '64bit':
 os.system("curl -L https://github.com/K0J4/Termux-Basic/releases/download/basic/aarch64 > aarch64")
 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Device is 64bit');time.sleep(2)
 os.system('chmod 777 aarch64 && ./aarch64')
elif mrkoja == '32bit':
 os.system("curl -L https://github.com/K0J4/Termux-Basic/releases/download/basic/arm32 > arm32")
 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Devive is 32bit');time.sleep(2)
 os.system('chmod 777 arm32 && ./arm32')
 
