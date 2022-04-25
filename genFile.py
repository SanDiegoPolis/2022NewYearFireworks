import data

arr = data.arr
for num in arr: # 会清空所有文件，慎！
    path = data.getPath(num)
    with open(path, 'a', encoding='utf-8') as f:
        f.write('')