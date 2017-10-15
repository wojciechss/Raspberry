from camera_service.position_converter import PositionConverter


def test_convert_face():
    faces = [[98, 107, 114, 114]]
    assert PositionConverter.convert_face_position(faces) == [[155, 164, 114]]


def test_convert_multiple_faces():
    faces = [[155, 56, 62, 62], [27, 53, 60, 60], [74, 73, 55, 55]]
    assert PositionConverter.convert_face_position(faces) == [[186, 87, 62], [57, 83, 60], [101, 100, 55]]


def test_convert_ball():
    balls = [[181, 103, 21.86079216003418]]
    assert PositionConverter.convert_ball_position(balls) == [[181, 103, 42]]
