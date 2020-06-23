def reverse(str):
    s = ""
    for ch in str:
        s = ch + s
    return s


# given string
mystr = "phani"
print("Given String: ", mystr)

# reversed string
print("Reversed String: ", reverse(mystr))