import cv2

class Videos2Frames:
  def __init__(self):
    pass

  def read_video(self, vid_file_path):
    videocap = cv2.VideoCapture(vid_file_path)
    return videocap

  def extract_frames(self, videocap):
    list_frames = []
    count = 0
    while True:
      success, image = videocap.read()
      if success:
        list_frames.append(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
      else:
        break
      count += 1
      print(success, count)
    return list_frames
