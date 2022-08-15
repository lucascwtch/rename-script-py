import os

folder = r'C:\Users\lucas\Pictures\icons\\'

count = 1

    
for file_name in os.listdir(folder):

    old_name = folder + file_name 
    
    file_name, file_extension = os.path.splitext(file_name)
    
    new_name = folder + 'Icon-' + str(count) + file_extension
    
    os.rename(old_name, new_name)
    count += 1
    
print(os.listdir(folder))
