import pytest


class TestLists:

    # тест, параметризованный декоратором parametrize
    @pytest.mark.parametrize("val", (4, "a", [1, 2, 3], {"key": 1}))
    def test_list_append(self, val):
        lst = [1, 2, 3]
        lst.append(val)
        assert lst[-1] == val

    # тест, параметризованный через фикстуру
    def test_list_pop(self, fixture_list_param):
        lst = ["a","b","c","d"]
        lst.pop(fixture_list_param)
        assert not (fixture_list_param in lst)

    def test_list_count(self):
        COUNT = 3
        lst = [1, 2, 3, 4]
        for i in range(COUNT):
            lst.append(lst[3])
        assert lst.count(lst[3]) == COUNT+1 and lst.count(lst[0]) == 1

    def test_list_clear(self):
        lst = [1, 2, 3, 4]
        assert lst.clear() == None
