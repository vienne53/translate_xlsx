文件名为6063outline.xlsx   
path:D:\Desktop\6063outline.xlsx
1. 安装依赖库
> 脚本用到了 googletrans 和 pandas，需要先安装这两个库。 打开命令行（PowerShell 或 CMD），输入：

pip install googletrans==4.0.0-rc1 pandas
> 注意：googletrans 推荐用 4.0.0-rc1 版本，兼容性更好。
2. 检查 Excel 文件路径
> 确保 D:\Desktop\6063outline.xlsx 这个文件存在。如果不在这个路径，请修改脚本中的 file_path 变量为实际路径。
3. 运行脚本
> 在命令行中，切换到脚本所在目录（假设在桌面）

cd D:\Desktop
> 然后运行：

python translate_excel.py  

4. 查看结果
> 运行成功后，会在桌面生成 6063outline_translated.xlsx 文件，翻译结果就在这个文件里。这里我们翻译的是C2-C143；翻译的内容放在最后一列

