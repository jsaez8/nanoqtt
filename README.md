# qcodes_qtt_extension
This is an extension of qtt where I develop my functions and examples

# Installation
1. conda create -n qcodes_qtt python=3.7
2. conda activate qcodes_qtt
3. pip install -e . -r requirements_lock.txt
4. conda install -c conda-forge geos

For being able to install qtt I had to modify some versions of the libraries. 
* dataclass==0.6
* qcodes==0.21.00

Also for using the Fast Duck it is needed to copy the folder called "IST_devices" in the path where qcodes is, for example: C:\Users\Nanoelectronics\Anaconda3\envs\qtt_dev_Jaime\Lib\site-packages\qcodes\instrument_drivers

For the new driver of the UHFLI: pip install zhinst-qcodes

# Initialize measurement notebook
(base) C:\Users\Nanoelectronics>K:

(base) K:\>cd Measurement

(base) K:\Measurement>cd Jaime

(base) K:\Measurement\Jaime>cd 20210302_10721_S22_Bottom_Left

(base) K:\Measurement\Jaime\20210302_10721_S22_Bottom_Left>conda activate qtt_dev_Jaime
