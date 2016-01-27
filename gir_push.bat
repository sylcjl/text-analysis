git add --all
@echo 請輸入這次上傳的Commit 
@set /p var1=請輸入：
git commit -m "%var1%"
git push origin master