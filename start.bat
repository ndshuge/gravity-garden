@echo off
chcp 65001 >nul
title 重力花园启动器
cd /d "%~dp0"
echo 正在启动本地服务器...
start "" /min cmd /c "python server.py"
timeout /t 1 /nobreak >nul
echo 打开游戏...
start "" "http://127.0.0.1:14000/"
echo 如果页面没自动打开，请手动访问 http://127.0.0.1:14000/
timeout /t 3 /nobreak >nul
exit
