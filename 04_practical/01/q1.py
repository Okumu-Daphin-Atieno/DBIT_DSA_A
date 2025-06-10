#reversing list
my_list = [20, 40, 60, 80, 100]
my_list.reverse()
print(my_list)

#rotating list
def rotate_list(lst, k):
    n=2
rotated_list=my_list[-2:] + my_list[:-2]
print (rotated_list)