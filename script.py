#Ali Ansaripur 
from tkinter import *
import pyperclip 
root = Tk()
root.geometry("900x900")
pass_details = StringVar()
myList = []

def see_wifi_pass():
    import subprocess
    global myList
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    myList.append("------------------------")
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            myList.append("Wifi-->" + i)
            # myList.append("--")
            myList.append("Password-->" +results[0])
            myList.append("------------------------")
        except IndexError:
            myList.append("Wifi-->" +i)
            # myList.append("--")
            myList.append("")

def show_wifi_pass():
    def listToString(s):
        # initialize an empty string
        myStr = ""

        # traverse in the string
        for ele in s:
            myStr = myStr +  ele + "\n"

            # return string
        return myStr
    myStr = listToString(myList)
    pass_details.set(myStr)


def copytoclipboard():
    password = pass_details.get()
    pyperclip.copy(password)


Label(root, text="ALI`s Wifi Password Checker", font="calibri 20 bold").place(x = 60,y = 50)
Button(root, text=">> Initiate Process Now <<", command=see_wifi_pass).place(x = 60, y = 90)
Button(root, text=">> Show wifi pass details <<", command=show_wifi_pass).place(x = 60, y = 130)
Entry(root, textvariable=pass_details).place(width=800, height=50, x = 60, y = 160)
Button(root, text=">> Copy to clipbord <<", command=copytoclipboard).place(x = 60, y = 220)

root.mainloop()
