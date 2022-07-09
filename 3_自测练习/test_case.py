#!/usr/bin/env python3

from my_solution import solution


# 测试用例
def test_solution():
    n = 5   # 定义物品数目为5
    c = 10  # 定义背包容量为10
    w = [2, 2, 6, 5, 4] # 定义物品的重量矩阵
    v = [6, 3, 5, 4, 6] # 定义物品的价值矩阵

    # 正确答案
    correct_solution = 15
    # 程序求解结果
    result = solution(n,c,w,v)
    assert result == correct_solution 
