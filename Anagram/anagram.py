def is_anagram(str1,str2):
    sorted_str1 = sorted(str1.strip().lower())
    sorted_str2 = sorted(str2.strip().lower())

    if sorted_str1 == sorted_str2:
        return f"Both {str1} and {str2} are anagram"
    else:
        return f"Both {str1} and {str2} are not anagram"

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

result = is_anagram(word1,word2)
print(result)
