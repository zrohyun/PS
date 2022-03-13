# 출력형태: 나선 배열 출력

# 1 2 1
# 2 3 2
# 1 2 1

# 1 2 3 4 1
# 4 5 6 5 2
# 3 4 7 4 3
# 2 5 6 5 4
# 1 4 3 2 1

# solution 1
# starting point: 4 corner
# clockwise: r-d-l-u
# not clockwise: l-d-r-u
from itertools import accumulate
def solution(n, clockwise):

  if n ==1: return[[1]]
  elif n == 2: return [[1,1],[1,1]]

  answer = [[0]*n for i in range(n)]
    
  st_point = [(0, 0), #left_top
        (0, n-1), #right_top
        (n-1, 0), #left_bottom
        (n-1, n-1)#right_bottom
        ] 
  
  # (y, x) direction
  RIGHT = (0, 1)
  LEFT = (0, -1)
  DOWN = (1, 0)
  UP = (-1, 0)
  

  route = [
  [RIGHT, DOWN, LEFT, UP], #left_top
  [DOWN, LEFT, UP, RIGHT], #right_top
  [UP, RIGHT, DOWN, LEFT], #left_bottom 
  [LEFT, UP, RIGHT, DOWN], #right_bottom
  ]
        
  if not clockwise:
    route = [
    [DOWN, RIGHT, UP, LEFT], #left_top
    [LEFT, DOWN, RIGHT, UP], #right_top
    [RIGHT, UP, LEFT, DOWN], #left_bottom 
    [UP, LEFT, DOWN, RIGHT], #right_bottom
    ]
    
  for i, r in zip(range(4), route):
    insert_spiral(answer, st_point[i], r)
        
  return answer

def insert_spiral(answer, st_point, r):
  y, x = st_point
  n = len(answer)

  #direction changing point
  #-2 계차수열  
  d_changing_point = list(accumulate(range(n-1, (n+1)%2, -2)))

  idx = 0 
  value = 1

  # x, y에 값 대입
  # 해당 값이 방향전환을 해야하는 지점인지 check
  # 전환이 필요하지 않다면 방향이동
  # 방향이 필요하다면 방향 전환 후 이동
  while True:
        
    answer[y][x] = value
    
    # changing point
    if value in d_changing_point: idx = (idx+1)%len(r)

    # if inserted last value 
    if (value == (d_changing_point[-1]+1)): break
  
    y,x = move(y,x,r[idx])      
    
    value += 1

def move(y,x,direction):
  y += direction[0]
  x += direction[1]
  return y,x



for n in range(1,10):
  arr = solution(n,True)
  s = len(str(arr[len(arr)//2][len(arr)//2]))

  for i in arr:
    for j in i:
      print(f"{j:^{s}}", end=' ')
    print()
  print()