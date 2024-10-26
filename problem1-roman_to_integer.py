def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        for index, char in enumerate(s):
            if (char == 'I'):
                if index + 1 < len(s) and (s[index+1] == 'V' or s[index+1] =='X'):
                    l.append(-1)
                else:
                    l.append(1)
            elif (char == 'V'):
                l.append(5)
            elif char == "X":
                if index + 1 < len(s) and (s[index+1] == 'L' or s[index+1] == 'C'):
                    l.append(-10)
                else:
                    l.append(10)
            elif (char == 'L'):
                l.append(50)
            elif char == "C":
                if index + 1 < len(s) and (s[index+1] == 'D' or s[index+1] == 'M'):
                    l.append(-100)
                else:
                    l.append(100)
            elif (char == 'D'):
                l.append(500)
            elif (char == 'M'):
                l.append(1000)
        return sum(l)
    

print(romanToInt("XVIII"))