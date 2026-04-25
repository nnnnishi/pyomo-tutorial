# pyomo-tutorial

数理最適化ライブラリ [Pyomo](https://www.pyomo.org/) のチュートリアル用リポジトリ。

## 概要

Pyomo は Python 上で数理最適化モデルを記述・求解するためのオープンソースライブラリ。線形計画法 (LP)、整数計画法 (MIP/IP)、非線形計画法 (NLP) などを統一的なインターフェースで扱える。

このリポジトリでは、基本的な使い方から実践的なモデリングまで段階的に学んでいく。

## 環境構築

### 必要なもの

- Python 3.10 以上
- Pyomo
- ソルバー: [HiGHS](https://highs.dev/) (`highspy`、pip で入る LP/MIP ソルバー)

### インストール

```bash
uv add pyomo highspy
```

Pyomo からは `SolverFactory("appsi_highs")` で呼び出せる。

### 動作確認

```bash
uv run python 01_linear_system.py
```

## 参考リンク

- [Pyomo 公式ドキュメント](https://pyomo.readthedocs.io/)
- [Pyomo GitHub](https://github.com/Pyomo/pyomo)
- [Pyomo Cookbook (Jeffrey Kantor)](https://jckantor.github.io/ND-Pyomo-Cookbook/)

## ライセンス

MIT
