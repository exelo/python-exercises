#!//usr/bin/python3.8

# Build a program
# return true if given 2 words they are Anagrams
# return false other wise

def isEqual(dict1, dict2):
    for k,v in dict1.items():
        if k not in dict2:
            return False

        if v != dict2[k]:
            return False
    
    for k,v in dict2.items():
        if k not in dict1:
            return False
        
        if v != dict1[k]:
            return False
            
    return True

def isAnagram(word1, word2):
    dict_word1 = {}
    dict_word2 = {}

    for letter in list(word1):
        if letter not in dict_word1:
            dict_word1[letter] = 1 
            continue

        dict_word1[letter]= dict_word1[letter] + 1
    
    for letter in list(word2):
        if letter not in dict_word2:
            dict_word2[letter] = 1 
            continue

        dict_word2[letter] = dict_word2[letter] + 1

    if isEqual(dict_word1, dict_word2):
        return True
    
    return False


def main():
    print(f"Tesing if both words are anagram")
    while True:
        print(f"To Exit just enter 'quit'")
        word1 = input("Enter first  word: ")
        if word1 == 'quit':
            break

        if not word1:
            print("please enter a word")
            continue

        word2 = input("Enter second word: ")
        if word2 == 'quit':
            break
        result = isAnagram(word1, word2)
        print(result)

if __name__ == "__main__":

    main()