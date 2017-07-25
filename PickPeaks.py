def pick_peaks(arr):

    pos = []
    peaks = []
    for i in range(1, len(arr) - 1):
        print(arr[i])
        if arr[i-1] < arr[i] > arr[i+1]:
            if max(arr[i: len(arr)]) != min(arr[i: len(arr)]):
                pos.append(i)
                peaks.append(arr[i])
        elif arr[i-1] < arr[i] == arr[i+1]:
            k = i
            while arr[i] == arr[k]:
                k += 1
                if k == len(arr) - 1:
                    break
            if arr[i] > arr[k]:
                pos.append(i)
                peaks.append(arr[i])
    return {"pos": pos, "peaks": peaks}
