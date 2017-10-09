import cv2
from camera_service.face_detector import FaceDetector


def test_detect_face():
    img = cv2.imread('tests/data/snapshot.jpg')
    uut = FaceDetector()
    result = uut.detect(img)
    assert len(result) == 1


def test_detect_faces():
    img = cv2.imread('tests/data/snap_multiple_faces.jpg')
    uut = FaceDetector()
    result = uut.detect(img)
    assert len(result) == 3


def test_no_face():
    img = cv2.imread('tests/data/empty.jpg')
    uut = FaceDetector()
    result = uut.detect(img)
    assert len(result) == 0

