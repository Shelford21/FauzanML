# Laporan Proyek Machine Learning

### Nama : Fauzan Fadhillah Arisandi

### Nim : 211351055

### Kelas : Pagi B

## Domain Proyek

Memprediksi harga laptop merupakan upaya yang krusial dan
signifikan.Semakin kesini laptop menjadi sering digunakan karena laptop
mudah di bawa kemana-mana , tidak seperti komputer.Maka dari itu banyak
yang menginginkan untuk mempunyai laptop tetapi sebagian besar
berkeinginan untuk memiliki spek laptop yang bagus tetapi tidak bisa
memprediksi harganya.Bagian yang penting dari sebuah laptop biasanya
merek dan model, RAM, ROM, GPU, CPU, dan sebagainya. Beberapa perusahaan
laptop berkinginan untuk membandingkan harga brand nya dengan brand yang
lain , untuk mengetahui harga yang dapat dijangkau oleh pembeli sehingga
memiliki peluang besar pembeli membeli brand nya.

## Business Understanding

Dikarnakan laptop itu praktis , mudah di bawa kemana-mana, dan banyak
yang menginginkan nya.Maka di butuhkan penelitian yang dapat memprediksi
harga laptop , yang sesuai dengan spesifikasi laptop yang pembeli
inginkan sehingga pembeli memiliki gambaran pada modal harga laptop yang
di inginkan. Perusahaan membutuhkan wawasan pada harga laptop brand
lain, supaya dapat membandingkan harga laptop brand nya dengan yang lain
sehingga dapat mengetahui harga yang terjangkau untuk pembeli.

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:

-   Pembeli tidak dapat memprediksi harga dengan spek laptop yang di
    inginkan
-   Perusahaan tidak dapat mengetahui harga laptop brand lain

### Goals Dengan Solution Statements

Menjelaskan tujuan dari pernyataan masalah:

-   Membuat penelitian untuk dapat memprediksi harga laptop yang
    dinginkan pembeli (dengan regresi linier)
-   Mendapatkan wawasan pada harga laptop brand lain (dengan menganalisis data)

## Data Understanding

\[Laptop Prices
Dataset\]\[<https://www.kaggle.com/datasets/anubhavgoyal10/laptop-prices-dataset/data>)

Pertama-tama saya upload kaggle.json untuk memiliki akses pada kaggle

``` python
from google.colab import files
files.upload()
```
Selanjutnya membuat direktori dan permission pada skrip ini

``` python
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!ls ~/.kaggle
```
Lalu mendownload dataset tersebut

``` python
!kaggle datasets download -d anubhavgoyal10/laptop-prices-dataset/
```
Mengunzip dataset

```python
!mkdir laptop-prices-dataset
!unzip laptop-prices-dataset.zip -d laptop-prices-dataset
!ls laptop-prices-dataset
```

Mengimpor Library yang dibutuhkan yakni matplotlib , seaborn ,pandas dan
numpy

``` python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
```

Membaca data csv
``` python
df = pd.read_csv('laptop-prices-dataset/laptopPrice.csv')
df.head()
```
![image](https://github.com/Shelford21/FauzanML/assets/122199835/3c874ef8-84ee-43b7-b7d8-d796200e87e7)


Memeriksa berapa baris dan kolom

``` python

df.shape
```

Mengetahui deskripsi pada data

``` python

df.describe()
```
![image](https://github.com/Shelford21/FauzanML/assets/122199835/6c68556a-725e-42a5-be38-1ec018b976a6)


``` python
df.info()
```
![Uploading image.png…]()



### Variabel-variabel pada Laptop Prices Dataset adalah sebagai berikut:

-   brand : Merupakan merek laptop \[Bertipe:String ,Contoh: Asus,Lenovo\]
-   processor_brand : Merupakan merek processor \[Bertipe:String , Contoh: Intel,AMD\]
-   processor_name : Merupakan nama processor \[Bertipe:String , Contoh: Core i3, Celeron
    Dual\]
-   processor_gnrtn : Merupakan generasi processor \[Bertipe:String , Contoh: 10th,11th\]
-   ram_gb : Merupakan kapasitas memori jangka pendek \[Bertipe:String , Contoh: 4 GB, 8
    GB\]
-   ram \_type : Merupakan tipe ram \[Bertipe:String ,Contoh: DDR4,LPDDR4X\]
-   ssd : Merupakan perangkat untuk menyimpan data yang dapat membaca
    dan menulis data hingga 550 MB/s\[Bertipe:String ,Contoh: 512 GB, 1024 GB\]
-   hdd : Merupakan perangkat untuk menyimpan data yang dapat membaca
    dan menulis data hingga kecepatan rata-rata 60 MB/s \[Bertipe:String ,Contoh: 1024
    GB\]
-   os : Merupakan sistem operasi untuk mengelola memori komputer dan
    proses-proses yang berjalan di komputer \[Bertipe:String ,Contoh: Windows\]
-   os_bit : Merupakan satuan data sistem operasi \[Bertipe:String ,contoh: 32-bit,
    64-bit\]
-   graphic_card_gb : Merupakan kapasitas kartu grafis \[Bertipe:String ,Contoh: 2 GB, 4
    GB\]
-   weight : Merupakan berat laptop \[Bertipe:String ,Contoh: Casual\]
-   warranty : Merupakan garansi pada laptop \[Bertipe:String ,Contoh: 1 year , 2
    years\]
-   Touchscreen : Merupakan tipe laptop dengan layar sentuh \[Bertipe:String ,Contoh:
    Yes, No\]
-   msoffice : Merupakan microsoft office pada laptop yang tujuannya
    meliputi mengolah data \[Bertipe:String ,Contoh: Yes,No\]
-   Price : Merupakan harga laptop \[Bertipe:String ,Contoh: 57990,76990\]
-   rating : Merupakan nilai pada laptop \[Bertipe:String ,Contoh: 3 stars, 4 stars\]
-   Number of Ratings : Merupakan berapa kali dilakukan penilaian pada
    laptop \[Bertipe:String ,Contoh: 14,739\]
-   Number of Reviews : Merupakan berapa kali dilakukan ulasan pada
    laptop \[Bertipe:String ,Contoh: 100,19\]

  

Mengetahui harga laptop berdasarkan Brand

``` python

df['brand'].value_counts()
sns.barplot(data = df , x=df['brand'],y=df['Price'])
```
![image](https://github.com/Shelford21/FauzanML/assets/122199835/7818de54-3e0b-458b-a1c7-3b569cab7493)

## Data Preparation

Untuk menyiapkan data yang akhirnya akan dijadikan model .perlu di hilangkan data yang berisi null dan yang duplikasi .Lalu perlu di
lakukan konversi data kategorikal ke data numerikal yaitu Langkah - langkah
yang perlu dilakukan adalah: 
1.Memilih kolom/Atribut data yang
krusial/penting yang berguna di dalam memprediksi harga 
2.Merubah isi
kolom tipe data kategorikal tersebut ke tipe data numerikal

Menemukan duplikasi baris,lalu di hilangkan , lalu menunjukan hasil
setelah di hilangkan/di drop

``` python

df.duplicated().sum()

df= df.drop_duplicates()

df.shape
```

Memeriksa apakah ada nilai null/NaN pada dataset

``` python

df.isna().sum()
```
![image](https://github.com/Shelford21/FauzanML/assets/122199835/487890d2-11b4-46c5-9f85-ee5967c6c0e2)


## Menunjukan nilai unik pada kolom yang krusial dalam memprediksi harga

Yakni kolom
brand,processor_brand,processor_name,processor_gnrtn,ram_gb,ram_type,ssd,hdd,os,os_bit,graphic_card_gb

``` python
tdk_perlu = ['weight','warranty','rating','Number of Ratings','Number of Reviews']
df = df.drop(columns=tdk_perlu)
```

``` python
df['brand'].unique()
```

``` python
df['processor_brand'].unique()
```

``` python
df['processor_name'].unique()
```

``` python
df['processor_gnrtn'].unique()
```

``` python
df['ram_gb'].unique()
```

``` python
df['ram_type'].unique()
```

``` python
df['hdd'].unique()
```

``` python
df['ssd'].unique()
```

``` python
df['os'].unique()
```

``` python
df['os_bit'].unique()
```

``` python
df['graphic_card_gb'].unique()
```

``` python
df['Touchscreen'].unique()
```

``` python
df['msoffice'].unique()
```

Merubah Nilai kategorikal ke nilai numerikal pada kolom
brand,processor_brand,processor_name,processor_gnrtn,ram_gb,ram_type,ssd,hdd,os,os_bit,graphic_card_gb

``` python

df['brand'].replace(['ASUS', 'Lenovo','acer','Avita','HP','DELL','MSI','APPLE'],[0,1,2,3,4,5,6,7], inplace=True)
df['processor_brand'].replace(['Intel', 'AMD', 'M1'],[0,1,2], inplace=True)
df['processor_name'].replace(['Core i3', 'Core i5', 'Celeron Dual', 'Ryzen 5', 'Core i7','Core i9', 'M1', 'Pentium Quad', 'Ryzen 3', 'Ryzen 7', 'Ryzen 9'],[0,1,2,3,4,5,6,7,8,9,10], inplace=True)
df['processor_gnrtn'].replace(['10th', 'Not Available', '11th', '7th', '8th', '9th', '4th','12th'],[10,0,11,7,8,9,4,12], inplace=True)
df['ram_gb'].replace(['4 GB', '8 GB', '16 GB', '32 GB'],[4,8,16,32], inplace=True)
df['ram_type'].replace(['DDR4', 'LPDDR4', 'LPDDR4X', 'DDR5', 'DDR3', 'LPDDR3'],[0,1,2,3,4,5], inplace=True)
df['hdd'].replace(['1024 GB', '0 GB', '512 GB', '2048 GB'],[1024,0,512,2048], inplace=True)
df['ssd'].replace(['0 GB', '512 GB', '256 GB', '128 GB', '1024 GB', '2048 GB','3072 GB'],[0,512,256,128,1024,2048,3072], inplace=True)
df['os'].replace(['Windows', 'DOS', 'Mac'],[0,1,2], inplace=True)
df['os_bit'].replace(['64-bit', '32-bit'],[64,32], inplace=True)
df['graphic_card_gb'].replace(['0 GB', '2 GB', '4 GB', '6 GB', '8 GB'],[0,2,4,6,8], inplace=True)
df['Touchscreen'].replace(['No', 'Yes'],[0,1], inplace=True)
df['msoffice'].replace(['No', 'Yes'],[0,1], inplace=True)
```
Menunjukan seberapa besar kolerasi nya
``` python
corr_matrix = df.corr()
plt.figure(figsize=(10,10))
sns.heatmap(corr_matrix, annot=True)
plt.show()
```
![output](https://github.com/Shelford21/FauzanML/assets/122199835/fda573d2-3830-46b5-8d85-8895c60a3336)

Menunjukan kolom setelah di replace

``` python
df.head()
```

## Modeling

Mengimpor train_test_split dari library sklearn dan Mengimpor
LinearRegression dari library sklearn

``` python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
```

menyingkatkan LinearRegression menjadi variable lr

``` python
lr = LinearRegression()
```

setelah sebelum nya sudah ditentukan kolom/atribut yang krusial , lalu
drop kolom Price (Yakni Variable dependen) pada dataframe

``` python
X = df.drop(['Price'], axis=1)
```

Masukan kolom Price pada variable y

``` python
y = df['Price']
```

lakukan split data , untuk data train dan data test. (Disini saya
masukan data test 25% dan data train 75 %)

``` python

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
```

Membuat Regresi Linier

``` python

lr.fit(X_train,y_train)
pred = lr.predict(X_test)
score = lr.score(X_test,y_test)
print('Akurasi model regresi linier = ') ,score 
```

Dari regresi linier menghasilkan akurasi 71%

``` python
input_data = np.array([[1,1,2,10,3,3,1024,512,1,64,2,1,1]])
prediction = lr.predict(input_data)
print('Prediksi Harga Laptop: ', prediction)
```

## Evaluation

R-squared (R2) adalah ukuran statistik yang mewakili proporsi varians
suatu variabel terikat yang dijelaskan oleh variabel bebas dalam model
regresi.

![image.png](vertopal_f79290feab8f4f2cbab7e9c0afe19f53/image.png)

``` python
from sklearn.metrics import r2_score
r2_DT = r2_score(y_test, pred)  
r2_DT

print(f"Precision = {r2_DT}")
```

didapatkan score 71% , sehingga dinyatakan bahwa variable dependen
dengan variable independen itu berkolerasi tinggi

## Deployment
![image](https://github.com/Shelford21/FauzanML/assets/122199835/b937ecb4-82a6-4068-9c0d-bc3b03515314)

[linkStreamlit](https://fauzanml-ambition.streamlit.app/)
