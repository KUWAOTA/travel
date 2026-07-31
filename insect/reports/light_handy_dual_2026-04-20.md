# エクアドル遠征向け ハンディライト調査レポート

**作成日**: 2026-04-20
**目的**: 昆虫採集（夜間ライトトラップ/樹幹叩き/獣道照射）と 素潜り魚突き（夜間海中）の両方で使うハンディライトを検討する
**購入期限**: 2026-04-28までに着荷
**対象者**: ユーザー（村田製作所エンジニア、昆虫採集＆素潜り両方実施）

---

## 0. 結論（先出し）

- **兼用は原則「非推奨」**。要件の競合が大きく、どちらかで妥協が出る。具体的には:
  - **水中用**は IP68 / 水深100m以上の完全防水・マグネティックスイッチ必須（水中で確実に切替）
  - **昆虫採集用**は陸上での軽量性・ヘッドマウント可能性・UV併用が有利
> ヘッドマウントは別で買うので、一旦手持ちライトの方を紹介して、とにかく光量がすべてらしいからそれで考えて
> UV併用はマストじゃないよ

- **ただし「1本だけ」なら**、**OrcaTorch D710 (3000lm, IP68, 150m)** か **Wurkkos DL40 (5000lm, IPX8, 100m)** が最有力。昆虫採集でも手持ち or バッグ取付で陸上使用可能。
- **ベスト構成は2本体制**:
  1. 水中魚突き専用 → **OrcaTorch D710** または **Sofirn SD05** （マグネティックスイッチ必須）
  2. 昆虫採集用 → 高光量ハンディ（**Nitecore P20iX** か **Olight Perun 2**）＋ **UV 365nmライト（Convoy S2+）** を追加
- **UVは強く推奨**。エクアドルでは夜間蛍光する甲虫（コメツキ類・サシガメ類）・蛾・サソリがよく反応する。365nmを1本加えると夜採集の成果が目に見えて変わる。

---

## 1. 兼用機（昆虫 + 水中魚突き両対応）候補

| # | 製品名 | 光量 | 防水/水深 | 重量 | スイッチ | 実売(目安) | 納期 | 備考 |
|---|---|---|---|---|---|---|---|---|
| 1 | **OrcaTorch D710** | 3000lm (Turbo)/1700/800/400 | IP68 / 150m | 約152g | サイドボタン | 約 14,000〜19,000円（Amazon.co.jp 在庫8個） | 国内発送、4/28間に合う | 21700 5000mAh付属、USB-C充電、ビーム6° スポット。定番。 |
| 2 | **Wurkkos DL40** | 5000lm/2000/800/300 | IPX8 / 150m | 約400g（電池込） | マグネティックリング | 約 10,000〜14,000円（Amazon） | 海外発送要注意。US在庫なら1週間前後 | 4×LH351D（高CRI 90）、26650×2本。陸上で重いが最強クラスの光量。 |
| 3 | **Sofirn SD05** | 3000lm / Turbo / High / Med / Low | IPX8 / 100m | 120g | マグネティックリング | 約 7,000〜9,500円（Amazon.com） | US発送。4/28まで要3〜5営業日、早めの決済推奨 | XHP50.2、21700 4000mAh。**軽量＋安価**、コスパ重視なら最適。 |
| 4 | **XTAR D36 5800II** | 5800lm(spot+flood)/4200(flood)/1600(spot) | IPX8 / 100m | 約690g | デュアルボタン+OLED | 約 22,000〜30,000円 | 国内外発送あり | 広角130°フラッド+スポット切替、9モード。**魚突き向きに極めて優秀**だが昆虫採集にはオーバースペック。 |
| 5 | **Big Blue AL2600XWP (Black Molly V)** | 2600lm（4段階） | 100m / IP表記なしだが完全防水 | 約360g | 回転スイッチ | 約 22,000〜30,000円（ダイビング専門店） | ダイビング専門店経由。国内在庫ありの店舗なら4/28間に合う | 120°超広角、赤LED併用、26650。**ダイビング定番**だが光量は控えめ。 |

### 兼用ジャッジ

- **昆虫採集の観点**: Sofirn SD05（120g）なら軽量でハンディ運用OK。DL40/D36は重くて長時間の夜間採集には不向き。
- **魚突き観点**: すべて水深100m対応で素潜り（〜20m）には十分過ぎる。D710の6°スポットは魚探しに良いが、魚突きで広く照らしたい派には D36 か AL2600XWP のフラッド有利。
- **UV非搭載**: いずれもUV非対応。昆虫採集でUVを使いたい場合は別途必須。

---

## 2. 別々プラン（推奨構成）

### 2-1. 昆虫採集専用ハンディ（高光量・軽量・長時間）

| # | 製品名 | 光量 | 重量 | 防水 | 電池 | 実売(目安) | 納期 | 特徴 |
|---|---|---|---|---|---|---|---|---|
| A | **Nitecore P20iX** | 4000lm/2000/1000/500/200/50 | 約158g（電池込） | IP68（1m防水） | 21700 5000mAh | 約 17,000〜20,000円 | Amazon.co.jp / nitecorestore 4/28OK | 4LED、スポット221mスロー。瞬時Turbo/Strobe、戦術運用向き。樹幹叩きに最適。 |
| B | **Fenix PD36R V2.0** | 1700lm/800/350/150/30 | 約151g | IP68 / 2m | 5000mAh 21700付属 | 約 12,000〜16,000円 | 国内発送OK | 396mスロー、18W USB-C充電、**タフで信頼性高い**。獣道照射向き。 |
| C | **Olight Perun 2** | 2500lm/1000/500/120/15/1 | 約111g | IPX8 / 2m | 21700 4000mAh | 約 14,000〜16,000円 | Olight公式/Amazon、4/28OK | **L字型**でヘッドマウント・マグネット吸着両対応。近接センサー、手持ち+ヘッドライト切替OK。**昆虫採集にはこれが最有力**。 |
| (参考) | SOFIRN IF19 | 2000lm（Turboは短時間） | 約80g | IPX8 / 2m | 21700 | 約 5,500〜7,000円 | Amazon経由 | 461m超ロングスロー、**最安クラス**。サブ機や予備向き。 |

**推奨**: **Olight Perun 2** を第一候補。軽量（111g）でL字型ヘッドマウント可能、両手を空けられる昆虫採集用途にベスト。マグネット吸着でテント/車内作業も便利。

### 2-2. 水中魚突き専用ライト（高光量・深度対応・手銛ホルダー互換）

| # | 製品名 | 光量 | 水深 | 重量 | スイッチ | 実売(目安) | 納期 | 手銛ホルダー互換 |
|---|---|---|---|---|---|---|---|---|
| X | **OrcaTorch D710** | 3000lm/1700/800/400 | 150m / IP68 | 152g | サイドボタン（防水） | 約 14,000〜19,000円 | Amazon.co.jp 在庫あり | 直径φ29mm、汎用ライトホルダー対応（PVC/ゴム製）。定番サイズ。 |
| Y | **Big Blue AL2600XWP** (Black Molly V) | 2600lm | 100m | 360g | 回転スイッチ | 約 22,000〜30,000円 | ダイビング専門店 | 1インチボール標準装備、**手銛・GoProマウント直結OK**。本格派向け。 |
| Z | **Wurkkos DL40** | 5000lm | 150m | 400g | マグネティックリング | 約 10,000〜14,000円 | Amazon/US | 直径φ45mm前後、大きめホルダー要。光量No.1クラスでコスパ良し。 |
| (参考) | Kraken Sports NR-1500 | 1500lm | 100m / 330ft | 500g | プッシュボタン | 国内取扱少 → 海外発送 4/28危うい | — | **現行はNR-1800に世代交代**。現在購入は非推奨。 |

**推奨**: **OrcaTorch D710** が第一候補。軽量・Amazon.co.jp国内発送で4/28に確実に届く・汎用ホルダー互換性良し。マグネティックスイッチではないが、サイドボタンはダイビンググローブでも押せる形状で実用上問題なし。

**予算に余裕があり、魚突き本格派なら**: Big Blue AL2600XWP（赤LED付きで魚を警戒させずに近づける）。

> Big Blue AL2600XWPよさそう、5000lmより高いやつはなさそう？
> 魚突きは常に本格で。魚が逃げない色のライトがあれば他のもリストアップしてほしい

---

## 3. UV（紫外線）ライト追加の是非

### 結論: **強く推奨**

エクアドル熱帯で夜間採集する場合、UVは単なるオプションではなく**ほぼ必須装備**。理由:

- **蛾・コメツキ類・タマムシ類**: 365nm UVに強く反応、白色光より集まりが良い
- **蛍光する甲虫**: ゾウムシ類・カミキリ類の一部は紫外線下で蛍光し、暗がりでも発見容易
- **サソリ**: 夜間UV照射下で青緑蛍光、**遠くからでも視認可能**（安全面でも重要）
- **サシガメ・獣道の捕食動物の目**: UV/白色併用で発見率UP

### 365nm vs 395nm の選び方

- **365nm（真のUV-A）**: 昆虫誘引・蛍光検出とも効果最大。ただし目に見えにくく、LEDも高価。**本命推奨**。
- **395nm**: 紫色の可視光が混ざり見やすいが、昆虫誘引効果は365nmより弱い。安価。

### おすすめUVライト

| # | 製品名 | 波長 | 出力 | 電池 | 実売(目安) | 納期 | 備考 |
|---|---|---|---|---|---|---|---|
| U1 | **Convoy S2+ UV 365nm (Nichia NCSU276A / LG UV LED)** | 365nm | 約3〜6W | 18650 | 約 4,500〜7,000円 | Aliexpress/Amazon | **UV界の定番**。LGチップ版は安価・出力控えめ、Nichia版は高輝度。フィルター付き推奨（可視光カット）。 |
| U2 | **Nitecore P20i UV (White+UV)** | 365nm（UV） + 1800lm白色 | 320mW UV + 1800lm | 21700 | 約 15,000〜20,000円 | Amazon/Nitecorestore | **白＋UV一体型**。1本で両用できる。採集効率UP。荷物軽減に有利。 |
| (参考) | RovyVon Aurora A28 G2 (365nm sidelight) | 365nm補助 + 600lm白 | 小出力UV | 内蔵 | 約 8,000〜10,000円 | Amazon | コンパクト過ぎてUV出力は少なめ。メイン機能は白色EDC。予備程度。 |

**推奨**: **Convoy S2+ 365nm（Nichia版）** を基本、予算と荷物削減優先なら **Nitecore P20i UV** 1本で白＋UV両対応。

---

## 4. 最終推奨構成（4/28までに揃える前提）

### パターンA: ミニマル2本構成（コスパ最良、合計 約25,000〜30,000円）

| 用途 | 製品 | 価格 | 購入先 |
|---|---|---|---|
| 水中魚突き | OrcaTorch D710 | 約15,000円 | Amazon.co.jp（国内在庫） |
| 昆虫＋UV | Nitecore P20i UV | 約18,000円 | Amazon.co.jp / Nitecorestore |

→ 2本で昆虫採集（白+UV）＋水中を全カバー。**最も合理的**。

### パターンB: 本格3本構成（性能最大、合計 約35,000〜45,000円）

| 用途 | 製品 | 価格 |
|---|---|---|
| 水中魚突き | OrcaTorch D710 or Big Blue AL2600XWP | 15,000〜28,000円 |
| 昆虫メイン | Olight Perun 2 | 14,000円 |
| UV専用 | Convoy S2+ 365nm (Nichia) | 6,000円 |

→ 各用途で最適解、重量分散でヘッドマウント運用しやすい。

### パターンC: 兼用1本+UV（最軽量、合計 約22,000円）

| 用途 | 製品 | 価格 |
|---|---|---|
| 水中+昆虫兼用 | Sofirn SD05 (120g 軽量) | 約8,000円 |
| UV | Convoy S2+ 365nm | 約6,000円 |
| 予備 | SOFIRN IF19 | 約6,000円 |

→ 荷物を極小にしたい場合の選択。**ただし水中で昆虫採集用途と交互に使うと塩害リスクあり**、メンテ必須。

---

## 5. 購入時の注意

1. **塩水使用後は必ず真水洗浄**。Oリングに塩が残ると次回水没リスク。兼用運用ではこれが最大の弱点。
2. **予備バッテリー最低1本**を忘れず。21700/26650はエクアドル現地調達困難。
3. **マグネティックリングスイッチ**は磁気カード・電子機器に近づけない。
4. **ホルダー類**は本体と同時購入推奨。汎用PVCホルダー（約1,500円）で D710 クラスは問題なく固定。
5. **UVライトは目・皮膚に長時間当てない**。特に365nmは自覚症状なく紫外線障害を起こし得る。防塵メガネ推奨。
6. **エクアドル税関**: リチウム電池の機内持ち込みは1本100Wh以下/2本まで（航空会社により差）。21700は約18Wh、26650は約26Whで問題なし。

---

## 6. 出典URL

### 兼用・水中ライト
- [OrcaTorch D710 公式ページ](https://www.orcatorch.com/product/D710.html)
- [OrcaTorch D710 Amazon.co.jp](https://www.amazon.co.jp/ORCATORCH-D710-%E3%83%80%E3%82%A4%E3%83%93%E3%83%B3%E3%82%B0%E3%83%A9%E3%82%A4%E3%83%88-3000%E3%83%AB%E3%83%BC%E3%83%A1%E3%83%B36%E5%BA%A6%E7%8B%AD%E5%85%89%E6%9D%9F%E6%B0%B4%E4%B8%AD%E3%83%A9%E3%82%A4%E3%83%88%E3%80%81IP68%E9%98%B2%E6%B0%B4%E5%A4%9C%E9%96%93%E6%BD%9C%E6%B0%B4%E6%87%90%E4%B8%AD%E9%9B%BB%E7%81%AF150%E3%83%A1%E3%83%BC%E3%83%88%E3%83%AB%E3%82%B9%E3%82%AD%E3%83%A5%E3%83%BC%E3%83%90-%E3%82%B0%E3%83%AA%E3%83%BC%E3%83%B3/dp/B0CZ6PGX75)
- [Wurkkos DL40 公式](https://wurkkos.com/products/dl40-powerful-5000lm-diving-light)
- [Wurkkos DL40 Amazon](https://www.amazon.com/wurkkos-DL40-Flashlight-Rechargeable-Underwater/dp/B0BD6T5VQ4)
- [Wurkkos DL70 公式](https://wurkkos.com/products/wurkkos-dl70-13000lm-dive-light)
- [Sofirn SD05 公式](https://www.sofirnlight.com/products/sofirn-sd05-scuba-dive-flashlight-3000-lumens-xhp50-3v-waterproof-light-100m-underwater)
- [Sofirn SD05 Amazon](https://www.amazon.com/Sofirn-Underwater-Flashlight-Waterproof-Magnetic/dp/B0GQGDLNCG)
- [XTAR D36 5800II 公式](https://www.xtar.cc/product/xtar-d36-5800ii-dive-light.html)
- [Big Blue AL2600XWP (Black Molly V) B&H](https://www.bhphotovideo.com/c/product/1450077-REG/bigblue_al2600xwp_ii_bk_black_molly_5_2600.html)
- [Big Blue AL2600XWP DIPNDIVE](https://dipndive.com/products/big-blue-al2600xwp-2600-lumens-extra-wide-beam-led-light)
- [Kraken Sports NR-1500](https://krakensports.ca/product/nr-1500/)

### 昆虫採集用ハンディ
- [Nitecore P20iX 公式](https://flashlight.nitecore.com/product/p20ix)
- [Nitecore P20iX Amazon](https://www.amazon.com/Nitecore-Rechargeable-Tactical-Flashlight-Organizer/dp/B094YQQ9VM)
- [Fenix PD36R V2.0 公式 Fenix Lighting](https://www.fenixlighting.com/products/fenix-pd36r-rechargeable-flashlight)
- [Fenix PD36R V2.0 Amazon](https://www.amazon.com/Fenix-PD36R-Flashlight-Rechargeable-Emergency/dp/B0CJL9Y2GL)
- [Olight Perun 2 Amazon](https://www.amazon.com/OLIGHT-Rechargeable-Headlamp-Waterproof-Flashlight/dp/B0B5TML62M)
- [Sofirn IF19 Amazon](https://www.amazon.com/sofirn-Flashlight-Rechargeable-Emergency-Searching/dp/B0BQRKHHTF)

### UV 365nm
- [Convoy S2+ UV 365nm 公式](https://convoylight.com/products/convoy-s2-black-uv-365nm-18650-flashlight-with-nichia-276a)
- [Convoy S2+ UV Amazon](https://www.amazon.com/S2-Flashlight-Fluorescent-Detection-Ultraviolet/dp/B09XQX89ZK)
- [Nitecore P20i UV B&H](https://www.bhphotovideo.com/c/product/1643466-REG/nitecore_p20i_uv_rechargeable_tactical.html)
- [RovyVon Aurora A28 G2 Amazon](https://www.amazon.com/Lumens-Flashlight-Nichia-RovyVon-Sidelight/dp/B0811SRKXR)
- [365nm vs 395nm 比較（waveform.co.jp 日本語）](https://waveform.co.jp/blogs/led%E7%9F%A5%E8%AD%98/uv-led%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF%E3%83%A9%E3%82%A4%E3%83%88-365nm%E3%81%A8395nm%E3%81%AE%E9%81%95%E3%81%84%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6)

### 参考（日本の魚突き・ライトトラップ情報）
- [水中ライトの選び方（TEN LOG）](https://tensyun.net/diver-light)
- [魚突き用水中ライト選び（arashioblog）](https://arashioblog.com/underwater-light/)
- [ライトトラップ入門（灯火総研）](https://light-trap.jp/trap.html)
- [激安UV-LEDでクワガタ採集（ちょうブログ）](https://www.choublog.site/lighttrap/)
