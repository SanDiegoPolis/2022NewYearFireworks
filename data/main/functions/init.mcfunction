execute if score debug debug matches 1 run say init

# 移除旧计分项
scoreboard objectives remove trigger
scoreboard objectives remove tick

# 添加新计分项
scoreboard objectives add trigger dummy
scoreboard objectives add tick dummy
scoreboard players set i tick 0
scoreboard players set i trigger 0
scoreboard players set fu trigger 0
scoreboard players set hndj trigger 0

scoreboard objectives setdisplay sidebar tick