def parallel_processing(z, s, data):
    output = []
    # TODO: write the function for simulating parallel tasks, create the output pairs
    threads = [(i, 0) for i in range(z)]
    for i in range(s):
        ti = data[i]
        thread_idx, start_time = min(threads, key=lambda x: x[1])
        output.append((thread_idx, start_time))
        threads[thread_idx] = (thread_idx, start_time+ti) 
    return output

def main():
    # TODO: input from keyboard
    # enter consists of two lines
    # z and s - first line
    # z - thread count 
    # s - job count
    z, s = map(int, input().split())

    # second line - data 
    # data - contains s integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(z,s,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread_idx, start_time in result:
        print(thread_idx, start_time)

if __name__ == "__main__":
    main()
