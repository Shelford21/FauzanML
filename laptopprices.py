import pickle
import streamlit as st
import sklearn

model = pickle.load(open('laptop-prices.sav', 'rb'))


st.title('Prediksi Harga Laptop')



brand= st.number_input('Input Brand', value=None)
st.write('[brand] 0=ASUS 1=Lenovo 2=Acer 3=Avita 4=HP 5=DELL 6=MSI 7=APPLE')

processor_brand= st.number_input('Input processor_brand', value=None)
st.write('[Processor Brand] 0=Intel 1=AMD 2=M1')

processor_name= st.number_input('Input processor_name', value=None)
st.write('[Processor Name] 0=Core i3 1=Core i5 2=Celeron Dual 3=Ryzen 5 4=Core i7 5=Core i9 6=M1 7=Pentium Quad 8=Ryzen 3 9=Ryzen 7 10=Ryzen 9')

processor_gnrtn= st.number_input('Input processor_gnrtn', value=None)
st.write('[Processor Generation] 10=10th 0=Not Available 11=11th 7=7th 8=8th 9=9th 4=4th 12=12th')

ram_gb= st.number_input('Input ram_gb', value=None)
st.write('[Ram GB] 4=4 GB 8=8 GB 16=16 GB 32=32 GB')

ram_type= st.number_input('Input ram_type', value=None)
st.write('[Ram Type] 0=DDR4 1=LPDDR4 2=LPDDR4X 3=DDR5 4=DDR3 5=LPDDR3')

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
