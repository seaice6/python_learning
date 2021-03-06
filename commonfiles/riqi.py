#!/bin/sh
# *********************************
# Author        : seaice6
# Last modified : 2020-06-10 星期三 00:09:14
# Email         : lhb16@outlook.com
# Filename      : datetime.py
# Description   : 
# *********************************

import datetime
today=datetime.datetime.now()
#current_time=today.strftime("%Y-%m-%d %H:%M:%S %A")  #秒输出多位小数，可用%X输出时间
#current_time=today.strftime("%Y-%m-%d %X")
current_time=today.strftime("%x %X")
print(today)
print(current_time)

'''附上参数表
%a   星期的简写。如 星期三为Web
%A   星期的全写。如 星期三为Wednesday
%b   月份的简写。如4月份为Apr
%B   月份的全写。如4月份为April 
%c:  日期时间的字符串表示。（如： 04/07/10 10:43:39）
%d:  日在这个月中的天数（是这个月的第几天）
%f:  微秒（范围[0,999999]）
%H:  小时（24小时制，[0, 23]）
%I:  小时（12小时制，[0, 11]）
%j:  日在年中的天数 [001,366]（是当年的第几天）
%m:  月份（[01,12]）
%M:  分钟（[00,59]）
%p:  AM或者PM
%S:  秒（范围为[00,61]，为什么不是[00, 59]，参考python手册~_~）
%U:  周在当年的周数当年的第几周），星期天作为周的第一天
%w:  今天在这周的天数，范围为[0, 6]，6表示星期天
%W:  周在当年的周数（是当年的第几周），星期一作为周的第一天
%x:  日期字符串（如：04/07/10）
%X:  时间字符串（如：10:43:39）
%y:  2个数字表示的年份
%Y:  4个数字表示的年份
%z:  与utc时间的间隔 （如果是本地时间，返回空字符串）
%Z:  时区名称（如果是本地时间，返回空字符串）
%%:  %% => %
'''
