'''
    Quick Sort
    Steps:
        1. Choose a pivot (close to middle point value).
        2. Compare each items in array with pivot.
        3. Sort them to left (smaller value) or right (larger value).
        4. Recursive call the sort function.
'''

import numpy as np
import unittest

class ArrObj:
    def __init__(self, index=None, value=None):
        self.index = index
        self.value = value

    def set_index(self, index):
        self.index = index

    def set_value(self, value):
        self.value = value

    def show(self):
        print('ArrObj: index = %s, value = %s' % (self.index,self.value))

class QuickSort:
    def get_pivot(self, arr):
        mid_point = len(arr)//2
        median = (arr[0]+arr[-1]+arr[mid_point])/3
        index = self.find_nearest(arr, median)
        pivot = ArrObj(index, arr[index])
        return pivot

    def find_nearest(self, arr, value):
        index = np.abs(arr - value).argmin()
        return index
        
    def quick_sort(self, arr):
        i = 0
        j = len(arr) - 2
        
        pivot = self.get_pivot(arr)
        # Swap pivot to the last element.
        arr[-1], arr[pivot.index] = arr[pivot.index], arr[-1]
        
        while j - i > 0:         
            if arr[i] >= pivot.value and arr[j] < pivot.value:
                arr[i], arr[j] = arr[j], arr[i]
            if arr[i] < pivot.value:
                i = i + 1
            if arr[j] >= pivot.value:
                j = j - 1
        if arr[i] > pivot.value:
            arr[-1], arr[i] = arr[i], arr[-1]
        else:
            arr[-1], arr[i+1] = arr[i+1], arr[-1]
        arr_list = [arr[:i],arr[i+1:]]
        for _arr in arr_list:
            if len(_arr) > 1:
                self.quick_sort(_arr)

        
class Testing(unittest.TestCase):
    def setUp(self):
        self.qSort = QuickSort()
        self.arr = np.array([1,2,3,4,5,6,7,8,9,10])
                
    def test_get_pivot(self):
        pivot = self.qSort.get_pivot(self.arr)
        self.assertEqual(pivot.value, 6)

    def test_basic_sorting(self):
        arr = np.array([1,2,9,8,7,3,0,4,5,6])
        self.qSort.quick_sort(arr)
        self.assertTrue(np.alltrue(arr == np.array([0,1,2,3,4,5,6,7,8,9])))

    def test_sorting_compare_with_numpy_sort(self):
        arr = np.random.rand(10)
        arr1 = arr
        arr1.sort()
        self.qSort.quick_sort(arr)
        np.testing.assert_array_equal(arr1, arr)

    def test_sorting_with_negative_value(self):
        messy_arr = np.array([5,11,7,8,9,4,6,3,1,2,0,-1,10])
        sorted_arr = np.array([-1,0,1,2,4,5,6,3,7,8,9,10,11])
        self.qSort.quick_sort(messy_arr)
        np.testing.assert_array_equal(sorted_arr, messy_arr)

    def test_sorting_with_float_number(self):
        messy_arr = np.array([0.1,0.2,0.05,0.7,0.001,0.21,0.91,0.0081])
        self.qSort.quick_sort(messy_arr)
        sorted_arr = np.array([0.001,0.0081,0.05,0.2,0.1,0.21,0.7,0.91])
        np.testing.assert_array_equal(sorted_arr, messy_arr)
        
if __name__ == '__main__':
    unittest.main()














    
