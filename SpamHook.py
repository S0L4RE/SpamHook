import os, sys, shutil
try:
    import requests
except ImportError:
    try:
        import pip
    except ImportError:
        raise RuntimeError("You do not have pip or the requests module installed.")
    else:
        try:
            os.system("pip3 install requests")
        except Exception as e:
            print("Failed to install requests module, details: {}".format(e))
        else:
            print("Installed requests module!")

print("SpamHook")
print("--------")
print("Utility that spams a Discord webhook.")
print("By Hexexpeck, version 1.0.0")
print("--------")
print("NOTE: Spam in this console window is normal.")
print("NOTE 2: Discord can rate limit you, so watch out.")
print("--------")
try:
    input = raw_input
except:
    pass

hookUrl = input("Webhook URL: ")
hookMsg = input("Message to spam: ")

runHook = True
while runHook is True:
    r = requests.post(hookUrl, data={'content': hookMsg, 'tts': 'true'})
    print("Executed webhook!")

print("Stopping webhook spam...")
