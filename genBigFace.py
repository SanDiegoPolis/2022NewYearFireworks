import data

def genBigFace(num, x_arr, y1, y2, z_arr, color1, color2, typ, mode = 'w'):
    path = data.getPath(num)
    pos3f = []
    pos3f2 = []

    if len(x_arr) < len(z_arr):
        Motion1 = '[0.5d,0.866d,0.0d]'
        Motion2 = '[-0.5d,0.866d,0.0d]'
        for x in x_arr:
            for z in z_arr:
                pos3f.append(f'{x} {y1} {z}')
                pos3f2.append(f'{x} {y2} {z}')
    elif len(z_arr) < len(x_arr):
        Motion1 = '[0.0d,0.866d,0.5d]'
        Motion2 = '[0.0d,0.866d,-0.5d]'
        for z in z_arr:
            for x in x_arr:
                pos3f.append(f'{x} {y1} {z}')
                pos3f2.append(f'{x} {y2} {z}')
    else:
        print('Error!genBigFace')
        input()
    
    typ = str(typ)

    with open(path, mode, encoding='utf-8') as f:
        # x2 = [-4369, -4311]
        # y = 92
        # y_2 = 101
        # z3 = [70, 64, 58]

        # color1 = [str(red), str(pink)]
        # color2 = [str(blue), str(cyan)]

        # color1 = [str(purple), str(orange)]
        # color2 = [str(green), str(lime)]

        # color1 = [str(blue), str(purple)]
        # color2 = [str(yellow), str(magenta)]
        
        # color1 = [str(pink), str(orange)]
        # color2 = [str(green), str(cyan)]

        for color in color1:
            color = str(color)
            for pos in pos3f[0:3]:
                Motion = Motion1
                s = 'summon minecraft:firework_rocket ' + pos + ' {Motion:' + Motion + ',FireworksItem:{id:"minecraft:firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Trail:1b,Type:' + typ + ',Colors:[I;' + color + ']}]}}}}'
                f.write(s + '\n')
            for pos in pos3f[3:]:
                Motion = Motion2
                s = 'summon minecraft:firework_rocket ' + pos + ' {Motion:' + Motion + ',FireworksItem:{id:"minecraft:firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Trail:1b,Type:' + typ + ',Colors:[I;' + color + ']}]}}}}'
                f.write(s + '\n')
            f.write('\n')

        for color in color2:
            color = str(color)
            for pos in pos3f2[0:3]:
                Motion = Motion1
                s = 'summon minecraft:firework_rocket ' + pos + ' {Motion:' + Motion + ',FireworksItem:{id:"minecraft:firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Trail:1b,Type:' + typ + ',Colors:[I;' + color + ']}]}}}}'
                f.write(s + '\n')
            for pos in pos3f2[3:]:
                Motion = Motion2
                s = 'summon minecraft:firework_rocket ' + pos + ' {Motion:' + Motion + ',FireworksItem:{id:"minecraft:firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Trail:1b,Type:' + typ + ',Colors:[I;' + color + ']}]}}}}'
                f.write(s + '\n')
            f.write('\n')