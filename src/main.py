from PIL import Image, ImageDraw
import os

def list_files(filepath, filetype):
   paths = []
   for root, dirs, files in os.walk(filepath):
      for file in files:
         if file.lower().endswith(filetype.lower()):
            paths.append(os.path.join(root, file))
   return(paths)

getThis = list_files("Screenshots/", "png")[0]

# print(getThis)

im = Image.open(getThis) #input("Directory > ")
additional_size = 6
f_co = (255, 0, 0)   # Red
t_co = (255, 255, 0) # Yellow
size = (4, 4)

def interpolate(f_co, t_co, interval):
    det_co =[(t - f) / interval for f , t in zip(f_co, t_co)]
    for i in range(interval): yield [round(f + det * i) for f, det in zip(f_co, det_co)]

#             #  Width                    #  Height
bg_size = (im.size[0]+additional_size, im.size[1]+additional_size)
gradient = Image.new('RGBA', bg_size, color=0)
draw = ImageDraw.Draw(gradient)

for i, color in enumerate(interpolate(f_co, t_co, im.width * 2)): draw.line([(i, 0), (0, i)], tuple(color), width=1)
gradient.show()
gradient.paste(im, size)

with open('img_result.png', 'wb') as f: gradient.save(f)

os.system("rm " + getThis.replace(" ", "\ "))
print("[*]          Completed")
