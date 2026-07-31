@echo off
chcp 65001 >nul
cd /d "C:\Users\ukowu\Desktop\travel\jobs"

codex resume 019f63a4-1c9f-7c32-82f2-0e5bf5f8ac47 ^
  "Read C:\Users\ukowu\Desktop\travel\jobs\rakus\interview_context.md and continue the interview coaching from the pending question. Reply in concise Japanese, ask one question at a time, and update the memo as new facts emerge." ^
  -C "C:\Users\ukowu\Desktop\travel\jobs" ^
  --dangerously-bypass-approvals-and-sandbox ^
  --search ^
  --no-alt-screen
