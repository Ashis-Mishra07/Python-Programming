# def f(n):
#     return n*n


# arr=[1,2,3,4,5]
# result=[]

# for i in arr:
#     result.append(f(i))

# print(str(result))

# multiprocess loop means we are running a function in a single core
# here the process can be a heavy process
# which might slows down ur system . In order to fasten the process we can use multiprocessing
# by diving / mapping the process to multiple cores
# and at the end reduce it to a single result


from multiprocessing import Pool

def f(n):
    return n*n


arr=[1,2,3,4,5]
p=Pool()
result=p.map(f,arr)

print(str(result))
     