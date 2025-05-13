from googletrans import Translator
import pandas as pd

# 加载 Excel 文件
file_path = r"D:\Desktop\6063outline.xlsx"
df = pd.read_excel(file_path)

# 翻译 C 列（C2 到 C143）
translator = Translator()
translated_texts = []

for idx, val in df.iloc[1:142, 2].items():  # C列是 index=2（0-based），跳过C1
    try:
        text = str(val)
        translated = translator.translate(text, src='auto', dest='zh-cn').text
        translated_texts.append(translated)
    except Exception as e:
        print(f"Error at row {idx+2}: {e}")
        translated_texts.append("TRANSLATION ERROR")

# 将翻译结果写入新的列
df.loc[1:142, 'C_Translated'] = translated_texts

# 保存结果
output_path = r"D:\Desktop\6063outline_translated.xlsx"
df.to_excel(output_path, index=False)
print("✅ 翻译完成！结果保存在：", output_path)
