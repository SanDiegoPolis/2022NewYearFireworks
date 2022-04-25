import data

small = data.small
big = data.big
star = data.star
burst = data.burst

def genBig(num, x3f, y_burst, y_small, y_big, y3f, z3f, color_burst, color_small, color_big, color3f, ori, mode = 'w', x2 = 'null', x3 = 'null', x_burst = 'null', x_small = 'null', x_big = 'null', z2 = 'null', z3 = 'null', z_burst = 'null', z_small = 'null', z_big = 'null'):
    path = data.getPath(num)

    pos_burst = []
    pos_small = []
    pos_big = []
    pos3f = []

    if ori == 'xy':
        for x in x3:
            pos_burst.append(f'{x} {y_burst} {z_burst}')
            pos_big.append(f'{x} {y_big} {z_big}')
        for x in x2:
            pos_small.append(f'{x} {y_small} {z_small}')
        for x in x3f:
            for z in z3f:
                pos3f.append(f'{x} {y3f} {z}')
    elif ori == 'yz':
        for z in z3:
            pos_burst.append(f'{x_burst} {y_burst} {z}')
            pos_big.append(f'{x_big} {y_big} {z}')
        for z in z2:
            pos_small.append(f'{x_small} {y_small} {z}')
        for z in z3f:
            for x in x3f:
                pos3f.append(f'{x} {y3f} {z}')
    else:
        print('Error!genBig')
        input()
    
    color_burst = str(color_burst)
    color_small = str(color_small)
    color_big = str(color_big)
    color3f = str(color3f)
    
    with open(path, mode, encoding='utf-8') as f:
        # x3 = [-4358, -4340, -4322] # burst和big共用
        # x2 = [-4349, -4331] # small
        # x3f = [-4369, -4311]

        # y_burst = 82
        # y_small = 92
        # y_big = 110
        # y3f = 92

        # z_burst = 160
        # z_small = 156
        # z_big = 152
        # z3f = [150, 156, 162]
              
        # # z3 = [31, 23, 15] # burst和big共用
        # # z2 = [27, 19] # small
        # # z3f = [38, 8]

        # # y_burst = 75
        # # y_small = 78
        # # y_big = 84
        # # y3f = 78

        # # x_burst = -4424
        # # x_small = -4427
        # # x_big = -4430
        # # x3f = [-4431, -4427, -4423]
        
        for pos in pos_burst:
            Motion = '[0.0d,0.1d,0.0d]'
            typ = str(burst)
            color = color_burst
            s = 'summon minecraft:firework_rocket ' + pos + ' {Motion:' + Motion + ',FireworksItem:{id:"minecraft:firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Trail:1b,Type:' + typ + ',Colors:[I;' + color + ']}]}}}}'
            f.write(s + '\n')
        f.write('\n')

        for pos in pos_small:
            Motion = '[0.0d,0.1d,0.0d]'
            typ = str(small)
            color = color_small
            s = 'summon minecraft:firework_rocket ' + pos + ' {Motion:' + Motion + ',FireworksItem:{id:"minecraft:firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Trail:1b,Type:' + typ + ',Colors:[I;' + color + ']}]}}}}'
            f.write(s + '\n')
        f.write('\n')

        for pos in pos_big:
            Motion = '[0.0d,0.1d,0.0d]'
            typ = str(big)
            color = color_big
            s = 'summon minecraft:firework_rocket ' + pos + ' {Motion:' + Motion + ',FireworksItem:{id:"minecraft:firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Trail:1b,Type:' + typ + ',Colors:[I;' + color + ']}]}}}}'
            f.write(s + '\n')
        f.write('\n')
        
        for pos in pos3f[0:3]:
            Motion = '[0.5d,0.866d,0.0d]' if ori == 'xy' else '[0.0d,0.866d,0.5d]'
            typ = str(burst)
            color = color3f
            s = 'summon minecraft:firework_rocket ' + pos + ' {Motion:' + Motion + ',FireworksItem:{id:"minecraft:firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Trail:1b,Type:' + typ + ',Colors:[I;' + color + ']}]}}}}'
            f.write(s + '\n')
        
        for pos in pos3f[3:]:
            Motion = '[-0.5d,0.866d,0.0d]' if ori == 'xy' else '[0.0d,0.866d,-0.5d]'
            typ = str(burst)
            color = color3f
            s = 'summon minecraft:firework_rocket ' + pos + ' {Motion:' + Motion + ',FireworksItem:{id:"minecraft:firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Trail:1b,Type:' + typ + ',Colors:[I;' + color + ']}]}}}}'
            f.write(s + '\n')
        f.write('\n')