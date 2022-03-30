import os
from fuzzywuzzy import fuzz,process
from xpinyin import Pinyin 
import json
import csv
import codecs
import subprocess
def Scoop_info(app_name):
    return subprocess.getoutput('scoop info '+ app_name)

def winget_info_id(app_id):
    cmd = "winget show --id " + app_id
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,universal_newlines=True).stdout.read()
    return pipe

def choco_install_app(app_name):
    os.system("choco install "+app_name)

def Scoop_install_app(app_name):
    os.system("scoop install " + app_name)

def winget_install_app_id(app_id):
    os.system("winget install --silent --accept-source-agreement --id "+ app_id)


def Scoop_search_lensi(name,buckets_list_install,search_limit,Scoop_install_place ):
    for ch in name:
        if '\u4e00' <= ch <= '\u9fff': ##识别中文
            p = Pinyin() #scoop 中文搜索不好，转为拼音
            name = p.get_pinyin(name,'')
            break
    # print(name)
    search_list = process.extract(name,buckets_list_install, limit=search_limit) 
    # 模糊搜索
    # print(search_list)
    app_name_all = []
    for i in range(0,search_limit):
        app_name = search_list[i][0][0][search_list[i][0][0].find('\\'):].strip("\\")
        app_name_install = search_list[i][0][0]
        app_json = []
        # print(app_name_install,app_name)
        app_name_json = Scoop_install_place + "\\buckets\\" + app_name_install[:app_name_install.find('\\')] + "\\bucket\\" + app_name + ".json"
        # app_name_json = "D:\\buckets\\" + app_name_install[:app_name_install.find('\\')] + "\\bucket\\" + app_name + ".json"
        # print(app_name_json)
        try:
            with open(app_name_json, 'r') as f:
                app_json = json.load(f)
                # 解析json，获取detail
            app_detail = [app_name_install,app_json["version"],app_json["description"],app_name,app_json["homepage"],app_name,"https://scoop.netlify.app/scoop.svg",fuzz.partial_ratio(app_name,app_name_install),"Scoop"]
            app_name_all.append(app_detail) 
            # TODO The missing 'n' and other ----BUG 放弃！！！ (╯▔皿▔)╯
        except:
            pass
            # print("error")
    return app_name_all

def Scoop_buckets_save(Scoop_install_place):#遍历scoop bucket 存入csv中
    #简单来说就是获取每个buckets里bucket的文件
    buckets_list_install = []
    os.chdir(Scoop_install_place+"\\buckets")
    buckets_names = os.listdir()
    for i in buckets_names:
        # print(i)
        dir = Scoop_install_place + "\\buckets\\" + i + "\\bucket"
        os.chdir(dir)
        bucket_list = os.listdir()
        for j in bucket_list:
            buckets_list_install.append(i+"\\"+j.strip(".json"))
    os.chdir("D:\\")
    file_csv = codecs.open("buckets_list_install.csv",'w+','utf-8')#追加
    writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for data in buckets_list_install:
        list_data = [data]
        writer.writerow(list_data) #写入csv 

def choco_info(app_name):
    app_detail = subprocess.getoutput('choco info '+ app_name)
    return app_detail

def choco_search(app_name,limmit_num): #choco搜索解析
    '''
    大致输出格式
    app_name_1|app_version_1
    app_name_1|app_version_1
    '''
    try:
        for ch in app_name:
            if '\u4e00' <= ch <= '\u9fff':
                p = Pinyin() 
                app_name = p.get_pinyin(app_name,'') #一样的，拼音搜索
                break
        # print(app_name)
        cmd = 'choco search '+ app_name + ' --limitoutput --page=1 --page-size=' + str(limmit_num)
        pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE, universal_newlines=True)
        search_result = pipe.stdout.read()
        pipe.communicate()#等待
        # print(search_result.replace("Directory 'C:\ProgramData\chocolatey\lib' does not exist.",""))
        #怎么说，这段真的乱。。。
        search_list = [] #干嘛的？我怎么知道 看上去像用|进行分离后的列表
        search_list_all = search_result.split() #通过空行分离成列表
        search_list_all_a = []  #干嘛的？我怎么知道 看上去像返回的列表，所有搜索到的软件的整合
        for name in search_list_all:
            search_list.append(name.split("|")) #遍历空行分离后的列表，再用|进行分离
        if search_list[0] == ['Directory']:
            del(search_list[0:5]) #排除"Directory 'C:\ProgramData\chocolatey\lib' does not exist."的干扰
            #好低效的方法
        # print(search_list)
        if len(search_list)==0:
            search_list = None 
            #排除空列表的错误？我觉得没用啊
            return search_list
            # print(search_list)
        # print(search_list)
        for i in search_list:
            app_name_true = str(i[0]) #获取非模糊名称
            # print(app_name_true)
            # print(cmd)
            cmd = "choco info "+ app_name_true
            # print(cmd)
            pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
            app_detail = str(pipe.stdout.read())
            pipe.communicate()
            app_detail = app_detail.replace("\\r","")
            app_detail = app_detail.replace("\\n","")
            # print(app_detail)
            # app_detail = subprocess.getoutput('choco info '+ app_name_true) #info 获取官网和detail
            if app_detail.find("0 packages found.") != -1:
                return None
            app_home_url = app_detail[int(app_detail.find('Software Site:')):int(app_detail.find("\n",app_detail.find("Software Site:")))].strip("Software Site:")
            app_detail_info = app_detail[int(app_detail.find('Summary: ')):int(app_detail.find("\n",app_detail.find("Summary: ")))].strip("Summary: ")
            # 获取官网
            # 部分有bug啊，但我不想解决
            # print(i[0],i[1],app_detail_url,app_name_true)
            search_list_all_a.append([i[0],i[1],app_detail_info,i[0],app_home_url.strip("\n"),app_name_true,"https://chocolatey.org/assets/images/global-shared/logo.svg",fuzz.partial_ratio(app_name,i[0]),"Choco"])
        # search_list_all_a.append("Choco")
        return search_list_all_a
    except:
        return None

def winget_search(app_name,limmit_num):#winget 搜索解析
    '''
    大致输出格式：
    -\|/ 
    名称          ID           版本    源
    -------------------------------------------
    xx xx xx xx
    <由于结果限制而截断了其他条目>
    '''
    try:
        search_result_list_all = []
        app_name = app_name.replace(" ","") #winget search 软件名中不能有空格
        # print(app_name)
        cmd = "winget search " + app_name + " -n " + str(limmit_num)
        # 一个非常非常非常又烂又低效的方法——存储到文件再读取
        # TODO 优化！！！
        pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)#subprocess 将输出保存到search_result.txt中
        search_result_list_un = pipe.stdout.readlines()[2:]#去除前三行干扰 有bug
        search_result_list = []
        pipe.communicate()
        for i in search_result_list_un:
            search_result_list.append(i.decode("utf-8"))
        # print(search_result_list)
        pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)#subprocess 将输出保存到search_result.txt中
        search_result_txt = pipe.stdout.read().decode("utf-8")
        pipe.communicate()#等待
        # print(search_result_txt)
        if search_result_txt.find("找不到与输入条件匹配的程序包。") != -1:
            return search_result_list_all #异常处理——找不到或根本不存在？
        if  search_result_txt.find("<由于结果限制而截断了其他条目>") != -1:
            search_result_list = search_result_list[:len(search_result_list)-1] # 去除末行干扰
        cnt_cut = 0
        for i in range(0,len(search_result_list)):
            if search_result_list[i] == "--------------------------------------------" : #为啥我觉得只要这一句就好了
                cnt_cut = i
                break
        search_result_list = search_result_list[cnt_cut:] #顺带解决开机第一次100%加载的bug
        search_result = [] #这又在干嘛？ 以空行分隔后的软件列表
        # print(search_result_list)
        for i in search_result_list:
            search_result.append(i.split())#以空行分隔
        for j in search_result:
            name = "".join(j[:len(j)-3]) #因为id version source 是连续的 不带空格的，所以确定这三个把前面的连起来
            del(j[:len(j)-3])
            j.insert(0,name)
            # print(name)
        # print (search_result)
        if search_result == []:#判断是否为空，防止报错
            search_result_list_all = None
            return search_result_list_all
        else:
            # print(len(search_result))
            # # print(search_result)
            if len(search_result) == 1: #防止range（0，0）的错误
                cmd = "winget show --id " + search_result[0][1]
                #换汤不换药
                pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)#subprocess 将输出保存到search_result.txt中
                info_result = pipe.stdout.read().decode("utf-8")
                pipe.communicate()#等待？
                info_result_url = info_result[int(info_result.find('URL:')):int(info_result.find("\n",info_result.find("URL:")))].strip("URL:")
                info_detail = info_result[int(info_result.find('描述: ')):int(info_result.find("\n",info_result.find("描述: ")))].strip("描述: ")
                #解析官网url
                # print(info_result_url)
                search_result_app = [search_result[0][0],search_result[0][2],info_detail.strip("\r"),search_result[0][0],info_result_url.strip("\r"),search_result[0][1],None,fuzz.partial_ratio(app_name,search_result[0][0]),"Winget"]
                #统一格式
                # print(search_result_app)
                search_result_list_all.append(search_result_app)
                # search_result.append("Winget")
                return search_result_list_all
            else:
                #print(search_result)
                for i in range(0,len(search_result)):#除len = 1的情况 其余同上
                    cmd = "winget show --id " + search_result[i][1]
                    #换汤不换药
                    pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)#subprocess 将输出保存到search_result.txt中
                    info_result = pipe.stdout.read().decode("utf-8")
                    pipe.communicate()#等待？
                    info_result_url = info_result[int(info_result.find('URL:')):int(info_result.find("\n",info_result.find("URL:")))].strip("URL:")
                    info_detail = info_result[int(info_result.find('描述: ')):int(info_result.find("\n",info_result.find("描述: ")))].strip("描述: ")
                    #解析官网url
                    # print(info_result_url)
                    search_result_app = [search_result[i][0],search_result[i][2],info_detail.strip("\r"),search_result[i][0],info_result_url.strip("\r"),search_result[i][1],None,fuzz.partial_ratio(app_name,search_result[i][0]),"Winget"]
                    #统一格式
                    # print(search_result_app)
                    search_result_list_all.append(search_result_app)
                    # search_result.append("Winget")
                # search_result.append("Winget")
        return search_result_list_all
    except:
        return None

def Scoop_buckets_load(): #加载csv到列表
    buckets_list_install = []
    os.chdir("D:\\")
    with open("buckets_list_install.csv", "r", encoding='UTF-8') as file:
        data = csv.reader(file)
        for row in data:
            # row_l = [row] 
            #读取csv
            # buckets_list_install.append(row_l)
            buckets_list_install.append(row)
    return buckets_list_install

