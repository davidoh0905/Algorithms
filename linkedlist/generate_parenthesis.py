class Solution(object):
    ## I am going to use recursion so that the next opening or closing parenthesis can be continuously be added based on rule
    def generateParenthesis(self, n):
        return self.generateParenthesisHelper(n, 0, "", [])
        ## State dictates decision : STATE STATE STATE STATE
        ## and I keep track of the state by "remainingOpenBrackets", "CurrentlyOpenBrackets"
        ## Other choices can be "remainingOpenBrackets", "remainingClosingBrackets"
        ## these two choices will require different evaluation criteria to take action
        ## but essentially the same thing


    def generateParenthesisHelper(self, remainingOpen, currentOpen, currentParen, parenthesisCombo):
        ## When there is no remaining parenthesis to open AND there is no current open parenthesis to close,
        ## it is time to stop.
        ## Base Case
        if remainingOpen == 0 and currentOpen == 0:
            # does it have to have return?
            return parenthesisCombo.append(currentParen)

        ## Three possible scenarios
        ## 1. no remaining parenthesis to open. just has already open parentheses to close
        if remainingOpen == 0 and currentOpen > 0:
            self.generateParenthesisHelper(0, currentOpen - 1, currentParen + ")", parenthesisCombo)
        ## 2. all open parentheses are paired. now time to open the remaining parenthses
        if remainingOpen > 0 and currentOpen == 0:
            self.generateParenthesisHelper(remainingOpen - 1, currentOpen + 1, currentParen + "(", parenthesisCombo)
        ## 3. there are open parentheses to be close but there are also remaining open parenthesis to open up. we've got both options.
        if remainingOpen > 0 and currentOpen > 0:
            self.generateParenthesisHelper(remainingOpen - 1, currentOpen + 1, currentParen + "(", parenthesisCombo)
            self.generateParenthesisHelper(remainingOpen + 0, currentOpen - 1, currentParen + ")", parenthesisCombo)

        ## every function will return once.
        ## all the recursion triggered from the initial trigger of the function are going to return with the base case
        ## initial trigger is guaranteed to bypass the base case return and hit return with the below final return
        return parenthesisCombo


print(Solution().generateParenthesis(3))

## https://www.youtube.com/watch?v=sz1qaKt0KGQ
## n matched parenethesis

## 1. Choice - state dictates choice

## 2. Constraints

## 3. Goals
## N * 2 placements


# Time and Space Complexity
# Space : Max Depth 2*N --> Call stack O(N)
# Time ... ?

























