class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashTable = {}
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for letter in letters:
            hashTable[letter] = 0
        for char in s:
            hashTable[char] += 1
        for char in t:
            hashTable[char] -= 1
        for key in hashTable.keys():
            if hashTable[key] == -1:
                return key
