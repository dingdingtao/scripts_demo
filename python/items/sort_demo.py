'''
Author: dingdingtao
Date: 2021-05-11 12:23:36
LastEditTime: 2021-05-11 14:34:35
LastEditors: dingdingtao
Description: 排序
'''


def bubbleSort(array):
    """
    冒泡排序
    """
    arr = array.copy()
    for index_x, item_x in enumerate(arr):
        for index_y, item_y in enumerate(arr[1:len(arr) - index_x]):
            # print(index_x,item_x,index_y, item_y)
            if arr[index_y] > item_y:
                tmp = arr[index_y + 1]
                arr[index_y + 1] = arr[index_y]
                arr[index_y] = tmp
    return arr



def selectionSort(array):
    """
    选择排序
    """
    arr = array.copy()
    for index_x, item_x in enumerate(arr):
        min_vindex = index_x
        for index_y, item_y in enumerate(arr[index_x + 1:]):
            # print(index_x,item_x,index_y, item_y)
            if arr[min_vindex] > item_y:
                min_vindex = index_y + index_x + 1
        arr[index_x] = arr[min_vindex]
        arr[min_vindex] = item_x
    return arr


def insertionSort(array):
    """
    插入排序
    """
    arr = array.copy()
    for index_x, item_x in enumerate(arr):
        for index_y, item_y in enumerate(arr[:index_x + 1]):
            if item_x < item_y:
                tmp = arr[index_x]
                arr[index_x] = arr[index_y]
                arr[index_y] = tmp
    return arr



def shellSort(arr):
    """
    希尔排序
    """
    pass



def mergeSort(arr):
    """
    归并排序
    """
    pass



def quickSort(arr):
    """
    快速排序
    """
    pass



def buildMaxHeap(arr):
    """
    堆排序
    """
    pass



def countingSort(arr):
    """
    计数排序
    """
    pass



def bucketSort(arr):
    """
    桶排序
    """
    pass



def radixSort(arr):
    """
    基数排序
    """
    pass



if __name__ == '__main__':
    arr = [2, 4, 3, 1, 5, 8, 7, 9, 6, 0]
    # arr = [2, 1, 3]
    sorted_arr = insertionSort(arr)
    print(sorted_arr)