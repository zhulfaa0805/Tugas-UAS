# UAS Data Mining - Preprocessing dan K-Means Clustering

## Nama
Nayla Rahmadhani

## Kelas
04TPLM007

## Mata Kuliah
Data Mining

## Dosen Pengampu
AGUNG PERDANANTO S.Kom, M.Kom

## Deskripsi
Project ini dibuat untuk memenuhi tugas Ujian Akhir Semester (UAS) mata kuliah Data Mining.

Tahapan yang dilakukan meliputi:
- Data Cleaning
- Penanganan Missing Value
- Encoding Data
- Standardisasi Data
- K-Means Clustering
- Elbow Method
- Silhouette Score
- Visualisasi Hasil Clustering

## Dataset
Dataset yang digunakan adalah **Titanic Dataset**.

Jumlah data: **891 baris**
Jumlah atribut: **12 kolom**

## Algoritma
K-Means Clustering

## Library
- pandas
- numpy
- matplotlib
- scikit-learn

## Cara Menjalankan Program
Install library:
pip install -r requirements.txt

Jalankan program:
python main.py

## Output Program
Program akan menghasilkan file berikut pada folder **hasil**:
- elbow_method.png
- scatter_plot.png
- hasil_cluster.csv
- silhouette_score.txt

## Kesimpulan
Dataset Titanic berhasil diproses melalui tahap preprocessing, kemudian dikelompokkan menggunakan algoritma K-Means menjadi 3 cluster berdasarkan karakteristik data penumpang.