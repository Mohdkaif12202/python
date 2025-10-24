# decotrator is the method which take the function as the argument and modify and change the behavior 
# of the function  and return it , it change or extend the function without changing the it's source code   
# the funciton which modify the actual function (mode) is written on top and 
# then decorator funtion @modifyer_fun_name and the main function
# at the end calling the function this is the formate of the decorator function if you don't follow 
# it give you an error

# def mode(x):# this is the modifyer function
#     def mod():
#         print("this line added by the decorator")
#         x()
#     return mod

# @mode #  this is the decorator function 
# def main(): # this is the main function
#     print("this line is the main function line and other is the modify by the decotrator function")

# main() # this is the calling the function , 
# # and if you don't use the decorator function ( @mode ) you call the function like this :-
# # modifyer_func_name(main_fuc_name)()  :-  mode(main)()

 
# process : >> fistly main function call hua jaha usse decorator mila fir decotrator execute hu fir use ne
# mod function ko return kiya or fir mod function call hua fir mod block me function se pehle or baad me jo
# add krna the wo add kiya or main function jo argument me gaya the usse call kr diya
# mtlb ki jab main function call hua tab python ne use ke jagha mod ko call kiya   

##########################################################################################################

# decorator with the argument with args or kwargs

def sum(func1):
    def sum1(c,d): # or def sum1(*args)
        print(f"Your number is = {c,d} ") 
        func1(c,d) # or func1(*args)
        print("bye.........")
    return sum1 

@ sum
def sum2(a,b):
    print(a+b)

sum2(5,6)