import time




start = time.time()
count = 0
while 0==0:
    if count > 100000000:
        break
    count += 1
end = time.time()

print(end-start)
