# LAPORAN PROYEK UAS DATA MINING

## Nama
Nayla Rahmadhani

## Mata Kuliah
Data Mining

## Judul
Preprocessing Data dan Implementasi Algoritma K-Means Clustering pada Dataset Titanic

---

# 1. Pendahuluan

## Latar Belakang
Data mining merupakan proses menggali informasi atau pola dari sekumpulan data. Salah satu teknik dalam data mining adalah clustering, yaitu proses mengelompokkan data berdasarkan kemiripan karakteristik tanpa mengetahui label data sebelumnya.

Pada proyek ini digunakan dataset Titanic untuk mengelompokkan penumpang berdasarkan beberapa atribut seperti umur, jenis kelamin, kelas penumpang, jumlah keluarga, tarif, dan pelabuhan keberangkatan. Sebelum proses clustering dilakukan, data terlebih dahulu dibersihkan agar menghasilkan analisis yang lebih baik.
---

# 2. Dataset

Dataset yang digunakan adalah **Titanic Dataset**.
Jumlah data:
- 891 baris
Jumlah atribut:
- 12 kolom

Atribut yang digunakan pada proses clustering adalah:
- Pclass
- Sex
- Age
- SibSp
- Parch
- Fare
- Embarked
---

# 3. Tahapan Preprocessing

## 3.1 Cleaning Data
Tahap pertama adalah membersihkan data. Proses yang dilakukan yaitu:
### a. Missing Value
Ditemukan data kosong pada beberapa kolom.
- Age : 177 data kosong
- Cabin : 687 data kosong
- Embarked : 2 data kosong

Penanganan yang dilakukan:
- Kolom Age diisi menggunakan nilai rata-rata (mean).
- Kolom Embarked diisi menggunakan nilai yang paling sering muncul (modus).
- Kolom Cabin dihapus karena memiliki terlalu banyak data kosong.

### b. Duplicate Data
Dilakukan pengecekan data duplikat menggunakan fungsi `drop_duplicates()`.
Hasilnya menunjukkan bahwa tidak terdapat data duplikat sehingga jumlah data tetap sebanyak 891 data.

### c. Encoding
Kolom **Sex** dan **Embarked** diubah menjadi data numerik menggunakan **LabelEncoder** agar dapat diproses oleh algoritma K-Means.

### d. Standardisasi
Data dinormalisasi menggunakan **StandardScaler** sehingga seluruh atribut memiliki skala yang sama.
---

# 4. Implementasi Clustering
Metode clustering yang digunakan adalah **K-Means Clustering**.
Sebelum menentukan jumlah cluster dilakukan evaluasi menggunakan **Elbow Method**.
Berdasarkan grafik Elbow Method diperoleh jumlah cluster terbaik yaitu **3 cluster**.
---

# 5. Hasil Clustering
Jumlah anggota setiap cluster adalah sebagai berikut.
| Cluster | Jumlah Data |
|----------|------------:|
| 0 | 139 |
| 1 | 540 |
| 2 | 212 |

Visualisasi hasil clustering ditampilkan menggunakan Scatter Plot dengan atribut Age dan Fare.
---

# 6. Evaluasi
Evaluasi dilakukan menggunakan **Silhouette Score**. Hasil yang diperoleh yaitu:
**Silhouette Score = 0.301**
Nilai tersebut menunjukkan bahwa proses clustering berhasil membentuk kelompok data yang cukup baik berdasarkan karakteristik penumpang.
---

# 7. Output Program
Program menghasilkan beberapa file yaitu:
- elbow_method.png
- scatter_plot.png
- hasil_cluster.csv
- silhouette_score.txt
---

# 8. Kesimpulan
Berdasarkan hasil preprocessing dan implementasi algoritma K-Means Clustering, dataset Titanic berhasil dikelompokkan menjadi tiga cluster. Tahapan preprocessing seperti penanganan missing value, encoding, penghapusan data yang tidak diperlukan, dan standardisasi membantu meningkatkan kualitas data sebelum proses clustering dilakukan.

Hasil evaluasi menggunakan Elbow Method menunjukkan bahwa jumlah cluster yang digunakan adalah tiga cluster, sedangkan Silhouette Score sebesar 0.301 menunjukkan bahwa hasil clustering cukup baik.
Secara keseluruhan, tujuan proyek untuk melakukan preprocessing data dan clustering berhasil dicapai.
---

# Daftar Pustaka
1. Han, J., Kamber, M., & Pei, J. *Data Mining: Concepts and Techniques*. Morgan Kaufmann.
2. Scikit-Learn Documentation. https://scikit-learn.org
3. Kaggle Titanic Dataset. https://www.kaggle.com/