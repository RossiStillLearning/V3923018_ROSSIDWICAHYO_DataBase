#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

dataBase = mysql.connector.connect(
host = "localhost",
user = "root",
password = ""
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE D3_TI_23")


# In[4]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    dataBase = "D3_TI_23"
)

cursorObject = dataBase.cursor()

tabelmatakuliah = """CREATE TABLE MATA_KULIAH(
                        KODE_MATA_KULIAH VARCHAR(10) NOT NULL PRIMARY KEY,
                        NAMA_MATA_KULIAH VARCHAR(50) NOT NULL,
                        WAKTU DATE,
                        RUANGAN VARCHAR(10) NOT NULL,
                        SKS CHAR(5) NOT NULL
                        )"""

tabelmahasiswa = """CREATE TABLE MAHASISWA(
                    NIM VARCHAR(10) NOT NULL PRIMARY KEY,
                    NAMA_MAHASISWA VARCHAR(30) NOT NULL,
                    ALAMAT VARCHAR(255) NOT NULL,
                    MATA_KULIAH_DIIKUTI VARCHAR(10) NOT NULL,
                    NO_TELEPON CHAR(12) NOT NULL,
                    FOREIGN KEY (MATA_KULIAH_DIIKUTI) REFERENCES MATA_KULIAH(KODE_MATA_KULIAH)
                    )"""

tabeldosen = """CREATE TABLE DOSEN(
                NIP VARCHAR(20) NOT NULL PRIMARY KEY,
                NAMA_DOSEN VARCHAR(50) NOT NULL,
                MATA_KULIAH_AJAR VARCHAR(50),
                NO_TELEPON CHAR(12) NOT NULL,
                FOREIGN KEY (MATA_KULIAH_AJAR) REFERENCES MATA_KULIAH(KODE_MATA_KULIAH)
                )"""

cursorObject.execute(tabelmatakuliah)
cursorObject.execute(tabelmahasiswa)
cursorObject.execute(tabeldosen)

dataBase.commit()
dataBase.close()


# In[6]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    dataBase = "D3_TI_23"
)

cursorObject = dataBase.cursor()

insertmatakuliah = "INSERT INTO MATA_KULIAH (KODE_MATA_KULIAH, NAMA_MATA_KULIAH, WAKTU, RUANGAN, SKS) VALUES(%s, %s, %s, %s, %s)"
valuematakuliah = [
    ("MK1", "Web", "2024-03-11", "L1R1", "2"),
    ("MK2", "UI&UX", "2024-03-11", "L2R2", "1"),
    ("MK3", "Jaringan", "2024-03-11", "L3R3", "2"),
    ("MK4", "Sistem", "2024-03-11", "L1R2", "1"),
    ("MK5", "English", "2024-03-11", "L2R1", "3")
]

insertmahasiswa = "INSERT INTO MAHASISWA (NIM, NAMA_MAHASISWA, ALAMAT, MATA_KULIAH, NO_tELEPON) VALUES (%s. %s, %s, %s, %s)"
valuemahasiswa = [
    ("M01", "Rossi", "Klaten", "MK1", "089612345678"),
    ("M02", "Dwi", "Solo", "MK2", "123456789012"),
    ("M03", "Cahyo", "Madiun", "Mk3", "098765432112").
    ("M04", "Azizi", "Jakarta", "MK4", "123409876512"),
    ("M05", "Indira", "Bandung", "Mk5", "098765123456")
]

insertdosen = "INSERT INTO DOSEN (NIP, NAMA_DOSEN, MATA_KULIAH_AJAR, NO_TELEPON) VALUES (%s, %s, %s, %s)"
valuedosen = [
    ("D01", "Aldean", "MK1", "098765432123"),
    ("D02", "Tegar", "MK2", "102938476510"),
    ("D03", "Andrian", "MK3", "019287651234"),
    ("D04", "Pauline", "MK4", "098154267801"),
    ("D05", "Delwyn", "MK5", "098123457801")
]

cursorObject.executemany(insermatakuliah, valuematakuliah)
cursorObject.executemany(insertmahasiswa, valuemahasiswa)
cursorObject.exwcutemany(insertdosen, valuedosen)

dataBase.commit()
dataBase.close()


# In[8]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "D3_TI_23"
)

cursorObject = dataBase.cursor()
showmatakuliah = "SELECT * FROM MATA_KULIAH"
cursorObject.execute(showmatakuliah)
hasil = cursorObject.fetchall()

print("==>Data Tabel Mata Kuliah<==")
for x in hasil:
    print(x)

dataBase.close()


# In[9]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "D3_TI_23"
)

cursorObject = dataBase.cursor()
showmahasiswa = "SELECT * FROM MAHASISWA"
cursorObject.execute(showmahasiswa)
hasil = cursorObject.fetchall()

print("==>Data Tabel Mahasiswa<==")
for x in hasil:
    print(x)

dataBase.close()


# In[10]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "D3_TI_23"
)

cursorObject = dataBase.cursor()
showdosen = "SELECT * FROM DOSEN"
cursorObject.execute(showdosen)
hasil = cursorObject.fetchall()

print("==>Data Tabel Dosen<==")
for x in hasil:
    print(x)

dataBase.close()


# In[11]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "D3_TI_23"
)

cursorObject = dataBase.cursor()
query = """
    SELECT MATA_KULIAH.NAMA_MATA_KULIAH, MAHASISWA.NAMA_MAHASISWA, DOSEN.NAMA_DOSEN
    FROM MAHASISWA
    JOIN MATA_KULIAH ON MAHASISWA.MATA_KULIAH_DIIKUTI = MATA_KULIAH.KODE_MATA_KULIAH
    JOIN DOSEN ON DOSEN.MATA_KULIAH_AJAR = MATA_KULIAH.KODE_MATA_KULIAH
"""

cursorObject.execute(query)
hasil = cursorObject.fetchall()

for row in hasil:
    print("Mata Kuliah : ", row[0])
    print("Mahasiswa : ", row[1])
    print("Dosen : ", row[2])
    print()
    
dataBase.close()


# In[ ]:




