import timeit
import mmap

FILESIZE = 10485760

def mmapped(size):
    #size is chunk size
    chunks = int(FILESIZE/size)
    data = b'1'*size
    f = open("testdoc","wb")
    f.close()
    with open("testdoc","r+b") as f:
        mapf = mmap.mmap(f.fileno(), FILESIZE)
        for i in range(chunks):
            offset = size * i
            mapf[offset:offset+size] = data

    

def written(size):
    chunks = int(FILESIZE/size)
    data = b'1'*size
    with open("testdoc", "wb") as f:
        for i in range(chunks):
            f.write(data)

if __name__ == '__main__':
    chunk_sizes = [10485760, 1048576, int(1048576/8), int(1048576/32), int(1048576/64)]
    for i in chunk_sizes:
        timer = timeit.Timer("written({})".format(i),"from __main__ import written")
        print("write() with chunks size {:<9}:".format(i),timer.timeit(number=10))
        timer = timeit.Timer("mmapped({})".format(i),"from __main__ import mmapped")
        print("mmapping with chunks size {:<8}:".format(i),timer.timeit(number=10))
        
    
