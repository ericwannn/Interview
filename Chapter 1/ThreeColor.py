# -*- coding:utf-8 -*-

''' 三色排序问题

    有一个只由0，1，2三种元素构成的整数数组，请使用交换、原地排序而不是使用计数进行排序。

    给定一个只含0，1，2的整数数组A及它的大小，请返回排序后的数组。保证数组大小小于等于500。

    测试样例：
    [0,1,1,0,2,2],6
    返回：[0,0,1,1,2,2]

'''
# -*- coding:utf-8 -*-

class ThreeColor:
    def sortThreeColor(self, A, n):
        # write code here
        i, j, k = 0, 0, n-1
        while i <= k:
            if A[i] == 1:
                pass
                i += 1
            elif A[i] == 0:
                A[i], A[j] = A[j], A[i]
                j += 1
                i += 1
            else:
                A[i], A[k] = A[k], A[i]
                k -= 1
        return A