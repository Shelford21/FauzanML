import pickle
import streamlit as st

model = pickle.load(open('laptop-prices.sav', 'rb'))


st.title('Prediksi Harga Laptop')


brand = st.selectbox('Pilih Brand', ['ASUS', 'Lenovo','Acer','Avita','HP','DELL','MSI','APPLE'])
if brand == 'ASUS':
    brand = 0
elif brand == 'Lenovo':
    brand = 1
elif brand == 'Acer':
    brand = 2
elif brand == 'Avita':
    brand = 3
elif brand == 'HP':
    brand = 4
elif brand == 'DELL':
    brand = 5
elif brand == 'MSI':
    brand = 6
elif brand == 'APPLE':
    brand = 7

processor_brand = st.selectbox('Pilih Processor Brand', ['Intel', 'AMD','M1'])
if processor_brand == 'Intel':
    brand = 0
elif processor_brand == 'AMD':
    brand = 1
elif processor_brand == 'M1':
    brand = 2

processor_name = st.selectbox('Pilih Nama Processor', ['Core i3', 'Core i5','Celeron Dual','Ryzen 5','Core i7','Core i9','M1','Pentium Quad','Ryzen 3','Ryzen 7','Ryzen 9'])
if processor_name == 'Core i3':
    processor_name = 0
elif processor_name == 'Core i5':
    processor_name = 1
elif processor_name == 'Celeron Dual':
    processor_name = 2
elif processor_name == 'Ryzen 5':
    processor_name = 3
elif processor_name == 'Core i7':
    processor_name = 4
elif processor_name == 'Core i9':
    processor_name = 5
elif processor_name == 'M1':
    processor_name = 6
elif processor_name == 'Pentium Quad':
    processor_name = 7
elif processor_name == 'Ryzen 3':
    processor_name = 8
elif processor_name == 'Ryzen 7':
    processor_name = 9
elif processor_name == 'Ryzen 9':
    processor_name = 10

processor_gnrtn = st.selectbox('Pilih processor_gnrtn', ['Not Available', '10th','11th','7th','8th','9th','4th','12th'])
if processor_gnrtn == 'Not Available':
    processor_gnrtn = 0
elif processor_gnrtn == '10th':
    processor_gnrtn = 10
elif processor_gnrtn == '11th':
    processor_gnrtn = 11
elif processor_gnrtn == '7th':
    processor_gnrtn = 7
elif processor_gnrtn == '8th':
    processor_gnrtn = 8
elif processor_gnrtn == '9th':
    processor_gnrtn = 9
elif processor_gnrtn == '4th':
    processor_gnrtn = 4
elif processor_gnrtn == '12th':
    processor_gnrtn = 12

ram_gb = st.selectbox('Pilih Kapasitas RAM', ['4 GB','8 GB' , '16 GB' ,'32 GB'])
if ram_gb == '4 GB':
    ram_gb = 4
elif ram_gb == '8 GB':
    ram_gb = 8
elif ram_gb == '16 GB':
    ram_gb = 16
elif ram_gb == '32 GB':
    ram_gb = 32

ram_type = st.selectbox('Pilih Tipe RAM', ['DDR4','LPDDR4','LPDDR4X','DDR5','DDR3','LPDDR3'])
if ram_type == 'DDR4':
    ram_type = 0
elif ram_type == 'LPDDR4':
    ram_type = 1
elif ram_type == 'LPDDR4X':
    ram_type = 2
elif ram_type == 'DDR5':
    ram_type = 3
elif ram_type == 'DDR3':
    ram_type = 4
elif ram_type == 'LPDDR3':
    ram_type = 5
    
hdd= st.number_input('Input hddd', value=None)
st.write('[ssd] 1024=1024 GB    0=0 GB  512=512 GB  2048=2048 GB')
         
ssd= st.number_input('Input ssd', value=None)
st.write('[ssd] 1024=1024 GB    0=0 GB  512=512 GB  2048=2048 GB 256=256 GB 128=128 GB  2048=2048 GB    3072=3072 GB')
         
os= st.number_input('Input os', value=None)
st.write('[os] 0=Windows 1=DOS 2=Mac')

os_bit= st.number_input('Input os_bit', value=None)
st.write('[os-bit] 64=64-bit 32=32-bit')

graphic_card_gb= st.number_input('Input graphic_car_gb', value=None)
st.write('[Graphic Card gb] 0=0 GB 2=2 GB 4=4 GB 6=6 GB 8=8 GB')

Touchscreen= st.number_input('Input Touchscreen', value=None)
st.write('[Touchscreen] 0=No 1=Yes')

msoffice= st.number_input('Input msoffice', value=None)
st.write('[Touchscreen] 0=No 1=Yes')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[brand,processor_brand,processor_name,processor_gnrtn,ram_gb,ram_type,hdd,ssd,os,os_bit,graphic_card_gb,Touchscreen,msoffice]]
    )
    st.write('Prediksi Harga Laptop (Rupiah): ', predict*191)
