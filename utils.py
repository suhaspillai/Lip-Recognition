import cv2
import os
class Utils:
  def __init__(self):
    pass
  def save_clip_regions(self, folder_path, list_clip_regions):
    import pdb;pdb.set_trace()
    for i, clip_region in enumerate(list_clip_regions):
      if not os.path.exists(folder_path):
        os.makedirs(folder_path)
      fname = os.path.join(folder_path, 'frame{:d}.jpg'.format(i))
      cv2.imwrite(fname, clip_region)

  def extract_folder_name(self, list_video_files):
    list_folder_name =[]
    for file_path in list_video_files:
      folder_name = os.path.basename(file_path).split('.')[0]
      list_folder_name.append(folder_name)
    return list_folder_name
