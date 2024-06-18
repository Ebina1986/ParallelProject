from fastapi import FastAPI
from fastapi.responses import JSONResponse , HTMLResponse
import threading
import time
import multiprocessing

app = FastAPI()

@app.get("/",response_class=HTMLResponse)
async def root():
    return """
    <html>
        <header>
            <p> Parallel Project </p>
        </header>
        <body>
            <p> THREAD Projects </p>
            <p><a href = "/Defining_Thread" >1-Defining_Thread </a></p>
            <p><a href = "/Determining_the_current_thread" >2- Determining_the_current_thread</a></p>
            <p><a href = "/Defining_a_thread_subclass" >3- Defining_a_thread_subclass</a></p>
            <p><a href = "/Thread_synchronization_with_a_lock" >4- Thread_synchronization_with_a_lock</a></p>
            <p><a href = "/Thread_synchronization_with_RLock" >5- Thread_synchronization_with_RLock</a></p>
            <p><a href = "/Thread_synchronization_with_semaphores" >6- Thread_synchronization_with_semaphores</a></p>
            <p><a href = "/Thread_synchronization_with_a_barrier" >7- Thread_synchronization_with_a_barrier</a></p> 
            <p> Process Projects </p>
            <p><a href = "/Spawning_a_process" >1- Spawning_a_process </a></p>
            <p><a href = "/Naming_a_Process" >2- Naming_a_Process</a></p>
            <p><a href = "/Running_in_background" >3- Running_in_background</a></p>
            <p><a href = "/Killing_a_process" >4- Killing_a_process</a></p>
            <p><a href = "/Defining_processes_in_a_subclass" >5- Defining_processes_in_a_subclass</a></p>
            <p><a href = "/Using_a_queue_to_exchange_data" >6- Using_a_queue_to_exchange_data</a></p>
            <p><a href = "/Synchronizing_processes" >7- Synchronizing_processes</a></p> 
            <p><a href = "/Using_a_process_pool" >8- Using_a_process_pool</a></p> 
        </body>
    </html>
    """




@app.get("/Defining_Thread")
async def defining_Thread():
    c = []
    def my_func(thread_number):
        c.append('my_func called by thread N°\{}'.format(thread_number))
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_func, args=(i,))
        threads.append(t)
        t.start()
        t.join()
    return JSONResponse(content= {"": c})


@app.get("/Determining_the_current_thread")
async def Determining_the_current_thread():
    c = []
    def function_A():
        c.append(threading.currentThread().getName() + str('--> starting'))

        time.sleep(2)
        c.append(threading.currentThread().getName() + str('--> exiting'))

    def function_B():
        c.append(threading.currentThread().getName() + str('--> starting'))

        time.sleep(2)
        c.append(threading.currentThread().getName() + str('--> exiting'))

    def function_C():
        c.append(threading.currentThread().getName() + str('--> starting'))

        time.sleep(2)
        c.append(threading.currentThread().getName() + str('--> exiting'))


    t1 = threading.Thread(name='function_A', target=function_A)
    t2 = threading.Thread(name='function_B', target=function_B)
    t3 = threading.Thread(name='function_C', target=function_C)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    return JSONResponse(content={"": c})


@app.get("/Defining_a_thread_subclass")
async def Defining_a_thread_subclass():
    import time
    import os
    from random import randint
    from threading import Thread
    c = []
    class MyThreadClass(Thread):
        def __init__(self, name, duration):
            Thread.__init__(self)
            self.name = name
            self.duration = duration

        def run(self):
            c.append("---> " + self.name + " running, belonging to process ID " + str(os.getpid()))

            time.sleep(self.duration)
            c.append("---> " + self.name + " over")

    start_time = time.time()

    # Thread Creation
    thread1 = MyThreadClass("Thread#1 ", randint(1, 10))
    thread2 = MyThreadClass("Thread#2 ", randint(1, 10))
    thread3 = MyThreadClass("Thread#3 ", randint(1, 10))
    thread4 = MyThreadClass("Thread#4 ", randint(1, 10))
    thread5 = MyThreadClass("Thread#5 ", randint(1, 10))
    thread6 = MyThreadClass("Thread#6 ", randint(1, 10))
    thread7 = MyThreadClass("Thread#7 ", randint(1, 10))
    thread8 = MyThreadClass("Thread#8 ", randint(1, 10))
    thread9 = MyThreadClass("Thread#9 ", randint(1, 10))
    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    # Thread joining
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    # End
    c.append("End")
    # Execution Time
    c.append("--- %s seconds ---" % (time.time() - start_time))
    return JSONResponse(content={"": c})

@app.get("/Thread_synchronization_with_a_lock")
async def Thread_synchronization_with_a_lock():
    import threading
    import time
    import os
    from threading import Thread
    from random import randint
    c = []
    # Lock Definition
    threadLock = threading.Lock()

    class MyThreadClass(Thread):
        def __init__(self, name, duration):
            Thread.__init__(self)
            self.name = name
            self.duration = duration
        def run(self):
            # Acquire the Lock
            threadLock.acquire()
            c.append("---> " + self.name +" running, belonging to process ID "+ str(os.getpid()))
            time.sleep(self.duration)
            c.append("---> " + self.name + " over")
            # Release the Lock
            threadLock.release()

    start_time = time.time()
    # Thread Creation
    thread1 = MyThreadClass("Thread#1 ", randint(1, 10))
    thread2 = MyThreadClass("Thread#2 ", randint(1, 10))
    thread3 = MyThreadClass("Thread#3 ", randint(1, 10))
    thread4 = MyThreadClass("Thread#4 ", randint(1, 10))
    thread5 = MyThreadClass("Thread#5 ", randint(1, 10))
    thread6 = MyThreadClass("Thread#6 ", randint(1, 10))
    thread7 = MyThreadClass("Thread#7 ", randint(1, 10))
    thread8 = MyThreadClass("Thread#8 ", randint(1, 10))
    thread9 = MyThreadClass("Thread#9 ", randint(1, 10))
    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    # Thread joining
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    # End
    c.append("End")
    # Execution Time
    c.append("--- %s seconds ---" % (time.time() - start_time))
    return JSONResponse(content={"": c})



@app.get("/Thread_synchronization_with_RLock")
async def Thread_synchronization_with_RLock():
    import threading
    import time
    import random
    c = []
    class Box:
        def __init__(self):
            self.lock = threading.RLock()
            self.total_items = 0

        def execute(self, value):
            with self.lock:
                self.total_items += value

        def add(self):
            with self.lock:
                 self.execute(1)

        def remove(self):
            with self.lock:
                self.execute(-1)

    def adder(box, items):
        c.append("N° {} items to ADD ".format(items))
        while items:
            box.add()
            time.sleep(1)
            items -= 1
            c.append("ADDED one item -->{} item to ADD ".format(items))

    def remover(box, items):
        c.append("N° {} items to REMOVE".format(items))
        while items:
            box.remove()
            time.sleep(1)
            items -= 1
            c.append("REMOVED one item -->{} item to REMOVE ".format(items))

    items = 10
    box = Box()
    t1 = threading.Thread(target=adder, args=(box, random.randint(10, 20)))
    t2 = threading.Thread(target=remover, args=(box, random.randint(1, 10)))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return JSONResponse(content={"": c})
@app.get("/Thread_synchronization_with_semaphores")
async def Thread_synchronization_with_semaphores():
    import logging
    import threading
    import time
    import random
    c = []
    LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    semaphore = threading.Semaphore(0)
    item = 0

    def consumer():
        logging.info('Consumer is waiting')
        c.append('Consumer is waiting')
        semaphore.acquire()
        logging.info('Consumer notify: item number {}'.format(item))
        c.append('Consumer notify: item number {}'.format(item))


    def producer():
        global item
        time.sleep(3)
        item = random.randint(0, 1000)
        logging.info('Producer notify: item number {}'.format(item))
        c.append('Producer notify: item number {}'.format(item))
        semaphore.release()

    # Main program
    for i in range(10):
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    return JSONResponse(content={"": c})

@app.get("/Thread_synchronization_with_a_barrier")
async def Thread_synchronization_with_a_barrier():
    from random import randrange
    from threading import Barrier, Thread
    from time import ctime, sleep
    c= []
    num_runners = 3
    finish_line = Barrier(num_runners)
    runners = ['Huey', 'Dewey', 'Louie']

    def runner():
        name = runners.pop()
        sleep(randrange(2, 5))
        c.append('%s reached the barrier at: %s ' % (name, ctime()))
        finish_line.wait()

    threads = []
    c.append('START RACE!!!!')
    for i in range(num_runners):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    c.append('Race over!')
    return JSONResponse(content={"": c})

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


#Prcessing Section
#1 Spawning a process

from multiprocessing import Queue
def myFunc(i,q):

    q.put('calling myFunc from process n°: %s' % i)
    for j in range(0, i):
        q.put('output from myFunc is :%s' % j)

@app.get("/Spawning_a_process")
async def Spawning_a_process():
    q = Queue()

    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,q))
        process.start()
        process.join()
    mf = []
    while not q.empty():
        mf.append(q.get())
    return JSONResponse(content={"": mf})

#2Naming a process
def nameProcess(q):
    name = multiprocessing.current_process().name
    q.put("Starting process name = %s " %name)
    time.sleep(3)
    q.put("Exiting process name = %s " %name)
@app.get("/Naming_a_Process")
async def Naming_a_Process():
    q = Queue()
    process_with_name = multiprocessing.Process(name='myFunc process', target=nameProcess , args=(q,))
    process_with_default_name = multiprocessing.Process(target=nameProcess, args=(q,))
    process_with_name.start()
    process_with_default_name.start()
    process_with_name.join()
    process_with_default_name.join()

    mf = []
    while not q.empty():
        mf.append(q.get())
    return JSONResponse(content={"": mf})


#3 Running processes in the background
def workInBackgroung(q):
    #name = multiprocessing.current_process().name
    name = multiprocessing.current_process().name
    q.put("Starting %s " % name)
    if name == 'background_process':
        for i in range(0, 5):
            q.put('---> %d ' % i)
        time.sleep(1)
    else:
        for i in range(5, 10):
            q.put('---> %d ' % i)
        time.sleep(1)
    q.put("Exiting %s " % name)

@app.get("/Running_in_background")
async def Running_in_background():
    q = Queue()
    background_process = multiprocessing.Process(name='background_process', target=workInBackgroung , args=(q,))
    background_process.daemon = True
    NO_background_process = multiprocessing.Process(name='NO_background_process', target=workInBackgroung , args=(q,))
    NO_background_process.daemon = False
    background_process.start()
    NO_background_process.start()

    mf = []
    for i in range(14) :
        mf.append(q.get())
    return JSONResponse(content={"": mf})

#4 Killing a process
def killingProcess(q):
    q.put('Starting function')
    for i in range(0, 10):
        q.put('-->%d' % i)
        time.sleep(1)
    q.put('Finished function')

@app.get("/Killing_a_process")
async def Killing_a_process():
    q = Queue()
    p = multiprocessing.Process(target=killingProcess(q))
    q.put('Process before execution: %s' % p.pid)
    q.put('Process run state: %s' % p.is_alive())
    p.start()
    q.put('Process running: %s' % p.pid)
    q.put('Process run state: %s' % p.is_alive())
    p.terminate()
    q.put('Process terminated: %s' % p.pid)
    q.put('Process run state: %s' % p.is_alive())
    p.join()
    q.put('Process joined: %s' % p.pid)
    q.put('Process run state: %s' % p.is_alive())
    q.put('Process: %s' % p.pid)
    q.put('Terminated by exit code: %s' % p.exitcode)

    mf = []
    while not q.empty():
        mf.append(q.get())
    return JSONResponse(content={"": mf})

# 5 : Defining processes in a subclass
from multiprocessing import Process
class DefineProcess(Process):
    def __init__(self , q):
        super().__init__()
        self.q = q
    def run(self):
        self.q.put('called run method by %s' % self.name)
        return

@app.get("/Defining_processes_in_a_subclass")
async def Defining_processes_in_a_subclass():
    q = Queue()
    for i in range(10):
        process = DefineProcess(q)
        process.start()
        process.join()

    mf = []
    while not q.empty():
        mf.append(q.get())
    return JSONResponse(content={"": mf})

#6 : Using a queue to exchange data
import random
class consumer(multiprocessing.Process):
    def __init__(self, queue , q):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.q = q
    def run(self):
        while True:
            if (self.queue.empty()):
                self.q.put("the queue is empty")
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                self.q.put('Process Consumer : item %d popped from by %s ' % (item, self.name))
                time.sleep(1)
class producer(multiprocessing.Process):
    def __init__(self, queue , q):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.q = q
    def run(self) :
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            self.q.put("Process Producer : item %d appended to queue %s"% (item,self.name))
            time.sleep(1)
            self.q.put("The size of queue is %s"% self.queue.qsize())

@app.get("/Using_a_queue_to_exchange_data")
async def Using_a_queue_to_exchange_data():
    q = Queue()
    queue = multiprocessing.Queue()
    process_producer = producer(queue,q)
    process_consumer = consumer(queue,q)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()
    mf = []
    while not q.empty():
        mf.append(q.get())
    return JSONResponse(content={"": mf})


#7 : Synchronizing processes
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime
def test_with_barrier(synchronizer, serializer , q):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        q.put("process %s ----> %s" %(name,datetime.fromtimestamp(now)))
def test_without_barrier(q):
    name = multiprocessing.current_process().name
    now = time()
    q.put("process %s ----> %s" %(name ,datetime.fromtimestamp(now)))

@app.get("/Synchronizing_processes")
async def Synchronizing_processes():
    q = Queue()
    synchronizer = Barrier(2)
    serializer = Lock()
    Process(name='p1 - test_with_barrier',target=test_with_barrier,args=(synchronizer,serializer,q)).start()
    Process(name='p2 - test_with_barrier',target=test_with_barrier,args=(synchronizer,serializer , q)).start()
    Process(name='p3 - test_without_barrier',target=test_without_barrier,args=(q,)).start()
    Process(name='p4 - test_without_barrier',target=test_without_barrier,args=(q,)).start()
    mf = []
    for i in range(4):
        mf.append(q.get())

    return JSONResponse(content={"": mf})


#8 : Using a process pool
def function_square(data):
    result = data*data
    return result

@app.get("/Using_a_process_pool")
async def Using_a_process_pool():
    q = Queue()
    inputs = list(range(0, 100))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)
    pool.close()
    pool.join()
    mf = []
    for i in pool_outputs :
        mf.append(i)
    return JSONResponse(content={"Pool": mf})