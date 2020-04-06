class Solution:

    @classmethod
    def approach_1(cls, address: str) -> str:
        return address.replace('.', '[.]')


print(Solution.approach_1('1.1.1.1'))
