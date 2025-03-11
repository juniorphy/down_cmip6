from pyesgf.search import SearchConnection
import os
import pandas as pd
import requests
from tqdm import tqdm
from pathlib import Path
from dict_models_cmip6_proj_amon_day import CMIP6_param_amon, CMIP6_param_daily #dicionario modelos diarios
import argparse

parser = argparse.ArgumentParser(description='')

parser.add_argument('--exp', type=str, default='historical',
                    help='Experiment of CMIP6, historical, ssp245, ssp585 etc')
parser.add_argument('--freq', type=str, default='day',
                    help='Frequency data: Amon or day')
parser.add_argument('--variable', type=str, default='pr',
                    help='Cmip6 variable name: pr, tas, tasmax, tasmin, hursmin, sfcWindmax, rlds, sfcWind')

args = parser.parse_args()
frequency = args.freq
experiment = args.exp
variable=args.variable

def set_param(expe,frequency,var):
    proj= 'CMIP6'
    source= dicionario[model][0]
    experiment=expe # 'ssp245' 'ssp585'
    variable=var #'pr, tas, rhum, sfcWindmax, hursmin'
    table= frequency
    variant_label = dicionario[model][1]
    node= dicionario[model][2]
    return proj, source, experiment, variable, table,  variant_label, node

def get_param(filename):
    print(filename)
    modelo = filename.split('_')[2]
    cenario = filename.split('_')[3]
    variavel = filename.split('_')[0]
    id = filename.split('_')[4]
    frequency = filename.split('_')[1]

    return modelo, cenario, variavel, id, frequency

def download(url, filename,experiment):
    print("Downloading ", filename)
    modelo, cenario, variavel, id, frequency  = get_param(filename)

    r = requests.get(url, stream=True)
    total_size, block_size = int(r.headers.get('content-length', 0)), 1024

    # Check if the request was successful (status code 200 indicates success)
    if r.status_code == 200:
        filepath = Path(f'data/{experiment}/{modelo}/{frequency}/{variavel}/{filename}')
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'wb') as f:
            for data in tqdm(r.iter_content(block_size),
                            total=total_size//block_size,
                            unit='KiB', unit_scale=True):
                f.write(data)
        print(f'File {filename} downloaded successfully.')
    else:
        print('Failed to download the file.')

if __name__ == '__main__':

    os.environ["ESGF_PYCLIENT_NO_FACETS_STAR_WARNING"] = "on"

    conn = SearchConnection('https://esgf-node.llnl.gov/esg-search', distrib=True)

    if frequency == 'Amon':
        dicionario = CMIP6_param_amon
    if frequency == 'day':
        dicionario = CMIP6_param_daily

    for im, model in enumerate(dicionario.keys()):
        print()
        print(f"{im+1:02d}")
        print('Experiment ', experiment,'\n' 'Model ', model,'\n' 'Frequency ', frequency )
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
        proj, source, experiment, variable, table, variant, node = set_param (experiment, frequency, variable)
        #print(proj, source, experiment, variable, table, variant, node)
        print('Node', node)
        query = conn.new_context(
        latest = True,
        project = proj,
        source_id = source,
        experiment_id = experiment, #experiment,# dcppA-hindcast', #,
        variable_id = variable,
        table_id= table,
        variant_label= variant,
        data_node = node)

        results = query.search()

        #test if model exists for a given subexperiment.
        if len(results) < 1:
            print("Error to get files or Doesn't exist file in this experiment!")
            print()
            continue

        files = list(map(lambda f : {'filename': f.filename, 'url': f.download_url}, results[0].file_context().search()))
        if len(results) == 2:

            files2 = list(map(lambda f : {'filename': f.filename, 'url': f.download_url},
                                    results[1].file_context().search()))
            files.extend(files2)

        for i in range(2, len(results)):
            files.extend(list(map(lambda f : {'filename': f.filename, 'url': f.download_url},
                                    results[i].file_context().search())))

        files = pd.DataFrame.from_dict(files)

        for index, row in files.iterrows():
            if os.path.isfile(f'data/{experiment}/{model}/{table}/{variable}/{row.filename}'):
                print(f"File {row.filename} exists! Skipping..")
            else:
                try:
                    download(row.url, row.filename, experiment)
                except:
                    print(model, node, 'something wrong')
                    break
        #exit()
