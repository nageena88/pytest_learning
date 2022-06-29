from scripts.chp2.video2.mapmaker_end import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(Exception) as exp:
        Point("Buenos Aires", 12.11386, -555.08268)
    assert str(exp.value) == "Invalid latitude, longitude combination"

    with pytest.raises(Exception) as exp:
        Point(5, 12.11368, 34.56870)
    assert str(exp.value) == "City name Must be an string"
