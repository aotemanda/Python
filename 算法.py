# 1、 Python3:快速排序:分而治之+递归
		
def quickSort(arr):
    if len(arr)<2:
    	return arr
    else:
    	baseValue=arr[0]
	lt=[m for m in arr[1:] if m<baseValue]
	eq=[q for q in arr if q==baseValue]
	gt=[n for n in arr[1:] if n>baseValue]
    return quickSort(lt)+eq+quickSort(gt)
arr=[2,6,7,2,6,7,8,9,4,5,1]
print(quickSort(arr))
