
from pyesgf.search import SearchConnection
import os
import pandas as pd
import requests
from tqdm import tqdm
from pathlib import Path 
from dict_models_cmip6_amon import CMIP6_dcpp_param_amon #dicionario modelos diarios
import argparse


parser = argparse.ArgumentParser(description='')
parser.add_argument('--subexp_year', type=int,
                    help='Sub Exp Year')
parser.add_argument('--exp', type=str, default='dcppA-hindcast',
                    help='Experiment of CMIP6')

args = parser.parse_args()
subexp_year = args.subexp_year
experiment = args.exp

def set_param_dcpp(expe,subexp):
    proj= 'CMIP6' 
    source= CMIP6_dcpp_param_amon[model][0]
    experiment=expe # dcppA-hindcast', #, 
    sub_experiment=f's{subexp}'
    variable= 'pr'#, tas'
    table= 'Amon'
    #member_id= CMIP6_param_day[model][1],
    node= CMIP6_dcpp_param_amon[model][1]
    return proj, source, experiment, sub_experiment, variable, table, node 

def get_param_dcpp(filename):
    print(filename)
    modelo = filename.split('_')[2] 
    cenario = filename.split('_')[3]
    variavel = filename.split('_')[0]
    id = filename.split('_')[4]
    frequency = filename.split('_')[1]
    subexp = filename.split('_')[4][0:5]
    
    return modelo, cenario, variavel, id, frequency, subexp

def download(url, filename,experiment):
    print("Downloading ", filename)
    modelo, cenario, variavel, id, frequency,subexp = get_param_dcpp(filename)
    
    r = requests.get(url, stream=True)
    total_size, block_size = int(r.headers.get('content-length', 0)), 1024
    
    # Check if the request was successful (status code 200 indicates success)
    if r.status_code == 200:
        filepath = Path(f'{experiment}/{modelo}/{frequency}/{variavel}/{subexp}/{filename}')
        filepath.parent.mkdir(parents=True, exist_ok=True) 
        with open(filepath, 'wb') as f:
            for data in tqdm(r.iter_content(block_size),
                            total=total_size//block_size,
                            unit='KiB', unit_scale=True):
                f.write(data)
        print(f'File {filename} downloaded successfully.')
    else:
        print('Failed to download the file.')
    # if total_size != 0 and os.path.getsize(filepath) != total_size:
    #     print("Downloaded size does not match expected size!\n",
    #           "FYI, the status code was ", r.status_code)


if __name__ == '__main__': 

    os.environ["ESGF_PYCLIENT_NO_FACETS_STAR_WARNING"] = "on"

    conn = SearchConnection('https://esgf-node.llnl.gov/esg-search', distrib=True)
    
    #experiment='dcppB-forecast' #'dcppA-hindcast' #dcppB-forecast'

    for model in CMIP6_dcpp_param_amon.keys():
        if subexp_year == None:
            print("---------------------------------------")
            
            print("Error!! give a year for subexp_year!! ")
            
            print("Usage: python3 down_cmip6_data.py --subexp_year=YYYY")
            
            print("---------------------------------------")
            exit() 
        for subexp in range(subexp_year,subexp_year+1):
            print()
            print('Experiment ',experiment,'\n', 'Model ', model,'\n', 'SubExperiment ', f's{subexp}')
            '''
            query = conn.new_context(
                latest = True,
                project= 'CMIP6',
                source_id= CMIP6_param_day[model][0],
                experiment_id= 'historical,ssp245, ssp585',
                variable_id= 'pr, tas, tasmax, tasmin',
                table_id= 'day',
                member_id= CMIP6_param_day[model][1],
                data_node= CMIP6_param_day[model][2])
            '''
            proj, source, experiment, sub_experiment, variable, table, node = set_param_dcpp(experiment, subexp_year)
            # print(proj, source, experiment, sub_experiment, variable, table, node)
            
            query = conn.new_context(
            latest = True,
            project = proj,
            source_id = source,
            experiment_id = experiment, #experiment,# dcppA-hindcast', #, 
            sub_experiment_id = sub_experiment,
            variable_id = variable,
            table_id= table,
            #member_id= CMIP6_param_day[model][1],
            data_node = node)
                            
            results = query.search()
            #test if model exists for a given subexperiment.
            if len(results) < 1:
                print("Error to get files or Doesn't exist file in this subexperiment!")
                print()
                continue 

            files = list(map(lambda f : {'filename': f.filename, 'url': f.download_url}, results[0].file_context().search()))
            #print(files)
            files2 = list(map(lambda f : {'filename': f.filename, 'url': f.download_url},
                                        results[1].file_context().search()))
            #print(files2)
            
            files.extend(files2)

            for i in range(2, len(results)):
                files.extend(list(map(lambda f : {'filename': f.filename, 'url': f.download_url},
                                        results[i].file_context().search())))

            files = pd.DataFrame.from_dict(files)
            #print(files['filename'].iloc[0])
            #discard = ["_210101-"]
            #files=files[~files.filename.str.contains('|'.join(discard))]
            #print(files)
            
            for index, row in files.iterrows():
                #print(f'{experiment}/{model}/{table}/{variable}/{sub_experiment}/{row.filename}')
                if os.path.isfile(f'{experiment}/{model}/{table}/{variable}/{sub_experiment}/{row.filename}'):
                    print("File exists. Skipping.")
                else:
                    download(row.url, row.filename, experiment)

        #exit() 
