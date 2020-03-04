# 学習用画像ペア振り分けツール

## 事前インストール

```
pip install -r requirements.txt
```
* python3環境が設定済みである前提

## 手順

- 画像の配置
  - 配置先
    - static/train_A: 元画像
    - static/train_B: GroundTruth
  - 元画像とGroundTruthは同一ファイル名ペアにする
    - ファイル名を「6桁数値.jpg(例: 000000.jpg)」とし、連番で配置する

- スクリプト実行
  ```
  python app.py
  ```

- 画像振り分け作業
  - ブラウザで「http://localhost:8888」でアクセス
  - 以下の画面が表示される
    ![flower](https://user-images.githubusercontent.com/14009787/75833590-d7b00400-5dfc-11ea-9475-21493d87e3d2.png)

- 結果
  - 「Use img」押下でsave配下に画像をコピーして次の画像へ
  - 「don't use」押下で対象画像のコピーをスキップして次の画像へ
  - 「Finished」の表示で完了

## その他

- 画像の削除考慮なし
  - コピー対象でないものをコピーしたら手動削除の必要あり
- 画像番号の指定機能なし

