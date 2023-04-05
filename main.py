def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(p) and not O(p)
    p = len(data)

    for i in range (p, -1, -1):
        j = i
        while True:
            s = (j * 2) + 1
            if s >= p:
                break
            if s+1 < p and data[s+1] < data[s]:
                s = s+1
            if data[j] > data[s]:
                swaps.append((j, s))
                data[j], data[s] = data[s], data[j]
                j = s
            else:
                break
    return swaps

def main(): 
    # TODO : add input and checks
    # Enter secondly for I or F 
    # 1 and 2 test from keyboard, 3 from files
    # Enter from keyboard
    
    text = input("I or F: ")
    if "I" in text:
        p = int(input())
        data = list(map(int, input().split()))
    
    elif "F" in text:
        f = input()
        if "a" not in f:
            with open("tests/" + f, 'r', encoding='utf-8') as x:
                PermissionError = int(x.readline())
                data = list(map(int, x.readline().split()))
    else:
        print("Error")
        return 
    
    assert data is not None and len(data) == p
    
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)
    
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= p*4
    
    # output all swaps
    print(len(swaps))
    
    for i, j in swaps:
        print(i, j)
       
if __name__ == "__main__":
    main()
