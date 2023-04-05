def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, create the output pairs
    threads = [(i, 0) for i in range(n)]
    for i in range(m):
        ti = data[i]
        thread_idx, start_time = min(threads, key=lambda x: x[1])
        output.append((thread_idx, start_time))
        threads[thread_idx] = (thread_idx, start_time+ti) 
    return output

def main():
    # TODO: crate waht you chose on keyboard
    # Enter consists of two lines
    # n and m - first line
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())

    # data - second life
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread_idx, start_time in result:
        print(thread_idx, start_time)

if name == "main":
    main()
