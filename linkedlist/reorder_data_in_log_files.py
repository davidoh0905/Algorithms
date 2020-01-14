class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digitlogs = []
        letterlogs = []
        for i in range(len(logs)):
            if logs[i].split(" ")[1].isdigit():
                digitlogs.append(logs[i])
            else:
                letterlogs.append(logs[i])

        def letterLogSort(letterLog):
            return (" ".join(letterLog.split(" ")[1:]), letterLog.split(" ")[0])

        ## Remember! sort is inplace. Sorted gives you return value
        letterlogs.sort(key=letterLogSort)

        return letterlogs + digitlogs


## Solution Provided
class Solution(object):
    def reorderLogFiles(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)