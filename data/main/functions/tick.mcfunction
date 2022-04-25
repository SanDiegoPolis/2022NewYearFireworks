# 计时系统
scoreboard players add i tick 1
execute if score i trigger matches 0 run scoreboard players set i tick 0

# 控制粒子
execute if score i tick matches 130 run scoreboard players set fu trigger 1
execute if score i tick matches 168 run scoreboard players set fu trigger 0
execute if score i tick matches 1256 run scoreboard players set hu trigger 1
execute if score i tick matches 1266 run scoreboard players set nian trigger 1
execute if score i tick matches 1276 run scoreboard players set da trigger 1
execute if score i tick matches 1286 run scoreboard players set ji trigger 1
execute if score i tick matches 1326 run scoreboard players set hu trigger 0
execute if score i tick matches 1326 run scoreboard players set nian trigger 0
execute if score i tick matches 1326 run scoreboard players set da trigger 0
execute if score i tick matches 1326 run scoreboard players set ji trigger 0

execute if score fu trigger matches 1 run function main:particle/fu
execute if score hu trigger matches 1 run function main:particle/hu
execute if score nian trigger matches 1 run function main:particle/nian
execute if score da trigger matches 1 run function main:particle/da
execute if score ji trigger matches 1 run function main:particle/ji

# 控制烟花
execute if score i tick matches 26 run function main:fw/26
execute if score i tick matches 44 run function main:fw/44
execute if score i tick matches 60 run function main:fw/60
execute if score i tick matches 69 run function main:fw/69
execute if score i tick matches 78 run function main:fw/78
execute if score i tick matches 86 run function main:fw/86
execute if score i tick matches 90 run function main:fw/90
execute if score i tick matches 94 run function main:fw/94
execute if score i tick matches 98 run function main:fw/98
execute if score i tick matches 102 run function main:fw/102
execute if score i tick matches 110 run function main:fw/110
execute if score i tick matches 126 run function main:fw/126
execute if score i tick matches 192 run function main:fw/192
execute if score i tick matches 200 run function main:fw/200
execute if score i tick matches 208 run function main:fw/208
execute if score i tick matches 232 run function main:fw/232
execute if score i tick matches 238 run function main:fw/238
execute if score i tick matches 244 run function main:fw/244
execute if score i tick matches 250 run function main:fw/250
execute if score i tick matches 262 run function main:fw/262
execute if score i tick matches 270 run function main:fw/270
execute if score i tick matches 278 run function main:fw/278
execute if score i tick matches 286 run function main:fw/286
execute if score i tick matches 298 run function main:fw/298
execute if score i tick matches 304 run function main:fw/304
execute if score i tick matches 312 run function main:fw/312
execute if score i tick matches 320 run function main:fw/320
execute if score i tick matches 330 run function main:fw/330
execute if score i tick matches 338 run function main:fw/338
execute if score i tick matches 346 run function main:fw/346
execute if score i tick matches 356 run function main:fw/356
execute if score i tick matches 372 run function main:fw/372
execute if score i tick matches 380 run function main:fw/380
execute if score i tick matches 406 run function main:fw/406
execute if score i tick matches 414 run function main:fw/414
execute if score i tick matches 430 run function main:fw/430
execute if score i tick matches 446 run function main:fw/446
execute if score i tick matches 466 run function main:fw/466
execute if score i tick matches 532 run function main:fw/532
execute if score i tick matches 540 run function main:fw/540
execute if score i tick matches 576 run function main:fw/576
execute if score i tick matches 584 run function main:fw/584
execute if score i tick matches 596 run function main:fw/596
execute if score i tick matches 600 run function main:fw/600
execute if score i tick matches 608 run function main:fw/608
execute if score i tick matches 616 run function main:fw/616
execute if score i tick matches 628 run function main:fw/628
execute if score i tick matches 632 run function main:fw/632
execute if score i tick matches 640 run function main:fw/640
execute if score i tick matches 648 run function main:fw/648
execute if score i tick matches 660 run function main:fw/660
execute if score i tick matches 664 run function main:fw/664
execute if score i tick matches 672 run function main:fw/672
execute if score i tick matches 680 run function main:fw/680
execute if score i tick matches 692 run function main:fw/692
execute if score i tick matches 696 run function main:fw/696
execute if score i tick matches 714 run function main:fw/714
execute if score i tick matches 722 run function main:fw/722
execute if score i tick matches 730 run function main:fw/730
execute if score i tick matches 738 run function main:fw/738
execute if score i tick matches 748 run function main:fw/748
execute if score i tick matches 756 run function main:fw/756
execute if score i tick matches 764 run function main:fw/764
execute if score i tick matches 772 run function main:fw/772
execute if score i tick matches 792 run function main:fw/792
execute if score i tick matches 808 run function main:fw/808
execute if score i tick matches 916 run function main:fw/916
execute if score i tick matches 932 run function main:fw/932
execute if score i tick matches 948 run function main:fw/948
execute if score i tick matches 956 run function main:fw/956
execute if score i tick matches 964 run function main:fw/964
execute if score i tick matches 972 run function main:fw/972
execute if score i tick matches 980 run function main:fw/980
execute if score i tick matches 996 run function main:fw/996
execute if score i tick matches 1012 run function main:fw/1012
execute if score i tick matches 1020 run function main:fw/1020
execute if score i tick matches 1028 run function main:fw/1028
execute if score i tick matches 1036 run function main:fw/1036
execute if score i tick matches 1052 run function main:fw/1052
execute if score i tick matches 1068 run function main:fw/1068
execute if score i tick matches 1082 run function main:fw/1082
execute if score i tick matches 1098 run function main:fw/1098
execute if score i tick matches 1110 run function main:fw/1110
execute if score i tick matches 1124 run function main:fw/1124
execute if score i tick matches 1224 run function main:fw/1224
execute if score i tick matches 1296 run function main:fw/1296
