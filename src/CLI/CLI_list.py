import os
from fuzzywuzzy import fuzz

def add_installed_app(app_name,app_source,app_version=" "):
    os.chdir("D:\Lensi")
    f = open("app_list.txt","r")
    app_list = f.readlines()
    f.close()
    app_list_real = []
    for i in app_list:
        if i.find("scoop") == -1 and i.find("choco") == -1 and i.find("winget") == -1:
            j=i.split()
            app_name_real = j[:len(j)-2]
            name = ""
            for k in app_name_real:
                name = name + k +" "
            name = name.strip(" ")
            del(j[:len(j)-2])
            j.insert(0,name)
            j[len(j)-1] = j[len(j)-1].replace("\n","")
            app_list_real.append(j)
    for i in range(0,len(app_list_real)):
        # print(app_list_real[i])
        # print(app_list_real[i][0])
        # print(app_name)
        # print(fuzz.partial_ratio(app_list_real[i][0],app_name))
        if fuzz.partial_ratio(app_list_real[i][0],app_name)>=90:
            app_list_real[i][0] = app_name
            app_list_real[i][1] = app_version
            app_list_real[i][2] = app_source
    write_text = ""
    for i in range(0,len(app_list_real)):
        write_text = write_text + app_list_real[i][0] + " " + app_list_real[i][1] + " " + app_list_real[i][2] + "\n"
    with open("app_list.txt","w") as f:
        f.write(write_text)
add_installed_app("Steam","qq","asasdfd")