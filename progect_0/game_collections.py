#тренировка для модуля NumPy
# массивы
import numpy as np
mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
        -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)
print(f'mystery = {mystery}')
mystery_new =mystery.copy()

print(f'mystery = {mystery}')

nans_index = np.isnan(mystery)

print(f'nans_index = {nans_index}')

print(f'mystery = {mystery}')

print(f'nans_index = {nans_index}')
n_nan = 0
for i in nans_index:
    #print(i)
    if i == True:
        n_nan +=1
print(f'n_nan = {n_nan}')

print(f'mystery = {mystery}')

mystery_new[np.isnan(mystery_new)]=0

print(f'mystery_new = {mystery_new}')

print(f'mystery = {mystery}')

print(f'mystery_new = {mystery_new}')

mystery_int = np.int32(mystery)
print(f'mystery_int = {mystery_int}')
print(f'mystery = {mystery}')
array = np.sort(mystery)
print(f'array = {array}')

table = array.reshape((5, 3), order='F')
print(f'table = {table}')
print(table.shape)
col = table[:,1]
print(col)