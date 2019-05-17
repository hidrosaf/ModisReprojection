import datetime
import csv
import os

import glob

st = datetime.datetime.now()
run_path = r"C:\Users\HPZ640\Downloads\Modis_Data\2018032_20180201"
run_path = r"C:\Users\HPZ640\Desktop\MOD10A1"
run_path = r"I:\FORMRT\20190101"
run_path = r"I:\FORMRT\20190102"
run_path = r"I:\FORMRT\20190103"
files = [os.path.join(run_path, row) for row in glob.glob1(run_path, "MOD10A1*.hdf")]


# temp_text = "\nINPUT_FILENAME = %s \n\n" \
#             "SPECTRAL_SUBSET = ( 0 0 0 0 1 0 0 ) \n\n" \
#             "SPATIAL_SUBSET_TYPE = INPUT_LAT_LONG  \n\n" \
#             #"SPATIAL_SUBSET_UL_CORNER = ( 75.0 -25.0 ) \n\n" \
#             # "SPATIAL_SUBSET_LR_CORNER = ( 35.0 45.0 )  \n\n" \
#             "OUTPUT_FILENAME = I:\modis_results\lbedo\%s.tif  \n\n" \
#             "RESAMPLING_TYPE = NEAREST_NEIGHBOR  \n\n" \
#             "OUTPUT_PROJECTION_TYPE = GEO  \n\n" \
#             "OUTPUT_PROJECTION_PARAMETERS = (   \n\n" \
#             "0.0 0.0 0.0  \n\n" \
#             "0.0 0.0 0.0  \n\n" \
#             "0.0 0.0 0.0  \n\n" \
#             "0.0 0.0 0.0  \n\n" \
#             "0.0 0.0 0.0 )  \n\n" \
#             "DATUM = WGS84  \n\n" \
#             "OUTPUT_PIXEL_SIZE = 0.005\n\n"
#

temp_text = "\nINPUT_FILENAME = %s \n\n" \
            "SPECTRAL_SUBSET = ( 1 0 0 0 0 0 0 ) \n\n" \
            "SPATIAL_SUBSET_TYPE = INPUT_LAT_LONG  \n\n" \
            "OUTPUT_FILENAME = I:\FORMRT\Y_\%s.tif  \n\n" \
            "RESAMPLING_TYPE = NEAREST_NEIGHBOR  \n\n" \
            "OUTPUT_PROJECTION_TYPE = GEO  \n\n" \
            "OUTPUT_PROJECTION_PARAMETERS = (   \n\n" \
            "0.0 0.0 0.0  \n\n" \
            "0.0 0.0 0.0  \n\n" \
            "0.0 0.0 0.0  \n\n" \
            "0.0 0.0 0.0  \n\n" \
            "0.0 0.0 0.0 )  \n\n" \
            "DATUM = WGS84  \n\n" \
            "OUTPUT_PIXEL_SIZE = 0.005\n\n"
print(temp_text)

for file_ in files:
    # if file_.find("MOD10A1.A2017344.h18v03.006.2017346032528") != -1:

    mid = datetime.datetime.now()

    # print(file_)
    t_text = temp_text % (file_, "".join(os.path.basename(file_).split(".")[2:5]))
    with open("".join(os.path.basename(file_).split(".")[2:5])+".prm", "w") as csvfile:
        csvfile.write(t_text)
    os.system(r"I:\MRT\bin\resample.exe -p " + os.path.join(r"I:\FORMRT", "".join(os.path.basename(file_).split(".")[2:5])) + ".prm")
    print(datetime.datetime.now() - mid)

print(datetime.datetime.now() -st)