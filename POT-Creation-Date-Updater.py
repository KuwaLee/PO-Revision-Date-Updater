import re
from datetime import datetime
import pytz

def update_pot_creation_date(file_path, timezone='UTC'):
    # 讀取 POT 檔案內容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 獲取當前時間戳記，並轉換為指定時區
    tz = pytz.timezone(timezone)
    now = datetime.now(tz)
    formatted_date = now.strftime('POT-Creation-Date: %Y-%m-%d %H:%M%z\\\\n')
    # 更新 "POT-Creation-Date" 時間戳記
    new_content = re.sub(r'POT-Creation-Date: .+\\n', formatted_date, content)

    # 將更新後的內容寫回檔案
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

# 使用範例
# 假設你的 POT 檔案路徑是 'path/to/your/template.pot'
# 並且你想將時區設定為 'Asia/Taipei'
update_pot_creation_date('path/to/your/template.pot', 'Asia/Taipei')