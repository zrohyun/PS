#F = G*m1*m2/(d*d)
# 양쪽 점을 ml,mr, 물체 질량 x일때
# G*ml*x/(d*d) == G*mr*x/(1-d)^2
# ml/(d^2) == mr/((1-d)^2)
# d에 대해 binary search하면 되지 않을까?