
def parallel_processing(x, y, data):
    output = []
    # TODO: write the function for simulating parallel tasks, create the output pairs
    threads = [(i, 0) for i in range(x)]
    for i in range(y):
        ti = data[i]
        thread_idx, start_time = min(threads, key=lambda x: x[1])
        output.append((thread_idx, start_time))
        threads[thread_idx] = (thread_idx, start_time+ti) 
    return output

def main():
    # TODO: create input from keyboard
    # Enter 2 lines
    # x and y will be first line
    # x - thread count 
    # y - job count
    x, y = map(int, input().split())

    # second line - data 
    # data - contains y integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(x,y,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread_idx, start_time in result:
        print(thread_idx, start_time)

if name == "main":
    main()
