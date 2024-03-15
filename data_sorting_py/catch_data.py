# pip install requests
# pip install fake_useragent
# pip install openpyxl
import urllib3 # 此行可加可不加，若不加入此行會跳出沒有SSL憑證訊息(對執行程序並無影響)。 pip install urllib3
import requests
from fake_useragent import UserAgent
from openpyxl import Workbook

urllib3.disable_warnings() #若不加 import urllib3 可刪除這行

# 需要修改的參數為以下
#---------------------------------------------------------------------------------------------
# 修改方式:先打開Nessus，選擇以掃描完的網站點進去，瀏覽器網址的上的網址最後會有一個數字
# 例如 https://localhost:8834/#/scans/reports/24/scan-summary，就以reports後面那個數字去替換schedule_id的"24"
schedule_id = 24

# 副檔名一律為.xlsx，修改檔案路徑
file_name = './購物網站/pchome.xlsx'

# 使用者資訊
login_data = {
    'username' : '',
    'password' : ''
}
#---------------------------------------------------------------------------------------------

url = f'https://localhost:8834/scans/{schedule_id}?limit=2500&includeHostDetailsForHostDiscovery=true'
login_url = 'https://localhost:8834/session'

session = requests.Session()
response = session.post(login_url, data=login_data, verify=False)
catch_token = response.json()
token = catch_token['token']
cookie = "token=" + token

wb = Workbook()
ws = wb.active

title = ['風險代號', '風險等級']
ws.append(title)

ua = UserAgent()
header = {
    'User-Agent': ua.random,
    'X-Cookie' : cookie
}

response = requests.get(url, headers=header, verify=False)

Sev = {1:"LOW", 2:"MEDIUM", 3:"HIGH", 4:"CRITICAL"}

if response.status_code == 200:
    root_json = response.json()

    for data in root_json['vulnerabilities']:
        information = []
        information.append((data['plugin_id']))
        
        if data['severity'] in Sev:
            information.append(Sev[data['severity']])
        elif data['severity'] == 0:
            continue
        else:
            print(f"Unknow severity_num:{data['severity']}")
            exit()

        ws.append(information)
else:
    print(f"Error, {response}")
    exit()

wb.save(file_name)

print('Program execution completed.')
