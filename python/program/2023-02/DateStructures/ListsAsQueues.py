# 列表也可以用作队列，最先加入的元素，最先取出（“先进先出”）；然而，列表作为队列的效率很低。
# 因为，在列表末尾添加和删除元素非常快，但在列表开头插入或移除元素却很慢（因为所有其他元素都必须移动一位）
# 实现队列最好用 [collections.deque]，可以快速从两端添加或删除元素
from collections import deque

queue = deque(["one", "two", "three"])
queue.append("four")  # Terry arrives
queue.append("five")  # Graham arrives
queue.popleft()  # The first to arrive now leaves

queue.popleft()  # The second to arrive now leaves

queue  # Remaining queue in order of arrival
