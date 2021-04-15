def findChildren(L,n):
    if n*2 > len(L) or n*2 == 0:
        return False
    else:
        return True

        
HeapList = [None,8,4,7,2,3,1]
position = 1
status  = findChildren(HeapList,position)

if status:
    print('Parent: %d' % HeapList[position])
    print('Left Child: %d' % HeapList[2*position])
    if (position*2 + 1) < (len(HeapList)):
        print('Right Child: %d' % HeapList[2*position +1])

