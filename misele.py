def ele(nmbr):
    list= set([11,22,33,44,55,66,77,88,99,100,101,110,102,32,434,2423,24,242,53,2432,435])
    nmbr = set([int(x) for x in nmbr])
    nmbr = nmbr.symmetric_difference(list)

    nmbr = sorted(nmbr)

    return nmbr

print(ele([11,44,55,66,77,88,99,100,101,434,2423,24,242,2432,435]))