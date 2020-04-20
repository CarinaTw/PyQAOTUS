
class TestDicts:

    def test_dict_del_element(self, fixture_dict_param):
        lst = ['sape', 'pape', 'rere', 'lui']
        dct = dict.fromkeys(lst)
        del dct[fixture_dict_param]
        assert not fixture_dict_param in dct

    def test_dict_keys_unique(self):
        tel = {'jack': 4098, 'sape': 4139}
        tel.setdefault('jack', 1111)
        assert not tel['jack'] == 1111 and len(tel) == 2

    def test_dict_get(self):
        tel = {'jack': 4098, 'sape': 4139}
        for k, val in tel.items():
            assert tel.get(k) == val

    def test_dict_add_new_element(self):
        tel = {'jack': 4098, 'sape': 4139}
        tel.setdefault('year', 2020)
        assert len(tel) == 3 and 'year' in tel

    def test_dict_to_list(self):
        tel = {'jack': 4098, 'sape': 4139}
        tel_list = list(tel.keys())
        assert type(tel_list) == type([]) and tel_list[0] == 'jack'
