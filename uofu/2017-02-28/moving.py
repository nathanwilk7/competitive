import sys

dist_left = int(sys.stdin.readline())
loc_cost = []
for line in sys.stdin:
    loc_cost.append(line.strip().split(' '))

cost_so_far = 0
current_loc = 0
while dist_left > 0:
    dist_cost = []
    for i in range(len(loc_cost)-1, -1, -1):
        if int(loc_cost[i][0]) > current_loc:
            
        dist_to = final_loc - int(loc_cost[i][0])
        if dist_to > 200:
            break
        cost_of = int(loc_cost[i][1])
        dist_cost.append((dist_to, cost_of))

    min_cost = 999999999999
    mindex = 0
    min_dist = 999
    for i in range(len(dist_cost)):
        if dist_cost[i][0] <= min_cost:
            min_cost = dist_cost[i][1]
            mindex = i
            min_dist = dist_cost[i][0]

    cost_so_far += min_dist * min_cost
