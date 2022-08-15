## permutation [a,b,c,...] = [a + permutation[b,c,...], b + permutation[a,c,..], ...]
## permutation [a] = [a]

def permutation(arr):

    perm_list = []
    if len(arr) == 1:
        return [arr]
    
    for i in arr:
        subset_arr = [x for x in arr if x != i]
        perm = permutation(subset_arr)
        print(perm)
        for t in perm:
            perm_list.append([i] + t)
    return perm_list