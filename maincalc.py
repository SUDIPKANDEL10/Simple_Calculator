import add_work
import sub_work
import mul_work
import div_work

print("welcome to the calculator enjoy using calculator")
a=int(input("enter the value:"))
b= int(input("enter the second value"))

tot_sum=add_work.add(a,b)
tot_sub=sub_work.sub(a,b)
tot_mul=mul_work.mul(a,b)
tot_div= div_work.div(a,b)

print(f"total sum is {tot_sum}, total subratctio is {tot_sub}, total multiplication is {tot_mul}, and total division is {tot_div}")
