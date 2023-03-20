import pytest
from pytest_factoryboy import register
from .factories import SongFactory
from .factories import StudentFactory

register(SongFactory)


@pytest.fixture
def students():
    return StudentFactory.create_batch(10)
