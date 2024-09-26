# Given a collection of intervals, merge all overlapping intervals into one.
def merge_overlapping_intervals(arr):
    # sort the intervals by their start time
    arr.sort(key=lambda x: x[0])

    # create list for storing the merged intervals
    merged = []

    # iterate through the intervals and check if it overlaps with the last interval in the merged list
    n = len(arr)
    for i in range(n):
        el = arr[i]
        if len(el) != 2:
            raise ValueError("Each element of the input array must be a list with two elements")
        if len(merged) > 0 and el[0] >= merged[-1][0] and el[0] <= merged[-1][1]:
            # if it overlaps, merge the intervals by updating the last value (if it's greater than the end of the previous range)
            if el[1] > merged[-1][1]:
                merged[-1][1] = el[1]
        else:
            # if it doesn't overlap, add the current interval to the merged list
            merged.append(el)
    return merged
