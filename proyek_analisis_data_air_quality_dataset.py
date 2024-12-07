# -*- coding: utf-8 -*-
"""Proyek Analisis Data - Air Quality Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gkp7OESKqIkWdH5YAOl5TB6zbzr5r_GX

# TUGAS PROYEK AKHIR MODUL BELAJAR ANALISIS DATA DENGAN PYTHON


*   NAMA : PANGESTU RAHMAT NOVIYANDA
*   ID DICODING : pangesturahmatn


---
# Menentukan Pertanyaan Bisnis Atau Analisis

1. Bagaimana pengaruh kecepatan angin (WSPM) terhadap penyebaran konsentrasi PM2.5 selama musim Panas (juni hingga agustus)?
2. Bagaimana pengaruh konsentrasi NO2 dan CO sebagai polutan yang dihasilkan kendaraan bermotor terhadap kualitas udara ?
3. Bagaimana pengaruh hujan terhadap polutan penyebab polusi udara?
4. Bagaimana hubungan antara konsentrasi NO2, dan CO dengan pembentukan O3 ?

---

# Import Semua Packages/Library yang Digunakan
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import numpy as np

"""# Data Wrangling
## Gathering Data
"""

!git clone https://github.com/marceloreis/HTI.git

import pandas as pd

df_Aotizhongxin = pd.read_csv("/content/HTI/PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv")
df_Changping = pd.read_csv("/content/HTI/PRSA_Data_20130301-20170228/PRSA_Data_Changping_20130301-20170228.csv")
df_Dingling = pd.read_csv("/content/HTI/PRSA_Data_20130301-20170228/PRSA_Data_Dingling_20130301-20170228.csv")
df_Dongsi = pd.read_csv("/content/HTI/PRSA_Data_20130301-20170228/PRSA_Data_Dongsi_20130301-20170228.csv")
df_Guanyuan = pd.read_csv("/content/HTI/PRSA_Data_20130301-20170228/PRSA_Data_Guanyuan_20130301-20170228.csv")
df_Gucheng = pd.read_csv("/content/HTI/PRSA_Data_20130301-20170228/PRSA_Data_Gucheng_20130301-20170228.csv")
df_Huairou = pd.read_csv("/content/HTI/PRSA_Data_20130301-20170228/PRSA_Data_Huairou_20130301-20170228.csv")
df_Nongzhanguan = pd.read_csv("/content/HTI/PRSA_Data_20130301-20170228/PRSA_Data_Nongzhanguan_20130301-20170228.csv")
df_Shunyi = pd.read_csv("/content/HTI/PRSA_Data_20130301-20170228/PRSA_Data_Shunyi_20130301-20170228.csv")
df_Tiantan = pd.read_csv("/content/HTI/PRSA_Data_20130301-20170228/PRSA_Data_Tiantan_20130301-20170228.csv")
df_Wanliu = pd.read_csv("/content/HTI/PRSA_Data_20130301-20170228/PRSA_Data_Wanliu_20130301-20170228.csv")
df_Wanshouxigong =pd.read_csv("/content/HTI/PRSA_Data_20130301-20170228/PRSA_Data_Wanshouxigong_20130301-20170228.csv")

df_Aotizhongxin.head()

df_Changping.head()

df_Dingling.head()

df_Dongsi.head()

df_Guanyuan.head()

df_Gucheng.head()

df_Huairou.head()

df_Nongzhanguan.head()

df_Shunyi.head()

df_Tiantan.head()

df_Wanliu.head()

df_Wanshouxigong.head()

"""# Assessing Data
Missing value
"""

print('Dataframe Aotizhongxin:')
print(df_Aotizhongxin.isna().sum())

print('\nDataframe Changping:')
print(df_Changping.isna().sum())

print('\nDataframe Dingling:')
print(df_Dingling.isna().sum())

print('\nDataframe Dongsi:')
print(df_Dongsi.isna().sum())

print('\nDataframe Guanyuan:')
print(df_Guanyuan.isna().sum())

print('\nDataframe Gucheng:')
print(df_Gucheng.isna().sum())

print('\nDataframe Huairou:')
print(df_Huairou.isna().sum())

print('\nDataframe Nongzhanguan:')
print(df_Nongzhanguan.isna().sum())

print('\nDataframe Shunyi:')
print(df_Shunyi.isna().sum())

print('\nDataframe Tiantan:')
print(df_Tiantan.isna().sum())

print('\nDataframe Wanliu:')
print(df_Wanliu.isna().sum())

print('\nDataframe Wanshouxigong:')
print(df_Wanshouxigong.isna().sum())

"""Setalah analisis nilai yang hilang atau kosong berdasarkan kolom-kolom tertentu, ada banyak sekali sehingga perlu kita atasi ditahap selanjutnya

# DUPLICATE DATA
"""

print('Dataframe Aotizhongxin:', df_Aotizhongxin.duplicated().sum())
print('Dataframe Changping:', df_Changping.duplicated().sum())
print('Dataframe Dingling:', df_Dingling.duplicated().sum())
print('Dataframe Dongsi:', df_Dongsi.duplicated().sum())
print('Dataframe Guanyuan:', df_Guanyuan.duplicated().sum())
print('Dataframe Gucheng:', df_Gucheng.duplicated().sum())
print('Dataframe Huairou:', df_Huairou.duplicated().sum())
print('Dataframe Nongzhanguan:', df_Nongzhanguan.duplicated().sum())
print('Dataframe Shunyi:', df_Shunyi.duplicated().sum())
print('Dataframe Tiantan:', df_Tiantan.duplicated().sum())
print('Dataframe Wanliu:', df_Wanliu.duplicated().sum())
print('Dataframe Wanshouxigong:', df_Wanshouxigong.duplicated().sum())

"""Tidak ada data yang duplicated

# OUTLIER
"""

def identify_outliers_iqr(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    return ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)

outliers_Aotizhongxin_iqr = identify_outliers_iqr(df_Aotizhongxin.select_dtypes(include=[np.number]))
outliers_Changping_iqr = identify_outliers_iqr(df_Changping.select_dtypes(include=[np.number]))
outliers_Dingling_iqr = identify_outliers_iqr(df_Dingling.select_dtypes(include=[np.number]))
outliers_Dongsi_iqr = identify_outliers_iqr(df_Dongsi.select_dtypes(include=[np.number]))
outliers_Guanyuan_iqr = identify_outliers_iqr(df_Guanyuan.select_dtypes(include=[np.number]))
outliers_Gucheng_iqr = identify_outliers_iqr(df_Gucheng.select_dtypes(include=[np.number]))
outliers_Huairou_iqr = identify_outliers_iqr(df_Huairou.select_dtypes(include=[np.number]))
outliers_Nongzhanguan_iqr = identify_outliers_iqr(df_Nongzhanguan.select_dtypes(include=[np.number]))
outliers_Shunyi_iqr = identify_outliers_iqr(df_Shunyi.select_dtypes(include=[np.number]))
outliers_Tiantan_iqr = identify_outliers_iqr(df_Tiantan.select_dtypes(include=[np.number]))
outliers_Wanliu_iqr = identify_outliers_iqr(df_Wanliu.select_dtypes(include=[np.number]))
outliers_Wanshouxigong_iqr = identify_outliers_iqr(df_Wanshouxigong.select_dtypes(include=[np.number]))


print("Outliers in df_Aotizhongxin (IQR):\n", df_Aotizhongxin[outliers_Aotizhongxin_iqr])
print("Outliers in df_Changping (IQR):\n", df_Changping[outliers_Changping_iqr])
print("Outliers in df_Dingling (IQR):\n", df_Dingling[outliers_Dingling_iqr])
print("Outliers in df_Dongsi (IQR):\n", df_Dongsi[outliers_Dongsi_iqr])
print("Outliers in df_Guanyuan (IQR):\n", df_Guanyuan[outliers_Guanyuan_iqr])
print("Outliers in df_Gucheng (IQR):\n", df_Gucheng[outliers_Gucheng_iqr])
print("Outliers in df_Huairou (IQR):\n", df_Huairou[outliers_Huairou_iqr])
print("Outliers in df_Nongzhanguan (IQR):\n", df_Nongzhanguan[outliers_Nongzhanguan_iqr])
print("Outliers in df_Shunyi (IQR):\n", df_Shunyi[outliers_Shunyi_iqr])
print("Outliers in df_Tiantan (IQR):\n", df_Tiantan[outliers_Tiantan_iqr])
print("Outliers in df_Wanliu (IQR):\n", df_Wanliu[outliers_Wanliu_iqr])
print("Outliers in df_Wanshouxigong (IQR):\n", df_Wanshouxigong[outliers_Wanshouxigong_iqr])

"""# BOXPLOT"""

numeric_columns = df_Aotizhongxin.select_dtypes(include='number').columns

plt.figure(figsize=(15, 10))
for i, column in enumerate(numeric_columns, 1):
    plt.subplot(len(numeric_columns), 1, i)
    sns.boxplot(x=df_Aotizhongxin[column])
    plt.title(f'Boxplot {column}')
    plt.xlabel(column)

plt.show()

"""Ada cukup banyak outlier yang bisa mempengaruhi analisis.
# Cleaning Data
Imputasi Isi Nilai Hilang dengan Mean<br>
Pisahkan kolom numerik dari kolom non-numerik
"""

numeric_columns_Aotizhongxin = df_Aotizhongxin.select_dtypes(include=[np.number])
non_numeric_columns_Aotizhongxin = df_Aotizhongxin.select_dtypes(exclude=[np.number])

numeric_columns_Changping = df_Changping.select_dtypes(include=[np.number])
non_numeric_columns_Changping = df_Changping.select_dtypes(exclude=[np.number])

numeric_columns_Dingling = df_Dingling.select_dtypes(include=[np.number])
non_numeric_columns_Dingling = df_Dingling.select_dtypes(exclude=[np.number])

numeric_columns_Dongsi = df_Dongsi.select_dtypes(include=[np.number])
non_numeric_columns_Dongsi = df_Dongsi.select_dtypes(exclude=[np.number])

numeric_columns_Guanyuan = df_Guanyuan.select_dtypes(include=[np.number])
non_numeric_columns_Guanyuan = df_Guanyuan.select_dtypes(exclude=[np.number])

numeric_columns_Gucheng = df_Gucheng.select_dtypes(include=[np.number])
non_numeric_columns_Gucheng = df_Gucheng.select_dtypes(exclude=[np.number])

numeric_columns_Huairou = df_Huairou.select_dtypes(include=[np.number])
non_numeric_columns_Huairou  = df_Huairou.select_dtypes(exclude=[np.number])

numeric_columns_Nongzhanguan = df_Nongzhanguan.select_dtypes(include=[np.number])
non_numeric_columns_Nongzhanguan = df_Nongzhanguan.select_dtypes(exclude=[np.number])

numeric_columns_Shunyi = df_Shunyi.select_dtypes(include=[np.number])
non_numeric_columns_Shunyi = df_Shunyi.select_dtypes(exclude=[np.number])

numeric_columns_Tiantan = df_Tiantan.select_dtypes(include=[np.number])
non_numeric_columns_Tiantan = df_Tiantan.select_dtypes(exclude=[np.number])

numeric_columns_Wanliu = df_Wanliu.select_dtypes(include=[np.number])
non_numeric_columns_Wanliu = df_Wanliu.select_dtypes(exclude=[np.number])

numeric_columns_Wanshouxigong = df_Wanshouxigong.select_dtypes(include=[np.number])
non_numeric_columns_Wanshouxigong = df_Wanshouxigong.select_dtypes(exclude=[np.number])

"""Imputasi untuk kolom numerik"""

numeric_columns_Aotizhongxin.fillna(numeric_columns_Aotizhongxin.mean(), inplace=True)
numeric_columns_Changping.fillna(numeric_columns_Changping.mean(), inplace=True)
numeric_columns_Dingling.fillna(numeric_columns_Dingling.mean(), inplace=True)
numeric_columns_Dongsi.fillna(numeric_columns_Dongsi.mean(), inplace=True)
numeric_columns_Guanyuan.fillna(numeric_columns_Guanyuan.mean(), inplace=True)
numeric_columns_Gucheng.fillna(numeric_columns_Gucheng.mean(), inplace=True)
numeric_columns_Huairou.fillna(numeric_columns_Huairou.mean(), inplace=True)
numeric_columns_Nongzhanguan.fillna(numeric_columns_Nongzhanguan.mean(), inplace=True)
numeric_columns_Shunyi.fillna(numeric_columns_Shunyi.mean(), inplace=True)
numeric_columns_Tiantan.fillna(numeric_columns_Tiantan.mean(), inplace=True)
numeric_columns_Wanliu.fillna(numeric_columns_Wanliu.mean(), inplace=True)
numeric_columns_Wanshouxigong.fillna(numeric_columns_Wanshouxigong.mean(), inplace=True)

"""Imputasi untuk kolom non-numerik"""

non_numeric_columns_Aotizhongxin.fillna(non_numeric_columns_Aotizhongxin.mode().iloc[0], inplace=True)
non_numeric_columns_Changping.fillna(non_numeric_columns_Changping.mode().iloc[0], inplace=True)
non_numeric_columns_Dingling.fillna(non_numeric_columns_Dingling.mode().iloc[0], inplace=True)
non_numeric_columns_Dongsi.fillna(non_numeric_columns_Dongsi.mode().iloc[0], inplace=True)
non_numeric_columns_Guanyuan.fillna(non_numeric_columns_Guanyuan.mode().iloc[0], inplace=True)
non_numeric_columns_Gucheng.fillna(non_numeric_columns_Gucheng.mode().iloc[0], inplace=True)
non_numeric_columns_Huairou.fillna(non_numeric_columns_Huairou.mode().iloc[0], inplace=True)
non_numeric_columns_Nongzhanguan.fillna(non_numeric_columns_Nongzhanguan.mode().iloc[0], inplace=True)
non_numeric_columns_Shunyi.fillna(non_numeric_columns_Shunyi.mode().iloc[0], inplace=True)
non_numeric_columns_Tiantan.fillna(non_numeric_columns_Tiantan.mode().iloc[0], inplace=True)
non_numeric_columns_Wanliu.fillna(non_numeric_columns_Wanliu.mode().iloc[0], inplace=True)
non_numeric_columns_Wanshouxigong.fillna(non_numeric_columns_Wanshouxigong.mode().iloc[0], inplace=True)

"""Gabungkan kembali kolom numerik dan non-numerik"""

df_Aotizhongxin_final = pd.concat([numeric_columns_Aotizhongxin, non_numeric_columns_Aotizhongxin], axis=1)
df_Changping_final = pd.concat([numeric_columns_Changping, non_numeric_columns_Changping], axis=1)
df_Dingling_final = pd.concat([numeric_columns_Dingling, non_numeric_columns_Dingling], axis=1)
df_Dongsi_final = pd.concat([numeric_columns_Dongsi, non_numeric_columns_Dongsi], axis=1)
df_Guanyuan_final = pd.concat([numeric_columns_Guanyuan, non_numeric_columns_Guanyuan], axis=1)
df_Gucheng_final = pd.concat([numeric_columns_Gucheng, non_numeric_columns_Gucheng], axis=1)
df_Huairou_final = pd.concat([numeric_columns_Huairou, non_numeric_columns_Huairou], axis=1)
df_Nongzhanguan_final = pd.concat([numeric_columns_Nongzhanguan, non_numeric_columns_Nongzhanguan], axis=1)
df_Shunyi_final = pd.concat([numeric_columns_Shunyi, non_numeric_columns_Shunyi], axis=1)
df_Tiantan_final = pd.concat([numeric_columns_Tiantan, non_numeric_columns_Tiantan], axis=1)
df_Wanliu_final = pd.concat([numeric_columns_Wanliu, non_numeric_columns_Wanliu], axis=1)
df_Wanshouxigong_final = pd.concat([numeric_columns_Wanshouxigong, non_numeric_columns_Wanshouxigong], axis=1)

"""Cek nilai yang hilang setelah imputasi"""

print("Nilai yang hilang di df_Aotizhongxin_final:\n", df_Aotizhongxin_final.isnull().sum())
print("Nilai yang hilang di df_Changping_final:\n", df_Changping_final.isnull().sum())
print("Nilai yang hilang di df_Dingling_final:\n", df_Dingling_final.isnull().sum())
print("Nilai yang hilang di df_Dongsi_final:\n", df_Dongsi_final.isnull().sum())
print("Nilai yang hilang di df_Guanyuan_final:\n", df_Guanyuan_final.isnull().sum())
print("Nilai yang hilang di df_Gucheng_final:\n", df_Gucheng_final.isnull().sum())
print("Nilai yang hilang di df_Huairou_final:\n", df_Huairou_final.isnull().sum())
print("Nilai yang hilang di df_Nongzhanguan_final:\n", df_Nongzhanguan_final.isnull().sum())
print("Nilai yang hilang di df_Shunyi_final:\n", df_Shunyi_final.isnull().sum())
print("Nilai yang hilang di df_Tiantan_final:\n", df_Tiantan_final.isnull().sum())
print("Nilai yang hilang di df_Wanliu_final:\n", df_Wanliu_final.isnull().sum())
print("Nilai yang hilang di df_Wanshouxigong_final:\n", df_Wanshouxigong_final.isnull().sum())

"""Winsorization untuk mengatasi outlier"""

def apply_winsorizing(df, lower_quantile=0.05, upper_quantile=0.95):
    df_winsorized = df.copy()
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            lower_limit = df[column].quantile(lower_quantile)
            upper_limit = df[column].quantile(upper_quantile)
            df_winsorized[column] = df[column].clip(lower=lower_limit, upper=upper_limit)
    return df_winsorized
df_Aotizhongxin_winsorized = apply_winsorizing(df_Aotizhongxin)
df_Changping_winsorized = apply_winsorizing(df_Changping)
df_Dingling_winsorized = apply_winsorizing(df_Dingling)
df_Dongsi_winsorized = apply_winsorizing(df_Dongsi)
df_Guanyuan_winsorized = apply_winsorizing(df_Guanyuan)
df_Gucheng_winsorized = apply_winsorizing(df_Gucheng)
df_Huairou_winsorized = apply_winsorizing(df_Huairou)
df_Nongzhanguan_winsorized = apply_winsorizing(df_Nongzhanguan)
df_Shunyi_winsorized = apply_winsorizing(df_Shunyi)
df_Tiantan_winsorized = apply_winsorizing(df_Tiantan)
df_Wanliu_winsorized = apply_winsorizing(df_Wanliu)
df_Wanshouxigong_winsorized = apply_winsorizing(df_Wanshouxigong)

"""Boxplots setelah winsorized untuk mengecek apakah masih ada outlier"""

def plot_boxplots_winsorized(df, title, figsize=(15, 10)):
    plt.figure(figsize=figsize)
    sns.boxplot(data=df, orient='h')
    plt.title(f'Boxplot After Winsorizing - {title}')
    plt.show()

plot_boxplots_winsorized(df_Aotizhongxin_winsorized, 'Aotizhongxin')
plot_boxplots_winsorized(df_Changping_winsorized, 'Changping')
plot_boxplots_winsorized(df_Dingling_winsorized, 'Dingling')
plot_boxplots_winsorized(df_Dongsi_winsorized, 'Dongsi')
plot_boxplots_winsorized(df_Guanyuan_winsorized, 'Guanyuan')
plot_boxplots_winsorized(df_Gucheng_winsorized, 'Gucheng')
plot_boxplots_winsorized(df_Huairou_winsorized, 'Huairou')
plot_boxplots_winsorized(df_Nongzhanguan_winsorized, 'Nongzhanguan')
plot_boxplots_winsorized(df_Shunyi_winsorized, 'Shunyi')
plot_boxplots_winsorized(df_Tiantan_winsorized, 'Tiantan')
plot_boxplots_winsorized(df_Wanliu_winsorized, 'Wanliu')
plot_boxplots_winsorized(df_Wanshouxigong_winsorized, 'Wanshouxigong')

"""Fixed data type"""

df_Aotizhongxin['date_time'] = pd.to_datetime(df_Aotizhongxin[['year', 'month', 'day', 'hour']])
df_Changping['date_time'] = pd.to_datetime(df_Changping[['year', 'month', 'day', 'hour']])
df_Dingling['date_time'] = pd.to_datetime(df_Dingling[['year', 'month', 'day', 'hour']])
df_Dongsi['date_time'] = pd.to_datetime(df_Dongsi[['year', 'month', 'day', 'hour']])
df_Guanyuan['date_time'] = pd.to_datetime(df_Guanyuan[['year', 'month', 'day', 'hour']])
df_Gucheng['date_time'] = pd.to_datetime(df_Gucheng[['year', 'month', 'day', 'hour']])
df_Huairou['date_time'] = pd.to_datetime(df_Huairou[['year', 'month', 'day', 'hour']])
df_Nongzhanguan['date_time'] = pd.to_datetime(df_Nongzhanguan[['year', 'month', 'day', 'hour']])
df_Shunyi['date_time'] = pd.to_datetime(df_Shunyi[['year', 'month', 'day', 'hour']])
df_Tiantan['date_time'] = pd.to_datetime(df_Tiantan[['year', 'month', 'day', 'hour']])
df_Wanliu['date_time'] = pd.to_datetime(df_Wanliu[['year', 'month', 'day', 'hour']])
df_Wanshouxigong['date_time'] = pd.to_datetime(df_Wanshouxigong[['year', 'month', 'day', 'hour']])

print(df_Aotizhongxin.dtypes)
print(df_Changping.dtypes)
print(df_Dingling.dtypes)
print(df_Dongsi.dtypes)
print(df_Guanyuan.dtypes)
print(df_Gucheng.dtypes)
print(df_Huairou.dtypes)
print(df_Nongzhanguan.dtypes)
print(df_Shunyi.dtypes)
print(df_Tiantan.dtypes)
print(df_Wanliu.dtypes)
print(df_Wanshouxigong.dtypes)

"""# Exploratory Data Analysis (EDA)
Gabungkan data
"""

df_all = pd.concat([df_Aotizhongxin, df_Changping, df_Dingling, df_Dongsi, df_Guanyuan, df_Gucheng, df_Huairou, df_Nongzhanguan, df_Shunyi, df_Tiantan, df_Wanliu, df_Wanshouxigong])

"""Mengonversi kolom date_time ke tipe datetime"""

df_all['date_time'] = pd.to_datetime(df_all[['year', 'month', 'day', 'hour']])

"""Analisis Deskriptif"""

print(df_all.describe())

"""Cek missing value"""

print(df_all.isnull().sum())

"""Drop missing value"""

df_all= df_all.dropna()

"""Mendeteksi dan menghitung baris dengan index duplikat"""

print(df_all.index.duplicated().sum())

"""Mendeteksi dan menampilkan kolom duplikat"""

print(df_all.columns[df_all.columns.duplicated()])

df_all = df_all.loc[:, ~df_all.columns.duplicated()]

df_all.to_csv('clean_df_all.csv', index=False)

"""Hubungan Angin dengan Persebaran PM2.5"""

plt.figure(figsize=(10, 6))
sns.scatterplot(x='WSPM', y='PM2.5', data=df_all)
plt.title('Scatterplot of Wind Speed vs PM2.5')
plt.show()

"""Korelasi antara variabel"""

corr_matrix = df_all[['PM2.5', 'WSPM', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap Kolerasi')
plt.show()

"""Konsentrasi Polutan dari Kendaraan Bermotor atau bahan bakar fosil (CO & NO2)"""

df_subset = df_all[['date_time', 'CO', 'NO2']].resample('M', on='date_time').mean().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x='date_time', y='CO', data=df_subset, label='CO')
sns.lineplot(x='date_time', y='NO2', data=df_subset, label='NO2')
plt.title('Konsentrasi CO dan NO2 Selama Beberapa Tahun (Rata-rata Bulanan)')
plt.legend()
plt.show()

"""Kaitan Hujan dengan Tingkat Polutan"""

df_all = df_all.reset_index(drop=True)
plt.figure(figsize=(30, 6))
sns.boxplot(x='RAIN', y='PM2.5', data=df_all)
plt.title('Pengaruh Hujan terhadap PM2.5')
plt.xlabel('Hujan (RAIN)', labelpad=20)
plt.ylabel('Konsentrasi PM2.5')


plt.xticks(rotation=45, ha='right')

plt.show()

"""Kaitan Polutan NO2 dan CO dengan O3"""

plt.figure(figsize=(10, 6))
sns.scatterplot(x='NO2', y='O3', data=df_all)
plt.title('Scatterplot of NO2 vs O3')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='CO', y='O3', data=df_all)
plt.title('Scatterplot of CO vs O3')
plt.show()

"""Correlation Heatmap khusus O3 dengan polutan lain"""

corr_matrix_O3 = df_all[['O3', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO']].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix_O3, annot=True, cmap='coolwarm')
plt.title('Correlation of O3 with Other Pollutants')
plt.show()

"""# Visualization & Explanatory Analysis

## Pertanyaan Pertama
1. Bagaimana pengaruh kecepatan angin (WSPM) terhadap penyebaran konsentrasi PM2.5 selama musim kemarau (Juni hingga Agustus)?
"""

df_all['month'] = df_all['date_time'].dt.month

dry_season_data = df_all[df_all['month'].isin([6, 7, 8])]

plt.figure(figsize=(12, 6))
sns.scatterplot(x='WSPM', y='PM2.5', data=dry_season_data)
plt.title('Hubungan Kecepatan Angin (WSPM) dengan PM2.5 Selama Musim Kemarau (Juni hingga Agustus)')
plt.xlabel('Kecepatan Angin (WSPM)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()

dry_season_data = df_all[df_all['month'].isin([6, 7, 8])]

monthly_avg = dry_season_data.groupby(['year', 'month']).agg({'WSPM': 'mean', 'PM2.5': 'mean'}).reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x='WSPM', y='PM2.5', hue='month', data=dry_season_data, marker='o', palette='coolwarm')
plt.title('Hubungan Kecepatan Angin (WSPM) dengan PM2.5 Selama Musim Kemarau (Juni hingga Agustus)')
plt.xlabel('Kecepatan Angin (WSPM)')
plt.ylabel('Konsentrasi PM2.5')
plt.legend(title='Bulan', labels=['Juni', 'Juli', 'Agustus'])
plt.show()

"""## Pertanyaan Ke 2
2. Bagaimana pengaruh konsentrasi NO2 dan CO sebagai polutan yang dihasilkan kendaraan bermotor terhadap kualitas udara?
"""

df_all['date_time_month'] = df_all['date_time'].dt.to_period('M')

monthly_avg = df_all.groupby('date_time_month').agg({
    'CO': 'mean',
    'NO2': 'mean',
    'PM2.5': 'mean',
    'PM10': 'mean',
    'SO2': 'mean',
    'O3': 'mean'
}).reset_index()

monthly_avg['date_time_month'] = monthly_avg['date_time_month'].dt.to_timestamp()

plt.figure(figsize=(14, 8))

sns.lineplot(x='date_time_month', y='CO', data=monthly_avg, label='CO', color='blue')
sns.lineplot(x='date_time_month', y='NO2', data=monthly_avg, label='NO2', color='red')
sns.lineplot(x='date_time_month', y='PM2.5', data=monthly_avg, label='PM2.5', color='green')
sns.lineplot(x='date_time_month', y='PM10', data=monthly_avg, label='PM10', color='purple')
sns.lineplot(x='date_time_month', y='SO2', data=monthly_avg, label='SO2', color='orange')
sns.lineplot(x='date_time_month', y='O3', data=monthly_avg, label='O3', color='cyan')

plt.title('Rata-rata Bulanan Konsentrasi Polutan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Polutan')

plt.xticks(ticks=monthly_avg['date_time_month'], labels=monthly_avg['date_time_month'].dt.strftime('%Y-%m'), rotation=45)

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

"""## Pertanyaan Ketiga
3. Bagaimana pengaruh hujan terhadap polutan penyebab polusi udara?
"""

df_all['RAIN_GROUP'] = pd.cut(df_all['RAIN'], bins=[0, 1, 4, 8, 10], labels=['No Rain', 'Light Rain', 'Moderate Rain', 'Heavy Rain'])

plt.figure(figsize=(12, 8))
sns.boxplot(x='RAIN_GROUP', y='PM2.5', data=df_all)
plt.title('Boxplot of PM2.5 by Rain Intensity')
plt.xticks(rotation=45)
plt.show()

df_all['RAIN_GROUP'] = pd.cut(df_all['RAIN'], bins=[0, 1, 4, 8, 10], labels=['No Rain', 'Light Rain', 'Moderate Rain', 'Heavy Rain'])

rain_group_avg = df_all.groupby('RAIN_GROUP')['PM2.5'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x='RAIN_GROUP', y='PM2.5', data=rain_group_avg, marker='o', color='blue')

plt.title('Rata-rata Konsentrasi PM2.5 Berdasarkan Intensitas Hujan')
plt.xlabel('Kelompok Intensitas Hujan')
plt.ylabel('Rata-rata Konsentrasi PM2.5')

plt.show()

"""## Pertanyaan Ke Empat
4. Bagaimana hubungan antara konsentrasi NO2, dan CO dengan pembentukan O3 ?
"""

df_all['date_time_month'] = df_all['date_time'].dt.to_period('M')

monthly_avg = df_all.groupby('date_time_month').agg({'NO2': 'mean', 'CO': 'mean', 'O3': 'mean'}).reset_index()

monthly_avg['date_time_month'] = monthly_avg['date_time_month'].dt.to_timestamp()

plt.figure(figsize=(12, 6))

sns.lineplot(x='date_time_month', y='NO2', data=monthly_avg, label='NO2', color='red')
sns.lineplot(x='date_time_month', y='CO', data=monthly_avg, label='CO', color='blue')
sns.lineplot(x='date_time_month', y='O3', data=monthly_avg, label='O3', color='green')

plt.title('Konsentrasi NO2, CO, dan O3 Bulanan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Polutan (NO2, CO, O3)')
plt.legend()

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

corr_matrix = df_all[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'WSPM', 'TEMP', 'RAIN']].corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap Korelasi Antara Variabel Polutan dan Faktor Lingkungan')
plt.show()

"""# Conclusion

## Dari analisis di atas, dapat disimpulkan bahwa:

1. Kecepatan angin (WSPM) berperan penting dalam penyebaran polutan. Ketika kecepatan angin tinggi, konsentrasi PM2.5 cenderung menurun karena polutan tersebar lebih luas, sehingga menciptakan tren negatif antara kecepatan angin dan konsentrasi PM2.5 karena polutan terbawa ke kawasan lain. Tetapi jika kecepatan angin sedang maka akan menambah persebaran polutan di kawasan tersebut, sehingga polutan menjadi meningkat bukan menurun.

2. Peningkatan konsentrasi CO dan NO₂ sering kali menunjukkan peningkatan aktivitas kendaraan bermotor atau pembakaran bahan bakar fosil. Hal ini menunjukkan bahwa kendaraan bermotor dan bahan bakar fosil berperan besar dalam kontribusi polutan yang menyebabkan polusi udara.

3. Hujan membantu mengurangi konsentrasi polutan, termasuk PM2.5. Polutan terbawa oleh air hujan, menyebabkan penurunan yang signifikan pada distribusi PM2.5. Namun, dalam kondisi hujan lebat, PM2.5 dapat meningkat seiring intensitas hujan karena pengadukan partikel dari permukaan tanah atau reaksi lainnya.

4. NO2 dan CO mempengaruhi pembentukan O3, ketika kadar NO2 naik maka kadar O3 akan menurun dan sebaliknya. NO2 bisa mengkatalisasi reaksi yang mengurangi konsentrasi O3 di atmosfer. Di lingkungan dengan tingkat CO tinggi, bisa memperlambat reaksi yang membentuk O3.
"""