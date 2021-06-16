# heappushは常に最小の値が先頭に来るので、pushする時とpopするときにマイナスにしておくと、降順で最大値を返すことができる
from heapq import heappush, heappop
import sys

que = []
ans = []
for line in sys.stdin:
    order = line.rstrip()
    cmd, *v = order.split()
    if cmd == 'insert':
        heappush(que, -int(v[0]))
    elif cmd == 'extract':
        ans.append("%d\n" % -heappop(que))
    elif cmd == 'end':
        break
sys.stdout.writelines(ans)
