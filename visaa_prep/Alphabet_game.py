array = input()
vowel_count = 0
consonant_count = 0
for i in array:
    if i.isalpha():
        if (i=='a' or i=='e' or  i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' ):
            vowel_count += 1
        else:
            consonant_count += 1
print(f"{vowel_count},{consonant_count}")
