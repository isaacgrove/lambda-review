# time complexity

def do_a_bunch_of_stuff(items):
    last_idx = len(items) - 1 # getting the length is O(1) because it was given to us
    # (and also because they increment the length counter as they insert stuff)
    
    print(items[last_idx]) # accessing an array element via index - O(1)
                           # printing or console logging - O(1)
    
    middle_idx = len(items) / 2 # arithmetic operations - O(1)
    idx = 0                     # initializing a variable - O(1)
    
    while idx < middle_idx: # running a loop over half the items - O(n/2)
        print(items[idx])
        idx = idx + 1
        
    for num in range(2000): # O(2000)
        print(num) # O(1)
        


# O(2n)
def removeDuplicate(arr):
  differents = {}
  
  for i in arr:
      
    if i not in differents:
      differents[i] = []
      
    differents[i] += [i]
    
  return differents.keys()
print(removeDuplicate([1,1,2,4,5,5,3,3,1,2]))