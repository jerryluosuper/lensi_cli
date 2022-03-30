'''
Author: your name
Date: 2022-03-27 09:03:38
LastEditTime: 2022-03-27 12:38:24
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\CLI\CLI_install.py
'''
import os
import zipfile
from os import path  
import winshell 

def create_shortcut_to_desktop(app_folder,file_name):  
    target = "D:\\Lensi\\APP_Portable\\" +app_folder + "\\" + file_name
    title = file_name
    s = path.basename(target)  
    fname = path.splitext(s)[0]  
    winshell.CreateShortcut(Path = path.join(winshell.desktop(), fname + '.lnk'),Target = target,Icon=(target, 0), Description=title)  

def create_shortcut_to_startup(app_folder,file_name):  
    target = "D:\\Lensi\\APP_Portable\\" +app_folder + "\\" + file_name
    title = file_name
    s = path.basename(target)  
    fname = path.splitext(s)[0] 
    winshell.CreateShortcut(Path = path.join(winshell.startup(),fname + '.lnk'),Target = target,Icon=(target, 0),Description=title) 

def create_shortcut_to_startmenu(app_folder,file_name):  
    target = "D:\\Lensi\\APP_Portable\\" +app_folder + "\\" + file_name
    title = file_name
    s = path.basename(target)  
    fname = path.splitext(s)[0] 
    Path = path.join(winshell.startup().strip("\Startup"),"Lensi Apps",fname + '.lnk')
    winshell.CreateShortcut(Path,Target = target,Icon=(target, 0),Description=title) 

def install(file_name,app_folder=None):
    os.chdir("D:\Lensi\Download")
    file_name_kinds = file_name[file_name.rfind("."):].strip(".")
    if file_name_kinds == "zip":
        zip_file = zipfile.ZipFile(file_name)
        zip_file.extractall("D:\Lensi\APP_Portable\\" + app_folder + "\\")
        zip_file.close()
    elif file_name_kinds == "msi":
        cmd = "msiexec /i " + "D:\Lensi\Download\\" + file_name + " /norestart  /passive"
        # print(cmd)
        os.system(cmd)
    elif file_name_kinds == "exe":
        cmd = file_name + "/S /D=D:\Lensi\APP_Installed"
        os.system(cmd)
    else:
        os.system(file_name)
install("SteamSetup.exe")
# create_shortcut_to_startmenu("geek","geek.exe")