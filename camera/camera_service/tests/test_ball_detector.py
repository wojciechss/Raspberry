import cv2
from camera_service.ball_detector import BallDetector


def test_detect_ball():
    img = cv2.imread('tests/data/ball.jpg')
    uut = BallDetector()
    result = uut.detect(img)
    assert len(result) == 1


def test_two_balls():
    img = cv2.imread('tests/data/two_balls.jpg')
    uut = BallDetector()
    result = uut.detect(img)
    assert len(result) == 1


def test_no_ball():
    img = cv2.imread('tests/data/empty.jpg')
    uut = BallDetector()
    result = uut.detect(img)
    assert len(result) == 0
