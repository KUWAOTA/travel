# スマホからCodexの会話を継続する設定

## PC側の状態

- Tailscale PCアドレス: `100.90.125.78`
- iPhone: 同じtailnetへ接続済み
- SSH: ポート22で起動済み・自動起動
- Windowsユーザー: `ukowu`
- Codex再開対象: この会話のセッションID `019f63a4-1c9f-7c32-82f2-0e5bf5f8ac47`
- 起動スクリプト: `C:\Users\ukowu\Desktop\travel\jobs\codex-phone.cmd`

## Termiusで一度だけ設定する内容

Hostを次の内容で登録する。

| 項目 | 値 |
| --- | --- |
| Label | Codex jobs |
| Address | `100.90.125.78` |
| Port | `22` |
| Username | `ukowu` |
| Password | Windowsアカウントのパスワード |
| Startup Command | `C:\Users\ukowu\Desktop\travel\jobs\codex-phone.cmd` |

Startup Commandを保存した後は、このHostへ接続するだけでCodexが起動し、この会話の続きが表示される。作業フォルダを移動するコマンドや、会話を説明するプロンプトは不要。

## Codexの権限

起動スクリプトは次の設定でCodexを再開する。

- 作業ルート: `C:\Users\ukowu\Desktop\travel\jobs`
- 承認ポリシー: `never`
- Sandbox: `workspace-write`
- コマンドのネットワークアクセス: 有効
- Web検索: 有効

このため、`jobs`配下の読み書きや通常のコマンド実行では承認画面が出ない。`jobs`の外へ書き込む操作は、承認を求めず失敗する。PC全体を無制限操作する`--yolo`は使用していない。

## 注意点

- Termiusは同じWindowsユーザー`ukowu`で接続する必要がある。別ユーザーではCodexの認証情報とセッション履歴を共有できない。
- PCの電源、Tailscale、SSHサービスが起動している必要がある。
- iOSがTermiusをバックグラウンド停止しても、再接続すれば同じCodexセッションを再開できる。
- デスクトップとスマホから同じ会話へ同時に入力しない。セッション履歴やファイル編集が競合する可能性がある。
- この会話を将来別セッションへ分岐・移行した場合は、`codex-phone.cmd`のセッションIDを更新する。
- 起動時は現在の会話セッションを再開し、`rakus\interview_context.md`を読み込んで、保留中の質問から面接対策を続ける。
