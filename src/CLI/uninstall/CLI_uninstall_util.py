import win32api,win32con
import os
import subprocess
import ctypes, sys
from fuzzywuzzy import process
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
        print("uninstall "+ software_name)
        uninstall_string = uninstall_string.replace('\\','\\\\')
        os.chdir("\\".join(uninstall_string.split('\\')[:-1]))
        cmd=uninstall_string.split('\\')[-1]
        print(cmd)
        subprocess.Popen("",executable=cmd)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def uninstall(app_name):
    if is_admin():
        softwares=get_software()
        # print(softwares)
        app_name_real = process.extractOne(app_name,softwares)[0]
        print("Uninstalling",app_name_real)
        uninstall_software(app_name_real)
        pass
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

uninstall("steam")