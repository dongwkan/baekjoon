import sys
input = sys.stdin.readline

a = []

def push(X):
    a.append(X)

def pop():
    if a == []:
        print(-1)
    else:
        print(a.pop())

def size():
    print(len(a))

def empty():
    if a == []:
        print(1)
    else:
        print(0)

def top():
    if a == []:
        print(-1)
    else:
        print(a[len(a) - 1])


N = int(input())
for _ in range(N):
    cmd = input().split()
    if cmd[0] == "push":
        push(int(cmd[1]))
    elif cmd[0] == "pop":
        pop()
    elif cmd[0] == "size":
        size()
    elif cmd[0] == "empty":
        empty()
    else:
        top()
