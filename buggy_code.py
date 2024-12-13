"""
This code contains some bugs and some errors.  
Find them and fix them.  
When you are done the program will print a message.
Write the message at the bottom of the code before submission
"""
def tract_and_rearrange(string):# give space between the code
str_1 = "".join(reversed(str[0:4].split('g'))).capitalize()
str_2 = "".join(str[6:13].splt('ro'))
str_3 = "".join("".join(reversed(list(str[14:20]))).split(str[17]))#str function is missing
str_4 = "".join(str[21:29].split(str[23:28]))

 return str_1 +  " + str_2 + " " + str_3 + " " str_4

def ultra_extrct_and_rearrange(string): #missing colon so i added it, so it can function
    first_transform = extract_and_rearrange(string)
return first_transform

print(ultra_extract_andrearrange("egthb quirock nwoGrb forijmpxv"))#double colon

