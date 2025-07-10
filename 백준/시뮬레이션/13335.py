from collections import deque

n, w, l = map(int, input().split())

t = list(map(int, input().split()))
trucks = deque(t)

time = 0
b = [0] * w
bridge = deque(b)

while(True):
    if not trucks:
        if sum(bridge) == 0:
            print(time)
            break
        else:
            time += 1
            bridge.popleft()
            bridge.append(0)
            continue

    time += 1
    m = bridge.popleft()
    l = l + m


    if l >= trucks[0] and len(bridge) < w:
        l = l - trucks[0]
        truck = trucks.popleft()
        bridge.append(truck)
    else:
        bridge.append(0)

