import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1~30日前のデータを元に、31日目のデータを予測する
# 使用する機械学習モデル：線形重回帰分析

# 以下はCSVから読み込んで単純に学習とスコア計算と結果を出しているが、
# 機械学習の基本の流れは「前処理、学習、評価」
# 前処理では欠損データがあったら、平均値や中央値で補ったり、欠損データのレコードを削除したりする
# 学習、評価では、訓練データをそのまま予測性能評価に使わず、データを訓練とテストで分割して行うのが一般的(ホールドアウト法)
# 評価では、思った通りの予測性能が出ていなかったら、チューニングを行う
# チューニングの例：データを増やす、前処理の仕方を変える、学習時の設定を変える、分析手法を変える等

# CSVから値を全部読み込んでDataFrame型の変数に格納
df = pd.read_csv('test.csv')

# 1~30日目用の配列(入力値)
tList = []
# 31日目用の配列(正解データ)
xList = []
for i in range(30, len(df)):
    tList.append(df.loc[i, '受注数'])
    xList.append([df.loc[i - 1, '受注数'],
                 df.loc[i - 2, '受注数'],
                 df.loc[i - 3, '受注数'],
                 df.loc[i - 4, '受注数'],
                 df.loc[i - 5, '受注数'],
                 df.loc[i - 6, '受注数'],
                 df.loc[i - 7, '受注数'],
                 df.loc[i - 8, '受注数'],
                 df.loc[i - 9, '受注数'],
                 df.loc[i - 10, '受注数'],
                 df.loc[i - 11, '受注数'],
                 df.loc[i - 12, '受注数'],
                 df.loc[i - 13, '受注数'],
                 df.loc[i - 14, '受注数'],
                 df.loc[i - 15, '受注数'],
                 df.loc[i - 16, '受注数'],
                 df.loc[i - 17, '受注数'],
                 df.loc[i - 18, '受注数'],
                 df.loc[i - 19, '受注数'],
                 df.loc[i - 20, '受注数'],
                 df.loc[i - 21, '受注数'],
                 df.loc[i - 22, '受注数'],
                 df.loc[i - 23, '受注数'],
                 df.loc[i - 24, '受注数'],
                 df.loc[i - 25, '受注数'],
                 df.loc[i - 26, '受注数'],
                 df.loc[i - 27, '受注数'],
                 df.loc[i - 28, '受注数'],
                 df.loc[i - 29, '受注数'],
                 df.loc[i - 30, '受注数']]
                 )

# fit関数の引数に入れるために、配列をデータフレームに変換
t = pd.DataFrame(tList, columns=['受注数'])
x = pd.DataFrame(xList, columns=['1日前',
                                 '2日前',
                                 '3日前',
                                 '4日前',
                                 '5日前',
                                 '6日前',
                                 '7日前',
                                 '8日前',
                                 '9日前',
                                 '10日前',
                                 '11日前',
                                 '12日前',
                                 '13日前',
                                 '14日前',
                                 '15日前',
                                 '16日前',
                                 '17日前',
                                 '18日前',
                                 '19日前',
                                 '20日前',
                                 '21日前',
                                 '22日前',
                                 '23日前',
                                 '24日前',
                                 '25日前',
                                 '26日前',
                                 '27日前',
                                 '28日前',
                                 '29日前',
                                 '30日前'])

# 訓練用データとテスト用データに分割(8:2)
x_train, x_test, y_train, y_test = train_test_split(
    x, t, test_size=0.2, random_state=0)

# 線形重回帰分析モデルを読み込み
model = LinearRegression()

# 訓練データを使用して重回帰分析で学習
model.fit(x_train, y_train)

# テストデータを使用して決定係数（予測性能の指標:0.0~1.0）を計算
print(model.score(x_test, y_test))

# 1日目~30日目を入力値として、予測してみる
new = [[20, 10, 30, 20, 10, 30, 20, 10, 30, 20,
       10, 30, 20, 10, 30, 20, 10, 30, 20, 10,
       30, 20, 10, 30, 20, 10, 30, 20, 10, 30]]

# 予測結果を表示
print(model.predict(new))
