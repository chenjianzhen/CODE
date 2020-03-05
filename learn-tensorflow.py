# -*- coding=utf-8 -*-
"""
-------------------------------
    Project:    AI
    File Name:  learn-tensorflow.py
    Description:
    Author:     Administrator
    Date:       2020/03/04
    Time:       13:24
-------------------------------
    Modify Activity:
                2020/03/04
-------------------------------
"""
__author__ = 'Administrator'


class Stack(object):
    """
    栈
    """
    def __init__(self, limit=10):
        self.stack = []         # 容器
        self.limit = limit      # 栈的容量

    def push(self, data):
        # 入栈
        if len(self.stack) >= self.limit:
            raise IndexError("超出栈容量极限")
        self.stack.append(data)

    def pop(self):
        # 出栈
        if self.stack:
            return self.stack.pop()
        else:
            # 不能弹出空栈
            raise IndexError("pop from an empty stack")

    def top(self):
        # 查看栈顶元素
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        # 查看栈是否为空
        return not bool(self.stack)

    def size(self):
        # 查看栈的长度
        return len(self.stack)

# 使用堆栈判断括号是否匹配
# 读取需要匹配的括号集合，逐个判断
# 1、如果是'('，入栈
# 2、如果是')'，并且栈不为空，说明栈中有匹配的'('，栈顶弹出；栈为空，这时又出现')'，说明不匹配,返回False,匹配失败
# 3、当括号集合遍历完后，返回stack.is_empty()，如果不为空，返回False,说明有多余的'('；为空，返回True,说明
#    都匹配了。
def match_brackets(brackets):
    stack = Stack(len(brackets))
    for bracket in brackets:
        if bracket == '(':
            stack.push(bracket)
        elif bracket == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


if __name__ == "__main__":
    brackets = ['()', '())', '(((()', '(()()']
    for bracket in brackets:
        ret = match_brackets(bracket)
        print('bracket:' + str(ret) + '\n')
