#!/usr/bin/bash
def get_weather_data_for_state(
    state='NY',
    data_dir='../Data/Weather',
    tarname=state+'.tgz',
    parquet=state+'.parquet'
    ):
'''
string arguments for state may be any one of AB,AL,AR,AZ,BC,CA,CO,CT,DC,DE,FL,GA,IA,ID,IL,IN,KS,KY,LA,MA,MB,
MD,ME,MI,MN,MO,MS,MT,NaN,NB,NC,ND,NE,NH,NJ,NM,NV,NY,OH,OK,ON,OR,PA,QC,RI,SC,SD,SK,TN,TX,UT,VA,VT,WA,WI,WV,WY
'''
%mkdir -p $data_dir
!rm -rf $data_dir/$tarname

command="curl https://mas-dse-open.s3.amazonaws.com/Weather/by_state_2/%s > %s/%s"%(tarname,data_dir,tarname)
print(command)
!$command
!ls -lh $data_dir/$tarname

cur_dir,=!pwd
%cd $data_dir
!tar -xzf $tarname
!du ./$parquet
%cd $cur_dir