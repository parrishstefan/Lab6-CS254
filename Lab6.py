def reverseString(s):
    newStr = ""
    for i in range(len(s)):
        newStr += s[len(s)-1-i]
    print(newStr)

reverseString("hello")