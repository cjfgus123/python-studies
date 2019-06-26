# String is immutable which we cannot change a character itself when string is there
# For example
name = "Chol Yoon"
name[0] = "P" 
# above command will give error due to 'immutability of String'

There is method we can change of element which is String concatenation
Following is method

last_letters = name[1:] 
#this will make last_letters = hol Yoon
#name[1:] line will select string in name from index '1' to the end of string

print("P" + last_letters)
#this will result in print "Phol Yoon"
#this is addtion of string and string concatenation

