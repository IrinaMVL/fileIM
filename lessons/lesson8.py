# class Category:
#     objs: list = []
#
#     @classmethod
#     def add(cls, name: str) -> int:
#         if name.title() in cls.objs:
#             raise ValueError('category name is not unique')
#         cls.objs.append(name.title())
#         return cls.objs.index(name.title())
#
# a = Category.add('Coffee')
# print(a)
# b = Category.add('tea')
# print(b)
# c = Category.add('coffEE')

class Numbers:

    def __init__(self, numbers):
        self.numbers = numbers

    def average(self) -> float:
        return sum(self.numbers) / len(self.numbers)

    def most_common(self):
        most_common_number = max(self.numbers, key=self.numbers.count)
        print(most_common_number)

a = Numbers(2, 3, 4, 3, 4, 3 ,5, 4, 4)
print(a)
