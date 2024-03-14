import pandas as pd
import os

merged_data = pd.DataFrame()

folder_path = '../應用型網站/nessus excel'
archive_path = ('../各網站分析統計/應用型網站_nessus.xlsx')

# 檔案合併
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(folder_path, filename)
        data = pd.read_excel(file_path)

        merged_data = pd.concat([merged_data, data], axis=0)

# -----------------------------------------------------------------------------
# 統整檔案資訊
# 各風險等級的總數
risk_count_by_level = merged_data['風險等級'].value_counts()

# 按照其他相同資訊進行分組，並計算每個組的數量
other_info_count = merged_data.groupby(['風險代號', '風險等級']).size().reset_index(name='數量')

# 創建 ExcelWriter 對象
with pd.ExcelWriter(archive_path, engine='openpyxl') as writer:
    # 將全數據寫入工作表
    merged_data.to_excel(writer, sheet_name='全數據', index=False)

    # 將各風險數量統計寫入工作表
    risk_count_by_level.to_frame(name='數量').to_excel(writer, sheet_name='各風險數量統計')

    # 將相同資訊統計寫入工作表
    other_info_count.to_excel(writer, sheet_name='相同資訊統計', index=False)

    # 將按風險等級劃分的相同資訊寫入不同的工作表
    for risk_level in other_info_count['風險等級'].unique():
        risk_level_data = other_info_count[other_info_count['風險等級'] == risk_level]
        # 刪除風險等級欄位
        risk_level_data = risk_level_data.drop(columns=['風險等級'])
        risk_level_data.to_excel(writer, sheet_name=f'風險等級_{risk_level}', index=False)
