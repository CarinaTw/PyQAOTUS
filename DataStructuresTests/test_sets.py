import pytest


class TestSets:

    # тест, параметризованный декоратором parametrize
    @pytest.mark.parametrize("val", ({1, 2, 3}, {1, 1}, {2}))
    def test_set_remove_dublicates(self, val):
        num_set = {1, 2, 3}
        num_set2 = num_set.copy()
        for i in val:
            num_set.add(i)
        assert num_set == num_set2 and len(num_set) == 3

    def test_set_elements_in_both_sets(self):
        num_set = {1, 2, 3, 1, 1, 3, 3}
        num_set2 = {1, 2, 3, 4}
        assert num_set & num_set2 == {1, 2, 3}

    def test_set_elements_not_in_both_sets(self):
        num_set = {1, 2, 3, 1, 1, 3, 3}
        num_set2 = {1, 2, 3, 4}
        assert num_set ^ num_set2 == {4}

    def test_set_elements_in_one_of_sets(self):
        num_set = {1, 2, 3, 1, 1, 3, 3}
        num_set2 = {0, 1, 2, 3, 4}
        assert num_set2 - num_set == {4, 0}