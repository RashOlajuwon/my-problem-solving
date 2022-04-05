"""

"""
# Brute-force solution first
# ans = 0
# for i in range(len(height)):
#     vol = 0
#     j = i+1
#     while j<len(height):
#         vol=max(((min(height[i],height[j]))*(j-i)), vol)
#         j+=1
#     ans = max(vol,ans)
# return ans

# Linear time optimized soltuion
l_ptr, r_ptr = 0, len(height)-1
cur = 0
while l_ptr<r_ptr:
    area = min(height[l_ptr],height[r_ptr])*(abs(l_ptr-r_ptr))
    # print(area)
    cur = max(area, cur)
    if height[l_ptr]>height[r_ptr]:
        r_ptr-=1
    else:
        l_ptr+=1
return cur
