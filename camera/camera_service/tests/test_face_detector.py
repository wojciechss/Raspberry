import cv2
from camera_service.face_detector import FaceDetector


def test_detect_face():
    img = cv2.imread('tests/data/snapshot.jpg')
    uut = FaceDetector()
    result = uut.run(img)
    content = result['content']
    assert result['type'] == 'face'
    assert len(content) == 1
    section = content[0]
    assert section['horizontal'] == 2
    assert section['vertical'] == 3
    assert section['distance'] == 2
    print(result)


def test_detect_faces():
    img = cv2.imread('tests/data/snap_multiple_faces.jpg')
    uut = FaceDetector()
    result = uut.run(img)
    content = result['content']
    assert result['type'] == 'face'
    assert len(content) == 3


def test_no_face():
    img = cv2.imread('tests/data/no_face.jpg')
    uut = FaceDetector()
    result = uut.run(img)
    content = result['content']
    assert result['type'] == 'face'
    assert len(content) == 0

