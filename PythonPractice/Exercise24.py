#Python program to check letter is vowel or not
def check_vowel(a):
    if a in ("aeiou"):
        print(" The supplied letter is a vowel")
        return
    else:
       print(" The supplied letter is not a vowel") 
       return

a = input("Please enter the latter: ")
check_vowel(a)
