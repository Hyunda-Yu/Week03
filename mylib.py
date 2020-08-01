def sum_air(gu_airs):
    sum =0
    for gu_air in gu_airs:
        air = gu_air['PM25']
        sum = sum + air
    return sum

def count_air(gu_airs):
    count=0
    for gu_air in gu_airs:
            count +=1
    return count

def avg_gu_air(gu_airs):
    #return sum_air(gu_airs)/count_air(gu_airs)
     return sum_air(gu_airs)/len(gu_airs)


