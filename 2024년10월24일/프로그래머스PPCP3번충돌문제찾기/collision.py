

class Point():
    def __init__(self,points:list,number):
        self.number=number
        self.x=points[0]
        self.y=points[1]
class Robot():
    def __init__(self,routes:list):
        self.routes=routes
        
def short_distance(start:list,end:list):
    start_x,start_y=start[0],start[1]
    end_x,end_y=end[0],end[1]
    if start_x<end_x:
        start_x+=1
    else:
        start_x-=1
    if start_y<end_y:
        start_y+=1
    else:
        start_y-=1
    return [start_x,start_y]

def solution(points,routes):
    Map={}
    for i,point in enumerate(points):
        Map[i+1]=point
    robot={}
    for i ,route in enumerate(routes):
        robot[i+1]=route
    map_copy=Map.copy()
    while True:
        start=map_copy[robot[1][0]]
        end=map_copy[robot[1][1]]
        short_distance(start,end)
        break
    
    
    return None

















points=[[3, 2], [6, 4], [4, 7], [1, 4]]	
routes=[[4, 2], [1, 3], [2, 4]]
solution(points,routes)