def maxProduct(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start == end:
        return arr[start], arr[start], arr[start]
    mid = (start + end) // 2

    maxprodB, maxB, minB = maxProduct(arr, start, mid)
    maxprodC, maxC, minC = maxProduct(arr, mid + 1, end)
    maxprodA = max(maxprodB, maxprodC, maxB * maxC, minB * minC)

    maxA = max(maxB, maxC)
    minA = min(minB, minC)
    if start == 0 and end == len(arr) - 1:
        return maxprodA
    else:
        return maxprodA, maxA, minA
