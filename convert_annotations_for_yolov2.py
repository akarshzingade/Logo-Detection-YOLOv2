import argparse
import os
from os import walk, getcwd
from PIL import Image
from shutil import copyfile

def convert(size, box):
   x = (box[0] + box[1])/2.0
   y = (box[2] + box[3])/2.0
   w = box[1] - box[0]
   h = box[3] - box[2]
   dw = 1./size[0]
   dh = 1./size[1]
   x = x*dw
   w = w*dw
   y = y*dh
   h = h*dh
   return (x,y,w,h)

def convert_annotation(input_path, output_path, obj_names_path,text_filename):
   if not os.path.exists(output_path):
      os.mkdir(output_path)

   train_files = [] # A list to keep track of all the train files. 

   for folder_name in os.listdir(input_path):
      try:
         if "no-logo" in folder_name or "filelist" in folder_name:
            continue
         for file_name in os.listdir(os.path.join(input_path,folder_name)):
            if '.png' in file_name and 'mask' not in file_name:
               copyfile(os.path.join(input_path,folder_name,file_name),os.path.join(output_path,file_name))
               train_files.append(os.path.abspath(file_name)+'\n')
            elif '.txt' in file_name and 'mask' not in file_name  :
               new_text = ""
               f = open(os.path.join(input_path,folder_name,file_name),'r')
               lines = f.read().split('\n')[:-1]
               f.close()
               for line in lines:
                  chunks = line.split(' ')
                  class_id = chunks[4]
                  xmin = chunks[0]
                  xmax = chunks[2]
                  ymin = chunks[1]
                  ymax = chunks[3]
                  img_path = str(os.path.join(input_path,folder_name,'%s.png'%(file_name.split('.')[0])))
                  img=Image.open(img_path)
                  w= int(img.size[0])
                  h= int(img.size[1])
                  b = (float(xmin), float(xmax), float(ymin), float(ymax))
                  bb = convert((w,h), b)
                  new_text += (str(class_id) + " " + " ".join([str(a) for a in bb]) + '\n')
               f = open(os.path.join(output_path,(file_name.replace('.gt_data',''))),'w')
               f.write(new_text)
               f.close()
            
      except:
         continue

   text = "".join(train_files)
   f = open(os.path.join(obj_names_path,text_filename+'.txt'),'w')
   f.write(text)
   f.close()

   f = open(os.path.join(obj_names_path,'className2ClassID.txt'),'r')
   classes_all = f.read().split('\n')[:-1]

   classes =[]

   for line in classes_all:
      classes.append(line.split('\t')[0]+'\n')


   text = "".join(classes)

   f = open(os.path.join(obj_names_path,'obj.names'),'w')
   f.write(text)
   f.close()


if __name__ == '__main__':
   # Instantiate the parser
   parser = argparse.ArgumentParser(description='Optional app description')

   # Optional positional argument
   parser.add_argument('--input_directory', 
                       help='An Optional positional argument for input directory')

   # Optional positional argument
   parser.add_argument('--output_directory', 
                       help='A Optional positional argument for output directory')

   # Optional positional argument
   parser.add_argument('--obj_names_path',
                       help='A Optional positional argument for obj.names')
   
   parser.add_argument('--text_filename',
                       help='A Optional positional argument for train.txt/test.txt')


   args = parser.parse_args()
   if (args.input_directory is None):
      args.input_directory = "./train"

   if not os.path.exists(args.input_directory):
      print (args.input_directory+" path does not exist!")
      quit()
   
   if (args.output_directory is  None):
      args.output_directory = './train_yolo'
   
   if (args.obj_names_path is  None):
      args.obj_names_path = './'

   if '.txt' in args.text_filename:
      args.text_filename = args.text_filename.replace('.txt','')
   
   print ("Input Directory: "+args.input_directory)
   print ("Output Directory: "+args.output_directory)
   print ("Name of the file that contains path to train/test images: "+args.text_filename+'.txt')
   convert_annotation(input_path=args.input_directory, output_path=args.output_directory, obj_names_path=args.obj_names_path,text_filename=args.text_filename)
