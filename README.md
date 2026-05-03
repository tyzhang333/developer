# Film Celebration

一个简易电影节网站。最终提交时建议部署到 GitHub Pages，视频用 Google Drive 公开链接嵌入。

## 怎么跑

```bash
python3 run.py
```

打开：

```text
http://127.0.0.1:8000
```

## 配置视频

网页会读取 `config.js` 里的 Google Drive 文件 ID：

```js
window.FILM_CONFIG = {
  driveFileId: "PUT_GOOGLE_DRIVE_FILE_ID_HERE",
  filmTitle: "C0030",
};
```

## 提交网址

Colab 的 `localhost:8000` 只能临时预览，不能作为最终提交网址。最终发布看 `PUBLISH.md`。
