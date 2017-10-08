from camera_service.position_calculator import PositionCalculator


def test_full_first_section():
    uut = PositionCalculator(section_size=0.75)
    assert uut.section(position=10, length=140, full_length=320) == 1


def test_first_section():
    uut = PositionCalculator(section_size=0.75)
    assert uut.section(position=69, length=120, full_length=320) == 1


def test_full_second_section():
    uut = PositionCalculator(section_size=0.75)
    assert uut.section(position=170, length=140, full_length=320) == 3


def test_second_section():
    uut = PositionCalculator(section_size=0.75)
    assert uut.section(position=131, length=120, full_length=320) == 3


def test_length_equal_to_half_full_length_first_section():
    uut = PositionCalculator(section_size=0.75)
    assert uut.section(position=0, length=160, full_length=320) == 1


def test_length_equal_to_half_full_length_second_section():
    uut = PositionCalculator(section_size=0.75)
    assert uut.section(position=160, length=160, full_length=320) == 3


def test_length_equal_full_length():
    uut = PositionCalculator(section_size=0.75)
    assert uut.section(position=0, length=320, full_length=320) == 2


def test_center_section():
    uut = PositionCalculator(section_size=0.75)
    assert uut.section(position=100, length=120, full_length=320) == 2


def test_length_smaller_distance_ok():
    uut = PositionCalculator(section_size=0.75)
    assert uut.distance(length=150, full_length=320) == 2


def test_length_bigger_distance_ok():
    uut = PositionCalculator(section_size=0.75)
    assert uut.distance(length=170, full_length=320) == 2


def test_distance_close():
    uut = PositionCalculator(section_size=0.75)
    assert uut.distance(length=180, full_length=320) == 1


def test_distance_far():
    uut = PositionCalculator(section_size=0.75)
    assert uut.distance(length=140, full_length=320) == 3
