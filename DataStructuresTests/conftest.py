import pytest


test_data = (0, 1, 3)
@pytest.fixture(params=test_data)
def fixture_list_param(request):
    return request.param


test_data = ['   ', '***', '======', '']
@pytest.fixture(params=test_data)
def fixture_string_param(request):
    return request.param


test_data = ['sape', 'pape', 'rere', 'lui']
@pytest.fixture(params=test_data)
def fixture_dict_param(request):
    return request.param