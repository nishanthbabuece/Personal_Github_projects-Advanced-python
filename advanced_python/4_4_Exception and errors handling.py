#syntax errors
# print('Hello)
# print('Hello' + 42)
# print('Hello' + [1, 2, 3])
# print('Hello' + {1: 'a', 2: 'b'})
# print('Hello' + (1, 2, 3))

#runtime errors
# print(1/0)
# print(1 + 'hello')
# print(int('hello'))
# print('hello'[10])

#logical errors
# def divide(a, b):
#     return a / b
# print(divide(10, 0))

#exception handling
# try:
#     print(1/0)
# except ZeroDivisionError:

# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print(e)

# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print(e)
# finally:
#     print('This will always execute')

# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print(e)
# except:
#     print('An error occurred')

# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print(e)
# except:
#     print('An error occurred')
# finally:
#     print('This will always execute')

class B(Exception):pass
class C(B):pass
class D(C):pass
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

#exceptions grouping

def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")
