## Steps for starting a spark cluster with Weather Data.

1. Start a cluster using `spark-notebook/run.py`
2. When the cluster is up, start a jupyter notebook.
3. From the jupyter console, start a terminal.
4. go to the main working directory: `cd /mnt/workspace/`
5. `ls` should show one file: `FilesIO.ipynb`
6. Clone your code directory (here we are cloning the main public repo):  
`git clone https://github.com/yoavfreund/Public-DSC291.git`
7. Go back to the Files console and open the notebook `aws-jupyter-scripts/FilesIO-for-DSC291.ipynb`
8. Executing the commands in this notebook will load the data into dataframes and will copy the meta-information files into the directory.
9. Use `sc.stop` before continuing to other notebooks.
10. Go to the directory `notebooks/Section2-PCA/PCA/data_preparation/` to start working with the dataframes.
11. Remember that you need to add the commands to load the dataframes (given at the end of `FilesIO-for-DSC291.ipynb` to the start of each of those notebooks.



## (4) Move files around local filesystem, HDFS and S3

As described in `s3helper.help()`, there are five methods for file transfers:

1. `s3helper.s3_to_hdfs(<s3_directory_path>, <HDFS_directory_path>)`
2. `s3helper.hdfs_to_s3(<HDFS_directory_path>, <s3_directory_path>)`
3. `s3helper.s3_to_local(<s3_file_path>, <local_file_path>)`
4. `s3helper.local_to_s3(<local_file_path>, <s3_directory_path>)`
5. `s3helper.local_to_hdfs(<local_dir_path>, <HDFS_dir_path>)`