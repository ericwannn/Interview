# 程序员面试

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

* [程序员面试](#程序员面试)
	* [1. 二叉树](#1-二叉树)
		* [1.1 二叉树打印](#11-二叉树打印)
			* [要求：](#要求)
			* [解决方案](#解决方案)
		* [1.2 二叉树序列化&反序列化](#12-二叉树序列化反序列化)
	* [2. 字符串](#2-字符串)
		* [2.1 判断是否为旋转词](#21-判断是否为旋转词)
			* [要求](#要求-1)
			* [解决方案](#解决方案-1)
		* [2.2 字符串旋转](#22-字符串旋转)
			* [要求](#要求-2)
			* [解决方案](#解决方案-2)
		* [2.3 字符串原地调整](#23-字符串原地调整)
			* [要求](#要求-3)
			* [解决方案](#解决方案-3)
		* [2.4 字符串最小拼接](#24-字符串最小拼接)
			* [要求](#要求-4)
			* [解决方案](#解决方案-4)
	* [3. 排序算法](#3-排序算法)
		* [3.1 各排序算法介绍](#31-各排序算法介绍)
			* [冒泡排序](#冒泡排序)
			* [选择排序](#选择排序)
			* [插入排序](#插入排序)
			* [归并排序](#归并排序)
			* [快速排序](#快速排序)
			* [堆排序](#堆排序)
			* [希尔排序](#希尔排序)
			* [计数排序](#计数排序)
			* [基数排序](#基数排序)
		* [3.2 各排序算法的比较](#32-各排序算法的比较)
			* [空间复杂度](#空间复杂度)

<!-- /code_chunk_output -->

## 1. 二叉树

### 1.1 二叉树打印

#### 要求：
* 二叉树按层遍历（宽度优先）
* 同行信息一起打印（自动换行）

#### 解决方案

* last: 指向正在打印的当前行的最右节点
* nlast: 下一行的最右节点
* 使用一个队列记录一行中需要打印的节点，每打印一个节点，将其子节点加入队列，并检验是否该节点为last节点，是的话换行。



### 1.2 二叉树序列化&反序列化

以先序遍历为例。重点在于消除歧义：
1. 假设序列化结果为str，初始时str为空字符串
2. 先序遍历二叉树时如果遇到空节点，在str末尾加上“#!”
3. 如果遇到不为空的节点，假设节点值为3，就在str末尾加上“3!”

## 2. 字符串

### 2.1 判断是否为旋转词

#### 要求

把字符串strqi前面任意部分移动到后面，形成旋转词

#### 解决方案

1. 判断长度是否相等
2. 长度相等，则生成str1+str1的大字符串
3. 检测str2是否为str1+str1的子串(KMP算法)

此最优解为O(n)

### 2.2 字符串旋转

#### 要求
"pig loves dog" --> "dog loves pig"

#### 解决方案

1. 实现字符串逆序的函数f
2. 利用f将整个字符串逆序（god sevol gip）
3. 对每个单词区域内将单词逆序（dog loves pig）

### 2.3 字符串原地调整

#### 要求
给定一个字符串str和整数i，将字符串str[0..i]移动到右侧。额外空间复杂度为O(1)，时间复杂度为O(n)。

例如: str=ABCDE, i=2, 调整为DEABC

#### 解决方案
1. str[0..i]逆序 (CBADE)
2. str[i+1..n]逆序 (CBAED)
3. 全部逆序 (DEABC)


### 2.4 字符串最小拼接

#### 要求 
给定一个字符串数组strs，找到一种拼接顺序使得所有字符串拼接起来之后的大字符串的字典顺序最小。
#### 解决方案
最优解时间复杂度为O(N*logN)。

1. 比较 str1+str2 和 str2+str1


## 3. 排序算法

### 3.1 各排序算法介绍

#### 冒泡排序
* 时间复杂度O(N^2)
* 两两交换，较大者向后移动。
 
#### 选择排序
* 时间复杂度O(N^2)
* 实现过程：每次从当前位置至末尾选择最小值放在当前位置。

#### 插入排序
* 时间复杂度O(N^2)
* 实现过程：每个元素与前面的元素比较，若小于前面的元素则继续向前查找，否则插入到该元素后面。

#### 归并排序
* 时间复杂度O(N*logN)
* 实现过程：
   1. 每个元素成为长度为1的有序区间；
   2. 每两个相邻区间合并并排序，形成长度为2的有序区间；
   3. 依次进行递归排序。

#### 快速排序
* 时间复杂度O(N*logN)
* 实现过程：
   1. 随机选择一个元素，比其小的元素移动到其左边，比其大的元素移动到右边；
   2. 对两边继续进行递归排序。

#### 堆排序
* 时间复杂度O(N*logN)
* 实现过程：将堆顶元素(该堆中的最大元素)与堆末尾元素调换并弹出，剩余元素递归进行该操作。

#### 希尔排序
* 时间复杂度O(N*logN)
* 实现过程：类似于步长逐步调整(通常为缩小)的插入排序。每次元素与向前步长个元素相比较，决定插入位置。


#### 计数排序
* 时间复杂度O(N)
* 基于桶排序的思想,建立一个有序空间，按照元素相应大小放入该有序空间中，再依次倒出。

#### 基数排序
* 时间复杂度O(N)
* 以十进制为例，首先按照个位放入桶中，倒出；
* 按照十位放入桶中，倒出；
* 依次类推。 

### 3.2 各排序算法的比较

#### 空间复杂度
* O(1)
   插入排序，选择排序，冒泡排序，堆排序，希尔排序
* O(logN)~O(N)
   快速排序
* O(N)
   归并排序
* O(M)
   (不基于比较的排序算法中)所选择的桶的数量

#### 稳定性
* 稳定的排序算法
   冒泡排序，插入排序，归并排序，计数排序，基数排序，桶排序
* 不稳定的排序算法
   选择排序，快速排序，希尔 排序，堆排序