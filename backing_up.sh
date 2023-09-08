#!/bin/bash

for EXP in 'A-hindcast' 'B-forecast' ; do 

echo $EXP gdrive

rsync -rv dcpp${EXP}/* /Volumes/GoogleDrive-106379421171705090873/My\ Drive/PROJETOS/dccp/dcpp${EXP}/.

echo $EXP HD backup

rsync -rv dcpp${EXP}/*  /Volumes/Lenovo/dcpp-decadal/dcpp${EXP}/.

done

exit 1


rsync -r dcppB-hindcast/* /Volumes/GoogleDrive-106379421171705090873/My\ Drive/PROJETOS/dccp/dcppB-hindcast/

rsync -r dcppB-hindcast/*  /Volumes/Lenovo/dcpp-decadal/dccpB-hindcast/.
