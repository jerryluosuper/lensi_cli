import shutil
import win32api,win32con
import os
from fuzzywuzzy import process,fuzz

global lensi_path
lensi_path = "D:\Lensi"

def get_all_installed_software():
    reg_root = win32con.HKEY_LOCAL_MACHINE
    reg_paths=[r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall",r"Software\Microsoft\Windows\CurrentVersion\Uninstall"]
    rst_list=[]
    for path in reg_paths:
        pkey = win32api.RegOpenKeyEx(reg_root,path)
        for item in win32api.RegEnumKeyEx(pkey):
            value_paths = path+"\\"+item[0]
            #print(value_paths)
            try:
                vkey = win32api.RegOpenKeyEx(reg_root,value_paths)
                DisplayName,key_type = win32api.RegQueryValueEx(vkey,"DisplayName")
                UninstallString,key_type = win32api.RegQueryValueEx(vkey,"UninstallString")
                #print({'name':DisplayName,'Uninstall string':UninstallString})
                rst_list.append((DisplayName,UninstallString))
                win32api.RegCloseKey(vkey)
            except:
                pass
        win32api.RegCloseKey(pkey)
    return rst_list

def get_software():
    rst_list = get_all_installed_software()
    rst =[]
    for each in rst_list:
        rst.append(each[0])
    return  rst

def uninstall_software(software_name):
    rst_list = get_all_installed_software()
    uninstall_string=""
    for each in rst_list:
        if each[0] == software_name:
            uninstall_string=each[1]
            break
    if uninstall_string=="":
        print("Not found installed program.")
        return
    else:
        uninstall_string = uninstall_string.replace('\\','\\\\')
        os.chdir("\\".join(uninstall_string.split('\\')[:-1]))
        cmd=uninstall_string.split('\\')[-1]
        print("Running",cmd,"in","\\".join(uninstall_string.split('\\')[:-1]))
        os.system(cmd)
        choice = input("Do you want to clean the folder(Y/N):")
        if choice == "Y" or choice == "y":
            try:
                shutil.rmtree("\\".join(uninstall_string.split('\\')[:-1]))
            except:
                pass
def uninstall(app_name):
    softwares=get_software()
    # print(softwares)
    app_name_real = process.extractOne(app_name,softwares)[0]
    print("Uninstalling",app_name_real)
    uninstall_software(app_name_real)

def add_uninstall_app(app_name):
    os.chdir(lensi_path)
    f = open("app_list.txt","r")
    app_list = f.readlines()
    f.close()
    app_list_real = []
    for i in app_list:
        if i.find("Lensi") == -1:
            j=i.split()
            app_name_real = j[:len(j)-2]
            name = ""
            for k in app_name_real:
                name = name + k +" "
            name = name.strip(" ")
            del(j[:len(j)-2])
            j.insert(0,name.lower())
            j[len(j)-1] = j[len(j)-1].replace("\n","")
            app_list_real.append(j)
    for i in range(0,len(app_list_real)):
        if fuzz.partial_ratio(app_list_real[i][0],app_name)>=90:
            del(app_list_real[i])
        else:
            app_list_real[i][0] = app_list_real[i][0].title()
    write_text = ""
    for i in range(0,len(app_list_real)):
        write_text = write_text + app_list_real[i][0] + " " + app_list_real[i][1] + " " + app_list_real[i][2] + "\n"
    write_text = "Lensi 0.1.2 pip\n" + write_text
    with open("app_list.txt","w") as f:
        f.write(write_text)

# uninstall("steam")
add_uninstall_app("steam")