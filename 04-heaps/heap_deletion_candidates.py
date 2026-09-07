candidates = []
arr = list(map(int, input().split()))

def is_complete_after_deletion(real_bt: list, indx):
    bt = real_bt.copy()
    bt[indx] = None
    if 2*indx >= len(bt):
        return bt[-1] is None

    if 2*indx + 1 < len(bt) and bt[2*indx + 1] is not None and bt[2*indx] > bt[2*indx + 1]:
            min_child_indx = 2*indx + 1
    else:
        min_child_indx = 2*indx

    bt[indx], bt[min_child_indx] = bt[min_child_indx], bt[indx]
    return is_complete_after_deletion(bt, min_child_indx)


n = len(arr)
for pointer in range(1, n-1):
    if is_complete_after_deletion(arr, pointer):
        candidates.append(str(arr[pointer]))

candidates.append(str(arr[-1]))
print(' '.join(candidates))

