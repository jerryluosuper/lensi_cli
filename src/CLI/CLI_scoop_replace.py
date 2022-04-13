import os
import subprocess
import time
def Scoop_update():
    os.system("scoop update")
def Scoop_buckets_replace(Scoop_install_place,to_replace,replace_to):#遍历scoop bucket 存入csv中
    #简单来说就是获取每个buckets里bucket的文件
    Scoop_update()
    cnt = 0;
    os.chdir(Scoop_install_place+"\\buckets")
    buckets_names = os.listdir()
    for i in buckets_names:
        dir = Scoop_install_place + "\\buckets\\" + i + "\\bucket"
        os.chdir(dir)
        bucket_list = os.listdir()
        for j in bucket_list:
            try:
                with open(j,"r",encoding='utf-8') as f:
                    json_text = f.read()
                if json_text.find(to_replace) != -1:
                    json_text = json_text.replace(to_replace,replace_to)
                    cnt = cnt + 1
                    with open(j,"w") as f:
                        f.write(json_text)
                        
            except:
                pass
    return cnt
# T1 = time.time()    
# print(Scoop_buckets_replace("D:\\Scoop","github.com","hub.fastgit.xyz"))
# T2 = time.time()
# print('程序运行时间:%s毫秒' % ((T2 - T1)*1000))
# print("Done!")
def Lensi_check_scoop():
    check_result = subprocess.getoutput('scoop -h')
    # print(check_result)
    if check_result.find("不") != -1:
        return False
    else:
        return True
print(Lensi_check_scoop())