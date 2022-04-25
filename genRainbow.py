import data
import math

yellow = data.yellow   # 黄色
lime = data.lime      # 黄绿色
red = data.red      # 红色
orange = data.orange   # 橙色
blue = data.blue      # 蓝色
purple = data.purple    # 紫色
magenta = data.magenta  # 品红色
pink = data.pink     # 粉色
green = data.green     # 绿色
cyan = data.cyan      # 青色

def genRainbow(num, x, y, z, ori, r):
    path = data.getPath(num)
    color_arr = [str(red),str(orange),str(yellow),str(green),str(blue),str(purple),str(pink)]
    typ = str(data.burst)

    with open(path, 'w', encoding='utf-8') as f:
        for i in range(-len(color_arr) + 1, len(color_arr)):
            angle = i * 15
            if ori == 'xy':
                xM = math.sin(math.radians(angle))
                yM = math.cos(math.radians(angle))
                Motion = f'[{xM}d,{yM}d,0.0d]'
                xP = x + xM * r
                yP = y + yM * r
                pos = f'{xP} {yP} {z}'
            elif ori == 'yz':
                zM = math.sin(math.radians(angle))
                yM = math.cos(math.radians(angle))
                Motion = f'[0.0d,{yM}d,{zM}d]'
                zP = z + zM * r
                yP = y + yM * r
                pos = f'{x} {yP} {zP}'
            else:
                print('Error!genRainbow')
                input()

            color = color_arr[abs(i)]

            s = 'summon minecraft:firework_rocket ' + pos + ' {Motion:' + Motion + ',FireworksItem:{id:"minecraft:firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Trail:1b,Type:' + typ + ',Colors:[I;' + color + ']}]}}}}'
            f.write(s + '\n')
        f.write('\n')