# 上野はしご酒MAP 〜YouTube居酒屋動画から〜

YouTubeの居酒屋・グルメ動画 8本から洗い出した上野・御徒町・湯島・鶯谷の名酒場 30軒を、
エリア別に色分けした地図＋一覧にまとめた静的サイト。
スポットをクリックすると、実際に飲み歩いている紹介動画（YouTube埋め込み）がモーダルで見られる。

公開URL: https://oneliner22.github.io/ueno-hashigozake-map/

## 構成

region-spot-map の現行テンプレ方式（ビルド工程なし）。`index.html` が `data/*.json` を実行時に fetch して描画する。

- `index.html` — スキル assets の `template-index.html` ＋上野版の差分（土日の営業フィルタ・一覧/詳細の土日営業時間表示）。
  ブックマーク／グループ／動線、出典・おすすめした人・近い順の絞り込み、新着・ランダムおすすめはテンプレ標準機能
- `data/spots.json` — エリアとスポット（出典は `sources[{type:"youtube",id}]`。上野版独自キー `sat`/`sun` と `*_class`(lunch/evening/closed/unknown)・`*_note`）
- `data/videos.json` — 出典YouTube動画（ID → タイトル/チャンネル）
- `data/config.json` — タイトル・リード文・地図中心/ズーム等
- `tools/build_spots.py` — スポット定義 → `data/spots.json`（土曜の営業時間もここ）
- `tools/fetch_weekend_hours.py` — Google Places で土日の営業時間を引く下調べ（→ `tools/weekend_hours_log.json`）
- `validate.py` — `data/*.json` の整合性チェック

## 更新手順

```
python tools/build_spots.py
python validate.py
python -m http.server 8731   # http://127.0.0.1:8731/ で確認（file:// では fetch が失敗する）
```

## 出典

スポット情報は以下のYouTube動画に基づく（動画の著作権は各チャンネルに帰属）:
酒山飲太郎チャンネル / 居酒屋の達人 by 塩見なゆ / ハーリーのグルメ / りとスポット /
たろぽんグルメ / 東京グルメ / よぉちゃんねるぅ

座標は国土地理院ジオコーディングAPI・食べログ・公式サイト等で裏取り（番地レベル）。
店名・所在が確定できないもの（例:「ごんたろう」）は「およその位置」と明記。
