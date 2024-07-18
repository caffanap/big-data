from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    # Membaca data dari file csv
    df = pd.read_csv('./data/dataset_wisatawan_2024.csv')
    indeks_dihapus = df.index[df.index > 38]
    
    # Menghapus baris berdasar dari indeks yang dipilih
    baris_dihapus = df.drop(index=indeks_dihapus)
    data_dipakai = baris_dihapus
    
    # hapus total asean
    hapus_asean = data_dipakai.index[data_dipakai.index == 10]
    hapus_baris = data_dipakai.drop(index=hapus_asean)
    data_final = hapus_baris

    # Visualisasi 1: Distribusi wisatawan per bulan
    df_sum = data_final.iloc[:, 1:-8].sum()
    
    # Konfersi data ke list
    data = df_sum.reset_index().values.tolist()
    
    # Mengambil data untuk x dan y
    labels = [row[0] for row in data]
    value = [row[1] for row in data]
    return render_template('dashboard.html.j2', labels=labels, values=value)