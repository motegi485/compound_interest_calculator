# compound-interest-calculator

元金・金利・期間から複利計算をシミュレーションするツールです。CLIとしても、Pythonライブラリとしても利用できます。

## インストール

```bash
uv add git+https://github.com/motegi485/compound_interest_calculator.git
# または
pip install git+https://github.com/motegi485/compound_interest_calculator.git
```

## 使い方

### ライブラリとして

```python
from compound_interest_calculator import calculate_compound_interest

calculate_compound_interest(principal=10000, interest_rate=5, years=3)
# => [10500, 11025, 11576]  # 各年末時点の合計金額
```

### CLIとして

```bash
uv run compound-interest-calculator
# または、リポジトリ内で
uv run main.py
```

元金・金利(%)・期間(年)を対話形式で入力すると、各年の合計金額が表示されます。

## 制限事項

- ライブラリ関数(`calculate_compound_interest`)は入力値の検証を行いません。負の元金・期間や、-100%以下の金利を渡した場合の挙動は未定義です(検証はCLI側でのみ行っています)。

## License

MIT
