import datetime                              # 导入日期时间类
#!/bin/sh
# *********************************
# Author        : seaice6
# Last modified : 2020-06-05 星期五 00:11:55
# Email         : lhb16@outlook.com
# Filename      : hhh
# Description   : 
# *********************************

# 定义一个列表
mot = ["坚持下去不是因为我很坚强，而是因为我别无选择",
       "含泪播种的人一定能笑着收获",
       "做对的事情比把事情做对重要",
       "命运给予我们的不是失望之酒，而是机会之杯",
       "明日永远新鲜如初，纤尘不染",
       "求知若饥，虚心若愚",
       "成功将属于那些从不说“不可能”的人"]
day=datetime.datetime.now().weekday()      # 获取当前星期
print(datetime.datetime.now())
print(mot[day])                              # 输出每日一帖
