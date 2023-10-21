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

### Goals

Menjelaskan tujuan dari pernyataan masalah:

-   Membuat penelitian untuk dapat memprediksi harga laptop yang
    dinginkan pembeli
-   Mendapatkan wawasan pada harga laptop brand lain

## Data Understanding

\[Laptop Prices
Dataset\]\[<https://www.kaggle.com/datasets/anubhavgoyal10/laptop-prices-dataset/data>)
:::

::: {.cell .markdown}
Mengimpor Library yang dibutuhkan yakni matplotlib , seaborn ,pandas dan
numpy
:::

::: {.cell .code execution_count="56"}
``` python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
```
:::

::: {.cell .markdown}
membaca data csv
:::

::: {.cell .code execution_count="23"}
``` python
df = pd.read_csv('laptopPrices/laptopPrice.csv')
df.head()
```

::: {.output .execute_result execution_count="23"}
```{=html}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>brand</th>
      <th>processor_brand</th>
      <th>processor_name</th>
      <th>processor_gnrtn</th>
      <th>ram_gb</th>
      <th>ram_type</th>
      <th>ssd</th>
      <th>hdd</th>
      <th>os</th>
      <th>os_bit</th>
      <th>graphic_card_gb</th>
      <th>weight</th>
      <th>warranty</th>
      <th>Touchscreen</th>
      <th>msoffice</th>
      <th>Price</th>
      <th>rating</th>
      <th>Number of Ratings</th>
      <th>Number of Reviews</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ASUS</td>
      <td>Intel</td>
      <td>Core i3</td>
      <td>10th</td>
      <td>4 GB</td>
      <td>DDR4</td>
      <td>0 GB</td>
      <td>1024 GB</td>
      <td>Windows</td>
      <td>64-bit</td>
      <td>0 GB</td>
      <td>Casual</td>
      <td>No warranty</td>
      <td>No</td>
      <td>No</td>
      <td>34649</td>
      <td>2 stars</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Lenovo</td>
      <td>Intel</td>
      <td>Core i3</td>
      <td>10th</td>
      <td>4 GB</td>
      <td>DDR4</td>
      <td>0 GB</td>
      <td>1024 GB</td>
      <td>Windows</td>
      <td>64-bit</td>
      <td>0 GB</td>
      <td>Casual</td>
      <td>No warranty</td>
      <td>No</td>
      <td>No</td>
      <td>38999</td>
      <td>3 stars</td>
      <td>65</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Lenovo</td>
      <td>Intel</td>
      <td>Core i3</td>
      <td>10th</td>
      <td>4 GB</td>
      <td>DDR4</td>
      <td>0 GB</td>
      <td>1024 GB</td>
      <td>Windows</td>
      <td>64-bit</td>
      <td>0 GB</td>
      <td>Casual</td>
      <td>No warranty</td>
      <td>No</td>
      <td>No</td>
      <td>39999</td>
      <td>3 stars</td>
      <td>8</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ASUS</td>
      <td>Intel</td>
      <td>Core i5</td>
      <td>10th</td>
      <td>8 GB</td>
      <td>DDR4</td>
      <td>512 GB</td>
      <td>0 GB</td>
      <td>Windows</td>
      <td>32-bit</td>
      <td>2 GB</td>
      <td>Casual</td>
      <td>No warranty</td>
      <td>No</td>
      <td>No</td>
      <td>69990</td>
      <td>3 stars</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ASUS</td>
      <td>Intel</td>
      <td>Celeron Dual</td>
      <td>Not Available</td>
      <td>4 GB</td>
      <td>DDR4</td>
      <td>0 GB</td>
      <td>512 GB</td>
      <td>Windows</td>
      <td>64-bit</td>
      <td>0 GB</td>
      <td>Casual</td>
      <td>No warranty</td>
      <td>No</td>
      <td>No</td>
      <td>26990</td>
      <td>3 stars</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>
```
:::
:::

::: {.cell .markdown}
Memeriksa berapa baris dan kolom
:::

::: {.cell .code execution_count="24"}
``` python

df.shape
```

::: {.output .execute_result execution_count="24"}
    (823, 19)
:::
:::

::: {.cell .markdown}
memeriksa apakah ada nilai null/NaN pada dataset
:::

::: {.cell .code execution_count="25"}
``` python

df.isna().sum()
```

::: {.output .execute_result execution_count="25"}
    brand                0
    processor_brand      0
    processor_name       0
    processor_gnrtn      0
    ram_gb               0
    ram_type             0
    ssd                  0
    hdd                  0
    os                   0
    os_bit               0
    graphic_card_gb      0
    weight               0
    warranty             0
    Touchscreen          0
    msoffice             0
    Price                0
    rating               0
    Number of Ratings    0
    Number of Reviews    0
    dtype: int64
:::
:::

::: {.cell .markdown}
Mengetahui deskripsi pada data
:::

::: {.cell .code execution_count="26"}
``` python

df.describe()
```

::: {.output .execute_result execution_count="26"}
```{=html}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
      <th>Number of Ratings</th>
      <th>Number of Reviews</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>823.000000</td>
      <td>823.000000</td>
      <td>823.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>76745.177400</td>
      <td>315.301337</td>
      <td>37.609964</td>
    </tr>
    <tr>
      <th>std</th>
      <td>45101.790525</td>
      <td>1047.382654</td>
      <td>121.728017</td>
    </tr>
    <tr>
      <th>min</th>
      <td>16990.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>46095.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>64990.000000</td>
      <td>17.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>89636.000000</td>
      <td>139.500000</td>
      <td>18.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>441990.000000</td>
      <td>15279.000000</td>
      <td>1947.000000</td>
    </tr>
  </tbody>
</table>
</div>
```
:::
:::

::: {.cell .code execution_count="27"}
``` python
df.info()
```

::: {.output .stream .stdout}
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 823 entries, 0 to 822
    Data columns (total 19 columns):
     #   Column             Non-Null Count  Dtype 
    ---  ------             --------------  ----- 
     0   brand              823 non-null    object
     1   processor_brand    823 non-null    object
     2   processor_name     823 non-null    object
     3   processor_gnrtn    823 non-null    object
     4   ram_gb             823 non-null    object
     5   ram_type           823 non-null    object
     6   ssd                823 non-null    object
     7   hdd                823 non-null    object
     8   os                 823 non-null    object
     9   os_bit             823 non-null    object
     10  graphic_card_gb    823 non-null    object
     11  weight             823 non-null    object
     12  warranty           823 non-null    object
     13  Touchscreen        823 non-null    object
     14  msoffice           823 non-null    object
     15  Price              823 non-null    int64 
     16  rating             823 non-null    object
     17  Number of Ratings  823 non-null    int64 
     18  Number of Reviews  823 non-null    int64 
    dtypes: int64(3), object(16)
    memory usage: 122.3+ KB
:::
:::

::: {.cell .markdown}
Menemukan duplikasi baris,lalu di hilangkan , lalu menunjukan hasil
setelah di hilangkan/di drop
:::

::: {.cell .code execution_count="28"}
``` python

df.duplicated().sum()

df= df.drop_duplicates()

df.shape
```

::: {.output .execute_result execution_count="28"}
    (802, 19)
:::
:::

::: {.cell .markdown}
### Variabel-variabel pada Laptop Prices Dataset adalah sebagai berikut:

-   brand : Merupakan merek laptop \[Contoh: Asus,Lenovo\]
-   processor_brand : Merupakan merek processor \[Contoh: Intel,AMD\]
-   processor_name : Merupakan nama processor \[Contoh: Core i3, Celeron
    Dual\]
-   processor_gnrtn : Merupakan generasi processor \[Contoh: 10th,11th\]
-   ram_gb : Merupakan kapasitas memori jangka pendek \[Contoh: 4 GB, 8
    GB\]
-   ram \_type : Merupakan tipe ram \[Contoh: DDR4,LPDDR4X\]
-   ssd : Merupakan perangkat untuk menyimpan data yang dapat membaca
    dan menulis data hingga 550 MB/s\[Contoh: 512 GB, 1024 GB\]
-   hdd : Merupakan perangkat untuk menyimpan data yang dapat membaca
    dan menulis data hingga kecepatan rata-rata 60 MB/s \[Contoh: 1024
    GB\]
-   os : Merupakan sistem operasi untuk mengelola memori komputer dan
    proses-proses yang berjalan di komputer \[Contoh: Windows\]
-   os_bit : Merupakan satuan data sistem operasi \[contoh: 32-bit,
    64-bit\]
-   graphic_card_gb : Merupakan kapasitas kartu grafis \[Contoh: 2 GB, 4
    GB\]
-   weight : Merupakan berat laptop \[Contoh: Casual\]
-   warranty : Merupakan garansi pada laptop \[Contoh: 1 year , 2
    years\]
-   Touchscreen : Merupakan tipe laptop dengan layar sentuh \[Contoh:
    Yes, No\]
-   msoffice : Merupakan microsoft office pada laptop yang tujuannya
    meliputi mengolah data \[Contoh: Yes,No\]
-   Price : Merupakan harga laptop \[Contoh: 57990,76990\]
-   rating : Merupakan nilai pada laptop \[Contoh: 3 stars, 4 stars\]
-   Number of Ratings : Merupakan berapa kali dilakukan penilaian pada
    laptop \[Contoh: 14,739\]
-   Number of Reviews : Merupakan berapa kali dilakukan ulasan pada
    laptop \[Contoh: 100,19\]
:::

::: {.cell .markdown}
Mengetahui harga laptop berdasarkan Brand
:::

::: {.cell .code execution_count="29"}
``` python

df['brand'].value_counts()
sns.barplot(data = df , x=df['brand'],y=df['Price'])
```

::: {.output .execute_result execution_count="29"}
    <AxesSubplot: xlabel='brand', ylabel='Price'>
:::

::: {.output .display_data}
![](vertopal_f8772d8520514154bb439925444862af/d87e448fe15e4b05c7d851b9a632405d61c5ef90.png)
:::
:::

::: {.cell .markdown}
## Data Preparation

Untuk menyiapkan data yang akhirnya akan dijadikan model . perlu di
lakukan konversi data kategorikal ke data numerikal. Langkah - langkah
yang perlu dilakukan adalah: 1.Memilih kolom/Atribut data yang
krusial/penting yang berguna di dalam memprediksi harga 2.Merubah isi
kolom tipe data kategorikal tersebut ke tipe data numerikal
:::

::: {.cell .markdown}
## Menunjukan nilai unik pada kolom yang krusial dalam memprediksi harga

Yakni kolom
brand,processor_brand,processor_name,processor_gnrtn,ram_gb,ram_type,ssd,hdd,os,os_bit,graphic_card_gb
:::

::: {.cell .code execution_count="30"}
``` python
tdk_perlu = ['weight','warranty','rating','Number of Ratings','Number of Reviews']
df = df.drop(columns=tdk_perlu)
```
:::

::: {.cell .code execution_count="31"}
``` python
df['brand'].unique()
```

::: {.output .execute_result execution_count="31"}
    array(['ASUS', 'Lenovo', 'acer', 'Avita', 'HP', 'DELL', 'MSI', 'APPLE'],
          dtype=object)
:::
:::

::: {.cell .code execution_count="32"}
``` python
df['processor_brand'].unique()
```

::: {.output .execute_result execution_count="32"}
    array(['Intel', 'AMD', 'M1'], dtype=object)
:::
:::

::: {.cell .code execution_count="33"}
``` python
df['processor_name'].unique()
```

::: {.output .execute_result execution_count="33"}
    array(['Core i3', 'Core i5', 'Celeron Dual', 'Ryzen 5', 'Core i7',
           'Core i9', 'M1', 'Pentium Quad', 'Ryzen 3', 'Ryzen 7', 'Ryzen 9'],
          dtype=object)
:::
:::

::: {.cell .code execution_count="34"}
``` python
df['processor_gnrtn'].unique()
```

::: {.output .execute_result execution_count="34"}
    array(['10th', 'Not Available', '11th', '7th', '8th', '9th', '4th',
           '12th'], dtype=object)
:::
:::

::: {.cell .code execution_count="35"}
``` python
df['ram_gb'].unique()
```

::: {.output .execute_result execution_count="35"}
    array(['4 GB', '8 GB', '16 GB', '32 GB'], dtype=object)
:::
:::

::: {.cell .code execution_count="36"}
``` python
df['ram_type'].unique()
```

::: {.output .execute_result execution_count="36"}
    array(['DDR4', 'LPDDR4', 'LPDDR4X', 'DDR5', 'DDR3', 'LPDDR3'],
          dtype=object)
:::
:::

::: {.cell .code execution_count="37"}
``` python
df['hdd'].unique()
```

::: {.output .execute_result execution_count="37"}
    array(['1024 GB', '0 GB', '512 GB', '2048 GB'], dtype=object)
:::
:::

::: {.cell .code execution_count="38"}
``` python
df['ssd'].unique()
```

::: {.output .execute_result execution_count="38"}
    array(['0 GB', '512 GB', '256 GB', '128 GB', '1024 GB', '2048 GB',
           '3072 GB'], dtype=object)
:::
:::

::: {.cell .code execution_count="39"}
``` python
df['os'].unique()
```

::: {.output .execute_result execution_count="39"}
    array(['Windows', 'DOS', 'Mac'], dtype=object)
:::
:::

::: {.cell .code execution_count="40"}
``` python
df['os_bit'].unique()
```

::: {.output .execute_result execution_count="40"}
    array(['64-bit', '32-bit'], dtype=object)
:::
:::

::: {.cell .code execution_count="41"}
``` python
df['graphic_card_gb'].unique()
```

::: {.output .execute_result execution_count="41"}
    array(['0 GB', '2 GB', '4 GB', '6 GB', '8 GB'], dtype=object)
:::
:::

::: {.cell .code execution_count="42"}
``` python
df['Touchscreen'].unique()
```

::: {.output .execute_result execution_count="42"}
    array(['No', 'Yes'], dtype=object)
:::
:::

::: {.cell .code execution_count="43"}
``` python
df['msoffice'].unique()
```

::: {.output .execute_result execution_count="43"}
    array(['No', 'Yes'], dtype=object)
:::
:::

::: {.cell .markdown}
Merubah Nilai kategorikal ke nilai numerikal pada kolom
brand,processor_brand,processor_name,processor_gnrtn,ram_gb,ram_type,ssd,hdd,os,os_bit,graphic_card_gb
:::

::: {.cell .code execution_count="44"}
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
:::

::: {.cell .code execution_count="45"}
``` python
corr_matrix = df.corr()
plt.figure(figsize=(10,10))
sns.heatmap(corr_matrix, annot=True)
plt.show()
```

::: {.output .display_data}
![](vertopal_f8772d8520514154bb439925444862af/03504bf511673ff96fa7f0bf1eed463b9434c891.png)
:::
:::

::: {.cell .markdown}
Menunjukan kolom setelah di replace
:::

::: {.cell .code execution_count="46"}
``` python
df.head()
```

::: {.output .execute_result execution_count="46"}
```{=html}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>brand</th>
      <th>processor_brand</th>
      <th>processor_name</th>
      <th>processor_gnrtn</th>
      <th>ram_gb</th>
      <th>ram_type</th>
      <th>ssd</th>
      <th>hdd</th>
      <th>os</th>
      <th>os_bit</th>
      <th>graphic_card_gb</th>
      <th>Touchscreen</th>
      <th>msoffice</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1024</td>
      <td>0</td>
      <td>64</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>34649</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1024</td>
      <td>0</td>
      <td>64</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>38999</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1024</td>
      <td>0</td>
      <td>64</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>39999</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
      <td>8</td>
      <td>0</td>
      <td>512</td>
      <td>0</td>
      <td>0</td>
      <td>32</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>69990</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>512</td>
      <td>0</td>
      <td>64</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>26990</td>
    </tr>
  </tbody>
</table>
</div>
```
:::
:::

::: {.cell .markdown}
## Modeling
:::

::: {.cell .markdown}
Mengimpor train_test_split dari library sklearn dan Mengimpor
LinearRegression dari library sklearn
:::

::: {.cell .code execution_count="52"}
``` python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
```
:::

::: {.cell .markdown}
menyingkatkan LinearRegression menjadi variable lr
:::

::: {.cell .code execution_count="48"}
``` python
lr = LinearRegression()
```
:::

::: {.cell .markdown}
setelah sebelum nya sudah ditentukan kolom/atribut yang krusial , lalu
drop kolom Price (Yakni Variable dependen) pada dataframe
:::

::: {.cell .code execution_count="53"}
``` python
X = df.drop(['Price'], axis=1)
```
:::

::: {.cell .markdown}
Masukan kolom Price pada variable y
:::

::: {.cell .code}
``` python
y = df['Price']
```
:::

::: {.cell .markdown}
lakukan split data , untuk data train dan data test. (Disini saya
masukan data test 25% dan data train 75 %)
:::

::: {.cell .code execution_count="49"}
``` python

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
```
:::

::: {.cell .markdown}
Membuat Regresi Linier
:::

::: {.cell .code execution_count="54"}
``` python

lr.fit(X_train,y_train)
pred = lr.predict(X_test)
score = lr.score(X_test,y_test)
print('Akurasi model regresi linier = ') ,score 
```

::: {.output .stream .stdout}
    Akurasi model regresi linier = 
:::

::: {.output .execute_result execution_count="54"}
    (None, 0.7102914487783226)
:::
:::

::: {.cell .markdown}
Dari regresi linier menghasilkan akurasi 71%
:::

::: {.cell .code execution_count="62"}
``` python
input_data = np.array([[1,1,2,10,3,3,1024,512,1,64,2,1,1]])
prediction = lr.predict(input_data)
print('Prediksi Harga Laptop: ', prediction)
```

::: {.output .stream .stdout}
    Prediksi Harga Laptop:  [173752.95413921]
:::

::: {.output .stream .stderr}
    c:\Users\ADMIN\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py:465: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names
      warnings.warn(
:::
:::

::: {.cell .code execution_count="88"}
``` python
from sklearn.metrics import r2_score
r2_DT = r2_score(y_test, pred)  
r2_DT

print(f"Precision = {r2_DT}")
```

::: {.output .stream .stdout}
    Precision = 0.7102914487783226
:::
:::

::: {.cell .markdown}
## Evaluation

R-squared (R2) adalah ukuran statistik yang mewakili proporsi varians
suatu variabel terikat yang dijelaskan oleh variabel bebas dalam model
regresi.
:::

::: {.cell .markdown}
![image.png](vertopal_f8772d8520514154bb439925444862af/image.png)
:::

::: {.cell .code execution_count="86"}
``` python
from sklearn.metrics import r2_score
r2_DT = r2_score(y_test, pred)  
r2_DT

print(f"Precision = {r2_DT}")
```

::: {.output .stream .stdout}
    Precision = 0.7102914487783226
:::
:::

::: {.cell .markdown}
didapatkan score 71% , sehingga dinyatakan bahwa variable dependen
dengan variable independen itu berkolerasi tinggi
:::

::: {.cell .markdown}
## Deployment
:::

::: {.cell .code execution_count="87"}
``` python
import pickle
filename = 'laptop-prices.sav'
pickle.dump(lr,open(filename,'wb'))
```
:::

::: {.cell .code}
``` python
```
:::
