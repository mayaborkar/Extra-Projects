palindromestr = raw_input ('What is your word? ')
ispalindrome = "yes"
counter = 0

while counter < len(palindromestr)/2:
    if palindromestr[counter] == palindromestr[len(palindromestr)-counter-1]:
        counter = counter+1
    else:
        ispalindrome = "No"
        break
if ispalindrome == "yes":
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")