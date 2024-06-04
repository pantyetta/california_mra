import pandas as pd
import matplotlib.pyplot as plt
import itertools

data_file_path = "./dataset/cal_housing.data"

df = pd.read_csv(data_file_path, header=None, names=["longitude","latitude","housingMedianAge","totalRooms","totalBedrooms","population","households","medianIncome","medianHouseValue"])

# データフレームの列数を取得
num_columns = df.shape[1]
# 列の名前を取得
columns = df.columns

# 2つずつの組み合わせを作成
combinations = list(itertools.combinations(range(num_columns), 2))

# 相関係数
corr = df.corr()
print(corr)

for i, (col1, col2) in enumerate(combinations):
    plt.figure(figsize=(7, 5))
    plt.scatter(df.iloc[:, col1], df.iloc[:, col2], marker='o', label=f'{columns[col1]} & {columns[col2]}')
    plt.title(f'{i} {columns[col1]} & {columns[col2]} {corr.iloc[col1, col2]}')
    plt.xlabel(f'{columns[col1]}')
    plt.ylabel(f'{columns[col2]}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    # 画像を保存
    plt.savefig(f'plot/{i}_{columns[col1]}_&_{columns[col2]}.png')
    plt.close()

print("save finish")