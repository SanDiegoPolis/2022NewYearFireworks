import data

def genFace(num, x_arr, y, z_arr, color, typ, mode = 'w'):
    path = data.getPath(num)
    pos3f = []

    if len(x_arr) < len(z_arr):
        Motion1 = '[0.5d,0.866d,0.0d]'
        Motion2 = '[-0.5d,0.866d,0.0d]'
        for x in x_arr:
            for z in z_arr:
                pos3f.append(f'{x} {y} {z}')
    elif len(z_arr) < len(x_arr):
        Motion1 = '[0.0d,0.866d,0.5d]'
        Motion2 = '[0.0d,0.866d,-0.5d]'
        for z in z_arr:
            for x in x_arr:
                pos3f.append(f'{x} {y} {z}')
    else:
        print('Error!genFace')
        input()

    color = str(color)
    typ = str(typ)

    with open(path, mode, encoding='utf-8') as f:        
        for pos in pos3f[0:3]:
            Motion = Motion1
            s = 'summon minecraft:firework_rocket ' + pos + ' {Motion:' + Motion + ',FireworksItem:{id:"minecraft:firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Trail:1b,Type:' + typ + ',Colors:[I;' + color + ']}]}}}}'
            f.write(s + '\n')
        for pos in pos3f[3:]:
            Motion = Motion2
            s = 'summon minecraft:firework_rocket ' + pos + ' {Motion:' + Motion + ',FireworksItem:{id:"minecraft:firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Trail:1b,Type:' + typ + ',Colors:[I;' + color + ']}]}}}}'
            f.write(s + '\n')
        f.write('\n')