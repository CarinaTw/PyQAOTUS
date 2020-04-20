
class TestStrings:

    def test_string_rstrip(self, fixture_string_param):
        a = "qwerty"
        a += fixture_string_param
        b = a.rstrip(fixture_string_param)
        assert b == a[0:len(a)-len(fixture_string_param)]

    def test_string_mult(self):
        a = "qwerty"
        a2 = a * 3
        assert a2[0:len(a)] == a and a2.count(a) == 3

    def test_string_access_by_index(self):
        a = "qwerty"
        for i in range(len(a)):
            assert a[i] in a

    def test_string_find(self):
        a = "qwerty"
        a_sub = "we"
        index = a.find(a_sub)
        for i in a:
            if i == a_sub[0]:
                ind = a.index(i)
        assert ind == index

