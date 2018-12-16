import dlib
class DetectFace:
  def __init__(self):
    pass

  def detect_face(self, img, img_file_path=None):
    """
    The function is used to detect faces in an image
    Args:
      img_file_path (str): Path to image file
    Returns:
      list contain tuple of face coordinates
                              (left, top, right, bottom)
    """
    #use dlib face detector
    #create dlib detector, this is hog with svm
    detector = dlib.get_frontal_face_detector()
    #win = dlib.image_window()
    if img_file_path:
      img = dlib.load_rgb_image(img_file_path)
    #detect number of faces in an image
    dets = detector(img)
    list_face_coord = [] # this will store left, top, right, bottom
    for i, d in enumerate(dets):
      list_face_coord.append((d.left(), d.top(), d.right(), d.bottom()))
    return list_face_coord

  def extract_faces(self, img, list_face_coord):
    """The function is used to extract faces from face coordinates
    Args:
      img (numpy): Image array
      list_face_coord (list): list contain tuple of face coordinates
                              (left, top, right, bottom)
    Returns:
      list of clip faces from image as numpy arrays
    """
    #from the img array extract the facees
    list_faces = []
    #Go through each face coordinates and store the array
    #or clip face region in the list
    for i, coord in enumerate(list_face_coord):
      left, top, right, bottom = coord
      list_faces.append(img[top:bottom, left:right])
    return list_faces
