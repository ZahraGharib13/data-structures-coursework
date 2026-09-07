def get_last_candidates(heap):
    candidates = []
    candidates.append(heap[-1])
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

    n = len(heap)
    for pointer in range(1, n-1):
        if is_complete_after_deletion(heap, pointer):
            candidates.append(heap[pointer])
    return candidates

def delete_from_heap(heap_arr, element):
    heap = heap_arr[1:]
    idx = heap.index(element)
    last = heap.pop() 

    n = len(heap)

    if idx < n:
        heap[idx] = last
        i = idx
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and heap[left] < heap[smallest]:
                smallest = left
            if right < n and heap[right] < heap[smallest]:
                smallest = right

            if smallest == i:
                break

            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
    return [0] + heap


def generate_orders(heap_arr, deleted_numbers=None):
    if deleted_numbers is None:
        deleted_numbers = []

    heap = heap_arr[1:]
    n = len(heap)

    if n == 1:
        base_order = [heap[0]]
        return [base_order + deleted_numbers[::-1]]

    candidates = get_last_candidates(heap_arr)
    result = []

    for c in candidates:
        new_heap = delete_from_heap(heap_arr, c)
        new_deleted = deleted_numbers + [c]
        sub_orders = generate_orders(new_heap, new_deleted)
        result.extend(sub_orders)

    return result

arr = list(map(int, input().split()))
orders = generate_orders(arr)

print(len(orders))