# def simple_coroutine():
#     try:
#         message = yield
#         print(f'Message received', message)
#
#
# gen = simple_coroutine()
#
# gen.send(None)
# gen.send('ok')
#
# import asyncio
#
#
# async def print_number():
#     num = 1
#     while True:
#         print(num)
#         num += 1
#         await asyncio.sleep(1)
#
#
# async def print_time():
#     count = 0
#     while True:
#         if count % 3 == 0:
#             print(f'{count} seconds passed')
#
#         count += 1
#
#         await asyncio.sleep(.5)
#
#
# async def main():
#     task1 = asyncio.create_task(print_number())
#     task2 = asyncio.create_task(print_time())
#
#     await asyncio.gather(task1, task2)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())
