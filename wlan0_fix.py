import subprocess

command_down = ["ip", "link", "set", "wlan0", "down"]

subprocess.call(command_down)
print("The Work Is Good!!!")

command_rename = ["ip", "link", "set", "wlan0", "name", "wlan0mon"]

subprocess.call(command_rename)
print("Goddamn The Work Is Done!!!")