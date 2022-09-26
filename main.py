#Write your code below this line 👇
import math
def paint_calc(height,width,cover):
  total_area = height*width
  no_of_cans = total_area/cover
  #fraction_val=no_of_cans-int(no_of_cans)
  #if(fraction_val!=0.0):
   # no_of_cans = int(no_of_cans)+1
  #else:
    #no_of_cans = int(no_of_cans)
  no_of_cans = math.ceil(no_of_cans2)
  print(f"total cans required are {no_of_cans}")




#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


