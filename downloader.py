from google.colab import drive
drive.mount('/content/drive')

url = input('Enter URL:\n')

import requests
import time
import os
r = requests.get(url,stream=True)
name = url.split('/')
file_name = name[-1].replace("%20" , " ")
total_size_in_bytes= int(r.headers.get('content-length', 0))
start = time.process_time()
total_size = 0
path = "/content/drive/My Drive/Movies/"

print("File Name = %s" %(file_name))
print("File Size = %d kb \n" %(int(total_size_in_bytes/1000)))
print("Starting download %s ..." %(file_name))
i=0
if os.path.exists(path+file_name):
  split_name = file_name.split('.')
  split_name.insert(-1,"-copy")
  file_name = '.'.join(split_name)
  while os.path.exists(path+file_name):
    i+=1
    split_name = file_name.split('.')
    split_name[-2] = f"-copy({i})"
    file_name = '.'.join(split_name)


with open(path+ file_name, "wb") as file:

  tic = time.perf_counter()
  
  for block in r.iter_content(chunk_size = 1024):
    if block:
      file.write(block)
      total_size += len(block)
      done = (100 * total_size / total_size_in_bytes)
      
      toc = time.perf_counter()
      if toc - tic >= 5:
        tic = toc
        print('%.2f%% Complete , Download Speed %.1f kb/s' % (done ,(total_size/(time.process_time() - start))/1000))  
  

  if total_size_in_bytes != 0 and total_size != total_size_in_bytes:
    print("ERROR, something went wrong")
  else:
    print("Download Compelete Time Elapsed: %.2f Seconds \n" % (time.process_time()-start))