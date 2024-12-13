the_num_list=[0,20,30,42,56,70,200,250,600,1000]

def n_list(num):
    print("The list:",list(num))
def n_sum(num):
    print("The total is:",sum(num))
def n_l(num):
    print("The largest:",max(num))
def n_r(num):
    print("The list in reversed:", list(reverse(num)))
def n_sm(num):
    print("The smallest:",min(num))
    
# Calling the functions to test them 
n_list(the_num_list)
n_sum(the_num_list)
n_l(the_num_list)
n_r(the_num_list)
n_sm(the_num_list)
