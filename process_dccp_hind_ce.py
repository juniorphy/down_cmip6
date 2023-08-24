# this script intends to process data from hindcast into commom datagrid
import xarray as xr
import pandas as pd
import glob
import os


def grab_region(fdirname):
    #print('Prcessing file ', fdirname, '...')
    print()
    cudir = os.path.dirname(fdirname)
    fname = os.path.splitext(os.path.basename(fdirname))[0]
    os.makedirs(f'{cudir}/ce', exist_ok=True)

    # Specify the lon-lat box coordinates
    lon_min = -50+360
    lon_max = -33+360
    lat_min = -21
    lat_max = 2
    # Specity input and output filename
    input_file = fdirname
    output_file = f'{cudir}/ce/{fname}_ce.nc'
    os.system(f"cdo -O sellonlatbox,{lon_min},{lon_max},{lat_min},{lat_max} {input_file} {output_file}")
    print('file created  ', output_file)

if __name__ == '__main__': 

    cdir = "./"
    wdir = cdir + 'dcppA-hindcast/'
    #wdir = cdir + 'dcppb-forecast/'

    models = [d for d in os.listdir(wdir) if os.path.isdir(os.path.join(wdir,d))]

    for model in sorted(models):
        fin = f'{wdir}{model}/Amon/pr/'
        
        for subexp in range(2005,2017):
            print(model, f's{subexp}')
            files = sorted(glob.glob(f'{fin}s{subexp}/*.nc'))
            for fdirname in files:
                grab_region(fdirname)
            
