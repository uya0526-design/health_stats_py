# health_stats / 体調管理CSV集計CLI

![Python](https://img.shields.io/badge/Python-3.12-blue)
![pytest](https://img.shields.io/badge/pytest-9.0.3-blue)
![License](https://img.shields.io/badge/License-ISC-blue)

---

## 概要 / Overview

メニュー番号を選択して、体調管理データ（血圧・体重）を読み込み、集計・表示を行う CLI ツールです。  
A CLI tool that loads health data (blood pressure and weight) and aggregates and displays it by selecting a menu number.

体調管理データは `data` フォルダ配下に `health_data.csv` という CSV ファイルとして保存してください。  
Save your health data as a CSV file named `health_data.csv` in the `data` folder.

CSV のフォーマットは「使用するCSVフォーマット」の項目を参照してください。  
For the CSV format, see the "CSV Format to Use" section.

集計ロジック（`src/calc.py`）は pytest による単体テストで検証しています。  
The aggregation logic (`src/calc.py`) is verified by unit tests with pytest.

---

## 機能 / Features

| # | 機能 / Feature |
|---|---|
| 1 | データの読み込み（再読み込み） / Load (reload) data |
| 2 | 体調記録を全件表示（ヘッダー行を除く） / Display all health records (without header row) |
| 3 | 全期間の平均・最高・最低血圧（収縮期・拡張期）を表示 / Display average, max, and min blood pressure (systolic & diastolic) for the entire period |
| 4 | 全期間の平均・最高・最低体重を表示 / Display average, max, and min weight for the entire period |
| 5 | 朝（morning）／夜（evening）別の集計を表示 / Display summary by morning / evening |
| 6 | 終了する / Exit |

---

## Tech Stack / 技術スタック

- **言語 / Language:** Python 3.12
- **標準ライブラリ / Standard library:** csv
- **テスト / Testing:** pytest 9.0.3

---

## Project Structure / フォルダ構成

```
health_stats_py/
├── src/
│   ├── __init__.py
│   ├── main.py          # エントリーポイント（CLI） / Entry point (CLI)
│   └── calc.py          # CSV読み込み・集計ロジック / CSV loading & aggregation logic
├── tests/
│   ├── __init__.py
│   └── test_calc.py     # 単体テスト / Unit tests
├── data/
│   └── health_data.csv  # 体調管理データ / Health management data
├── requirements.txt     # 依存パッケージ一覧 / Dependencies
├── LEARNING_LOG.md      # 学習記録 / Learning log
└── README.md
```

---

## Getting Started / セットアップ

### 必要環境 / Prerequisites

- Python 3.12

### 1. リポジトリのクローン / Clone the repository

```bash
git clone https://github.com/uya0526-design/health_stats_py.git
cd health_stats_py
```

### 2. 仮想環境の作成と有効化 / Create and activate a virtual environment

```bash
python -m venv venv

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
```

### 3. 依存パッケージのインストール / Install dependencies

```bash
pip install -r requirements.txt
```

### 4. アプリの起動 / Run the app

```bash
python src/main.py
```

### 5. テストの実行 / Run tests

```bash
pytest
```

---

## 実行例 / Example

メニュー3（血圧の集計）を選び、その後メニュー6で終了する例です。  
An example of selecting menu 3 (blood pressure summary) and then exiting with menu 6.

```
Health Stats
-------------
1. Load Data
2. Display All Health Records without header row
3. Display Average, Maximum, and Minimum Blood Pressure (Systolic and Diastolic) for the Entire Period
4. Display Average, Maximum, and Minimum Weight for the Entire Period
5. Display Summary by Morning/Evening
6. Exit
-------------
Enter the menu number: 3
Blood Pressure (Systolic / Diastolic):
    Average: 124.83 / 79.5
    Maximum: 143 / 92
    Minimum: 107 / 68
-------------
1. Load Data
2. Display All Health Records without header row
3. Display Average, Maximum, and Minimum Blood Pressure (Systolic and Diastolic) for the Entire Period
4. Display Average, Maximum, and Minimum Weight for the Entire Period
5. Display Summary by Morning/Evening
6. Exit
-------------
Enter the menu number: 6
Exiting program...
```

---

## 使用するCSVフォーマット / CSV Format to Use

| カラム名 | 型 | 説明 |
|---|---|---|
| date | str | 測定日（YYYY-MM-DD） |
| time | str | 測定時刻（HH:MM） |
| period | str | 朝夜区分（morning / evening） |
| systolic | int | 最高血圧（mmHg） |
| diastolic | int | 最低血圧（mmHg） |
| weight | float | 体重（kg） |

---

## Notes / 注意事項

- データの集計には `data/health_data.csv` ファイルが必要です。  
  The `data/health_data.csv` file is required for data aggregation.
- 起動時に初回読み込みが行われます。メニュー1で再読み込みできます。  
  Data is loaded on startup, and can be reloaded with menu 1.
- データが0件、またはファイルが見つからない場合はメッセージを表示します。  
  A message is displayed if there is no data or the file is not found.
- 不正な行はスキップし、その旨のメッセージを表示します。  
  Invalid rows are skipped and a message is displayed.
- 朝（morning）／夜（evening）の判定にはカラム `period` を使用します。  
  The `period` column is used to determine morning / evening.
- 集計結果は小数点第二位まで表示します。  
  Aggregated results are displayed to two decimal places.
- 朝／夜別の集計は、血圧と体重の双方について平均・最高・最低を表示します。  
  The morning / evening summary shows the average, maximum, and minimum for both blood pressure and weight.
