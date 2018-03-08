###Adding a list to beginning of another list
##data = [1,2,3]
##print("Before: ", data)
##data[0:0] = ["a"]
##print("After:  ", data)


###Centering text between fill characters
##print("ABC".center(7, "*"))
##print("ABC".center(8, "*"))


#removing certian characters from string ends
string = "8A1A9"
print("init string: ", string)
print("right strip: ", string.rstrip("0123456789"))
print("left strip:  ", string.lstrip("0123456789"))
print("strip:       ", string.strip("0123456789"))
