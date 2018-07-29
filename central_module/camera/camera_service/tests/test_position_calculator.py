from camera_service.section_calculator import SectionCalculator


def test_center_section():
    uut = SectionCalculator()
    assert uut.calculate(3, 45, 45, 90, 90) == (2, 2)


def test_left_section():
    uut = SectionCalculator()
    pos = uut.calculate(3, 20, 45, 90, 90)
    assert uut.calculate(3, 20, 45, 90, 90) == (1, 2)


def test_right_section():
    uut = SectionCalculator()
    assert uut.calculate(3, 70, 45, 90, 90) == (3, 2)


def test_up_section():
    uut = SectionCalculator()
    assert uut.calculate(3, 45, 20, 90, 90) == (2, 1)


def test_down_section():
    uut = SectionCalculator()
    assert uut.calculate(3, 45, 70, 90, 90) == (2, 3)


def test_start_first_sections():
    uut = SectionCalculator()
    assert uut.calculate(3, 0, 0, 90, 90) == (1, 1)


def test_end_first_sections():
    uut = SectionCalculator()
    assert uut.calculate(3, 30, 30, 90, 90) == (1, 1)


def test_end_second_sections():
    uut = SectionCalculator()
    assert uut.calculate(3, 60, 60, 90, 90) == (2, 2)


def test_end_third_sections():
    uut = SectionCalculator()
    assert uut.calculate(3, 90, 90, 90, 90) == (3, 3)
