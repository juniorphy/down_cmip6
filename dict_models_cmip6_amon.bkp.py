# -*- coding: utf-8 -*-
"""
Dictionary monthly parameters for CMIP6 model.

Dictionary format:
    CMIP6_param_amom = {'Model':[source_id, member_id, data_node], ... }

Parameters description(daily):
    source_id:                      name model
    member_id:                      r1i1p1f1, r1i1p1f2 ...
    data_node:                      institutions for download 

Site inf: 
    https://esgf-node.llnl.gov/search/cmip6/

Usage:
    baixar_dados_cmip6.py

Last update: 2023-07-06 
"""

CMIP6_param_amom = {
'ACCESS-CM2':                                  [      'ACCESS-CM2',   'r1i1p1f1',             'esgf.nci.org.au'], # gn
'ACCESS-ESM1-5':                               [   'ACCESS-ESM1-5',   'r1i1p1f1',             'esgf.nci.org.au'], # gn
'AWI-CM-1-1-MR':                               [   'AWI-CM-1-1-MR',   'r1i1p1f1',               'esgf3.dkrz.de'], # gn
'BCC-CSM2-MR':                                 [     'BCC-CSM2-MR',   'r1i1p1f1',              'aims3.llnl.gov'], # gn
'CAS-ESM2-0':                                  [      'CAS-ESM2-0',   'r1i1p1f1',              'esg.lasg.ac.cn'], # gn
'CIESM':                                       [           'CIESM',   'r1i1p1f1',   'cmip.dess.tsinghua.edu.cn'], # gr
'CMCC-ESM2':                                   [       'CMCC-ESM2',   'r1i1p1f1',          'esgf-node2.cmcc.it'], # gn
'CanESM5':                                     [         'CanESM5',   'r1i1p1f1',       'crd-esgf-drc.ec.gc.ca'], # gn
'CanESM5-1':                                   [       'CanESM5-1',   'r1i1p1f1',       'crd-esgf-drc.ec.gc.ca'], # gn
'EC-Earth3':                                   [       'EC-Earth3',   'r1i1p1f1',          'esg-dn2.nsc.liu.se'], # gr
'EC-Earth3-CC':                                [    'EC-Earth3-CC',   'r1i1p1f1',                 'esgf.bsc.es'], # gr
'EC-Earth3-Veg':                               [   'EC-Earth3-Veg',   'r1i1p1f1',          'esg-dn1.nsc.liu.se'], # gr
'EC-Earth3-Veg-LR':                            ['EC-Earth3-Veg-LR',   'r1i1p1f1',          'esg-dn1.nsc.liu.se'], # gr
'FGOALS-g3':                                   [       'FGOALS-g3',   'r1i1p1f1',              'esg.lasg.ac.cn'], # gn
'FIO-ESM-2-0':                                 [     'FIO-ESM-2-0',   'r1i1p1f1',             'cmip.fio.org.cn'], # gn
'GFDL-ESM4':                                   [       'GFDL-ESM4',   'r1i1p1f1',       'esgdata.gfdl.noaa.gov'], # gr1
'INM-CM4-8':                                   [       'INM-CM4-8',   'r1i1p1f1',               'esgf3.dkrz.de'], # gr1
'INM-CM5-0':                                   [       'INM-CM5-0',   'r1i1p1f1',               'esgf3.dkrz.de'], # gr1
'IPSL-CM6A-LR':                                [    'IPSL-CM6A-LR',   'r1i1p1f1',      'esgf-data04.diasjp.net'], # gr
'MIROC6':                                      [          'MIROC6',   'r1i1p1f1',      'esgf-data02.diasjp.net'], # gn
'MPI-ESM1-2-HR':                               [   'MPI-ESM1-2-HR',   'r1i1p1f1',               'esgf3.dkrz.de'], # gn
'MPI-ESM1-2-LR':                               [   'MPI-ESM1-2-LR',   'r1i1p1f1',               'esgf3.dkrz.de'], # gn
'MRI-ESM2-0':                                  [      'MRI-ESM2-0',   'r1i1p1f1',      'esgf-data03.diasjp.net'], # gn
'NESM3':                                       [           'NESM3',   'r1i1p1f1',              'esg.lasg.ac.cn'], # gn

'CNRM-CM6-1':                                  [      'CNRM-CM6-1',   'r1i1p1f2',            'esg1.umr-cnrm.fr'], # gr
'CNRM-CM6-1-HR':                               [   'CNRM-CM6-1-HR',   'r1i1p1f2',            'esg1.umr-cnrm.fr'], # gr
'CNRM-ESM2-1':                                 [     'CNRM-ESM2-1',   'r1i1p1f2',            'esg1.umr-cnrm.fr'], # gr
'GISS-E2-1-G':                                 [     'GISS-E2-1-G',   'r1i1p1f2',      'dpesgf03.nccs.nasa.gov'], # gn
'GISS-E2-1-H':                                 [     'GISS-E2-1-H',   'r1i1p1f2',      'dpesgf03.nccs.nasa.gov'], # gn
'MIROC-ES2L':                                  [      'MIROC-ES2L',   'r1i1p1f2',      'esgf-data02.diasjp.net'], # gn
'UKESM1-0-LL':                                 [     'UKESM1-0-LL',   'r1i1p1f2',             'esgf.ceda.ac.uk'], # gn

'HadGEM3-GC31-LL':                             [ 'HadGEM3-GC31-LL',   'r1i1p1f3',             'esgf.ceda.ac.uk'], # gn 
}

