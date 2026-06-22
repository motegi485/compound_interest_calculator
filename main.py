def calculate_compound_interest(principal: int, interest_rate: float, years: int) -> list[int]:
    """
    指定された年数の複利計算を行い、各年の合計金額のリストを返す
    """
    result = []
    total_amount = principal

    for _ in range(years):
        total_amount *= (1 + interest_rate / 100)
        result.append(int(total_amount))

    return result

def main():
    print("==== 金利シミュレーター ====")

    # 正しい入力が得られるまでループで質問を繰り返す
    while True:
        try:
            principal = int(input("元金を入力=> "))
            interest_rate = float(input("金利（％）を入力=> "))
            years = int(input("期間（年）を入力=> "))

            if principal < 0 or years < 0:
                print("エラー：元金と期間（年）は正の値を入力してください")
                continue

            if interest_rate <= -100:
                print("エラー：金利は-100％より大きい値を入力してください")
                continue

            break
        
        except ValueError:
            print("エラー：数値以外の文字が入力されました。正しい数値を入力してください。")
            continue


    print(f"\n====={years}年間のシミュレート結果=====")

    yearly_result = calculate_compound_interest(principal, interest_rate, years)
    digits = len(str(years))

    for i, amount in enumerate(yearly_result, start=1):
        print(f"{i:{digits}}年目の合計金額：{amount:,}円")

    print("===================================")

    

if __name__ == "__main__":
    main()
