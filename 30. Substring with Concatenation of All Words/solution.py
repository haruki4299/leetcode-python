class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
    
        ans = []
        if not s or not words:
            return ans

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        word_frequency = {}  # Dictionary to store the frequency of each word in 'words'
        
        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

        for i in range(word_len):
            left = i
            right = i
            current_words = {}  # Dictionary to store the frequency of words in the current window
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                print(word)
                right += word_len
                
                if word in word_frequency:
                    if word in current_words:
                        current_words[word] += 1
                    else:
                        current_words[word] = 1
                        
                    while current_words[word] > word_frequency[word]:
                        left_word = s[left:left + word_len]
                        print("left_words")
                        print(left_word)
                        left += word_len
                        current_words[left_word] -= 1
                
                    if right - left == total_len:
                        ans.append(left)

                else:
                    current_words.clear()
                    left = right

        return ans

        """
        ans = []
        l1 = len(words[0])
        l2 = len(words)
        l3 = len(s)



        def recFind(s, words, curIndex, ans, l1, l2, l3):
            if curIndex < l3 - l1 * l2 + 1:
                a = 0
                temp = list(words)
                while a < l2: 
                    word = ""
                    for i in range(l1):
                        word = word + s[curIndex + i + (a * l1)]
                    if word in temp:
                        temp.remove(word)
                        a += 1
                    else:
                        break
                if a == l2:
                    ans.append(curIndex)
                recFind(s, words, curIndex+1, ans, l1, l2, l3)
        
        recFind(s,words,0,ans,l1,l2,l3)

        return ans
        """
