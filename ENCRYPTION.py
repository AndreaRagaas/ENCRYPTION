#Pseudocode
#ask the user for input
input_str = input("Write the text that you wanted to encrypt: ")
output_str = ""
#check each character
for i in range(len(input_str)):
#if a, change to *
    if input_str[i] == "a":
        output_str += "*"
#if e, change to &
    elif input_str[i] == "e":
        output_str += "&"
#if i, change to #
#if o, change to +
#if u, change to !
#print output