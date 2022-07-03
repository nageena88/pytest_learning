# import resource
import pytest

from scripts import data_processor, map_population_update
from test_fixtures_end import map_data_location, prep_transform_data


def test_data_population_update(prep_transform_data):
    """
    Happy path test
    """
    data_to_transform, population_dict = prep_transform_data
    data_to_transform.add_population(population_dict)
    for row in data_to_transform.get_data():
        assert "Population" in row
        assert "Updated" in row


def test_data_population_no_update(prep_transform_data):
    """
    sad path test: We don't want tha data transformed twice.
    """
    data_to_transform, population_dict = prep_transform_data
    data_to_transform.add_population(population_dict)
    data_to_transform.add_population(population_dict)
    with pytest.raises(Exception) as ext:
        data_to_transform.add_population(population_dict)
    assert str(ext.value) == "You cannot transform the data twice"
