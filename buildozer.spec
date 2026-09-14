[app]

# 应用信息
title = VidPlayer
package.name = vidplayer
package.domain = org.vidplayer

# 源码目录（main.py、vidcore.py、vidutil.py 都在当前目录）
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf,ttc,otf

version = 1.0.0

# 依赖：python3 + kivy 界面 + ffpyplayer(含 ffmpeg 解码) + pillow(默认封面生成)
requirements = python3, kivy, ffpyplayer, pillow

# 屏幕方向：四个方向都列出 = 可自由横竖屏旋转
orientation = portrait, landscape, portrait-reverse, landscape-reverse

# 安卓权限：读取视频、写入 VidPic 封面、安卓11+管理所有文件
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, READ_MEDIA_VIDEO, READ_MEDIA_IMAGES, MANAGE_EXTERNAL_STORAGE

# 目标 SDK / 最低 SDK / 架构
android.api = 34
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

# 自动接受 SDK 协议、开启 AndroidX
android.accept_sdk_license = True
android.enable_androidx = True

# python-for-android 版本。
# 旧版 v2024.01.21 的 ffmpeg 配方是 n4.3.1（2020 年），与其配套的 NDK r25b
# 不兼容，ffpyplayer 编译会直接崩溃（主 build.log 为空就是此症状）。
# 改用 develop：ffmpeg 8.0.1 + NDK r28c，且 freetype 已改用镜像源（不再 502）。
p4a.branch = develop

# 本地配方覆盖目录：修复 develop/v2026.05.09 的 ffmpeg 配方 bug——
# `--disable-everything` 被 `flags = [...]` 误覆盖，导致 ffmpeg 全量编译所有编解码器
# → GitHub Actions 7GB 内存耗尽崩溃（主 build.log 为空）。这里用修正后的配方
# （改为 `flags += [...]`）覆盖，保留最小 mp4 编解码集。
p4a.local_recipes = ./local_recipes

# 应用图标与启动画面（可爱粉主题素材，PIL 预生成）
icon.filename = assets/icon.png
presplash.filename = assets/presplash.png

# 非全屏（保留状态栏，方便操作文件选择器）
fullscreen = 0

# 编译日志级别
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
