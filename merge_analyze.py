import pandas as pd
import xarray as xr
import numpy as np
import os
import glob
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from pfct import PlotMaps as pm 

def set_master_grid():
    lon_min = -49+360
    lon_max = -34+360
    lat_min = -10
    lat_max = 1
    step = 0.25
    lon = np.arange(lon_min, lon_max+step, step)
    lat = np.arange(lat_min, lat_max+step, step)
    da_coords = xr.DataArray(dims = ['lon', 'lat'] , coords = [lon, lat] )
    return da_coords

def merge_time(model, year1,year2, wdir):

    if model not in ['HadGEM3-GC31-MM', 'EC-Earth3']:
        return

    fin = f'{wdir}{model}/Amon/pr/'
    for subexp in range(year1, year2 + 1):

        print(model, f's{subexp}')

        files = sorted(glob.glob(f'{fin}s{subexp}/ce/*_ce.nc'))
        
        memb = [ ff.split('_')[4].split('-')[1] for ff in files]
        memb=set(memb)
        for mm in memb:
            files = np.sort(glob.glob(f'{fin}s{subexp}/ce/*{mm}*_ce.nc'))
            fname = files[0].split('_')
            with xr.open_mfdataset(files, 
                                  data_vars='minimal', coords='minimal', 
                                  compat='override', combine='nested', concat_dim=['time'],
                                  engine='netcdf4') as mdf:
                
                if model == 'HadGEM3-GC31-MM':
                    ini=mdf.pr.time.values[0].strftime('%Y%m')
                    fim=mdf.pr.time.values[-1].strftime('%Y%m')
                else: 
                    ini=pd.to_datetime(mdf.pr.time.values[0]).strftime('%Y%m')
                    fim=pd.to_datetime(mdf.pr.time.values[-1]).strftime('%Y%m')
               
                fout = f'{fname[0]}_{fname[1]}_{fname[2]}_{fname[3]}_{fname[4]}_{fname[5]}_{ini}-{fim}_membs.nc'
                #mdf.mean(dim='bnds',skipna=True, keep_attrs=None)
                mdf.to_netcdf(fout)
            
def process_hind(model, year1, year2, wdir):
    #model='FGOALS-f3-L'

    if model in ['CNRM-ESM2-1', 'HadGEM3-GC31-MM', 'EC-Earth3']:
        offset=2+12
    if model == 'CanESM5':
        offset=0+12
    if model in ['FGOALS-f3-L','CMCC-CM2-SR5','MIROC6','MPI-ESM1-2-LR']:
        offset=2+12
   
    fin = f'{wdir}{model}/Amon/pr/'
    f_ds = []
    for subexp in range(year1, year2 + 1):
        
        print(model, f's{subexp}')
        if model in ['HadGEM3-GC31-MM', 'EC-Earth3']:
            files =  sorted(glob.glob(f'{fin}s{subexp}/ce/*{subexp+10}*_membs.nc'))
        else:
            files = sorted(glob.glob(f'{fin}s{subexp}/ce/*ce.nc'))
        
 
        with xr.open_mfdataset(files, 
                                   combine='nested', concat_dim=['ensemble'],
                                engine='netcdf4') as mdf:
            #mdf=mdf.mean(dim='bnds', skipna=True)
            
            ds_coords = set_master_grid()
            latnew = ds_coords.coords['lat']
            lonnew = ds_coords.coords['lon']

            mdf2 = mdf.pr.interp(lat=latnew, lon=lonnew, method='linear')
            mdf2 = mdf2.to_dataset()
            #print(mdf2.pr.values)

            #exit()
            mdens = mdf2.pr.mean(axis=0, skipna=True)
            mmean = mdens*86400*30
            mannual = mmean.isel(time=slice(offset,60 + offset)).mean(axis=0, skipna=False)*12
            #print(mannual)
            #exit()
            dsa = mannual.to_dataset()
            
            dsa['year'] = [subexp]
            dsa.to_netcdf(f'{fin}s{subexp}/ce/pr_annual_5-year-mean_{model}_{subexp+1}-{subexp+6}.nc')
            f_ds.append(dsa)
            
            
    pr_hind = xr.concat(f_ds, dim='year')
    pr_hind.to_netcdf(f'pr_annual_5-year-mean_{model}_hind-9118.nc')
    #pr_hind.to_netcdf(f'pr_annual_5-year-mean_{model}_{subexp}.nc')

def process_fcst(model, year1, ddir):

    if model in ['CNRM-ESM2-1', 'HadGEM3-GC31-MM', 'EC-Earth3']:
        offset=2+12
    if model == 'CanESM5':
        offset=0+12
    if model in ['FGOALS-f3-L','CMCC-CM2-SR5','MIROC6','MPI-ESM1-2-LR']:
        offset=2+12

    fin = f'{ddir}{model}/Amon/pr/'
    f_ds = []
    for subexp in range(year1, year1 + 1):


        print(model, f's{subexp}')
        if model in ['HadGEM3-GC31-MM', 'EC-Earth3']:
            files =  sorted(glob.glob(f'{fin}s{subexp}/ce/*_membs.nc'))
        else:
            files = sorted(glob.glob(f'{fin}s{subexp}/ce/*ce.nc'))


        print(f'{fin}s{subexp}/ce/*ce.nc')

        with xr.open_mfdataset(files,
                                combine='nested', concat_dim='ensemble',
                                engine='netcdf4') as mdf:

            ds_coords = set_master_grid()
            latnew = ds_coords.coords['lat']
            lonnew = ds_coords.coords['lon']

            mdf2 = mdf.pr.interp(lat=latnew, lon=lonnew, method='linear')
            mdf2 = mdf2.to_dataset()

            mdens = mdf2.pr.mean(axis=0, skipna=False)
            mmean = mdens*86400*30
            mannual = mmean.isel(time=slice(offset,60 + offset)).mean(axis=0, skipna=False)*12

            dsa = mannual.to_dataset()

            dsa['year'] = [subexp]
            dsa.to_netcdf(f'{fin}s{subexp}/ce/pr_annual_5-year-mean_{model}_{subexp+1}-{subexp+6}.nc')
            f_ds.append(dsa)


    pr_hind = xr.concat(f_ds, dim='year')
    #pr_hind.to_netcdf(f'pr_annual_5-year-mean_{model}_hind-8110.nc')
    pr_hind.to_netcdf(f'pr_annual_5-year-mean_{model}_{subexp}.nc')
    

def process_metric(model):
    ds = xr.open_dataset(f'pr_annual_5-year-mean_{model}_hind-8110.nc')
    ds_mean = ds.mean(dim='year',skipna=False) 
    ds_std = ds.std(dim='year',skipna=False)

    return ds, ds_mean, ds_std

def read_obs_ce(year1, year2):

    dsobs = xr.open_dataset('analysis/pr_daily_funceme_obs_19730101_20230821_kriging_valid_rain.nc')
    dsobs = dsobs.rename({'longitude' : 'lon'})
    dsobs = dsobs.rename({'latitude' : 'lat'})

    dsobs['lon'] = dsobs['lon']+360.

    ds_coords = set_master_grid()
    latnew = ds_coords.coords['lat']
    lonnew = ds_coords.coords['lon']
    
    daobs = dsobs.pr.interp(lat=latnew, lon=lonnew, method='linear')
    dsobs = daobs.to_dataset()

    dannual = dsobs.resample(time='AS').sum(skipna=False)
    dannual = dannual.sel(time=slice(f'{year1}-01-01',f'{year2}-12-31'))

    return dannual

def read_fcst(model, year):
    dsfcst = xr.open_dataset(f'pr_annual_5-year-mean_{model}_{year}.nc')
    return dsfcst

def ploting(annual_accumulation, model):

    ### Definir paleta de cores
    colors_acum = ['#FFFFFF', '#ae000c', '#ff2e1b', '#ff5f26', '#ff9d37', '#fbe78a',
                 '#FFFFC5','#99FFFF', '#00FFFF', '#00CCFF', '#1199FF', '#2A5AEA', '#2A2AEA', '#00007F']
    
    colors_anom = ['#340003', 
                            '#ae000c', '#ff2e1b', '#ff5f26', '#ff9d37', '#fbe78a', '#FFFFC5', 
                            '#ffffff', 
                            '#99FFFF', '#00FFFF', '#00CCFF', '#1199FF', '#2A5AEA', '#2A2AEA', 
                            '#00007F']
    
    levels = np.arange(-110, 130, 20)
    pm.plotmap(annual_accumulation[0,:,:], annual_accumulation.lat[:], annual_accumulation.lon[:]-360, fig_name = f'teste-{model}.png',
    maptype = "fill", dpi = 300, ocean_mask=0, dstk='ceara', boldfont = True, barinf = 'both', barcolor = colors_anom, barlevs = levels,
    meridians = np.arange(0,360,1.), parallels = np.arange(-90,90,1.), fig_title = f'{model}\nAnomalia percentual da precipitação Anual média 2025-2029',
    fig_title_fs = 16, fig_title_weight ='bold', latsouthpoint = -8, latnorthpoint = -2, lonwestpoint = -42, loneastpoint = -37, pltsize = (10, 8),
    xtxtpos = -0.2, ytxtpos = -0.07, con = 'ce',con_mask = 'ce', boldfonts = True)

if __name__ == '__main__': 

    cdir = "./"
    #cdir = "/Volumes/Lenovo/dcpp-decadal/"
    wdir = cdir + 'dcppA-hindcast/'
    fdir = cdir + 'dcppB-forecast/'

    #models = [d for d in os.listdir(wdir) if os.path.isdir(os.path.join(wdir,d))]
    #models = ['EC-Earth3',  'HadGEM3-GC31-MM', 'MPI-ESM1-2-LR']
    models = ['HadGEM3-GC31-MM', 'MPI-ESM1-2-LR']
    
#models = ['MIROC6', 'FGOALS-f3-L', 'CanESM5', 'MPI-ESM1-2-LR']  # modelos usados prev 2021

    for model in sorted(models):
        #merge_time(model, 1981, 2018, wdir)
        #merge_time(model, 2023, 2023, fdir)
        
        process_hind(model, 1991, 2018, wdir)
        #process_hind(model, 2023, 2023, fdir)
        #process_fcst(model, 2023, fdir)
        #continue
        #abrindo metricas do hincast mean and std
        
        dshind, dshind_mean, dshind_std = process_metric(model)

        # lendo dado observado
        dsobs = read_obs_ce(1981, 2010)
        dsobs_mean = dsobs.mean(dim='time',skipna=False) 
        dsobs_std = dsobs.std(dim='time',skipna=False)
        
        # lendo fcst 2023
        dsfcst = read_fcst(model, 2023)

        dshindline = (dshind.pr - dshind_mean.pr )*dsobs_std.pr / dshind_std.pr + dsobs_mean.pr
        # corrigindo 
        dsfcstline = (dsfcst.pr - dshind_mean.pr )*dsobs_std.pr / dshind_std.pr + dsobs_mean.pr 
        anom = (dsfcstline - dshindline.mean(dim='year', skipna=False)) / dshindline.mean(dim='year', skipna=False) *100
        
        ploting(anom, model)
        
        anom = anom.to_dataset()
        anom.to_netcdf(f'anom_annual_{model}.nc')


    os.system('cdo -O ensmean anom_annual_*.nc anom-ensmean.nc')

    ds = xr.open_dataset('anom-ensmean.nc')
    ploting(ds.pr,'Media_dos_Modelos')
    
        
