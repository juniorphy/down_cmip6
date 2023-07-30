# -*- coding: utf-8 -*-
"""
Dictionary daily parameters for CMIP6 model.

Dictionary format:
    CMIP6_param_day = {'Model':[source_id, member_id, data_node], ... }

Parameters description(daily):
    source_id:                      name model
    member_id:                      r1i1p1f1, r1i1p1f2 ...
    data_node:                      institutions for download 

Site inf: 
    https://esgf-node.llnl.gov/search/cmip6/

Usage:
    baixar_dados_cmip6.py

Last update: 2023-06-15 
"""

CMIP6_param_day = {
'ACCESS-CM2':                                  [      'ACCESS-CM2',   'r1i1p1f1',             'esgf.nci.org.au'], # gn
'ACCESS-ESM1-5':                               [   'ACCESS-ESM1-5',   'r1i1p1f1',             'esgf.nci.org.au'], # gn
'CMCC-ESM2':                                   [       'CMCC-ESM2',   'r1i1p1f1',          'esgf-node2.cmcc.it'], # gn
'CanESM5':                                     [         'CanESM5',   'r1i1p1f1',       'crd-esgf-drc.ec.gc.ca'], # gn
'EC-Earth3':                                   [       'EC-Earth3',   'r1i1p1f1',          'esg-dn2.nsc.liu.se'], # gr
'EC-Earth3-CC':                                [    'EC-Earth3-CC',   'r1i1p1f1',                 'esgf.bsc.es'], # gr
'EC-Earth3-Veg-LR':                            ['EC-Earth3-Veg-LR',   'r1i1p1f1',      'esgf-data04.diasjp.net'], # gr
'FGOALS-g3':                                   [       'FGOALS-g3',   'r1i1p1f1',              'esg.lasg.ac.cn'], # gn
'GFDL-CM4':                                    [        'GFDL-CM4',   'r1i1p1f1',       'esgdata.gfdl.noaa.gov'], # gr1 & gr2
'GFDL-ESM4':                                   [       'GFDL-ESM4',   'r1i1p1f1',       'esgdata.gfdl.noaa.gov'], # gr1
'INM-CM4-8':                                   [       'INM-CM4-8',   'r1i1p1f1',         'esgf-data1.llnl.gov'], # gr1
'INM-CM5-0':                                   [       'INM-CM5-0',   'r1i1p1f1',         'esgf-data1.llnl.gov'], # gr1
'IPSL-CM6A-LR':                                [    'IPSL-CM6A-LR',   'r1i1p1f1',      'esgf-data04.diasjp.net'], # gr
'KACE-1-0-G':                                  [      'KACE-1-0-G',   'r1i1p1f1',   'esgf-nimscmip6.apcc21.org'], # gr
'KIOST-ESM':                                   [       'KIOST-ESM',   'r1i1p1f1',          'polaris.pknu.ac.kr'], # gr1
'MIROC6':                                      [          'MIROC6',   'r1i1p1f1',      'esgf-data02.diasjp.net'], # gn
'MPI-ESM1-2-HR':                               [   'MPI-ESM1-2-HR',   'r1i1p1f1',      'esgf-data04.diasjp.net'], # gn
'MPI-ESM1-2-LR':                               [   'MPI-ESM1-2-LR',   'r1i1p1f1',      'esgf-data04.diasjp.net'], # gn
'MRI-ESM2-0':                                  [      'MRI-ESM2-0',   'r1i1p1f1',         'esgf-data1.llnl.gov'], # gn
'NESM3':                                       [           'NESM3',   'r1i1p1f1',              'esg.lasg.ac.cn'], # gn
'NorESM2-LM':                                  [      'NorESM2-LM',   'r1i1p1f1',       'noresg.nird.sigma2.no'], # gn
'NorESM2-MM':                                  [      'NorESM2-MM',   'r1i1p1f1',       'noresg.nird.sigma2.no'], # gn
'TaiESM1':                                     [         'TaiESM1',   'r1i1p1f1',     'esgf.rcec.sinica.edu.tw'], # gn

'CNRM-CM6-1':                                  [      'CNRM-CM6-1',   'r1i1p1f2',            'esg1.umr-cnrm.fr'], # gr
'CNRM-ESM2-1':                                 [     'CNRM-ESM2-1',   'r1i1p1f2',            'esg1.umr-cnrm.fr'], # gr
'MIROC-ES2L':                                  [      'MIROC-ES2L',   'r1i1p1f2',      'esgf-data02.diasjp.net'], # gn
'UKESM1-0-LL':                                 [     'UKESM1-0-LL',   'r1i1p1f2',             'esgf.ceda.ac.uk'], # gn

'HadGEM3-GC31-LL':                             [ 'HadGEM3-GC31-LL',   'r1i1p1f3',             'esgf.ceda.ac.uk'], # gn 
}