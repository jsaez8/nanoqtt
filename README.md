# qcodes_qtt_extension
This is an extension of qtt where I develop my functions and examples

# Installation
Make sure that you have already installed Anaconda in your computer. You can download it from here https://www.anaconda.com/products/individual

Also you need to download qtt library and save it in the desired path, for example: C:\\Users\YourUserName\qtt

Type the following instructions in the Anaconda Prompt:
1. conda create -n qcodes_qtt python=3.7
2. conda activate qcodes_qtt

3. Change the directory to the path where you saved qtt. For example: cd C:\\Users\YourUserName\qtt
4. pip install -e . -r requirements_lock.txt
5. conda install -c conda-forge geos

For being able to install qtt I had to modify some versions of the libraries. 
* dataclass==0.6
* qcodes==0.21.00

Also for using the Fast Duck it is needed to copy the folder called "IST_devices" in the path where qcodes is, for example: C:\Users\Nanoelectronics\Anaconda3\envs\qtt_dev_Jaime\Lib\site-packages\qcodes\instrument_drivers

# Initialize measurement notebook
(base) C:\Users\Nanoelectronics>K:

(base) K:\>cd Measurement

(base) K:\Measurement>cd Jaime

(base) K:\Measurement\Jaime>cd 20210302_10721_S22_Bottom_Left

(base) K:\Measurement\Jaime\20210302_10721_S22_Bottom_Left>conda activate qtt_dev_Jaime
