import pytest
from sum import mysum

@pytest.mark.parametrize('numbers, output', [
    ([1, 2, 3], 6),
    ([1, 2, 3, 4, 5], 15),
    ([1, 2, 3, 3, 1], 10),
    ([12,11, 1], 24),
    ([1, 2, 3, 1,20], 27)
    # Ajoutez des tests pour que la somme des éléments de la liste soit égale à 10, 24 et 27
])
def test_mysum(numbers, output):
    assert mysum(numbers) == output
    assert type(numbers[0]) == int
    assert (len(numbers) % 2) == 1
