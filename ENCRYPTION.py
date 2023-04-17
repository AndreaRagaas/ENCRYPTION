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
    elif input_str[i] == "i":
        output_str += "#"
#if o, change to +
    elif input_str[i] == "o":
        output_str += "+"
#if u, change to !
    elif input_str[i] == "u":
        output_str += "!"
    else:
        output_str += input_str[i]
#print output
print(output_str)