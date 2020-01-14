class Solution(object):
    def romanToInt(self, s):
        RomIntMap = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}
        numericRepresentation = 0
        return self.romanToIntHelper(s, RomIntMap, 0, numericRepresentation)

    def romanToIntHelper(self, s, RomIntMap, startIndex, numericRepresentation):

        ## BASE CASE of this recursion
        ## if the starting index of the recursion is out of bound of the string, then returm
        ## this is not like other recursions where it triggers branches.
        ## it is going forward type of recursion
        ## so only the very last recursion will return the final value.
        ## all other returns are triggers
        if startIndex >= len(s):
            return numericRepresentation

        ## if it is not out of bound, let's finally start with the current number
        currentNum = RomIntMap[s[startIndex]]

        ## But then, if I am the very last number, there's nothing to do
        ## If it is the last number, just add and return
        if startIndex == len(s) - 1:
            return numericRepresentation + RomIntMap[s[startIndex]]

        ## if I am not the very last number, now let's apply the rule that I have found.
        nextNum = RomIntMap[s[startIndex + 1]]
        ## Case 1 : next number is bigger
        ## subtraction only happens with one smaller number in the front. therefore, I only have to look at current and the next in this case
        if currentNum < nextNum:
            numericRepresentation += (nextNum - currentNum)
            ## and since I have already dealt with the next number, start with the two index after
            return self.romanToIntHelper(s, RomIntMap, startIndex + 2, numericRepresentation)

        ## Case 2 : if next number is smaller --> Add and start recursion
        ## if the next number is either equal or smaller, that is just all addition
        if currentNum >= nextNum:
            numericRepresentation += currentNum
            return self.romanToIntHelper(s, RomIntMap, startIndex + 1, numericRepresentation)

        return numericRepresentation


print(Solution().romanToInt("III"))
print(Solution().romanToInt('IV'))
print(Solution().romanToInt('IX'))
print(Solution().romanToInt('LVIII'))
print(Solution().romanToInt('MCMXCIV'))