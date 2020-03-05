# -*- coding=utf-8 -*-
"""
-------------------------------
    Project:    AI
    File Name:  animation.py
    Description:
    Author:     Administrator
    Date:       2020/03/02
    Time:       18:46
-------------------------------
    Modify Activity:
                2020/03/02
-------------------------------
"""
__author__ = 'Administrator'

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

def animate(i):
    line.set_ydata(np.sin(x + i/10.0))
    return line

def init():
    line.set_ydata(np.sin(x))
    return line

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

ani = animation.FuncAnimation(fig=fig,          # 进行动画绘制的figure
                              func=animate,     # 自定义动画函数
                              frames=100,       # 动画长度，一次循环包括的帧数
                              init_func=init,   # 自定义开始帧
                              interval=20,      # 更新频率，以ms计
                              blit=False)       # 更新所有的点还是仅更新产生变化的点

plt.show()
