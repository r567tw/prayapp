"""
這裡是function區!!!!!
"""

#讀取檔案
def readfile(name):
    file = open(name, 'r')
    content=file.read()
    print(content)
    file.close()

#寫取檔案
def writefile(name,content):
    file = open(name, 'a+', encoding = 'UTF-8')
    file.write(content)
    print('檔案寫入成功')
    file.close()

#建立檔案
def build():
    file = open('praydata.csv', 'w', encoding = 'UTF-8')
    file.write('﻿禱告事項,被禱告人或者禱告者,應許日期\n')
    print('檔案建立成功')
    file.close()
"""
這裡以上是function區
"""

import os
if (not os.path.exists("praydata.csv")):
    build()

data='praydata.csv'
play='1'

#歡迎訊息

print('歡迎使用禱告簿程式')
print('我的網站樂在信仰中 http://r567tw.usite.tw/')

while (play != '0' ):
    access=input("新增禱告事項請輸入1，觀看禱告事項請輸入2： ")
    if (access=='1'):
        add='1'
        while (add != '0'):
            content=input('請輸入你的禱告事項:')+','
            content=content+input('請輸入你的被禱告人或者禱告者:')+','
            content=content+input('請輸入你的應許日期(若沒有則輸入N):')+'\n'
            writefile(data,content)
            add=input("是否要繼續輸入下一筆?(若結束則輸入0)：")
        play=input("是否要離開程式?(若結束則輸入0)：")
    elif (access=='2'):
        readfile(data)
        play=input("是否要離開程式?(若結束則輸入0)：")
    #小小彩蛋-宣告我的名字就可以結束程式~~
    elif (access=="I'm Jimmy fang"):
        quit()
    else:
        print('輸入錯誤，請重新輸入ㄧ次')
quit()








