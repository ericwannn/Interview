-*- coding:utf-8 -*-
```
在一个二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
```

class Solution:
    def find(self, target, array):
        y = len(array)
        x = len(array[0])
        i = x-1
        j = 0
        while i >= 0 and j < y-1:
            if array[j][i] == target:
                return True
            elif array[j][i] > target:
                i -= 1
            else:
                j += 1
        return False

