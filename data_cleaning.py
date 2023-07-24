import os
import pandas as pd




def files_reading():
    # files location in folder
    files_location = os.path.abspath(os.path.dirname(__file__)) + "\\all_files"
    try:
        os.makedirs(files_location)
    except:
        pass


    new_dir = os.path.abspath(os.path.dirname(__file__))  + "\\files"
    into_file = os.chdir(new_dir)
    total_files = os.listdir(into_file)


    count = True
    number = 0
    while count:
        # folders
        new_dirs = new_dir + "\\" + total_files[number]
        numbers = 0
        data_folder = os.chdir(new_dirs)
        list_of_files = os.listdir(data_folder)
        for i in list_of_files:
            try:

                data = pd.read_csv(i, error_bad_lines=False,
                                skiprows=range(0, 4), engine='python')
                data["label"] = [total_files[number]
                                for i in range(0, data.shape[0])]
                location_of_allFiles = files_location + \
                    f'\\{total_files[number]}file{numbers}.csv'
                data.to_csv(location_of_allFiles)
                numbers += 1
            except:
                pass

        number += 1
        if number > 5:
            count = False







