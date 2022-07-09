#!/usr/bin/env python3
# 给定n种物品和一个背包，物品i的重量是w_i，物品对应的价值为v_i，背包的总容量为c。
# 应如何选择装入背包中的物品，使得装入背包中物品的总价值达到最大？

def solution(n, c, w, v):

    # 计算价值矩阵b
    def dynamic_plan(n, c, w, v):
        b = [[-1 for j in range(c + 1)] for i in range(n + 1)] # 初始化价值矩阵，值设置为-1

        for j in range(c + 1):
            b[0][j] = 0 # 当物品数目为0时，背包所容纳物品的价值为0；

        for i in range(1, n + 1):   
            for j in range(1, c + 1):   
                b[i][j] = b[i - 1][j]   # 不装入物品i时，背包容量为j时的最大价值复制给b[i][j]   

                if j >= w[i - 1] and b[i][j] < b[i - 1][j - w[i - 1]] + v[i - 1]:   # 如果装入物品i比不装入物品i时的价值高，那么选择装入物品i
                    b[i][j] = b[i - 1][j - w[i - 1]] + v[i - 1] 

        return b

    # 输出选择的物品
    def need_goods(n, c, w, b):
        print('最大价值为:', b[n][c])
        x = [False for i in range(n)] # 记录每一个物品是否被装入，刚开始全部设置False；
        j = c
        for i in range(1, n + 1):
            if b[i][j] > b[i - 1][j]:   # 如果装入物品i比不装入物品i时价值高，那么表示已经装入物品i
                x[i - 1] = True # 记录物品i被装入
                j -= w[i - 1]   # 更改此时背包的容量
        print('选择的物品为:')
        for i in range(n):
            if x[i]:
                print(f'第 {i + 1} 个,', end='')    # 打印选择装入的物品
        print('')

    b = dynamic_plan(n, c, w, v)    # 计算价值矩阵
    need_goods(n, c, w, b)  # 输出背包最大价值以及如何选择物品装入


if __name__ == '__main__':
    n = 5   # 定义物品数目为5
    c = 10  # 定义背包容量为10
    w = [2, 2, 6, 5, 4] # 定义物品的重量矩阵
    v = [6, 3, 5, 4, 6] # 定义物品的价值矩阵
    solution(n,c,w,v)
