class Category:
    categories: list = []

    @classmethod
    def add(cls, name: str) -> int:
        if name in cls.categories:
            raise ValueError('name is not unique')
        cls.categories.append(name)
        return cls.categories.index(name)

    @classmethod
    def get(cls, index: int) -> int:
        if index not in cls.categories:
            raise IndexError('index is not find')
        return cls.categories.name