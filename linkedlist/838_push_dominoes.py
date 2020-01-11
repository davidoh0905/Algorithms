class Solution(object):
    def pushDominoes(self, dominoes):
        dominoes = list(dominoes)
        dotRanges = []
        i = j = 0
        while i < len(dominoes):
            if dominoes[i] == ".":
                j = i + 1
                while j < len(dominoes) and dominoes[j] == ".":
                    j += 1
            else:
                i += 1
                continue
            dotRanges.append([i, j])
            i = j + 1

        for dotRange in dotRanges:
            L = dotRange[0]
            R = dotRange[1]
            if L==0:
                if R<len(dominoes) and dominoes[R]=='L':
                    for i in range(L, R):
                        dominoes[i] = 'L'
                    print(dominoes)
                    continue
            else


            # L L / 0 L
            if (L==0 and dominoes[R]=='L') or (L!=0 and dominoes[L-1]=='L' and dominoes[R]=='L'):
                print("L L / 0 L")
                for i in range(L,R):
                    dominoes[i]='L'
                print(dominoes)
                continue
            # L R : don't do anything
            # R L
            if L-1 > 0 and dominoes[L-1]=='R' and dominoes[R]=='L':
                print("R L")
                while R-1 > L :
                    dominoes[L]="R"
                    dominoes[R-1]="L"
                    L += 1
                    R -= 1
                print(dominoes)
            # R R / R end
            if dominoes[L]=='R' and (dominoes[R]=='R' or R==len(dominoes)):
                print("R R / R end")
                for i in range(L,R):
                    dominoes[i]='R'
                continue

        return "".join(dominoes)



print(Solution().pushDominoes(".L.R...LR..L.."))