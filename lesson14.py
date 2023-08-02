# # from time import sleep
# from threading import (
#     current_thread,
#     main_thread,
#     Thread,
#     Timer,
#     Event,
#     Lock,
#     RLock,
#     Semaphore,
#     Barrier,
#     active_count,
#     get_ident,
#     local
# )
# from requests import Session
# # from threading import enumerate as threading_enumerate
# # from queue import Queue, LifoQueue, PriorityQueue
# #
# #
# lock1 = Lock()
# # rlock1 = RLock()
# # event = Event()
# # l = local()
# # semaphore1 = Semaphore(5)
# # barrier1 = Barrier(5)
# # q = Queue(5)
# # pq = PriorityQueue(5)
# # pq.put((20, 'Hello'))
# # pq.put((1, 'World'))
# # pq.put((3, 'Python'))
# # print(pq.get())
# # print(pq.get())
# # print(pq.get())
# #
# #
# # def function1():
# #     sleep(3)
# #     event.set()
# #
# #
# # def function2():
# #     event.wait(1)
# #     event.clear()
# #     print("I'm work!")
# #
# #
# # def foo():
# #     with semaphore1:
# #         for _ in range(10):
# #             with rlock1:
# #                 print(current_thread().name)
# #             sleep(1)
# #
# #
# # # if __name__ == '__main__':
# # #     threads = [Thread(target=foo, name=f'Thread-{i}') for i in range(10)]
# # #     for thread in threads:
# # #         thread.start()
# #     # thread1 = Thread(target=function1)
# #     # thread2 = Thread(target=function2)
# #     # thread1.start()
# #     # thread2.start()
#
# from multiprocessing import Process, Lock
#
#
# lock2 = Lock()
#
#
# def get_request():
#     with Session() as session:
#         for _ in range(10):
#             response = session.get(
#                 url='https://catalog.onliner.by/'
#             )
#             with lock2:
#                 print(response.status_code)
#
#
# if __name__ == '__main__':
#     processes = [Process(target=get_request) for _ in range(100)]
#     for process in processes:
#         process.start()

from asyncio import (
    sleep,
    Lock,
    Semaphore,
    Barrier,
    Event,
    Queue,
    current_task,
    get_event_loop,
    create_task,
    run,
    set_event_loop_policy,
    WindowsSelectorEventLoopPolicy
)
from aiohttp import ClientSession


async def foo():
    async with ClientSession() as session:
        for _ in range(100):
            response = await session.get(
                url='https://www.kufar.by/l'
            )
            print(response.status)


async def main():
    tasks = [create_task(foo()) for _ in range(10)]
    for task in tasks:
        await task


if __name__ == '__main__':
    run(main())
