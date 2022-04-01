import subprocess
def get_app_installed():
    app_result = subprocess.getoutput("WMIC product get name")
    print(app_result)
    app_list_get = app_result.split("\n")
    app_list = []
    for i in app_list_get:
        if i != '' and i != 'Name' and i != 'HOTKEY':
            app_list.append(i[:i.find("  ")])
    return app_list



get_app_installed()