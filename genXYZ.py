import data

def genCMD(num, pos, color, typ, mode):
    path = data.getPath(num)
    color = str(color)
    typ = str(typ)
    with open(path, mode, encoding='utf-8') as f:
        for p in pos:
            Motion = '[0.0d,0.1d,0.0d]'
            s = 'summon minecraft:firework_rocket ' + p + ' {Motion:' + Motion + ',FireworksItem:{id:"minecraft:firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Trail:1b,Type:' + typ + ',Colors:[I;' + color + ']}]}}}}'
            f.write(s + '\n')
        f.write('\n')

def genXYZ(num, x_arr, y_arr, z_arr, color, typ, mode = 'w'):
    pos = []
    for x in x_arr:
        for y in y_arr:
            for z in z_arr:
                pos.append(f'{x} {y} {z}')

    genCMD(num, pos, color, typ, mode)