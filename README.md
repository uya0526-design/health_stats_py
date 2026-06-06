# health_stats / 体調管理CSV集計CLI

![Python](https://img.shields.io/badge/Python-3.12-blue)
![pytest](https://img.shields.io/badge/pytest-9.0.3-blue)
![License](https://img.shields.io/badge/License-ISC-blue)

---

## 概要 / Overview

メニュー番号を選択して、体調管理データを読み込んで集計および表示を行う CLI ツールです。  
体調管理データは `data` フォルダ配下に「health_data.csv」という CSV ファイルとして保存してください。  
CSVのフォーマットは 使用するCSVフォーマット の項目を参照してください。

This is a CLI tool that allows you to select a menu number to load, summarize, and display your health management data.
Please save your health management data as a CSV file named "health_data.csv" in the `data` folder.
Please refer to the "CSV Format to Use" section for the CSV format.

---

## 機能 / Features

| # | 機能 / Feature |
|---|---|
| 1 | データの読み込み（再読み込み） / Loading (reloading) data |
| 2 | 体調記録を全件表示 / Display All Health Records |
| 3 | 全期間の平均・最高・最低血圧（収縮期・拡張期）の表示 / Display Average, Maximum, and Minimum Blood Pressure (Systolic and Diastolic) for the Entire Period |
| 4 | 全期間の平均・最高・最低体重の表示 / Display Average, Maximum, and Minimum Weight for the Entire Period |
| 5 | 朝（morning）／夜（evening）別の集計表示 / Display Summary by Morning/Evening |
| 6 | 終了する / Exit |

---

## Tech Stack / 技術スタック

- **言語 / Language:** Python 3.12
- **テスト / Testing:** pytest 9.0.3

---

## Project Structure / フォルダ構成

```
health_stats_py/
├── src/
│   ├── __init__.py
│   ├── main.py          # エントリーポイント / Entry point
│   └── calc.py          # CSV集計ロジック / csv calculation control logic
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

```
To be added later
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

- データの集計には `data/health_data.csv` ファイルが必要となります。  
  The `data/health_data.csv` file is required for data aggregation.
- 起動時に初回読み込みが発生します。
  An initial loading process occurs upon startup.
- 読み込みデータが0件、あるいは不正なファイル名やファイルが見つからない場合はメッセージを表示します。
  A message will be displayed if no data is found, or if there are invalid file names or no files are found.
- 不正な行はスキップしてメッセージを表示します。
  Invalid lines will be skipped and a message will be displayed.
- 朝と夜の集計にはカラム「period」を使用して判断します。
  The column "period" is used to determine the morning and evening totals.
- 集計結果は小数点第二位までを表示します。
  The aggregated results will be displayed to two decimal places.
- 朝（morning）／夜（evening）別の集計表示は血圧と体重の双方の平均、最高、最低を集計します。
  The morning/evening summary displays the average, maximum, and minimum values ​​for both blood pressure and weight.
