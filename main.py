import data
from genBig import *
from genXYZ import *
from genBigFace import *
from genFace import *
from genRainbow import *
from genParticleXYZ import *
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
color_arr = data.color_arr

small = data.small
big = data.big
star = data.star
burst = data.burst

# genBig(num = 192, ori = 'xy',
#        x3 = [-4358, -4340, -4322], x2 = [-4349, -4331], x3f = [-4311, -4369],
#        y_burst = 82, y_small = 92, y_big = 110, y3f = 92,
#        z_burst = 160, z_small = 156, z_big = 152, z3f = [150, 156, 160],
#        color_burst = red, color_small = purple, color_big = magenta, color3f = orange
#        )

# genBig(num = 200, ori = 'xy',
#        x3 = [-4358, -4340, -4322], x2 = [-4349, -4331], x3f = [-4311, -4369],
#        y_burst = 82, y_small = 92, y_big = 110, y3f = 92,
#        z_burst = 160, z_small = 156, z_big = 152, z3f = [150, 156, 160],
#        color_burst = yellow, color_small = blue, color_big = cyan, color3f = lime
#        )

# genBig(num = 208, ori = 'xy',
#        x3 = [-4358, -4340, -4322], x2 = [-4349, -4331], x3f = [-4311, -4369],
#        y_burst = 82, y_small = 92, y_big = 110, y3f = 92,
#        z_burst = 160, z_small = 156, z_big = 152, z3f = [150, 156, 160],
#        color_burst = green, color_small = orange, color_big = red, color3f = pink
#        )

# genBig(num = 540, ori = 'yz',
#        z3 = [31, 23, 15], z2 = [27, 19], z3f = [38, 8],
#        y_burst = 72, y_small = 80, y_big = 92, y3f = 80,
#        x_burst = -4424, x_small = -4427, x_big = -4430, x3f = [-4431, -4427, -4423],
#        color_burst = yellow, color_small = pink, color_big = green, color3f = blue
#        )
# genBig(num = 540, ori = 'yz', mode = 'a',
#        z3 = [31, 23, 15], z2 = [27, 19], z3f = [38, 8],
#        y_burst = 72, y_small = 80, y_big = 92, y3f = 80,
#        x_burst = -4424, x_small = -4427, x_big = -4430, x3f = [-4431, -4427, -4423],
#        color_burst = orange, color_small = red, color_big = lime, color3f = cyan
#        )

# genXYZ(num = 576, x_arr = [-4424], y_arr = [80], z_arr = [27], color = cyan, typ = small)
# genXYZ(num = 584, x_arr = [-4424], y_arr = [80], z_arr = [19], color = orange, typ = small)
# genXYZ(num = 596, x_arr = [-4427], y_arr = [84], z_arr = [29], color = lime, typ = burst)
# genXYZ(num = 600, x_arr = [-4427], y_arr = [84], z_arr = [17], color = purple, typ = burst)

# genXYZ(num = 608, x_arr = [-4427], y_arr = [84], z_arr = [25], color = green, typ = star)
# genXYZ(num = 608, x_arr = [-4427], y_arr = [84], z_arr = [33], color = blue, typ = star, mode = 'a')

# genXYZ(num = 616, x_arr = [-4427], y_arr = [84], z_arr = [13], color = red, typ = star)
# genXYZ(num = 616, x_arr = [-4427], y_arr = [84], z_arr = [21], color = magenta, typ = star, mode = 'a')

# genXYZ(num = 628, x_arr = [-4430], y_arr = [88], z_arr = [29], color = lime, typ = burst)
# genXYZ(num = 628, x_arr = [-4430], y_arr = [88], z_arr = [29], color = yellow, typ = burst, mode = 'a')

# genXYZ(num = 632, x_arr = [-4430], y_arr = [88], z_arr = [17], color = purple, typ = burst)
# genXYZ(num = 632, x_arr = [-4430], y_arr = [88], z_arr = [17], color = red, typ = burst, mode = 'a')

# genXYZ(num = 640, x_arr = [-4424], y_arr = [80], z_arr = [27], color = pink, typ = small)
# genXYZ(num = 648, x_arr = [-4424], y_arr = [80], z_arr = [19], color = green, typ = small)
# genXYZ(num = 660, x_arr = [-4427], y_arr = [84], z_arr = [29], color = cyan, typ = burst)
# genXYZ(num = 664, x_arr = [-4427], y_arr = [84], z_arr = [17], color = magenta, typ = burst)

# genXYZ(num = 672, x_arr = [-4427], y_arr = [84], z_arr = [25], color = red, typ = star)
# genXYZ(num = 672, x_arr = [-4427], y_arr = [84], z_arr = [33], color = yellow, typ = star, mode = 'a')

# genXYZ(num = 680, x_arr = [-4427], y_arr = [84], z_arr = [13], color = purple, typ = star)
# genXYZ(num = 680, x_arr = [-4427], y_arr = [84], z_arr = [21], color = blue, typ = star, mode = 'a')

# genXYZ(num = 692, x_arr = [-4430], y_arr = [88], z_arr = [29], color = orange, typ = burst)
# genXYZ(num = 692, x_arr = [-4430], y_arr = [88], z_arr = [29], color = magenta, typ = burst, mode = 'a')

# genXYZ(num = 696, x_arr = [-4430], y_arr = [88], z_arr = [17], color = cyan, typ = burst)
# genXYZ(num = 696, x_arr = [-4430], y_arr = [88], z_arr = [17], color = pink, typ = burst, mode = 'a')

# genBigFace(num = 714, x_arr = [-4431, -4427, -4423], y1 = 80, y2 = 87, z_arr = [8,38], color1 = [color_arr[3],color_arr[1]], color2 = [color_arr[2],color_arr[4]], typ = burst)
# genXYZ(num = 722, x_arr = [-4424], y_arr = [76], z_arr = [31,23,15], color = color_arr[2], typ = burst)
# genFace(num = 730, x_arr = [-4431, -4427, -4423], y = 80, z_arr = [8,38], color = color_arr[5], typ = burst)
# genXYZ(num = 738, x_arr = [-4424], y_arr = [76], z_arr = [31,23,15], color = color_arr[7], typ = burst)

# genBigFace(num = 748, x_arr = [-4431, -4427, -4423], y1 = 80, y2 = 87, z_arr = [8,38], color1 = [color_arr[7],color_arr[5]], color2 = [color_arr[6],color_arr[0]], typ = burst)
# genXYZ(num = 756, x_arr = [-4424], y_arr = [76], z_arr = [31,23,15], color = color_arr[9], typ = burst)
# genFace(num = 764, x_arr = [-4431, -4427, -4423], y = 80, z_arr = [8,38], color = color_arr[6], typ = burst)
# genXYZ(num = 772, x_arr = [-4424], y_arr = [76], z_arr = [31,23,15], color = color_arr[1], typ = burst)

# genXYZ(num = 792, x_arr = [-4427], y_arr = [78], z_arr = [35,27,19,11], color = color_arr[4], typ = burst)
# genXYZ(num = 808, x_arr = [-4427], y_arr = [78], z_arr = [35,27,19,11], color = color_arr[0], typ = burst)

# genRainbow(num = 916, ori = 'xy', x = -4532, y = 80, z = 75, r = 8)
# genXYZ(num = 932, x_arr = [-4536, -4528], y_arr = [84], z_arr = [83], color = color_arr[0], typ = small)
# genXYZ(num = 932, x_arr = [-4536, -4528], y_arr = [84], z_arr = [83], color = color_arr[2], typ = small, mode = 'a')

# genBig(num = 948, ori = 'xy',
#        x3 = [-4540, -4532, -4524], x2 = [-4536, -4528], x3f = [-4517, -4547],
#        y_burst = 84, y_small = 92, y_big = 100, y3f = 90,
#        z_burst = 87, z_small = 91, z_big = 95, z3f = [85, 91, 97],
#        color_burst = color_arr[5], color_small = color_arr[1], color_big = color_arr[9], color3f = color_arr[6]
#        )
# genXYZ(num = 956, x_arr = [-4540, -4532, -4524], y_arr = [92], z_arr = [99], color = color_arr[0], typ = star)
# genXYZ(num = 956, x_arr = [-4540, -4532, -4524], y_arr = [92], z_arr = [99], color = color_arr[8], typ = star, mode = 'a')

# genBig(num = 964, ori = 'xy',
#        x3 = [-4540, -4532, -4524], x2 = [-4536, -4528], x3f = [-4517, -4547],
#        y_burst = 84, y_small = 92, y_big = 100, y3f = 90,
#        z_burst = 103, z_small = 107, z_big = 111, z3f = [101, 107, 113],
#        color_burst = color_arr[3], color_small = color_arr[2], color_big = color_arr[5], color3f = color_arr[9]
#        )
# genXYZ(num = 972, x_arr = [-4540, -4532, -4524], y_arr = [92], z_arr = [115], color = color_arr[0], typ = star)
# genXYZ(num = 972, x_arr = [-4540, -4532, -4524], y_arr = [92], z_arr = [115], color = color_arr[6], typ = star, mode = 'a')

# genRainbow(num = 980, ori = 'xy', x = -4532, y = 80, z = 123, r = 8)
# genXYZ(num = 996, x_arr = [-4536, -4528], y_arr = [84], z_arr = [131], color = color_arr[4], typ = small)
# genXYZ(num = 996, x_arr = [-4536, -4528], y_arr = [84], z_arr = [131], color = color_arr[7], typ = small, mode = 'a')

# genBig(num = 1012, ori = 'xy',
#        x3 = [-4540, -4532, -4524], x2 = [-4536, -4528], x3f = [-4517, -4547],
#        y_burst = 84, y_small = 92, y_big = 100, y3f = 90,
#        z_burst = 135, z_small = 139, z_big = 143, z3f = [133, 139, 145],
#        color_burst = color_arr[1], color_small = color_arr[6], color_big = color_arr[3], color3f = color_arr[5]
#        )
# genXYZ(num = 1020, x_arr = [-4540, -4532, -4524], y_arr = [92], z_arr = [147], color = color_arr[0], typ = star)
# genXYZ(num = 1020, x_arr = [-4540, -4532, -4524], y_arr = [92], z_arr = [147], color = color_arr[2], typ = star, mode = 'a')

# genBig(num = 1028, ori = 'xy',
#        x3 = [-4540, -4532, -4524], x2 = [-4536, -4528], x3f = [-4517, -4547],
#        y_burst = 84, y_small = 92, y_big = 100, y3f = 90,
#        z_burst = 151, z_small = 155, z_big = 159, z3f = [149, 155, 161],
#        color_burst = color_arr[8], color_small = color_arr[6], color_big = color_arr[5], color3f = color_arr[1]
#        )
# genXYZ(num = 1036, x_arr = [-4540, -4532, -4524], y_arr = [92], z_arr = [163], color = color_arr[7], typ = star)
# genXYZ(num = 1036, x_arr = [-4540, -4532, -4524], y_arr = [92], z_arr = [163], color = color_arr[0], typ = star, mode = 'a')

# genFace(num = 1052, x_arr = [-4517, -4547], y = 90, z_arr = [157,163,169], color = color_arr[2], typ = burst)
# genFace(num = 1052, x_arr = [-4517, -4547], y = 90, z_arr = [157,163,169], color = color_arr[4], typ = burst, mode = 'a')
# genBig(num = 1068, ori = 'xy',
#        x3 = [-4540, -4532, -4524], x2 = [-4536, -4528], x3f = [-4517, -4547],
#        y_burst = 84, y_small = 92, y_big = 100, y3f = 90,
#        z_burst = 159, z_small = 163, z_big = 167, z3f = [157, 163, 169],
#        color_burst = color_arr[1], color_small = color_arr[6], color_big = color_arr[9], color3f = color_arr[7]
#        )
# genBig(num = 1068, ori = 'xy', mode = 'a',
#        x3 = [-4540, -4532, -4524], x2 = [-4536, -4528], x3f = [-4517, -4547],
#        y_burst = 84, y_small = 92, y_big = 100, y3f = 90,
#        z_burst = 159, z_small = 163, z_big = 167, z3f = [157, 163, 169],
#        color_burst = color_arr[8], color_small = color_arr[5], color_big = color_arr[0], color3f = color_arr[3]
#        )

# genFace(num = 1082, x_arr = [-4517, -4547], y = 90, z_arr = [157,163,169], color = color_arr[5], typ = burst)
# genFace(num = 1082, x_arr = [-4517, -4547], y = 90, z_arr = [157,163,169], color = color_arr[8], typ = burst, mode = 'a')
# genBig(num = 1098, ori = 'xy',
#        x3 = [-4540, -4532, -4524], x2 = [-4536, -4528], x3f = [-4517, -4547],
#        y_burst = 84, y_small = 92, y_big = 100, y3f = 90,
#        z_burst = 159, z_small = 163, z_big = 167, z3f = [157, 163, 169],
#        color_burst = color_arr[4], color_small = color_arr[1], color_big = color_arr[7], color3f = color_arr[3]
#        )
# genBig(num = 1098, ori = 'xy', mode = 'a',
#        x3 = [-4540, -4532, -4524], x2 = [-4536, -4528], x3f = [-4517, -4547],
#        y_burst = 84, y_small = 92, y_big = 100, y3f = 90,
#        z_burst = 159, z_small = 163, z_big = 167, z3f = [157, 163, 169],
#        color_burst = color_arr[2], color_small = color_arr[6], color_big = color_arr[0], color3f = color_arr[9]
#        )

# genXYZ(num = 1110, x_arr = [-4540, -4532, -4524], y_arr = [92], z_arr = [163], color = color_arr[6], typ = star)
# genXYZ(num = 1110, x_arr = [-4540, -4532, -4524], y_arr = [92], z_arr = [163], color = color_arr[9], typ = small, mode = 'a')

# genXYZ(num = 1124, x_arr = [-4540, -4532, -4524], y_arr = [92], z_arr = [163], color = color_arr[3], typ = star)
# genXYZ(num = 1124, x_arr = [-4540, -4532, -4524], y_arr = [92], z_arr = [163], color = color_arr[8], typ = small, mode = 'a')

# genBig(num = 1224, ori = 'xy',
#        x3 = [-4358, -4340, -4322], x2 = [-4349, -4331], x3f = [-4311, -4369],
#        y_burst = 70, y_small = 80, y_big = 92, y3f = 80,
#        z_burst = 221, z_small = 225, z_big = 229, z3f = [219, 225, 261],
#        color_burst = color_arr[3], color_small = color_arr[0], color_big = color_arr[7], color3f = color_arr[6]
#        )
# genBig(num = 1224, ori = 'xy', mode = 'a',
#        x3 = [-4358, -4340, -4322], x2 = [-4349, -4331], x3f = [-4311, -4369],
#        y_burst = 70, y_small = 80, y_big = 92, y3f = 80,
#        z_burst = 221, z_small = 225, z_big = 229, z3f = [219, 225, 261],
#        color_burst = color_arr[5], color_small = color_arr[8], color_big = color_arr[4], color3f = color_arr[2]
#        )

# genBig(num = 1296, ori = 'xy',
#        x3 = [-4358, -4340, -4322], x2 = [-4349, -4331], x3f = [-4311, -4369],
#        y_burst = 70, y_small = 80, y_big = 92, y3f = 80,
#        z_burst = 221, z_small = 225, z_big = 229, z3f = [219, 225, 261],
#        color_burst = color_arr[5], color_small = color_arr[1], color_big = color_arr[2], color3f = color_arr[7]
#        )
# genBig(num = 1296, ori = 'xy', mode = 'a',
#        x3 = [-4358, -4340, -4322], x2 = [-4349, -4331], x3f = [-4311, -4369],
#        y_burst = 70, y_small = 80, y_big = 92, y3f = 80,
#        z_burst = 221, z_small = 225, z_big = 229, z3f = [219, 225, 261],
#        color_burst = color_arr[0], color_small = color_arr[3], color_big = color_arr[6], color3f = color_arr[8]
#        )
# genFace(num = 1296, x_arr = [-4311, -4369], y = 89, z_arr = [219, 225, 261], color = color_arr[4], typ = burst, mode = 'a')
# genFace(num = 1296, x_arr = [-4311, -4369], y = 89, z_arr = [219, 225, 261], color = color_arr[9], typ = burst, mode = 'a')
# genXYZ(num = 1296, x_arr = [-4349, -4331], y_arr = [80], z_arr = [225], color = color_arr[2], typ = star, mode = 'a')
# genXYZ(num = 1296, x_arr = [-4349, -4331], y_arr = [80], z_arr = [225], color = color_arr[4], typ = star, mode = 'a')

# genParticleXYZ(name = 'hu', x_arr = [-4322], y_arr = [85.5], z_arr = [221], mode = 'w')
# genParticleXYZ(name = 'hu', x_arr = [i for i in range(-4326,-4321)], y_arr = [85.5-10/13], z_arr = [221])
# genParticleXYZ(name = 'hu', x_arr = [-4322], y_arr = [85.5-10/13*2], z_arr = [221])
# genParticleXYZ(name = 'hu', x_arr = [i for i in range(-4327,-4317)], y_arr = [85.5-10/13*3], z_arr = [221])
# genParticleXYZ(name = 'hu', x_arr = [-4318,-4326.4], y_arr = [85.5-10/13*4], z_arr = [221])
# genParticleXYZ(name = 'hu', x_arr = [-4318,-4322], y_arr = [85.5-10/13*5], z_arr = [221])
# genParticleXYZ(name = 'hu', x_arr = [-4318,-4322], y_arr = [85.5-10/13*6], z_arr = [221])
# genParticleXYZ(name = 'hu', x_arr = [-4318,-4320], y_arr = [85.5-10/13*6-0.2], z_arr = [221])
# genParticleXYZ(name = 'hu', x_arr = [-4318,-4321], y_arr = [85.5-10/13*6-0.1], z_arr = [221])
# genParticleXYZ(name = 'hu', x_arr = [-4318,-4323], y_arr = [85.5-10/13*6+0.1], z_arr = [221])
# genParticleXYZ(name = 'hu', x_arr = [-4318,-4324], y_arr = [85.5-10/13*6+0.2], z_arr = [221])
# genParticleXYZ(name = 'hu', x_arr = [-4318,-4322,-4325.6], y_arr = [85.5-10/13*7], z_arr = [221])
# genParticleXYZ(name = 'hu', x_arr = [-4318,-4322,-4323,-4324,-4325,-4326], y_arr = [85.5-10/13*8], z_arr = [221])
# genParticleXYZ(name = 'hu', x_arr = [-4318], y_arr = [85.5-10/13*9], z_arr = [221])
# genParticleXYZ(name = 'hu', x_arr = [-4317.4,-4321,-4322,-4323,-4324], y_arr = [85.5-10/13*10], z_arr = [221])
# genParticleXYZ(name = 'hu', x_arr = [-4317.2,-4320.4,-4324], y_arr = [85.5-10/13*11], z_arr = [221])
# genParticleXYZ(name = 'hu', x_arr = [-4316.9,-4320,-4324,-4327], y_arr = [85.5-10/13*12], z_arr = [221])
# genParticleXYZ(name = 'hu', x_arr = [-4316.5,-4319,-4324,-4325,-4326,-4327], y_arr = [85.5-10/13*13], z_arr = [221])

# genParticleXYZ(name = 'nian', x_arr = [i for i in range(-4338,-4331)], y_arr = [84.4], z_arr = [221], mode = 'w')
# genParticleXYZ(name = 'nian', x_arr = [i for i in range(-4338,-4331)], y_arr = [81.1], z_arr = [221])
# genParticleXYZ(name = 'nian', x_arr = [i for i in range(-4339,-4328)], y_arr = [77.8], z_arr = [221])
# genParticleXYZ(name = 'nian', x_arr = [-4335], y_arr = [i/100 for i in range(7550,8331,110)], z_arr = [221])
# genParticleXYZ(name = 'nian', x_arr = [-4331.5], y_arr = [78,79,80], z_arr = [221])
# genParticleXYZ(name = 'nian', x_arr = [-4331.0], y_arr = [85.5], z_arr = [221])
# genParticleXYZ(name = 'nian', x_arr = [-4330.8], y_arr = [84.4], z_arr = [221])
# genParticleXYZ(name = 'nian', x_arr = [-4330.4], y_arr = [83.3], z_arr = [221])
# genParticleXYZ(name = 'nian', x_arr = [-4329.8], y_arr = [82.2], z_arr = [221])
# genParticleXYZ(name = 'nian', x_arr = [-4329.0], y_arr = [81.1], z_arr = [221])

# genParticleXYZ(name = 'da', x_arr = [-4346], y_arr = [82.5,83.5,84.5,85.5], z_arr = [221], mode = 'w')
# genParticleXYZ(name = 'da', x_arr = [i for i in range(-4351,-4340)], y_arr = [82], z_arr = [221])
# ang = math.atan(1.5)
# for i in range(0,8):
#     x1 = - 4345.5 + 6.5 * (1 - math.cos(ang/6*i))
#     x2 = - 4345.5 - 6.5 * (1 - math.cos(ang/6*i))
#     y = 81.5 - 6.5 * math.sin(ang/6*i)
#     genParticleXYZ(name = 'da', x_arr = [x1], y_arr = [y], z_arr = [221])
#     genParticleXYZ(name = 'da', x_arr = [x2], y_arr = [y], z_arr = [221])

# genParticleXYZ(name = 'ji', x_arr = [-4358], y_arr = [85.4,84.3,83.2,82.1,81.0], z_arr = [221], mode = 'w')
# genParticleXYZ(name = 'ji', x_arr = [i for i in range(-4363,-4352)], y_arr = [83.75], z_arr = [221])
# genParticleXYZ(name = 'ji', x_arr = [i for i in range(-4362,-4353)], y_arr = [81.0], z_arr = [221])
# genParticleXYZ(name = 'ji', x_arr = [i for i in range(-4361,-4354)], y_arr = [79.0], z_arr = [221])
# genParticleXYZ(name = 'ji', x_arr = [i for i in range(-4361,-4354)], y_arr = [76.0], z_arr = [221])
# genParticleXYZ(name = 'ji', x_arr = [-4355], y_arr = [i/100 for i in range(7550,7901,125)], z_arr = [221])
# genParticleXYZ(name = 'ji', x_arr = [-4361], y_arr = [i/100 for i in range(7550,7901,125)], z_arr = [221])