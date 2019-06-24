import img2pdf
import os
import sys
from time import sleep
from PIL import Image
#Input is a folder output is the same folder but has pdf images instead of 
def remove_alpha_channel(file_path):
    try:
        print(f'Failed to Convert {file_path} to PDF\n Trying to remove the alpha channel')
        sleep(2)
        img_alpha = Image.open(file_path)
        img_alpha.convert('RGB')
        os.remove(file_path) 
        img_alpha.save(file_path)
    except:
        print(f'Failed to remove alpha channel from {file_path} and therefore didnot convert it to a pdf')
        sleep(2)
               
def get_folder():
    return input("Enter Path To folder:\n")
def get_list_of_files(path):
    list_of_files = list()
    for (dirpath, dirnames, filenames) in os.walk(path):
        list_of_files += [os.path.join(dirpath, file) for file in filenames]
    return list_of_files

def convert_jpeg_to_pdf(file_paths):
    print("This is the convert_jpeg_to_pdf")
    index = 0.0
    for file_path in file_paths:
        if file_path.lower().endswith(('.png', '.jpeg', '.jpg', '.gif')):
            os.chdir(os.path.dirname(file_path))
            file_name = os.path.basename(file_path)
            file_name_with_extension = f'{os.path.  splitext(file_name)[0]}.pdf'
            print(file_name)
            print(file_name_with_extension)
            #Remove Alpha Channel from all files

            with open(file_name_with_extension, "wb") as pdf:
                try:
                    print(file_path)
                    pdf.write(img2pdf.convert(file_path))
                    index = index + 1.0
                    percentage = (index / len(file_paths)) * 100
                    print(f'Percentage Complete:%{percentage}')
                    os.remove(file_path)
                except:
                    remove_alpha_channel(file_path)
def main():
    list_files = get_list_of_files(get_folder())
    print(list_files) 
    convert_jpeg_to_pdf(list_files)
    sys.exit(1)
if __name__ == "__main__":
     main()