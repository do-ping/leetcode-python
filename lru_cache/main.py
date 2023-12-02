from typing import Optional, Dict


class LRUCache:
    class Node:
        def __init__(self, key: int, val: int):
            self.key: int = key
            self.val: int = val
            self.next: Optional["LRUCache.Node"] = None
            self.prev: Optional["LRUCache.Node"] = None

        def __repr__(self):
            return (
                f"key={self.key} val={self.val} "
                f"next={self.next.key if self.next else None} "
                f"prev={self.prev.key if self.prev else None}"
            )

    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("lru cache capacity must be > 0")
        self.capacity: int = capacity
        self._head: Optional[LRUCache.Node] = None
        self._tail: Optional[LRUCache.Node] = None
        self._cache: Dict[int, LRUCache.Node] = {}

    def _add_node(self, node: Node):
        if not self._head:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

        if node.key not in self._cache:
            self._cache[node.key] = node

    def _move_to_head(self, node: Node):
        if node == self._head:
            return

        if node == self._tail:
            self._tail, self._tail.next = self._tail.prev, None
        else:
            node.prev.next, node.next.prev = node.next, node.prev

        self._add_node(node)

    def _remove_tail(self) -> int:
        if not self._tail:
            return -1

        tail_key = self._tail.key
        self._tail = self._tail.prev
        if self._tail:
            self._tail.next = None
        else:
            self._head = None

        return tail_key

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1

        node = self._cache[key]
        self._move_to_head(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            node = self._cache[key]
            node.val = value
            self._move_to_head(node)
            return

        node = LRUCache.Node(key=key, val=value)
        self._add_node(node)
        self._cache[key] = node

        if len(self._cache) > self.capacity:
            tail_key = self._remove_tail()
            del self._cache[tail_key]


class LRUCacheDict:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("lru cache capacity must be > 0")
        self.capacity: int = capacity
        self._cache: Dict[int, int] = {}

    def get(self, key: int) -> int:
        val = self._cache.pop(key, -1)
        if val != -1:
            self._cache[key] = v
        return val

    def put(self, key: int, val: int):
        if key not in self._cache:
            if len(self._cache) == self.capacity:
                del self._cache[next(iter(self._cache))]
        else:
            self._cache.pop(key)

        self._cache[key] = val


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == "__main__":
    data: tuple[list[str], list[list[int]], list[int | None]]
    for data in [
        (
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            [None, None, None, 1, None, -1, None, -1, 3, 4],
        ),
        (
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 0], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            [None, None, None, 0, None, -1, None, -1, 3, 4],
        ),
    ]:
        actions: list[str] = data[0]
        values: list[list[int]] = data[1]
        result: list[int | None] = data[2]

        lru: LRUCacheDict = None

        for n, action in enumerate(actions):
            if action == "LRUCache":
                capacity = values[n][0]
                lru = LRUCacheDict(capacity=capacity)
            elif action == "put":
                k, v = values[n]
                lru.put(k, v)
            elif action == "get":
                k = values[n][0]
                want = result[n]
                got = lru.get(k)

                # print(
                #     f"get_n={n} lru_capacity={values[0][0]} k={k} want={want} got={got}"
                # )

                assert want == got, f"want={want} got={got}"
            else:
                raise ValueError(f"Unknown action '{action}'")
