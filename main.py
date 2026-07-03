print("="*55)
print("PROYEK UAS DATA MINING")
print("="*55)
print("Nama      : Nayla Rahmadhani")
print("Dataset   : Titanic Dataset")
print("Algoritma : K-Means Clustering")
print("="*55)

# ============================================
# PROYEK UAS DATA MINING
# PREPROCESSING DAN K-MEANS CLUSTERING
# Dataset: Titanic
# ============================================

# Import library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# ==========================
# Membaca Dataset
# ==========================

print("=" * 50)
print("MEMBACA DATASET")
print("=" * 50)

# Membaca file CSV
df = pd.read_csv("dataset/Titanic-Dataset.csv")

# Menampilkan 5 data pertama
print(df.head())

# Menampilkan ukuran dataset
print("\nUkuran Dataset:")
print(df.shape)

# Menampilkan informasi dataset
print("\nInformasi Dataset:")
print(df.info())

# Mengecek missing value
print("\nMissing Value:")
print(df.isnull().sum())

# =====================
# CLEANING DATA
# =====================

print("\n" + "=" * 50)
print("CLEANING DATA")
print("=" * 50)

# Mengisi nilai kosong pada kolom Age dengan nilai rata-rata
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Mengisi nilai kosong pada kolom Embarked dengan nilai yang paling sering muncul (modus)
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Menghapus kolom Cabin karena terlalu banyak data yang kosong
df.drop(columns=["Cabin"], inplace=True)

# Mengecek kembali apakah masih ada missing value
print("\nMissing Value Setelah Cleaning:")
print(df.isnull().sum())

# Mengecek jumlah data sebelum menghapus duplikat
print("\nJumlah data sebelum menghapus duplikat :", len(df))

# Menghapus data yang duplikat
df.drop_duplicates(inplace=True)

# Menampilkan jumlah data setelah duplikat dihapus
print("Jumlah data setelah menghapus duplikat :", len(df))

# ===================
# ENCODING DATA
# ===================

print("\n" + "=" * 50)
print("ENCODING DATA")
print("=" * 50)

# Membuat objek LabelEncoder
le = LabelEncoder()

# Mengubah kolom Sex menjadi angka
# male = 1, female = 0 (atau sebaliknya)
df["Sex"] = le.fit_transform(df["Sex"])

# Mengubah kolom Embarked menjadi angka
df["Embarked"] = le.fit_transform(df["Embarked"])

print("\nData setelah Encoding:")
print(df[["Sex", "Embarked"]].head())

# ====================
# MEMILIH FITUR
# ====================

print("\n" + "=" * 50)
print("MEMILIH FITUR")
print("=" * 50)

# Memilih kolom yang digunakan untuk clustering
X = df[[
    "Pclass",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Embarked"
]]

print(X.head())

# ==========================
# STANDARDISASI DATA
# ==========================

print("\n" + "=" * 50)
print("STANDARDISASI DATA")
print("=" * 50)

# Membuat objek StandardScaler
scaler = StandardScaler()

# Melakukan standardisasi data
X_scaled = scaler.fit_transform(X)
print("Standardisasi data berhasil dilakukan.")

# =================
# ELBOW METHOD
# =================

print("\n" + "=" * 50)
print("ELBOW METHOD")
print("=" * 50)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Membuat grafik Elbow Method
plt.figure(figsize=(8,5))
plt.plot(range(1,11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Jumlah Cluster")
plt.ylabel("WCSS")
plt.grid(True)

# Simpan gambar
plt.savefig("hasil/elbow_method.png")
plt.show()
print("Grafik Elbow Method berhasil disimpan.")

# ========================
# K-MEANS CLUSTERING
# ========================

print("\n" + "=" * 50)
print("K-MEANS CLUSTERING")
print("=" * 50)

# Membuat model K-Means dengan 3 cluster
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)
# Melakukan clustering
df["Cluster"] = kmeans.fit_predict(X_scaled)
print("\nJumlah data pada setiap cluster:")
print(df["Cluster"].value_counts().sort_index())

# =======================
# SILHOUETTE SCORE
# =======================

print("\n" + "=" * 50)
print("SILHOUETTE SCORE")
print("=" * 50)
score = silhouette_score(X_scaled, df["Cluster"])
print(f"Silhouette Score : {score:.3f}")
with open("hasil/silhouette_score.txt", "w") as file:
    file.write(f"Silhouette Score : {score:.3f}")

# =================================
# MENYIMPAN HASIL CLUSTER
# =================================

df.to_csv("hasil/hasil_cluster.csv", index=False)
print("\nHasil clustering berhasil disimpan.")

# ===========================
# VISUALISASI CLUSTER
# ===========================

plt.figure(figsize=(8,6))
plt.scatter(
    df["Age"],
    df["Fare"],
    c=df["Cluster"]
)
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Hasil Clustering K-Means")
plt.grid(True)
plt.savefig("hasil/scatter_plot.png")
plt.show()
print("\nScatter Plot berhasil disimpan.")

print("\nPROGRAM SELESAI")

print("\n"+"="*55)
print("PROGRAM BERHASIL DIJALANKAN")
print("="*55)
print("File yang dihasilkan:")
print("- elbow_method.png")
print("- scatter_plot.png")
print("- hasil_cluster.csv")
print("- silhouette_score.txt")
