import os

folders = ['output_v1']
path = r'C:\Users\Avell\Desktop\output_v2'

n = 0
for folder in folders:
  for image in os.scandir(folder):
    n+=1
    os.rename(image.path, os.path.join(path, '{:06}.txt'.format(n)))