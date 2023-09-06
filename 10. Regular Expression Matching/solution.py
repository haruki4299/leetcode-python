class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        l1 = len(s)
        l2 = len(p)

        def rem(s,p,l1,l2):
            print(s,p)
            print(l1,l2)
            if l1 == 0 and l2 == 0:
                return True
            elif l1 != 0 and l2 == 0:
                return False
            elif l1 == 0 and l2 != 0 and p[l2-1] != '*':
                print("l1 is zero but l2 has a " + p[l2-1])
                return False
            elif l1 == 0 and l2 != 0 and p[l2-1] == '*':
                return rem(s,p[0:l2-2],l1,l2-2)

            # Take last character
            charS = s[l1-1]
            charP = p[l2-1]
            if charP not in ['*','.']:
                print("Found: " + charP)
                if charS != charP:
                    print("Not same character: " + charS + " and " + charP)
                    return False
                else: 
                    print("Matched pair " + charS + " and " + charP)
                    return rem(s[0:l1-1],p[0:l2-1],l1-1,l2-1)

            elif charP == '.': 
                print("Found wildcard")
                return rem(s[0:l1-1],p[0:l2-1],l1-1,l2-1)
                
            elif charP == '*':
                print("Found repeat")
                repChar = p[l2-2]
                print("Character is: " + repChar)
                if repChar != '.':
                    print("Not Wildcard! Character is: " + repChar)
                    i = 0
                    while i <= l1:
                        if i != 0:
                            char = s[l1-i]
                            if char != repChar:
                                print("Found Different character")
                                break
                        print("Cutting here with " + s[0:l1-i] + " and " + p[0:l2-2])
                        result = rem(s[0:l1-i],p[0:l2-2],l1-i,l2-2)
                        if result == True:
                            return True
                        print("Cutting here did not work :<")
                        i += 1
                    
                    print("no more to remove")
                    return False
                else: 
                    print("Any Character Because. Character is: " + repChar)
                    i = 0
                    while i <= l1:
                        print("i and l1: " + str(i) + " " + str(l1))
                        print("Cutting here with " + s[0:l1-i] + " and " + p[0:l2-2])
                        result = rem(s[0:l1-i],p[0:l2-2],l1-i,l2-2)
                        if result == True:
                            return True
                        print("results were false so lets remove the next character with " + s + " and " + p)
                        i += 1
                    print("no more to remove")
                    return False


        return rem(s,p,l1,l2)
