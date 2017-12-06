'''
find NN in kd tree
'''

def findNN(root,query)
    NN = root.elt
    min_dist= computeDist(query,NN)
    nodeList=[]
    temp_root=root
    while temp_root:
        nodeList.append(temp_root)
        dd = computeDist(query,temp_root.elt)
        if min_dist>dd:
            NN = temp_root.elt
            min_dist=dd
        ss = temp_root.split
        if query[ss]<=temp_root.elt[ss]:
            temp_root=temp_root.left
        else:
            temp_root=temp_root.right
    while nodelist:
        back_elt=nodeList.pop()
        ss = back_elt.split
        print ('back.elt=',back_elt.elt)
        if abs(query[ss]-back_elt.elt[ss])<min_dist:
            if (query[ss]<=back_elt.elt[ss]):
                temp_root=back_elt.right
            else:
                temp_root=back_elt.left
            if temp_root:
                nodeList.append(temp_root)
                curDist=computeDist(query,temp_root.elt)
                if min_dist>curDist:
                    min_dist=curDist
                    NN = temp_root.elt
    return NN,min_dist

def computeDist(pt1,pt2):
    sum=0.0
    for in range(len(pt1)):
        sum=sum+(pt1[i]-pt2[i])**2
    return math.sqrt(sum)
