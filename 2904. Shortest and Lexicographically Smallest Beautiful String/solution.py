class Solution:
    # Return true if the second element is smaller than the first
    def compare(self, shortest: str, other: str):
        l1 = len(shortest)
        l2 = len(other)
        if l1 > l2:
            return True
        elif l1 < l2:
            return False
        else:
            # equal length
            for i in range(l1):
                char1 = shortest[i]
                char2 = other[i]
                if char1 == "1" and char2 == "0":
                    return True
                if char1 == "0" and char2 == "1":
                    return False
            return False

    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        l = len(s)
        i = 0
        shortest = ""
        while i < l: 
            if s[i] != "1":
                i += 1
                continue
            if k == 1:
                return "1"
            j = i + 1
            count = 1
            while j < l:
                if s[j] == "1":
                    count += 1
                if count == k:
                    if shortest == "" or self.compare(shortest, s[i:j+1]):
                        shortest = s[i:j+1]
                    break
                j += 1
            if j == l:
                break
            i += 1
        return shortest

    
