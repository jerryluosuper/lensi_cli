from setuptools import setup
setup(  
    name = 'Lensi',  
    version = '0.1.2', 
    description = 'Lensi, install apps from QQ 360 Hippo Scoop Winget Choco',  
    license = 'MIT License',  
    install_requires = ["bs4","fuzzywuzzy","fire","requests","configparser","tqdm","winshell","xpinyin"],  
    packages = ['Lensi_CLI'],  # 要打包的项目文件夹
    include_package_data=True,   # 自动打包文件夹内所有数据
    author = 'Lensit',  
    author_email = '1570515219@qq.com',
    url = 'https://gitee.com/lensit/lensi_cli/',
    entry_points={"console_scripts": ["lensi = Lensi_CLI.__main__:main"]},
)  

