num = (1, 0)
tree = set()
tree.add(num)
stack = list(tree)

def getCollatz(num):
    a = num[0] * 2
    tree.add((a, num))
    stack.append((a, num))
    b = (num[0] - 1) / 3
    if b % 2 == 1:
        tree.add((b, num))
        stack.append((b, num))
    
while 0 < len(stack) < 1000:
    num = stack.pop(0)
    print(len(stack))
    getCollatz(num)
