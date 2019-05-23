import calendar

'''
    w = 每个日期之间的间隔字符数
    l = 每周所占用的行数
    c = 每月之间的间隔字符数
'''
cal = calendar.calendar(2017)
# print(cal)

cal = calendar.calendar(2020, l=0, c=5)
print(cal)