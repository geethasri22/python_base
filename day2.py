#finding second largest in array
class Solution:
    def getSecondLargest(self, arr):
        n= len(arr)
        if n<2:
            return -1
        first = second = float('-inf')
        for num in arr:
            if num > first:
                second = first
                first =num
            elif num > second and num !=first:
                second = num
        if second == float('-inf'): #intialisation for finding second largest
            return -1
        else:
            return second
                
