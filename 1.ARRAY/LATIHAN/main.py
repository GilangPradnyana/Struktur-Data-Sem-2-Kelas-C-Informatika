import numpy as np
# # print(numpy.__version__)


ar1 = np.array([30, 60, 80, 65, 70])

# print (ar1)

# MIN MAX MEDIAN


nKecil = np.min(ar1)
print(f'Nilai Terkecil : {nKecil}')

nKecil = np.max(ar1)
print(f'Nilai Terbesar : {nKecil}')

nKecil = np.mean(ar1)
print(f'Nilai Rata-Rata : {nKecil}')


# ARRAY 2 DIMENSI

ar2 = np.array ([
  [30,40,50,60],
  [12,20,10,23]
]
                )

print(ar2[0,2])

# ARRAY 3 DIMENSI

ar2 = np.array ([
  [
    [30,50,60],
    [10,5,6],
    [30,10,20]
  ]
])

print (ar2[0,1,2]) # => 6