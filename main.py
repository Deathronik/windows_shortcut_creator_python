import os
import winshell
def create_shortcut(i):
    target_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

    with winshell.shortcut(target_path) as link:
        link.path = target_path
        link.description = f"Discord #{i}"
        link.arguments = f'--profile-directory="Profile {i + 2}"'
        link.icon_location = (rf"%USERPROFILE%\AppData\Local\Google\Chrome\User Data\Profile {i + 2}\Google Profile.ico", 0)
        link.working_directory = "E:\\Learn\\Learn_python\\discords-shortcut-creator"

    os.rename("chrome.exe.lnk", f"Discord #{i}.lnk")

for i in range(1, 67):
    create_shortcut(i)
