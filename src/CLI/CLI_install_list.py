import os


global lensi_path
lensi_path = "D:\Lensi"
global path_now
path_now = os.getcwd()
def out_put_list():
    os.chdir(lensi_path)
    f = open("app_list.txt","r")
    app_list = f.readlines()
    f.close()
    app_list_real = []
    for i in app_list:
        if i.find("scoop") == -1 and i.find("choco") == -1 and i.find("winget") == -1 and i.find("Lensi") == -1 and i.find("lensi") == -1:
            j=i.split()
            app_name = j[:len(j)-2]
            name = ""
            for k in app_name:
                name = name + k +" "
            name = name.strip(" ")
            del(j[:len(j)-2])
            j.insert(0,name)
            j[len(j)-1] = j[len(j)-1].replace("\n","")
            del(j[len(j)-2])
            app_list_real.append(j)
    write_text = ""
    for i in range(0,len(app_list_real)):
        write_text = write_text + app_list_real[i][0] + " " + app_list_real[i][1] + "\n"
    os.chdir(path_now)
    with open("app_list.txt","w") as f:
        f.write(write_text)

def in_put_list(file_name):
    os.chdir(path_now)
    f = open(file_name,"r")
    app_list = f.readlines()
    f.close()
    app_list_real = []
    for i in app_list:
        j=i.split()
        app_name = j[:len(j)-1]
        name = ""
        for k in app_name:
            name = name + k +" "
        name = name.strip(" ")
        del(j[:len(j)-1])
        j.insert(0,name)
        j[len(j)-1] = j[len(j)-1].replace("\n","")
        app_list_real.append(j)
    # print(app_list_real)

# out_put_list()
in_put_list("app_list.txt")