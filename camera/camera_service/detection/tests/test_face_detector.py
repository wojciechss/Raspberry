from detection.face_detector import FaceDetector


def test_detect_face():
    uut = FaceDetector('camera_service/tests/data/snapshot.jpg')
    result = uut.analyze()
    content = result['content']
    assert result['type'] == 'face'
    assert len(content) == 1
    section = content[0]
    assert section['horizontal'] == 2
    assert section['vertical'] == 3
    assert section['distance'] == 2
    print(result)

def test_detect_faces():
    uut = FaceDetector('camera_service/tests/data/snap_multiple_faces.jpg')
    result = uut.analyze()
    content = result['content']
    assert result['type'] == 'face'
    assert len(content) == 3


def test_no_face():
    uut = FaceDetector('camera_service/tests/data/no_face.jpg')
    result = uut.analyze()
    content = result['content']
    assert result['type'] == 'face'
    assert len(content) == 0

def test_no_face2():
    uut = FaceDetector('camera_service/tests/data/lastsnap.jpg')
    result = uut.analyze()
    content = result['content']
    assert result['type'] == 'face'
    assert len(content) == 0