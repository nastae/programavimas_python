import myModule

def isPalindrome(s):
    return s == s[::-1]

print("Funkcija yra: 12. nustatyti ar duota simbolių eilutė yra palindromas")
print("1. Python'ui parašyti funkciją ..")
print(isPalindrome("asa"))
print("1. .. ir jos išplėtimą C kalba.")
print(myModule.isPalindrome(tuple(["asa"])))