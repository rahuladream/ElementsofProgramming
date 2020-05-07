import os
import numpy as np
def getMinCost(employee_id, job_id):
    m, n = 0, 0
    cost = np.column_stack((employee_id, job_id))
    R = cost.shape[0]
    C = cost.shape[1]
    tc = [[0 for x in range(C)] for x in range(R)] 

    tc[0][0] = cost[0][0] 

    # Initialize first column of total cost(tc) array 
    for i in range(1, m + 1): 
        tc[i][0] = tc[i-1][0] + cost[i][0] 
  
    # Initialize first row of tc array 
    for j in range(1, n + 1): 
        tc[0][j] = tc[0][j-1] + cost[0][j] 
  
    # Construct rest of the tc array 
    for i in range(1, m + 1): 
        for j in range(1, n + 1): 
            tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], 
                            tc[i][j-1]) + cost[i][j] 
  
    return tc[m][n] 

    # # initialize first column of total cost
    # for i in range(1, m+1):
    #     employee_id[i] = employee_id[i-1] + 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    employee_id_count = int(input().strip())

    employee_id = []

    for _ in range(employee_id_count):
        employee_id_item = int(input().strip())
        employee_id.append(employee_id_item)

    job_id_count = int(input().strip())

    job_id = []

    for _ in range(job_id_count):
        job_id_item = int(input().strip())
        job_id.append(job_id_item)

    result = getMinCost(employee_id, job_id)
    
    print("Result",result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
