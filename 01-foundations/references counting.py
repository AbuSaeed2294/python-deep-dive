import ctypes;
import sys


# ctypes let python to bypass it's rules and it directly talk to low level C memory.
def getReferenceCounts(address):
    return ctypes.c_long.from_address(address).value

arr = [1,2,3];

print(getReferenceCounts(id(arr))) # return 1, as till this line, the reference of arr is hold by only one variable i.e arr.

arr_copy = arr
arr_copy1 = arr
arr_copy2 = arr
print(getReferenceCounts(id(arr_copy))) # return 4, as the reference is hold by 4 variables in total


#using sys 

test_var = [1, 2, 3]

# This will print 2 (1 for test_var, +1 for sys.getrefcount)
print(f"using sys :: {sys.getrefcount(test_var)}")

a = test_var
b = test_var

# This will print 4 (test_var, a, b, +1 for sys.getrefcount)
print(f"using sys again :: {sys.getrefcount(test_var)}")