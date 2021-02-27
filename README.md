# qcodes_qtt_extension
This is an extension of qtt where I develop my functions and examples

# Installation
1. conda create -n qcodes_qtt python=3.7
2. conda activate qcodes_qtt
3. pip install -e . -r requirements_lock.txt
4. conda install -c conda=forge geos

For being able to install qtt I had to modify some versions of the libraries. 
* dataclass==0.6
* qcodes==0.21.00

Also for using the Fast Duck it is needed to copy the folder called "IST_devices" in the path where qcodes is, for example: C:\Users\Nanoelectronics\Anaconda3\envs\qtt_dev_Jaime\Lib\site-packages\qcodes\instrument_drivers
