
import time, os
from sympy import fft
from threading  import Thread,  current_thread
from multiprocessing import Process, current_process

def fast_fourier_transform():
    
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    # print(f"{pid} * {processName} * {threadName} ---->Start FFT")
    # seq = [15, 21, 13, 44, 20, 69, 29, 59, 49, 67, 98, 91, 34]
    # transform = fft(seq)
    # #print (transform)
    
    counter = 20
    while(counter):
        print(f"{pid} * {processName} * {threadName} ---->Start FFT")
        seq = [15, 21, 13, 44, 45, 67, 40, 10, 40, 90]
        transform = fft(seq)
        counter = counter-1
        #print (transform)

if __name__ == "__main__":
    start = time.time()
    p1 = Process(target = fast_fourier_transform, args = ())
    p2 = Process(target = fast_fourier_transform, args = ())
    p3 = Process(target = fast_fourier_transform, args = ())
    p4 = Process(target = fast_fourier_transform, args = ())
    p5 = Process(target = fast_fourier_transform, args = ())
    p6 = Process(target = fast_fourier_transform, args = ())
    p7 = Process(target = fast_fourier_transform, args = ())
    p8 = Process(target = fast_fourier_transform, args = ())
    p9 = Process(target = fast_fourier_transform, args = ())
    p10 = Process(target = fast_fourier_transform, args = ())
    p11 = Process(target = fast_fourier_transform, args = ())
    p12 = Process(target = fast_fourier_transform, args = ())
    p13 = Process(target = fast_fourier_transform, args = ())
    p14 = Process(target = fast_fourier_transform, args = ())
    p15 = Process(target = fast_fourier_transform, args = ())
    p16 = Process(target = fast_fourier_transform, args = ())

      
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p11.start()
    p12.start()
    p13.start()
    p14.start()
    p15.start()
    p16.start()

    
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()
    p11.join()
    p12.join()
    p13.join()
    p14.join()
    p15.join()
    p16.join()

    
    end = time.time()
    print('Time taken in seconds: ', end - start)