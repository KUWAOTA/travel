# インド遠征：これだけ見ればよい図

```mermaid
flowchart TD
    S([今すぐ連絡]) --> G{gardenに入れる？}
    G -->|8/8・8/9にオーナー同行可| G1[最優先：garden<br/>実記録あり＋街灯あり]
    G -->|本人は不在| G2{managerを紹介してもらえる？}
    G2 -->|Yes| G1
    G2 -->|No| U

    G1 --> U{大学の正式許可が取れる？}
    U -->|記録者・教員がhost<br/>夜間入構可| U1[第2優先：大学 2～3夜<br/>実記録あり＋街灯あり]
    U -->|No / 返答なし| H

    U1 --> R{残りの日程}
    H[保険：Honey Valley 3夜<br/>許可・ガイドを組みやすい] --> R
    R -->|Naduganiで案内人＋合法な場所が確定| N[Nadugani 2～3夜]
    R -->|Naduganiが未確定| F[Fringe Ford 2～3夜<br/>私有地＋Shaji＋UV可]

    classDef primary fill:#d9f2e6,stroke:#18794e,color:#102a20,stroke-width:2px;
    classDef secondary fill:#e7efff,stroke:#315ea8,color:#14213d,stroke-width:2px;
    classDef backup fill:#fff2cc,stroke:#9a6700,color:#332600,stroke-width:1px;
    classDef decision fill:#f3f4f6,stroke:#667085,color:#111827,stroke-width:1px;
    class G1,U1 primary;
    class H,N,F secondary;
    class G,G2,U,R decision;
    class S backup;
```

## 優先順位

```text
1. garden   ：実際の観測記録＋街灯あり
2. 大学     ：実際の観測記録＋街灯あり
3. Honey Valley：上の許可が取れない場合の確実な保険
4. Nadugani ：記録根拠は強いが、現地の人と合法な観察場所が未確定
5. Fringe Ford：対象種記録は弱いが、観察を実行しやすい
```

## 今日送る連絡は3件だけ

```text
garden → 8/8か8/9に訪問できるか。不在ならmanagerを紹介してほしい
大学   → 記録者／教員に、18～22時の入構と記録街灯の案内を依頼
Honey Valley → 上の返事待ちなので、変更可能な3泊だけ仮押さえ
```

## 車

```text
自走レンタカーは借りない
→ 訪問先が確定してから、空港送迎＋地点間移動を運転手付きで予約
```

判断期限は **8月2日夜**。gardenと大学のどちらかから許可が取れたら、そこを中心に国内線・宿・車を決める。
