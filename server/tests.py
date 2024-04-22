import os, datetime
from django.urls import reverse

# Define a function to list all files and folders in a directory

def list_files_and_folders(directory, fobject):
    # List all files and folders in the directory
    try:
        contents = os.listdir(directory)
    except NotADirectoryError as e:
        print(e)
    try:
        # Iterate through each item in the directory
        for item in contents:
            # Get the full path of the item
            full_path = directory + "/" + item
            # Skip hidden files and folders (starting with ".")
            if item.startswith('.'):
                continue
            
            # Initialize an empty dictionary to store information about the item
            item_info = {}
            
            # Check if the item is a file or directory
            if os.path.isfile(full_path):
                # If it's a file, populate the item_info dictionary with file information
                item_info['name'] = item
                item_info['type'] = 'file'
                file_size_bytes = os.path.getsize(full_path)

                if file_size_bytes >= 1024 * 1024:  # If size is greater than or equal to 1 MB
                    item_info['size'] = str(file_size_bytes // (1024 * 1024)) + " MB"
                elif file_size_bytes >= 1024 * 1024 * 1024:  # If size is greater than or equal to 1 GB
                    item_info['size'] = str(file_size_bytes // (1024 * 1024 * 1024)) + " GB"
                else:
                    item_info['size'] = str(file_size_bytes // 1024) + " KB"

                item_info['last_modified'] = datetime.datetime.fromtimestamp(os.path.getmtime(full_path))
                item_info['path'] = full_path
                
            elif os.path.isdir(full_path):
                # If it's a directory, populate the item_info dictionary with folder information
                item_info['name'] = item
                item_info['type'] = 'folder'
                item_info['size'] = os.path.getsize(full_path)  # For folders, size can be set to 0
                item_info['last_modified'] = datetime.datetime.fromtimestamp(os.path.getmtime(full_path))
                item_info['path'] = full_path
            
            # Append the item_info dictionary to the fobject list
            fobject.append(item_info)
            
    except Exception as e:            # If there is an error, print the error message
        print(e)



'''
# Replace 'path_to_directory' with the path to the directory you want to inspect
directory = 'C:\\Users\\Rocky\\Documents\\Jubayer\\Web\\File server'
# Initialize an empty list to store file and folder information
fobject = []
list_files_and_folders(directory, fobject)

# Print the file and folder information
for item in fobject:
    print(item)
'''