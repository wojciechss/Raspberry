from face_detector_service.image_analyzer import ImageAnalyzer


def test_detect_face():
    uut = ImageAnalyzer('face_detector_service/tests/data/snapshot.jpg')
    uut.is_face_detected()

def test_detect_faces():
    uut = ImageAnalyzer('face_detector_service/tests/data/snap_multiple_faces.jpg')
    uut.is_face_detected()
