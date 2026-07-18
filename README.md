# 上野はしご酒MAP 〜YouTube居酒屋動画から〜

YouTubeの居酒屋・グルメ動画 8本から洗い出した上野・御徒町・湯島・鶯谷の名酒場 30軒を、
エリア別に色分けした地図＋一覧にまとめた単一HTMLサイト。
スポットをクリックすると、実際に飲み歩いている紹介動画（YouTube埋め込み）がモーダルで見られる。

公開URL: https://oneliner22.github.io/ueno-hashigozake-map/

## 構成

- `index.html` — 生成物（データ埋め込み済み単一ファイル、file:// でも動く）
- `template.html` — テンプレート（Leaflet + markercluster、YouTube埋め込みモーダル）
- `build_spots.py` — スポット定義（エリア/ジャンル/座標/説明/出典動画ID）→ `data/spots.json`
- `build_html.py` — `data/*.json` + `template.html` → `index.html`
- `data/videos.json` — 出典YouTube動画（ID → タイトル/チャンネル）
- `data/config.json` — タイトル・リード文・地図中心/ズーム等

## ビルド

```
python build_spots.py
python build_html.py
```

## 出典

スポット情報は以下のYouTube動画に基づく（動画の著作権は各チャンネルに帰属）:
酒山飲太郎チャンネル / 居酒屋の達人 by 塩見なゆ / ハーリーのグルメ / りとスポット /
たろぽんグルメ / 東京グルメ / よぉちゃんねるぅ

座標は国土地理院ジオコーディングAPI・食べログ・公式サイト等で裏取り（番地レベル）。
店名・所在が確定できないもの（例:「ごんたろう」）は「およその位置」と明記。
