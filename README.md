# pyomo-tutorial

数理最適化ライブラリ [Pyomo](https://www.pyomo.org/) のチュートリアル用リポジトリ。

## 概要

Pyomo は Python 上で数理最適化モデルを記述・求解するためのオープンソースライブラリ。線形計画法 (LP)、整数計画法 (MIP/IP)、非線形計画法 (NLP) などを統一的なインターフェースで扱える。

このリポジトリでは、基本的な使い方から実践的なモデリングまで段階的に学んでいく。

## 環境構築

### 必要なもの

- Python 3.10 以上
- Pyomo
- ソルバー（用途に応じて）
  - **GLPK** / **CBC**: 線形・整数計画 (オープンソース)
  - **Ipopt**: 非線形計画 (オープンソース)
  - **Gurobi** / **CPLEX**: 商用 (高速、アカデミックライセンスあり)

### インストール

```bash
# uv を使う場合
uv venv
uv pip install pyomo

# pip を使う場合
python -m venv .venv
source .venv/bin/activate
pip install pyomo

# ソルバー (macOS / Homebrew)
brew install glpk
brew install coin-or-tools/coinor/cbc
brew install ipopt
```

### 動作確認

```bash
python -c "import pyomo.environ as pyo; print(pyo.__version__)"
glpsol --version
```

## チュートリアル構成 (予定)

| # | テーマ | 内容 |
|---|--------|------|
| 01 | はじめての Pyomo | 簡単な LP を ConcreteModel で書いて解く |
| 02 | 集合・パラメータ・変数 | Set / Param / Var の使い方 |
| 03 | 制約と目的関数 | Constraint / Objective、ルール関数 |
| 04 | 整数計画 | 二値変数を使った割当・選択問題 |
| 05 | 抽象モデル | AbstractModel と外部データ (DAT/JSON) |
| 06 | 古典問題集 | 輸送問題、ナップサック、施設配置、TSP |
| 07 | 非線形計画 | Ipopt を使った NLP |
| 08 | デバッグと可視化 | モデルの確認、解の取り出し、Pandas 連携 |

## 参考リンク

- [Pyomo 公式ドキュメント](https://pyomo.readthedocs.io/)
- [Pyomo GitHub](https://github.com/Pyomo/pyomo)
- [Pyomo Cookbook (Jeffrey Kantor)](https://jckantor.github.io/ND-Pyomo-Cookbook/)

## ライセンス

MIT
