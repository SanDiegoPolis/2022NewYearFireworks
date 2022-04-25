def genCMD(name, pos, mode):
    path = f'./data/main/functions/particle/{name}.mcfunction'
    with open(path, mode, encoding='utf-8') as f:
        for p in pos:
            s = 'particle minecraft:end_rod ' + p + ' 0.2 0.2 0.2 0 10 force'
            f.write(s + '\n')

def genParticleXYZ(name, x_arr, y_arr, z_arr, mode = 'a'):
    pos = []
    for x in x_arr:
        for y in y_arr:
            for z in z_arr:
                pos.append(f'{x} {y} {z}')

    genCMD(name, pos, mode)