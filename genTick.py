import data

arr = data.arr
path_tick = './data/main/functions/tick.mcfunction'
with open(path_tick, 'a', encoding='utf-8') as f:
    for num in arr:
        s1 = 'execute if score i tick matches ' + str(num) + ' run function main:fw/' + str(num)
        f.write(s1 + '\n')