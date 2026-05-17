class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisiteMap=defaultdict(set)
        for pair in prerequisites:
            prerequisiteMap[pair[0]].add(pair[1])
        visitSet= set()

        def dfs(course):
            if course in visitSet:
                return False
            if prerequisiteMap[course]=={}:
                return True
            visitSet.add(course)
            for prereq in prerequisiteMap[course]:
                if not dfs(prereq): return False
            visitSet.remove(course)
            prerequisiteMap[course]={}
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True