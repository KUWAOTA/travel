# インド昆虫観察旅行・統合改訂版

作成：2026-07-31  
反映資料：`gpt_naturalist.md`、`reply/gpt.txt`、`reply/gpt2.txt`、`reply/gpt3.txt`、`reply/2934さん.txt`、`reply/kumar.txt`、既存reports、iNaturalistの現行記録

## 今回の結論

【2026-07-31修正】実際の対象種観測記録がgardenと大学の敷地内にあるというユーザー確認を最優先すると、前版の順位は逆転する。**第一候補はgarden、第二候補は大学**であり、Honey Valley、Nadugani、Fringe Fordはその後の保険・追加観測地である。

1. gardenについて、8月10日のオーナー出国前に訪問できるか、または不在時の管理者へ正式に引き継いでもらう。
2. 大学について、記録者または教員をホストとして、夜間入構・既存灯観察の承認を得る。
3. 両方の許可が取れれば、国内線と車をこの二地点に合わせて組む。
4. 片方だけ許可が取れれば、そこを3夜程度の主拠点とし、地理的に近いHoney Valley、Nadugani、Fringe Fordのいずれかを第二拠点にする。
5. どちらも許可が取れない場合のみ、Honey Valleyを本命に戻す。

最終ルートは次の決定木になる。

```text
gardenの夜間観察許可が取れたか
    ├─ Yes → gardenを8/8～9以前の最優先地点にする
    └─ No  → 不在時managerへの引継ぎ可否を確認
                 ↓
大学の正式ホスト＋夜間入構許可が取れたか
    ├─ Yes → 大学を2～3夜の主拠点にする
    └─ No  → Honey Valley 3泊へ
                 ↓
残りの日程は、地理と許可に応じてNaduganiまたはFringe Ford
```

同一敷地内の実観測記録は、広域ラベル、周辺地域の記録、一般的に良好な森林環境より強い。gardenと大学は、そこへ行けさえすれば「対象種が実際に来た照明または環境」を反復確認できる。最大の課題は生息可能性ではなく、夜間アクセスの承認である。したがって今は、宿を先に決めるより、両地点から明確なYes/Noと具体条件を得ることが先になる。

## 狙う種の整理

今回の主対象は以下でよい。

- `Odontolabis burmeisteri`（ブルマイスターツヤクワガタ）
- `Odontolabis versicolor`（ベルシコロール）
- `Odontolabis delesserti`（デレッセル）
- `Hexarthrius davisoni`（ダビソン）
- `Prosopocoilus giraffa nilgiriensis` など南インドのギラファ類

`Rhaetus westwoodi` は南インド西ガーツの主対象と同じ地理系統ではなく、既存reportsでもアルナーチャル方面の候補として扱われていた。今回の短い南インド行程に混ぜず、Ashwin氏に「別地域の情報をご存じなら将来の参考に聞きたい」と添える程度に留める。

## 追加資料で重要になった事実

### 1. Ashwin氏の価値は「記録者＋案内可能性」

`gpt3.txt` では、Ashwin氏がクワガタの複数記録を持ち、案内にも前向きで、Honey Valley周辺でOdontolabisを見たことがあるという文脈になっている。iNaturalist上でも `ashwinv` はYevakapadiで2021年8月21日に `O. burmeisteri` を記録している。[該当記録](https://www.inaturalist.org/observations/92542211)

これは、一般的な「Kodaguは環境がよい」という話より強い。今後Ashwin氏に聞くべきなのは広い分布論ではなく、**具体的な同行日、集合場所、移動方法、土地所有者への確認、発見方法**である。

ただし、2934さんは「自身のmoth trapや屋外灯では見ていない」「信頼できる実見情報もない」と回答している。矛盾ではなく、人物と経験が違う。計画上は、Ashwin氏の個別実見を重視しつつ、「毎年普通に見られる」とまでは一般化しない。

### 2. Naduganiは生物学的には強いが、運用面が空白

`gpt2.txt` には、ビークワ記事、`Lower Nadugani` の2022年8月成虫情報、海外のWDラベル、中国語圏の標本情報、Gudalur / Nilgiriの資料断片がまとまっている。少なくとも、Naduganiという地名が単なる環境推測ではなく、標本・飼育流通圏で具体的に残っている点は重要である。

ただし、標本販売ラベルやSNSは次の問題を持つ。

- 採集地点が広く丸められている可能性
- 違法採集や再販売を含み、情報源に連絡しにくい可能性
- 同定、年、標高、発見方法の検証が難しい
- 「Lower Nadugani」が現在の一般的な地名・宿泊地点とは限らない

したがってNaduganiを本命にする条件は、標本ラベルの追加収集ではなく、**現地で夜間観察を成立させる人または施設を一つ確保すること**である。

### 3. Mudigere / Chikmagalurは根拠が強いが、今回の導線から外れる

SCARABSの記事には、Mudigere周辺・標高約1,000mのコーヒー農園で、腐朽した大木の下から `O. burmeisteri` の大型幼虫7頭、大学の学生標本から2003年7月採集の98mm雄が確認されたとある。また、同地域のLucanidaeシーズンを5～9月とし、街灯、樹液、腐朽材を確認する観察方法が記されている。[SCARABS 85](https://scarabsnewsletter.com/scarabs_85.pdf)

これは生息環境を考えるうえで非常に有用で、「低地だけ」ではなく、**中標高の湿潤なコーヒー農園＋在来シェードツリー＋大きな腐朽材**というモデルを支持する。一方、Kannur―Kodagu―Wayanad / Nilgiriの導線からMudigereへ足すと移動負担が大きい。Ashwin氏が具体日と合法な観察場所を用意できる場合に限り、北部ルート全体と入れ替える候補であり、三つ目の拠点として足さない。

### 4. IISER Thiruvananthapuramは観測記録があるため生物学的な本命

大学敷地内に対象種の実観測記録があるなら、観察者バイアスは「記録数をそのまま個体密度とみなさない」という注意に留まる。候補地としての価値を下げる理由にはならない。常設街灯を毎夜同じ条件で確認できるため、許可さえ取れれば森林ロッジより再現性が高い可能性がある。一方、IISER TVMの公開ルールでは、学生が招く一般ゲストは原則5:00～22:00、24時間前までの申請とホストが必要で、研究室訪問には教員の事前許可が必要である。[Visitors Entry Request](https://dosa.iisertvm.ac.in/rules-notices/visitors-entry-request)

よって、大学は「門前の街灯を勝手に見る場所」ではない。次の四つが教員または正式なホストから確認できた場合だけ候補になる。

1. 外国人ゲストの入構手続き
2. 日没後の観察時間と退出時刻
3. 既存灯周辺の写真撮影可否
4. UV灯・白幕を使わない場合／使う場合のそれぞれの可否

正式なホストと18時以降の入構が取れれば、北部ルートを短縮してでも優先する価値がある。22時退出でも、日没後2～3時間の既存灯巡回は可能である。まずライトトラップの許可ではなく、**過去に対象種が記録された既存街灯を、記録者と一緒に確認できるか**を聞く。

### 5. gardenは最優先の訪問先

実際の対象種記録がgarden内にあるなら、gardenは最優先の訪問先である。オーナー本人が8月10日から海外へ行くため、可能なら8月8日または9日に訪問する。日程が合わない場合は、まずWhatsAppで連絡し、画像を示して頻度を聞くと同時に、不在時の管理者へ会話を引き継いでもらう。

出国前に回収すべき情報は次の順である。

1. 写真の種を、そのgarden内で本人が見たか
2. 年に何回程度、何月、何時、どの天候で見るか
3. 街灯、建物の壁、地面、樹木のどこで見たか
4. 同じ個体・同じ日の連続写真ではなく、独立した複数回の記録か
5. 8月10日以降に対応できるmanager、caretaker、gardener、security担当を紹介できるか
6. その人から夜間入場と撮影の許可を取れるか

本人が不在でも管理者が受入可能なら最優先候補のままである。可能であれば「観測された街灯・建物周辺をmanagerが案内する」「到着時にsecurityへ伝える」「何時まで観察できるか」をオーナー、管理者、自分の三者WhatsAppで確定させる。

## 候補地の再評価

採点は「生息・対象種根拠40点」「8月との一致15点」「現地協力者・許可25点」「移動効率10点」「雨天代替10点」。

| 順位 | 地域 | 生息根拠 | 実行性 | 総合 | 判断 |
|---:|---|---:|---:|---:|---|
| 1 | garden | 40/40 | 許可待ち | 95/100相当 | 同一敷地の実記録と常設灯がある。8/10前の訪問、またはmanagerへの引継ぎを最優先。 |
| 2 | IISER TVM | 40/40 | 正式ホスト待ち | 92/100相当 | 同一キャンパスの実記録と街灯がある。ホスト、入構、22時までの観察を確定できれば主拠点。 |
| 3 | Honey Valley / Yevakapadi / Kakkabe / Naladi | 34/40 | 38/45 | 82/100 | 周辺記録と手配体制はあるが、今回の連絡相手は対象種の再現性を確認できていない。上位二地点が不可の場合の本命。 |
| 4 | Nadugani / Lower Nadugani / Devala / Gudalur | 38/40 | 19/45 | 72/100 | 標本・記事根拠は強いが、観察できる敷地と人が未確定。 |
| 5 | Fringe Ford / Wayanad | 24/40 | 43/45 | 78/100 | 種記録より実施体制が強い保険。Shaji氏、自前UV許可、私有地が揃う。 |
| 6 | Mountain Shadows Resort / Wayanad | 34/40 | 26/45 | 73/100 | 2026年7月4日の `O. delesserti` 施設名つき記録あり。許可と料金の返答次第。 |
| 7 | Mudigere / Chikmagalur | 39/40 | 18/45 | 70/100 | 記録は強い。Ashwin氏が具体的に案内できる場合のみ入替候補。 |
| 8 | Munnar / Idukki | 32/40 | 25/45 | 67/100 | 両Odontolabisの現代記録はあるが、今回の一次候補より遠い。 |
| 9 | Kodaikanal | 28/40 | 16/45 | 53/100 | `O. delesserti`、`H. davisoni` など高地種には強いが、今回の移動日数では外す。 |

Mountain Shadowsの直近記録：[O. delesserti、2026-07-04](https://www.inaturalist.org/observations/377953380)  
Honey Valleyの施設名つき記録：[O. burmeisteri、2023-12-22](https://www.inaturalist.org/observations/194744236)  
Karnatakaのライトトラップ明記記録：[O. burmeisteri](https://www.inaturalist.org/observations/102010667)

## 最終ルート案

### Plan A：gardenと大学の両方で許可が取れる

gardenを8月8～9のどちらか、少なくともオーナー出国前に置く。その後、大学で2～3夜の観察を行う。残りは両地点から地理的に近い実績地を一つだけ加える。gardenの所在地が資料内に残っていないため、このルートの空港・移動時刻は固有名を確認してから確定する。

重要なのは、gardenと大学を「一晩ずつ顔を出す場所」にしないことである。独立した複数夜の記録がある方を2～3夜、もう一方を最低1～2夜とし、同じ街灯を反復確認する。

### Plan B：gardenまたは大学の片方だけ許可が取れる

許可が取れた実記録地点を3夜の主拠点にし、残り3夜を最も近いHoney Valley、Nadugani、Fringe Fordのいずれかに置く。遠い地点を三つ以上つながない。

### Plan C：gardenと大学の許可がどちらも取れない

| 日付 | 行程 |
|---|---|
| 8/7 | ムンバイ着、空港周辺泊 |
| 8/8 | NMI → Kannur。運転手付き車でHoney Valleyへ |
| 8/8～11 | Honey Valley 3泊。Ashwin氏／現地ナチュラリスト同行を最低1夜 |
| 8/11 | Honey Valley → Wayanad経由 → Gudalur / Nadugani。日中移動 |
| 8/11～14 | Nadugani側3泊。許可済み私有地、農園、既存灯を中心に観察 |
| 8/14 | NaduganiからKozhikode空港へ移動、Mumbaiへ戻る |
| 8/15 | ムンバイ予備日 |
| 8/16 | 夜の国際線 |

Nadugani側からはKannurへ戻るよりKozhikode空港を使う方が地理的に自然な可能性が高い。国内線は別切りなので、購入前に8月14日の直行便時刻、預託荷物、変更条件を航空会社画面で確認する。山道とモンスーンを考え、空港到着予定は出発3時間以上前に置く。

Nadugani側で「現地同行者＋合法な夜間場所」が確定すればHoney Valley＋Nadugani、確定しなければ次のHoney Valley＋Fringe Ford案を使う。

| 日付 | 行程 |
|---|---|
| 8/7 | ムンバイ着 |
| 8/8 | NMI 13:40 → CNN 15:25、Honey Valleyへ |
| 8/8～11 | Honey Valley 3泊 |
| 8/11 | Honey Valley → Fringe Ford |
| 8/11～14 | Fringe Ford 3泊、Shaji氏と観察 |
| 8/14 | Kannurへ。CNN 16:25 → BOM 18:10 |
| 8/15 | ムンバイ予備日 |
| 8/16 | 帰国 |

Kannur空港の現行時刻表には土曜のNMI→CNN `6E 793` と、金曜のCNN→BOM `6E 2012` が掲載されている。[Kannur International Airport](https://kannurairport.aero/passengers/schedules)

### 例外：Ashwin氏からMudigere／Bengaluru側の具体案が来る

次の四条件がすべて揃った場合だけPlan A/Bから乗り換える。

- 8月8～14日のうち同行できる具体日が2夜以上
- 対象種の近年の成虫実見、または再現性のある街灯・農園情報
- 私有地所有者または施設管理者の夜間観察許可
- 空港からの運転手付き車またはAshwin氏との移動方法が確定

「Bangalore周辺に可能性がある」だけでは切り替えない。SCARABS記事自体も、Bangalore市内から良好なLucanidae生息地までは数時間必要と述べている。

## 車の方針

追加資料を見ても、**自走レンタカーは不要**という結論は変わらない。必要なのは、運転手付き車と、最後の悪路で宿が用意する4WDである。

- Plan A/B：gardenと大学の正確な所在地を起点に、到着空港→実記録地点1→実記録地点2→出発空港の一方向移動にする
- Plan C：Kannur空港→Honey Valley→Nadugani→Kozhikode空港、またはKannur空港→Honey Valley→Fringe Ford→Kannur空港

Ashwin氏が同乗を提案した場合は、燃料・toll・食事・必要なら宿泊をこちらで負担する。ただし、好意の車だけを唯一の移動手段にせず、帰りの有料車を別に確保する。

## 連絡の優先順位と期限

| 期限 | 相手 | 取るべきアクション | 判定に必要な回答 |
|---|---|---|---|
| 今夜・最優先 | gardenオーナー | 写真送付、8/8～9訪問打診、頻度質問、不在時担当者の紹介依頼 | 独立記録回数、月、街灯、訪問日時、managerの連絡先 |
| 今夜・最優先 | 大学の記録者／教員 | 正式ホスト、入構申請、対象種が来た街灯の案内を依頼 | 訪問可能日、18～22時の入構、写真、同行者名 |
| 今夜 | Ashwin氏 | 一般論を終え、同行日・場所の種類・移動を具体化 | 8/8～14のどの日か、Honey Valleyか別地域か、車、土地許可 |
| 今夜 | Honey Valley / Suresh氏 | 上位候補の回答待ちとして変更可能な3泊を仮押さえ | 空室、キャンセル期限、設置場所、料金 |
| 8/1 | Nadugani / Gudalurの宿・自然写真家・農園 | 同時に3～5件照会 | 既存灯、私有地、夜間同行、2名3泊、運転手紹介 |
| 8/1 | Fringe Ford | Plan B用に3泊を仮押さえ | 料金、食事、空室、送迎、屋根のある安全な設置場所 |
| 8/1 | Mountain Shadows | 直近記録の発見状況と夜間許可を照会 | スタッフの認識、既存灯巡回、UV可否、料金 |
| 8/3夜 | 自分 | Plan AかBを確定 | Naduganiで「人＋場所」が確定したか |

## 送信文案

### Ashwin氏：次は約束を取り付ける

```text
Hello Ashwin,

Thank you again. Your observations and willingness to help are now one of the most important parts of our planning.

We are considering staying at Honey Valley for three nights, either 8–11 August or 9–12 August. Would you personally be available to join us for one or more evenings during either period? If another area where you have seen stag beetles would be substantially better, we can still change the route.

To make the booking decision, could you please tell me:

1. which dates you may be available;
2. whether we should meet at Honey Valley or another general area;
3. whether the beetles you saw were at existing lights, on the ground/road, or during a night walk;
4. whether permission from a landowner or property manager can be arranged; and
5. whether we should hire our own car and driver, or whether we could travel with you and cover all fuel, tolls and other costs.

We do not expect any guarantee of finding beetles. We only want a practical, legal and safe arrangement for photography without collecting.

Best regards,
Takuma
```

この文面は「どこがよいですか」という情報収集段階から、「いつ、どこで、どう合流するか」という予約段階へ進める。Ashwin氏がHoney ValleyではなくKadumane / Mudigere等を提案した場合も、比較に必要な情報が同じ形式で返ってくる。

### gardenオーナー：WhatsAppで写真を添付

```text
Hello [Name],

Thank you again for your help. I understand that you will be travelling abroad from 10 August, so I would like to ask a few practical questions before you leave.

I am attaching photos of the stag beetles I am especially interested in: Odontolabis burmeisteri, O. versicolor, O. delesserti, Hexarthrius davisoni and Prosopocoilus giraffa.

Have you personally seen any of these in your garden? If yes, were they seen on several separate dates, or only once? Approximately how often do you see large stag beetles in a normal monsoon season, and in which months?

Were they found near a streetlight or building light, on a wall or on the ground, or on trees during a night walk? The general situation is enough; I do not need a sensitive exact point.

Since you will be away, would it be possible to introduce me by WhatsApp to the manager, caretaker, gardener or security person who will be responsible for the property? I would like to ask whether two visitors could legally check the existing lights and photograph insects for a few hours after dark. We will not collect, handle or remove anything.

Thank you very much.
```

写真は、飼育個体や大顎型だけでなく、雌と小型雄も含む識別用コラージュにする。相手が「似た虫を見た」だけの場合は、過去写真の有無を聞き、無理に種名を誘導しない。

### Nadugani / Gudalurの宿・農園への短い照会

```text
Hello,

We are two naturalists from Japan planning to stay around Gudalur / Nadugani for three nights between 11 and 14 August. Our purpose is only to photograph stag beetles and other nocturnal insects; we will not collect, handle or remove wildlife.

Do large stag beetles such as Odontolabis or Prosopocoilus occasionally come to outdoor lights at your property or nearby during the monsoon? Have staff seen them in July or August?

If we stay with you, would we be permitted to check existing lights after dark, and could a local naturalist or staff member accompany us safely? If the owner agrees, we can also bring a small battery-powered UV light and white sheet, but we will use it only with explicit permission on private, non-protected land.

Could you also arrange a driver from Honey Valley/Kakkabe to your property and later to Kozhikode Airport?

Thank you,
Takuma Uno
```

### IISER TVM：送るなら正式なホスト確認に限定

```text
Subject: Request for advice on a short non-collecting nocturnal beetle observation visit

Dear Professor / BEE Lab,

I am a naturalist from Japan visiting India in August for non-collecting insect photography and iNaturalist documentation. I have noticed the rich nocturnal insect observations from the IISER Thiruvananthapuram campus.

I understand that the campus is not open for informal night access and that a faculty/student host and prior visitor approval are required. Would your group ever be able to host or advise two visitors for a short evening observation before 10 pm between 8 and 10 August? We would only photograph insects around existing lights unless a different method were explicitly approved. We will not capture, handle or remove insects.

If this is not possible, I completely understand. Advice about a public or private location where legal night observation is welcomed would also be very helpful.

Best regards,
Takuma Uno
```

大学は返答がなければ追撃しない。研究者に観光案内を求めるのではなく、正式な短時間訪問の可否だけを尋ねる。

## 観測戦略の修正

追加資料から、ライトだけでなく次の三方式を同格にする。

1. **既存灯巡回**：SCARABS記事ではMudigereでギラファ雄が街灯下の道路を歩いていた。
2. **樹液・樹幹探索**：日没前に大木の傷、発酵果実、樹液を確認する。
3. **地面・建物周辺の反復確認**：大型Odontolabisは灯火へ直接飛来する個体だけでなく、壁・道路・落下地点で見つかる可能性がある。

腐朽材は生息環境の確認には重要だが、今回は非採集・非捕獲である。私有地所有者とガイドの許可なく倒木を動かさない。SCARABS記事にある幼虫探索をそのまま再現する必要はない。

## 予約判断

現時点で実行すべき順序は以下である。

1. gardenオーナーに8月8～9の訪問を打診し、不在時managerも同じWhatsApp会話へ加えてもらう。
2. 大学の記録者または教員から、正式ホストと夜間入構のYes/Noを取る。
3. 両地点の所在地、観察日、対象種、発見された街灯を一覧化する。
4. 回答期限を8月2日夜とし、少なくとも片方が確定したら国内線・宿・運転手をその地点中心で購入する。
5. Honey Valleyを変更可能条件で3泊仮押さえする。
6. Ashwin氏に具体日を提示し、同行のYes/Noを取る。
7. Fringe Fordをキャンセル条件を確認したうえでPlan Cの保険にする。
8. Nadugani側は「人＋夜間場所」が得られた場合だけ採用する。

この計画の中心は、候補地の数を増やすことではない。**最低3夜を同じ地域に置き、対象種の実見者または夜間観察を合法的に成立させられる人物と一緒に動くこと**である。

## 不確実な点

- `gpt2.txt` 内のNaduganiに関する海外販売・中国語圏ラベルは、元URLが保存されておらず、この改訂では補助根拠として扱った。
- gardenの固有名、観察ID、オーナーとの実際の会話本文は資料内にない。そのため優先度は保留とした。
- `gpt3.txt` にはAshwin氏への返信案はあるが、その後の実返信全文は保存されていない。同行可能と断定せず、具体確認を最優先にした。
- 国内線時刻・空室・道路状況・雨予報は変わるため、予約時と出発48時間前に再確認する。

この四点が追加されれば、次の版では宿・車・観測夜を完全に確定した最終旅程表まで落とせる。
