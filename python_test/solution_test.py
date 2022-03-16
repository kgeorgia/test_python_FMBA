import os
from glob import glob

labels_dir = "/tmp/labels"

image_extension = ["png", "jpg", "jpeg"]
meta_extension = ["json"]
paths_list = glob(os.path.join(labels_dir, "*"))

result = []
for path in paths_list:
    if os.path.isdir(path):
        folder_name = os.path.basename(path)
        json_list = []
        image_list = []
        folder_dict = {folder_name: []}
        files_in_folder = glob(os.path.join(path, "*"))

        for item in files_in_folder:
            parse_name = os.path.basename(item).split(".")

            if len(parse_name) < 2:
                continue

            if parse_name[-1].lower() in meta_extension:
                json_list.append(parse_name[0])

            if parse_name[-1].lower() in image_extension:
                image_list.append(parse_name[0])
        
        for item_json in json_list:
            if item_json in image_list:
                filename = item_json + ".*"
                folder_dict[folder_name].append(glob(os.path.join(path, filename)))

        if len(folder_dict[folder_name]) != 0:
            result.append(folder_dict)

print(result)