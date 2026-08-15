my_var = 10;

print(my_var) #10

a = 100;
b = a;

# both will print same refrence number, as id() return the object refrence in base 10 integer, like 4380070144.
print(id(a))
print(id(b))

# we can also use hex method for getting object refrence, hex will return in hexdecimal (recommended way) string i.e. 0x64,
print(hex(a))
print(hex(b))

# Concatenating string i.e injecting variable into string, there are two way i.e.
print("the variable my_var value as :", format(my_var)) #by passing comma separate value, format function will add space by default
print("the variable my_var value as : {0}".format(my_var)) # by direclty calling a format method on string, both will print same result
print("the value {0} is hold by my_var variable".format(my_var)) # by injecting variable in the middle of a string
print("the value {} is hold by my_var variable".format(my_var)) # we can also remove the index of format function argument, format will handle by default
print("the value {0} is hold by my_var, a hold {1} and b hold {2}".format(my_var, a, b)) # will need to mention index, if multiple arguemnt are passed, 
print("the value {} is hold by my_var, a hold {} and b hold {}".format(my_var, a, b)) # if index is not mentioned, then compiler will use the format function argument sequence, 
print(f"the variable my_var value is : {my_var}") # new and recommended way for inejecting variable in string
print(f"the value {my_var} is hold by my_var variable") # new and recommended way for inejecting variable in string