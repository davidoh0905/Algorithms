### Revisit this mother fucker

import collections
class Solution(object):
    """
    def canFinish(self, numCourses, prerequisites):
        adjMatrix = [[[0,0] for i in range(numCourses)] for j in range(numCourses)]

        for edge in prerequisites:
            adjMatrix[edge[0]][edge[1]] = [1,0]

        print(adjMatrix)

        for edge in prerequisites:
            if adjMatrix[edge[0]][edge[1]][1] == 1:
                return False
            else:
                adjMatrix[edge[0]][edge[1]][1] = 1
        return True
    """

    def canFinish(self, numCourses, prerequisites):
        # build adjacency data structure : This time using Dictionary
        adjDict = collections.defaultdict(list)
        # loop through all the edges and only keep track of nodes that points to somewhere else and its destination
        for edge in prerequisites:
            adjDict[edge[0]].append(edge[1])

        startNodes = adjDict.keys()
        return self.detectCycle(adjDict, startNodes, numCourses)

    def detectCycle(self, adjDict, startNodes, numCourses):

        for node in startNodes:
            print("starting with node : ", node)
            isVisited = [0 for i in range(numCourses)]
            isCycle = self.detectCycleHelper(adjDict, node, isVisited)
            if not isCycle:
                return False
        return True

    def detectCycleHelper(self, adjDict, node, isVisited):
        print(isVisited)
        # Base Case
        if node not in adjDict:
            return True
        # Work
        if isVisited[node]==1:
            return False
        else:
            isVisited[node]=1
        # Recursion : but if it is triggered individually and not dependent in straight line....
        # how is it going to gather....
        res = True
        for nextNode in adjDict[node]:
            print("triggering recursion with : ", nextNode, isVisited)
            res = res and self.detectCycleHelper(adjDict, nextNode, isVisited[:])
        return res



#print(Solution().canFinish(6, [[0,1],[1,3],[0,2],[2,1],[3,0],[4,5]]))
#print(Solution().canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]  ))
print(Solution().canFinish(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]  ))

