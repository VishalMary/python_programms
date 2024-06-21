def rainwater(height):
    if not height:
        return 0
    l=0
    r=len(height)-1
    max_l=height[l]
    max_r=height[r]
    res=0
    while l<r:
        if max_l<max_r:
            l+=1
            max_l=max(max_l,height[l])
            res+=max_l-height[l]
        else:
            r-=1
            max_r=max(max_r,height[r])
            res+=max_r-height[r]
    return res
    
l=[4,3,4,5,6,1,0,6,7]
print(rainwater(l))