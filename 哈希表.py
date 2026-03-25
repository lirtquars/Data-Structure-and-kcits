class HashTable:
    def __init__(self, size=10):
        # 哈希表大小（数组长度）
        self.size = size
        # 初始化哈希表：每个位置是一个链表（用列表模拟）
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        """
        哈希函数：把 key 转成数组索引
        """
        return hash(key) % self.size

    def put(self, key, value):
        """插入或更新 key-value"""
        index = self._hash(key)
        # 遍历链表，看 key 是否已经存在
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                # 存在则更新
                self.table[index][i] = (key, value)
                return
        # 不存在则追加
        self.table[index].append((key, value))

    def get(self, key):
        """根据 key 获取 value"""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        # 没找到
        return None

    def remove(self, key):
        """删除 key"""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

    def __str__(self):
        """方便打印查看"""
        return str(self.table)

