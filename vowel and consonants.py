string=input("Enter a String:")
vowels=0
consonants=0
for i in string:
    if i in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):
        vowels+=1
    else:
        consonants+=1
print("Vowels:",vowels)
print("Consonants:",consonants)