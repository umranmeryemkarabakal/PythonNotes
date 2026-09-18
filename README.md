# PythonNotes

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge" alt="Matplotlib" />
</p>

## Overview

Python notes from the basics up to NumPy, pandas and Matplotlib, kept as Jupyter notebooks plus a few scripts on exceptions, threading and serialization.

**Quick start:** `jupyter notebook`

## Proje hakkında

Temel Python'dan NumPy, pandas ve Matplotlib'e kadar uzanan, Jupyter defterlerinde tutulmuş notlar.

## İçerik

- `01`–`04`: veri tipleri, koşullar, döngüler, comprehension, fonksiyonlar, `*args/**kwargs`, lambda, LEGB
- `05`: OOP, kalıtım, çok biçimlilik, özel metotlar
- `06`: dosya işlemleri, hata yakalama, özyineleme
- `07`–`09`: NumPy, pandas, Matplotlib
- `10`: dosya açma modları
- `11`–`13`: `try/except/finally`, `threading`, `pickle` ile serileştirme

## Kurulum ve çalıştırma

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

```bash
jupyter notebook
```

## Dosya yapısı

```text
PythonNotes/
├── pickle/
│   ├── cities.bin
│   └── cities.bind
├── 01-DataType-Operaation-Print-String-Index-List-Dictionary-Sets-Tuples.ipynb
├── 02-Boolean-IfControls-ForLoop-Continue-Break-Fast-WhileLoop.ipynb
├── 03-Range-Enumerate-Random-Zip-ListComprehension.ipynb
├── 04-Method-Function-Args-Kwargs-Map-Filter-Lambda-Scope-LEGB.ipynb
├── 05-ClassesOOP-Inheritance-Polimorphism-Encapsulation-Abstaction-SpecialMetods.ipynb
├── 06-CreateFile-HandlingErrors-Recursion.ipynb
├── 07-numpy.ipynb
├── 08-pandas.ipynb
├── 09-Matplot.ipynb
├── 10-fileOpen.ipynb
└── … ve 3 öğe daha
```
