# 交通手段と航空券メモ

作成日: 2026-04-14

## 結論

- 今回の条件では、`アルナーチャル直近の空港だけで最安を追う` より、`日本 → インドの入口空港` と `インド国内線` を分けて考えた方が現実的です。
- 入口空港の優先順位は、暫定で `CCU`、次点 `GAU`、その次が `DEL` です。
- 理由は、`CCU` が国際線価格で比較的戦いやすく、かつ `HGI / DIB / GAU` への国内移動の組み立て余地があるためです。

## 暫定比較

注意:
以下は 2026-04-14 時点のオンライン検索結果ベースです。特に 2026-08-08 から 2026-08-16 のピンポイント最安は、検索サービス差と在庫変動が大きく、`参考値` として見てください。

| 優先 | ルート | 日程 | 概算 | コメント | ソース |
|---|---|---|---:|---|---|
| A | 大阪(KIX) → コルカタ(CCU) | 2026-07-26 → 2026-08-08 | ₹78,890/人 | 8月前半寄りで拾えた安値実例。今回の本番日程ど真ん中ではないが、価格感の目安として有用 | Expedia, Google Flights |
| B | 大阪(KIX) → コルカタ(CCU) | 2026-08-05 → 2026-08-25 | $755/人 | 長め休暇向け。お盆周辺を含む安値実例 | Skyscanner |
| C | 大阪市 → グワハティ(GAU) | 2026-08-08 → 2026-08-16 | Google Flights上で最安表示 `￥267,495～`、表示便は約 `￥757,080 / 2人` | 実務上は強い入口だが、今回のピンポイント検索では高い | Google Flights |
| D | 大阪(KIX) → デリー(DEL) | 2026-09-03 → 2026-09-11 | ₹41,785/人 | 参考安値。8月条件から外れるが、価格下限の参考 | Expedia, Google Flights |

## 交通戦略

### 1. 第一候補

- `日本 → CCU`
- `CCU → HGI` または `CCU → DIB`
- その後は車移動

向いている候補地:
- `Ziro - Talley Valley`
- `Roing - Mayudia - Dibang Valley`

### 2. 第二候補

- `日本 → GAU`
- その後は車で `Bhalukpong - Bomdila - Dirang` 方面へ

向いている候補地:
- `West Kameng`
- `Sessa / Eaglenest`

### 3. 第三候補

- `日本 → DEL`
- `DEL → HGI / GAU / DIB`

向いているケース:
- 国際線の価格差が大きい場合
- 国内線を別切りして総額最適化したい場合

## 現地アクセスの考え方

### Ziro / Talley Valley

- 実務上は `HGI(ホロンギ) / Naharlagun / Itanagar` 側から車で入る動線が組みやすいです。
- Talley Valley は州観光サイトでも案内があり、Ziro起点で考えるのが自然です。

### West Kameng

- `GAU` から陸路で `Bhalukpong - Bomdila - Dirang` に上がる動線が組みやすいです。
- 長距離陸路になるので、初日は `Bhalukpong` か `Bomdila` で1泊挟む前提が安全です。

### Dibang Valley

- `DIB` から `Roing - Mayudia` に入るのが素直です。
- `Anini` まで伸ばすと遠征色がかなり強くなります。

## 有休の置き方

### 推奨案

- 本命: `2026-08-07(金)` と `2026-08-17(月)` を有休候補にする
- 理由:
  金夜発や前泊、月曜着の吸収がしやすく、航空券比較の自由度が高いからです。

### 価格優先案

- `2026-08-06(木)` と `2026-08-07(金)`、または `2026-08-17(月)` と `2026-08-18(火)` を許容
- 理由:
  国際線はお盆ど真ん中を1日ずらすだけで差が出る可能性があるためです。

## 次アクション

1. Google Flights と Skyscanner で `KIX / ITM / HND / NRT` 発を同条件で再比較
2. `CCU / GAU / DEL` を入口にした総額で比較
3. PAP業者から、どの入口空港を前提にした旅程が一番組みやすいか回答をもらう

## 参照

- Google Flights GAU検索結果:
  https://www.google.com/travel/flights/search?tfs=CBwQAhojEgoyMDI2LTA4LTA4agwIAhIIL20vMGRxeXdyBwgBEgNHQVUaIxIKMjAyNi0wOC0xNmoHCAESA0dBVXIMCAISCC9tLzBkcXl3QAFAAUgBcAGCAQsI____________AZgBAQ
- Google Flights Osaka to Kolkata:
  https://www.google.com/travel/flights/flights-from-osaka-to-kolkata.html?gl=IN&hl=en
- Google Flights Osaka to New Delhi:
  https://www.google.com/travel/flights/flights-from-osaka-to-new-delhi.html?gl=IN&hl=en
- Expedia Osaka to Kolkata:
  https://www.expedia.co.in/lp/flights/kix/ccu/osaka-to-kolkata
- Expedia Osaka to Delhi:
  https://www.expedia.co.in/lp/flights/kix/del/osaka-to-delhi
- Skyscanner Osaka to India:
  https://www.skyscanner.co.nz/routes/osaa/in/osaka-to-india.html
- Talley Valley:
  https://arunachaltourism.com/talley-valley-2/
