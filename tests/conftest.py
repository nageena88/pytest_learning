import os

import pytest

from scripts import data_processor


@pytest.fixture(scope="module")
def city_list_location():
    return "tests/resources/cities/"


@pytest.fixture(scope="module")
def process_data(city_list_location):
    files = os.listdir(city_list_location)

    def _specify_type(file_name_or_type):
        data = None
        for f in files:
            if file_name_or_type in f:
                if file_name_or_type != ".json":
                    data = data_processor.csv_reader(city_list_location + f)
                else:
                    data = data_processor.json_reader(city_list_location + f)
        return data

    yield _specify_type


"""
Note:
Fixtures with @pytest.fixture(scope="session", autouse=True) must remain in this file # noqa: E501
"""
# pytest_plugins = [
#    "tests.fixtures.cities",
#    "tests.fixtures.data_processing",
# ]
