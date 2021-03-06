"""Tests linkedlist.py"""

import sys,os

# Add dsalgs package to path
filepath=os.path.abspath(__file__)
dsalgs_path=os.path.dirname(os.path.dirname(filepath))
sys.path.append(dsalgs_path)

from dsalgs.utilities import swap,merge, partition

class TestSwap:

	def test_swap_array_size_2(self):
		arr=[1,2]

		swap(arr,0,1)

		assert arr[0] == 2
		assert arr[1] == 1

	def test_reswap(self):
		arr=[1,2]

		swap(arr,0,1)
		swap(arr,0,1)

		assert arr[0] == 1
		assert arr[1] == 2

class TestMerge:

	def test_simplest_merge(self):
		arr1=[0]
		arr2=[1]

		arr=merge(arr1,arr2)

		assert arr[0] == 0
		assert arr[1] == 1

	def test_equal_merge(self):
		arr1=[1]
		arr2=[1]

		arr=merge(arr1,arr2)

		assert arr[0] == 1
		assert arr[1] == 1

	def test_long_merge(self):
		arr1=[1,3,7,9,13,15,17,17,19]
		arr2=[0,6,10,13,13,13,16,20]

		arr=merge(arr1,arr2)

		assert arr[0] == 0
		assert arr[1] == 1
		assert arr[-1] == 20
		assert arr[-2] == 19

class TestPartition:
	'''
	Tests the partition utility.
	'''

	def test_partition_length_1(self):
		arr=[1]

		arr, i = partition(arr)

		assert i == 0
		assert arr == [1]

	def test_partition_ordered_length_3(self):
		arr=[1,2,3]

		arr,i = partition(arr)

		assert i == 2
		assert arr == [1,2,3]

	def test_partition_length_5(self):
		arr=[4,9,2,5,6]

		arr, i = partition(arr)

		assert i == 3
		assert arr == [4,2,5,6,9]