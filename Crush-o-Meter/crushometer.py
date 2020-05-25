names = []

def countOcc():
    occ = {}
    for n in names:
        for c in n:
            if c not in occ:
                occ[c] = 1
            else:
                occ[c] +=1
    return occ

def splitList(list1):
    out = []
    for elem in list1:
        for c in str(elem):
            out.append(int(c))
    return out

def sumRecursive(occurs):
    if len(occurs) <= 2:
        return occurs
    
    new_occurs = []
    is_even = len(occurs)%2 == 0
    for i in range(0, len(occurs)):
        if i < (len(occurs)-(i+1)):
            new_occurs.append(occurs[i] + occurs[-(i+1)])
        else:
            break
    if not is_even:
        new_occurs.append(occurs[i])
    return sumRecursive(splitList(new_occurs))

names.append(input("Insert first name\n").strip(' '))
names.append(input("Insert second name\n").strip(' '))

tmp_occ = countOcc()

occurrences = [ v for v in tmp_occ.values()]

res = sumRecursive(occurrences)

print("Your affinity is {}%".format(''.join(str(e) for e in res)))