# スマホからCodexを継続する設定

PC側の設定は完了しました。

- [スマホ接続用の起動スクリプト](../../jobs/codex-phone.cmd)
- [Termiusの設定値と運用方法](../../jobs/REMOTE_CODEX_PHONE.md)

## 設定した動作

Termiusから接続すると、次のCodexセッションを直接再開します。

- セッションID: `019f63a4-1c9f-7c32-82f2-0e5bf5f8ac47`
- 対象: 現在のこの会話
- 作業ルート: `C:\Users\ukowu\Desktop\travel\jobs`
- 承認: 一切表示しない
- 書き込み: `jobs`配下のみ
- コマンドのネットワークアクセス: 有効
- Web検索: 有効

`--yolo`によるPC全体の無制限操作にはしていません。`jobs`外への書き込みが必要な操作は、許可を求めず失敗します。

## iPhoneのTermiusで一度だけ入力する設定

| 項目 | 値 |
| --- | --- |
| Label | Codex jobs |
| Address | `100.90.125.78` |
| Port | `22` |
| Username | `ukowu` |
| Password | Windowsアカウントのパスワード |
| Startup Command | `C:\Users\ukowu\Desktop\travel\jobs\codex-phone.cmd` |

以後は、このHostへ接続するだけです。フォルダ移動、Codexの起動、この会話の説明は不要です。TermiusはHostのStartup CommandでAIエージェントを自動起動できることを公式に案内しています。[Termius公式: AI agents on mobile](https://termius.com/blog/8-tips-for-using-ai-agents-on-mobile-in-termius)

## 確認済み

- PCとiPhoneは同じTailscaleネットワークへ接続済み
- PCのTailscale IPは`100.90.125.78`
- SSHサービスは実行中・自動起動
- Tailscale IPのTCPポート22へ接続可能
- SSH接続ユーザー`ukowu`とCodexセッションの所有ユーザーが一致
- 起動スクリプトからCodex CLI `0.145.0`を実行可能
- 固定したセッションIDが現在の会話であることを、最新ユーザーメッセージから確認済み
- `resume`の起動引数がCodex CLIで正常に解析されることを確認済み

Codex公式仕様上、`codex resume SESSION_ID`は保存済み会話を継続し、`-C`は作業ルート、`--ask-for-approval never`は承認なし、`--sandbox workspace-write`は作業領域内の書き込み許可を設定します。[Codex CLI command reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli)

## 制約

TermiusのiPhoneアプリ自体はPC側から操作できないため、上記Host設定だけはスマホで一度登録する必要があります。登録後の日常操作はHostをタップするだけです。

iOSがTermiusをバックグラウンド停止する場合がありますが、再接続時に同じ保存済みCodexセッションを再開します。[Termius公式: background sessions](https://support.termius.com/hc/en-us/articles/900006226306-Keep-your-Termius-sessions-alive-in-the-background)
