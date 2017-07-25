def loop_size(node):
    '''
    Solution for kata https://www.codewars.com/kata/can-you-get-the-loop
    '''
    arr = []
    while True:
        try:
            arr.index(node.next)
            break
        except:
            arr.append(node.next)
            node = node.next
    startLoop = arr.index(node.next)
    return len(arr[startLoop: len(arr)])
