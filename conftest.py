import pytest

@pytest.fixture
def first_fixture():
    print("\n ==> print from first fixture")

    yield
    print("\nBye from first_fixture!")

@pytest.fixture(params=[1,2,3])
def fixture_with_params(request):
    return request.param