class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        NOT_CHECKED, CHECKING, COMPLETED = 0, 1, 2
        def has_deadlock( course )->bool:
            
            if course_state[course] == CHECKING:
                return True
            
            elif course_state[course] == COMPLETED:
                return False
            
            
            course_state[course] = CHECKING
            
            for pre_course in requirement[course]:
                
                if has_deadlock( pre_course ):
                    return True
                
                                
            course_state[course] = COMPLETED
            
            return False

        requirement = collections.defaultdict( list )
        
        for course, pre_course in prerequisites:
            requirement[course].append( pre_course )

        course_state = [ NOT_CHECKED for _ in range(numCourses) ]

        for course_idx in range(0, numCourses):
            
            if has_deadlock(course_idx):
                return False
        return True