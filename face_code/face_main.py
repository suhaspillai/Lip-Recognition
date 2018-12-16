from face_code.face_detection import DetectFace
from face_code.videos_to_frames import Videos2Frames
from utils import Utils
import argparse
import os

def save_face_region(tot_vid_files, list_folder_path):
  obj_detect_face = DetectFace()
  obj_vid_frames = Videos2Frames()
  obj_utils = Utils()
  for i, f_vid_path in enumerate(tot_vid_files):
    videocap = obj_vid_frames.read_video(f_vid_path)
    list_frames = obj_vid_frames.extract_frames(videocap)
    tot_faces = []
    for frame in list_frames:
      list_face_coord = obj_detect_face.detect_face(frame)
      if list_face_coord:
        faces = obj_detect_face.extract_faces(frame,
                                                      list_face_coord)
        tot_faces.extend(faces)
    if tot_faces:
      obj_utils.save_clip_regions(list_folder_path[i], tot_faces)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-vp', '--path_videos',
                      help='path where videos are stored')
  parser.add_argument('-sp', '--save_path', help='path to save faces')
  args = parser.parse_args()
  path_videos = args.path_videos
  save_path = args.save_path
  obj_utils = Utils()
  tot_vid_files = [os.path.join(path_videos, fname) for fname in os.listdir(path_videos)]
  folder_names = obj_utils.extract_folder_name(tot_vid_files)
  list_folder_path = [os.path.join(save_path, folder_name) for folder_name in folder_names]
  save_face_region(tot_vid_files, list_folder_path)

if __name__ == '__main__':
  main()
