import math
up = 1
right = 1
left = - 1
down = - 1

Vmovement=(up + up + up + up + up + down + down + down)
Hmovement=(left + left + left + right + right)


total = (Vmovement**2+Hmovement**2)
ans= math.sqrt(total)
ans1=round(ans)
print("robot_position:",Vmovement , Hmovement)
print("Distance Travelled",ans1)



