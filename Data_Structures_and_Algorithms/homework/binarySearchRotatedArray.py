# binary search of a sorted array, but the array is rotated
# Example: [5,6,7,0,1,2,3,4]

def csSearchRotatedSortedArray(nums, target):
    # do it again but the array is rotated
    def BinarySearchForPivotIdx(nums, target):
        '''Returns what should be the start index of the sorted array'''
        low = 0
        high = len(nums) - 1
        while nums[low] > nums[high]:
            mid = (low + high) // 2
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return mid
            if nums[mid] < nums[low]:
                high = mid
            else:
                low = mid
        return None
    
    def csBinarySearch(nums, target):
        '''Regular binary search of a sorted array'''
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
    
    # begin logic
    # if the array is actually rotated
    if nums[0] > nums[-1]:
        idx = BinarySearchForPivotIdx(nums, target)
        if not idx:
            # our pivot array function returned None, probably an empty array
            return -1
        
        if target >= nums[0] and target <= nums[idx - 1]:
            # Search the array up to the pivot
            return csBinarySearch(nums[0:idx], target)
        else:
            # Search the array after the pivot
            return csBinarySearch(nums[idx:], target) + idx
    else:
        # the array isn't rotated. Do regular binary search.
        return csBinarySearch(nums, target)
        
    

lst = []
for i in range(0,100,2):
    lst.append(i)
lst.insert(0,500)
print(lst)
print(csSearchRotatedSortedArray(lst,-1))