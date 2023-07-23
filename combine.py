import os
import csv, glob
           

def combining_csv():
    """ This function is used to combine the multiple csv file in the single csv file """
    basedir = os.path.abspath(os.path.dirname(__file__)) + "\\all_files"
    print(basedir)
    Avg_Dir = os.path.abspath(os.path.dirname(__file__)) 
    print(Avg_Dir)
    heading = True

    csv_file_list = glob.glob(os.path.join(basedir, '*.csv')) # returns the file list
  

    with open(os.path.join(Avg_Dir, 'Output.csv'), 'w', newline='') as f:
        wf = csv.writer(f, lineterminator='\n')

        for files in csv_file_list:
            with open(files, 'r') as r: 
                if heading == True:
                    pass
                    #next(r) 
                    # # SKIP HEADERS
                else:
                    next(r)
                rr = csv.reader(r)
                for row in rr:
                    wf.writerow(row)
                heading = False






