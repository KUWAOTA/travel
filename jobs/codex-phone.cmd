@echo off
chcp 65001 >nul
cd /d "C:\Users\ukowu\Desktop\travel\jobs"

codex resume 019f63a4-1c9f-7c32-82f2-0e5bf5f8ac47 ^
  "Read C:\Users\ukowu\Desktop\travel\jobs\rakus\interview_context.md completely, especially '最優先で読む現在地'. Resume from the latest task, not a stale pending question. Before every interview question, show all item completion percentages, mark the target with an arrow, and state the missing information and purpose. Ask one concise Japanese question at a time and update the memo." ^
  -C "C:\Users\ukowu\Desktop\travel\jobs" ^
  --dangerously-bypass-approvals-and-sandbox ^
  --search ^
  --no-alt-screen
