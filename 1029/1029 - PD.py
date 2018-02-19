fib_array = [0, 1]
calls_array = [0, 0]

def fill_arrays(n):
    if (len(fib_array) > n):
        return
    
    for i in range(len(fib_array), n+1):
        fib_array.append(fib_array[i-1] + fib_array[i-2])
        calls_array.append(calls_array[i-1] + calls_array[i-2] + 2)

x = int(raw_input())

for i in range(x):
    n = int(raw_input())

    fill_arrays(n)

    fib_result = fib_array[n]
    qty_calls = calls_array[n]

    print "fib(%d) = %d calls = %d" % (n, qty_calls, fib_result)