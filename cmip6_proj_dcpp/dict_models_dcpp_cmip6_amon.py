# -*- coding: utf-8 -*-
"""
Dictionary monthly parameters for CMIP6 model.

Dictionary format:
    CMIP6_dcpp_param_amom = {'Model':[source_id, data_node]}

Parameters description (CMIP6 - DCPP - monthy):
    source_id:                      name model
    data_node:                      institutions for download 

Site inf: 
    https://esgf-node.llnl.gov/search/cmip6/
    https://aims2.llnl.gov/search
Usage:
    down_cmip6_dcpp_data.py

Last update: 2025-02-05 
"""

CMIP6_dcpp_param_amon = {
#'CMCC-CM2-SR5':                                [     'CMCC-CM2-SR5',        'esgf-node2.cmcc.it'], 
#'CNRM-ESM2-1':                                 [      'CNRM-ESM2-1',          'esg1.umr-cnrm.fr'], 
#'CanESM5':                                     [          'CanESM5',     'crd-esgf-drc.ec.gc.ca'],
# 'HadGEM3-GC31-MM':                             [  'HadGEM3-GC31-MM',       'esgf-data1.llnl.gov'],
# 'EC-Earth3':                                   [        'EC-Earth3',               'esgf.bsc.es'], 
#'FGOALS-f3-L':                                 [      'FGOALS-f3-L',       'esgf-data1.llnl.gov'],
 'HadGEM3-GC31-MM':                             [  'HadGEM3-GC31-MM',       'esgf.ceda.ac.uk'],
# 'MIROC6':                                      [           'MIROC6',    'esgf-data02.diasjp.net'],
# 'MPI-ESM1-2-LR':                               [    'MPI-ESM1-2-LR',               'esgf.dwd.de'],
}
