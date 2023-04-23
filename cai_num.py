# -*- coding:utf-8 -*-

"""
@Author : zhangch
@Contact : zhangch@digilink.link
@Date : 
@Desc : 
"""

import random

# 随机生成一个1到100之间的数字
number = random.randint(1, 100)

# 初始化猜测次数为0
guesses = 0

# 提示玩家输入猜测的数字，直到猜对为止
while True:
    guess = int(input("请猜一个1到100之间的数字："))
    guesses += 1

    if guess == number:
        print("恭喜你，猜对了！你一共猜了%d次。" % guesses)
        break
    elif guess < number:
        print("你猜的数字太小了，请再试一次。")
    else:
        print("你猜的数字太大了，请再试一次。")