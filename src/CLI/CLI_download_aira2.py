import os
def download_aria2(link,SIP="D:\Scoop",lensi_path):
    exe_path = SIP +"\shims\aria2c.exe"
    order = exe_path +'--dir='+lensi_path +'\Download '+  ' --allow-overwrite=true --split=16 --max-connection-per-server=16 --console-log-level=warn  --no-conf=true --follow-metalink=true --metalink-preferred-protocol=https --summary-interval=0 --continue --min-tls-version=TLSv1.2 --retry-wait=2 --min-split-size=1M ' + link
    os.system(order)
if __name__ == '__main__':
    link = '"http://dl.softmgr.qq.com/original/Office/blender-2.80-windows64.msi"'
    download_aria2(link)