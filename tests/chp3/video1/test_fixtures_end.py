import pytest

from scripts import data_processor, map_population_update


@pytest.fixture(scope="session")
def map_data_location():
    yield "tests/resources/cities/clean_map.csv"


@pytest.fixture(scope="function")
def prep_transform_data(map_data_location):
    population_dict = {
        "Andorra": 77142,
        "Argentina": 44780677,
        "Cape Verde": 546388,
        "Germany": 83670653,
        "Greece": 10473455,
        "India": 1366417754,
        "Japan": 128860301,
        "Morocco": 36471769,
        "Senegal": 16296364,
        "United States": 329064917,
    }
    data = data_processor.csv_reader(map_data_location)
    data_to_transform = map_population_update.MapData(data, False)
    yield data_to_transform, population_dict
