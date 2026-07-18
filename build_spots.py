# -*- coding: utf-8 -*-
"""上野版スポット定義 -> data/spots.json
YouTube居酒屋動画8本(ヨウヤク堂在庫)から洗い出した上野・御徒町・湯島・鶯谷の名酒場。
videos は data/videos.json のIDを参照。
座標: 国土地理院ジオコーディングAPI実測(番地レベル)。同番地の店は微小オフセット。
sun: 日曜の営業時間(2026年7月調査、食べログ/公式サイト等)。sun_class: lunch(15時前開店)/evening/closed。
"""
import json, io

AREAS = [
    {"id": "ameyoko",    "name": "アメ横・上野駅ガード下",   "color": "#e8543f"},
    {"id": "uenoeki",    "name": "上野駅前・入谷口",         "color": "#2f9e7d"},
    {"id": "hirokoji",   "name": "上野広小路・御徒町",       "color": "#3f7fd6"},
    {"id": "yushima",    "name": "湯島",                     "color": "#e0489a"},
    {"id": "higashi",    "name": "東上野・新御徒町",         "color": "#b07d2a"},
    {"id": "uguisudani", "name": "鶯谷・根岸",               "color": "#7b5cd6"},
]

SPOTS = []
def add(slug, name, area, cat, lat, lng, approx, desc, videos, sun=None, sun_class=None, sun_note=None):
    s = {"slug": slug, "name": name, "area": area, "cat": cat,
         "lat": lat, "lng": lng, "approx": approx, "desc": desc, "videos": videos}
    if sun: s["sun"] = sun
    if sun_class: s["sun_class"] = sun_class
    if sun_note: s["sun_note"] = sun_note
    SPOTS.append(s)

# ---- アメ横・上野駅ガード下 ----
add("daitoryo-honten", "もつ焼 大統領 本店", "ameyoko", "もつ焼き・焼き鳥", 35.710354, 139.774841, False,
    "昭和24〜25年創業、上野に来たら外せない超有名店（上野6-10-14 ガード下）。馬肉を使ったあっさり味の「もつ煮込み」（420円〜500円）や1本90円〜の香ばしいもつ焼きが絶品で、ホッピーやレモンサワーが進む。予算2,000円以下で大満足。混雑回避は開店直後か21時以降。",
    ["JTP89EctfbA", "Hj2dpTKIzog", "ScQoJ2IuCMQ", "NADn-gXE8sU", "1fg5Mc6ypBI"],
    sun="10:00〜23:30", sun_class="lunch", sun_note="無休。閉店時刻は情報源により揺れあり")
add("daitoryo-shiten", "もつ焼 大統領 支店", "ameyoko", "もつ焼き・焼き鳥", 35.710377, 139.775269, False,
    "本店が満席のときに重宝する席数多めの支店（上野6-13-2、肉の大山の隣）。とろっとした食感の「ユッケ」や甘辛いタレの「しろたれ焼き」（150円）、特製煮込み（420円）が人気。レモンサワーは中身（焼酎）だけの追加注文でお得に2杯目を飲める。",
    ["JTP89EctfbA", "xDaX4Xal_PU"],
    sun="10:00〜23:30", sun_class="lunch", sun_note="無休")
add("takioka", "たきおか（上野1号店）", "ameyoko", "せんべろ・立ち飲み", 35.710316, 139.775238, False,
    "上野最強クラスの「せんべろ」立ち飲み店（上野6-9-14）。酎ハイ250円、ホロホロの牛煮込み300〜400円、マグロ刺し350円と驚きの安さで、注文から数十秒で料理が出てくるスピード感も魅力。ほとんどのメニューがワンコイン以内。",
    ["JTP89EctfbA", "RfMoyKVIty4"],
    sun="7:00〜23:30", sun_class="lunch", sun_note="無休。朝7時から飲める")
add("kadokura", "立飲み カドクラ", "ameyoko", "せんべろ・立ち飲み", 35.710331, 139.775436, False,
    "外でも立ち飲みが楽しめる開放的で活気あふれる人気店（上野6-13-1）。名物の「ハムカツ」（320円・チーズ入りはとろ〜り溢れ出る）、ほろほろの「牛すじ煮込み」、肉野菜炒め（400円）が人気。予算1,500円ほどで気軽に楽しめる。",
    ["NADn-gXE8sU", "1fg5Mc6ypBI"],
    sun="11:00〜22:00", sun_class="lunch", sun_note="年中無休。金土祝前日は23:00まで")
add("ohyama", "肉の大山 上野店", "ameyoko", "せんべろ・立ち飲み", 35.710377, 139.775335, False,
    "お肉屋さん直営で店頭立ち飲みができる店（上野6-13-2）。「やみつきコロッケ」（70円）やジューシーな荒挽き「やみつきメンチ」（130円）を片手に、「下町のピンドン」ことバイスサワーを流し込むのが最高。",
    ["xDaX4Xal_PU"],
    sun="11:00〜22:00", sun_class="lunch", sun_note="年中無休（元旦除く）。平日は23:00まで")
add("kacchan", "天ぷら酒場 かっちゃん", "ameyoko", "せんべろ・立ち飲み", 35.711117, 139.775040, False,
    "上野駅高架下の天ぷら立ち飲み（上野6-12-13）。1,200円の「せんべろセット」で天ぷら盛り合わせとサイコロ4個（最大4杯分のドリンク）が付く抜群のコスパ。締めの「一口カレー」も人気。※動画内では「がっちゃん」と紹介されているが正式名は「かっちゃん」。",
    ["RfMoyKVIty4"],
    sun="11:00〜21:45", sun_class="lunch", sun_note="年中無休")
add("hamachan", "地魚屋台 浜ちゃん 上野店", "ameyoko", "天ぷら・海鮮", 35.710358, 139.775101, False,
    "大統領の斜め向かいにある天ぷらと海鮮の店（上野6-9-13）。天ぷらはほとんどが100円台と激安で、大ぶりの穴子や海苔明太子、紅生姜、とろっとろのナス（150円）が人気。「大根おろし」が無料・食べ放題で、天つゆにたっぷり入れて贅沢に味わえる。ホッピーセット440円。",
    ["NADn-gXE8sU", "xDaX4Xal_PU"],
    sun="11:30〜23:00", sun_class="lunch", sun_note="無休。開店時刻は情報源により10:00〜11:30と揺れあり")
add("toribancho", "鳥番長 上野店", "ameyoko", "もつ焼き・焼き鳥", 35.709549, 139.776245, False,
    "焼き鳥や唐揚げ、ボリューム満点の「鳥丸焼き」が名物の居酒屋（上野6-7-18・昭和通り沿い）。炭火で香ばしく焼き上げる「鶏肉の七輪焼き」もがっつり食べたい人におすすめ。",
    ["JTP89EctfbA"],
    sun="11:30〜23:30", sun_class="lunch", sun_note="土日祝は昼から。平日は17:00開店")
add("hokuhan", "みちのく料理 北畔", "ameyoko", "老舗・郷土の味", 35.709953, 139.775909, False,
    "昭和34年創業、青森出身の初代が開いたみちのく酒場（上野6-7-10）。山菜や刺身などの北東北の味覚と、弘前の地酒「ジョッパリ」が楽しめる。歴史と旅情を感じる名店。",
    ["Hj2dpTKIzog"],
    sun="定休日", sun_class="closed", sun_note="日曜・祭日定休（8月は土曜も休み）")
add("tarumatsu", "たる松 本店", "ameyoko", "老舗・郷土の味", 35.708794, 139.775177, False,
    "昭和29年創業（上野6-4-13）。「東京で良質な樽酒を飲ませる店」として始まり、杉の香りが広がる樽酒を升で楽しめる。",
    ["Hj2dpTKIzog"],
    sun="定休日", sun_class="closed", sun_note="日曜定休（公式サイト）")
add("cocktailworks", "COCKTAIL WORKS 上野", "ameyoko", "バー・ビストロ", 35.709949, 139.776276, False,
    "クラシックな空間で本格カクテルを静かに楽しむバー（上野6-7-15）。シンガポール・ラッフルズホテルのレシピを忠実に再現した「シンガポールスリング」が名物。デートの2軒目に最適。",
    ["ScQoJ2IuCMQ"],
    sun="17:30〜翌2:30", sun_class="evening", sun_note="年末年始のみ休み")

# ---- 上野駅前・入谷口 ----
add("butabazaar", "東京豚バザール", "uenoeki", "個性派・バル・中華", 35.712360, 139.777695, False,
    "上野駅徒歩1分（上野7-3-2 上野TSDビル5F）。富士の麓で育ったプレミアムポーク「ルイビ豚」を溶岩焼きやしゃぶしゃぶで堪能できる。カウンター席もありカジュアルなデートにもおすすめ。",
    ["mfLOWcJThd8"],
    sun="16:00〜22:30", sun_class="evening", sun_note="土日祝はディナーのみ")
add("seiseihanten", "晴々飯店", "uenoeki", "個性派・バル・中華", 35.714684, 139.779556, False,
    "上野駅入谷口徒歩2分のテレビでも話題の本格四川中華（上野7-8-16）。驚くほどのボリュームとリーズナブルな価格が魅力で、3,300円の食べ飲み放題コースもある。",
    ["mfLOWcJThd8"],
    sun="定休日", sun_class="closed", sun_note="日曜定休。月〜土は11:00〜15:00/17:00〜23:00")
add("lecrin", "ブラッスリー・レカン", "uenoeki", "バー・ビストロ", 35.713696, 139.776917, False,
    "上野駅直結、かつての上野駅貴賓室の跡地を利用した格調高いフレンチ（アトレ上野 レトロ館1F）。天井が高くラグジュアリーな空間ながらランチは2,500円からコースを楽しめる。※現在は「The Arts Fusion by L'écrin」としてリニューアル営業。",
    ["mfLOWcJThd8"],
    sun="11:00〜22:00", sun_class="lunch", sun_note="無休（アトレ上野に準ずる）。閉店時刻は情報源により揺れあり")
add("santaro", "街かど酒場 さんたろう", "uenoeki", "個性派・バル・中華", 35.712471, 139.778076, False,
    "「大人のサイゼ」と親しまれる、ワインや洋食（ステーキ等）を格安で楽しめる大衆酒場（上野7-3-9 アルベルゴ上野1F・上野駅入谷口徒歩2分）。注文は用紙に書いて渡すシステム。ほていちゃん系列。",
    ["1fg5Mc6ypBI"],
    sun="14:00〜23:00", sun_class="lunch", sun_note="土日祝は14:00開店（平日16:00）。不定休")

# ---- 上野広小路・御徒町 ----
add("torahachi", "やきとん酒場 上野 とら八", "hirokoji", "もつ焼き・焼き鳥", 35.708340, 139.772202, False,
    "炭火焼きのやきとんが自慢の大衆酒場（上野2-2-2・上野広小路駅徒歩1分）。新鮮なレバーを軽く炙った「レバーのねぎまみれ」が一押し。お通しや席料がなくリーズナブル。",
    ["JTP89EctfbA"],
    sun="16:00〜23:00", sun_class="evening", sun_note="定休は年末年始のみ（公式サイト）")
add("tokitori", "焼き鳥 刻鳥", "hirokoji", "もつ焼き・焼き鳥", 35.706318, 139.772964, False,
    "ミシュラン獲得店出身の店主による全予約制の焼き鳥店（上野3-23-3 J-ROADビル2F・御徒町駅徒歩3分）。低温調理の肉刺身から始まり、一本一本丁寧に焼かれたジューシーな串、こだわりの親子丼までコースで堪能できる。",
    ["ScQoJ2IuCMQ"],
    sun="定休日", sun_class="closed", sun_note="日曜・祝日休み。月〜土17:00〜24:00・要予約")
add("renkon", "れんこん", "hirokoji", "個性派・バル・中華", 35.709808, 139.774292, False,
    "アメ横近く、和の趣ある3階建て一軒家風のれんこん料理専門店（上野4-9-1・上野駅徒歩2分）。食感が楽しい「れんこんと海老のはさみ揚げ」など様々な創作れんこん料理が味わえる。",
    ["mfLOWcJThd8"],
    sun="16:00〜23:00", sun_class="evening", sun_note="無休（年末年始のみ休）")
add("nagaokaya", "下町バル ながおか屋", "hirokoji", "個性派・バル・中華", 35.709248, 139.772125, False,
    "臭みのないジューシーな「ラムチョップ」が看板メニューの活気あるバル（上野2-9-5・上野駅徒歩7分）。フロアごとにワイワイ系から落ち着いたバー風まで雰囲気が異なる。",
    ["mfLOWcJThd8"],
    sun="12:00〜23:00", sun_class="lunch", sun_note="無休。金曜のみ17:00開店")
add("tamura", "焼肉 たむら 上野本店", "hirokoji", "個性派・バル・中華", 35.708569, 139.772385, False,
    "16時〜翌朝まで営業する、地元の人に愛される隠れた名店（上野2-2-7）。コリコリ旨い「テール塩焼き」（680円）や、締めに最適な「コムタンスープ」「テグタンスープ」が絶品。",
    ["RfMoyKVIty4"],
    sun="16:00〜翌5:00", sun_class="evening", sun_note="月〜土は翌9:00まで、日曜は翌5:00まで")
add("papin", "御徒町ワイン食堂パパン", "hirokoji", "バー・ビストロ", 35.705734, 139.773071, False,
    "絶品フレンチをお手頃価格で楽しめるビストロ（上野3-18-2 ふるかわビル1F）。名物の「アリゴ（チーズマッシュポテト）」や、しっとり柔らかい「牛ハラミのステーキ」はワインが進む逸品。",
    ["ScQoJ2IuCMQ"],
    sun="定休日", sun_class="closed", sun_note="日曜・祝日定休。平日16:00〜/土14:00〜")

# ---- 湯島 ----
add("dagiorgio", "da GIORGIO", "yushima", "個性派・バル・中華", 35.707527, 139.771561, False,
    "ナポリピッツァ日本大会（カプートカップ）優勝の実績を持つ名店（湯島3-37-14）。水牛モッツァレラをふんだんに使った「マルゲリータD.O.C」や、ロール状のシグニチャーピッツァ「ジョルジョ」が絶品。",
    ["ScQoJ2IuCMQ"],
    sun="11:30〜14:30 / 17:00〜22:00", sun_class="lunch", sun_note="日祝もランチ営業あり。月曜定休")
add("iwateya", "岩手屋 本店", "yushima", "老舗・郷土の味", 35.708031, 139.770767, False,
    "創業75年、岩手県盛岡市出身の創業者が開いた店（湯島3-38-8）。ひっつみ汁やドンコ汁、三陸直送の海の幸など、岩手の味覚を堪能できる。",
    ["Hj2dpTKIzog"],
    sun="定休日", sun_class="closed", sun_note="日曜・祝日定休。月〜土16:00〜22:00")
add("chanfe", "CHANFE TOKYO", "yushima", "バー・ビストロ", 35.709068, 139.771317, False,
    "ロサンゼルスで高級店を経営していた店主がオープンした大人の隠れ家バー（湯島3-44-9 地下）。ミシュラン店でしか飲めない高級ビール「ROCOCO Tokyo WHITE」や美しいカクテル、大人のためのバスクチーズケーキを提供。",
    ["ScQoJ2IuCMQ"],
    sun="17:30〜22:00", sun_class="evening", sun_note="不定休あり。一部サイトに閉店表記があるため訪問前に要確認")

# ---- 東上野・新御徒町 ----
add("torisei", "鳥清", "higashi", "もつ焼き・焼き鳥", 35.710892, 139.777817, False,
    "家族3代、半世紀以上守られてきた暖簾の老舗焼き鳥店（東上野3-17-3）。毎朝仕入れる新鮮な鶏肉を丁寧に串打ちした焼き鳥や鳥わさが絶品。",
    ["Hj2dpTKIzog"],
    sun="定休日", sun_class="closed", sun_note="日曜・祝日定休。平日17:00〜")
add("masumi", "真澄", "higashi", "老舗・郷土の味", 35.706615, 139.780960, False,
    "1955年創業、佐竹商店街近くの老舗酒場（台東4-25-2・新御徒町駅徒歩1分）。建て替え後も老舗の風格を保ち、こだわりのポテトサラダなど質の高いメニューを提供。",
    ["Hj2dpTKIzog"],
    sun="定休日", sun_class="closed", sun_note="土日祝定休")

# ---- 鶯谷・根岸 ----
add("sasanoya", "炭焼き やきとり ささのや", "uguisudani", "もつ焼き・焼き鳥", 35.720844, 139.779800, False,
    "1950年創業、うぐいすだに跨線橋のふもとで長年愛される昭和レトロな超格安やきとり店（根岸1-3-20・鶯谷駅近く）。1串90円からというリーズナブルさ。",
    ["Hj2dpTKIzog"],
    sun="定休日", sun_class="closed", sun_note="日曜・祝日定休。月〜土は15:00頃〜22:00")
add("sekisho", "居酒屋 関所", "uguisudani", "天ぷら・海鮮", 35.722263, 139.777985, False,
    "昭和49年創業。なんと「元三島神社」の社殿下ビル1階にある珍しい店（根岸1-7-3・鶯谷駅北口徒歩1分）。寿司修業を積んだ主人が握るリーズナブルな寿司や新鮮な海鮮が評判。",
    ["Hj2dpTKIzog"],
    sun="定休日", sun_class="closed", sun_note="日曜・祝日定休。月〜土16:30〜23:30")
add("shinanoji", "信濃路 鶯谷店", "uguisudani", "老舗・郷土の味", 35.722370, 139.777878, False,
    "昭和47年創業、朝7時から深夜まで営業する食堂兼酒場（根岸1-7-4・鶯谷駅北口すぐ）。夜勤明けの客などで賑わい、約100種類に及ぶ豊富なメニューが魅力。",
    ["Hj2dpTKIzog"],
    sun="7:00〜23:50", sun_class="lunch", sun_note="年中無休。朝7時から飲める")
add("kagiya", "鍵屋", "uguisudani", "老舗・郷土の味", 35.722107, 139.780365, False,
    "安政3年（江戸時代！）創業という圧倒的な歴史を誇る名店（根岸3-6-23）。絶妙な燗酒と伝統的な江戸のつまみ、落ち着いた空間が魅力。旧店舗は江戸東京たてもの園に移築されている。",
    ["Hj2dpTKIzog"],
    sun="定休日", sun_class="closed", sun_note="日曜・祝日定休。月〜土17:00〜21:00")

# ---- 出力 & バリデーション ----
videos = json.load(io.open("data/videos.json", encoding="utf-8"))
missing = [(s["slug"], v) for s in SPOTS for v in s["videos"] if v not in videos]
print("video id not found:", missing if missing else "none")
slugs = [s["slug"] for s in SPOTS]
assert len(slugs) == len(set(slugs)), "duplicate slug"
areas = {a["id"] for a in AREAS}
assert all(s["area"] in areas for s in SPOTS), "unknown area"
nosun = [s["slug"] for s in SPOTS if "sun" not in s or "sun_class" not in s]
print("spots without sunday hours:", nosun if nosun else "none")
assert all(s.get("sun_class") in ("lunch", "evening", "closed") for s in SPOTS), "bad sun_class"

json.dump({"areas": AREAS, "spots": SPOTS},
          io.open("data/spots.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("spots:", len(SPOTS), "areas:", len(AREAS),
      "videos used:", len({v for s in SPOTS for v in s['videos']}),
      "| sun lunch:", sum(1 for s in SPOTS if s["sun_class"] == "lunch"),
      "evening:", sum(1 for s in SPOTS if s["sun_class"] == "evening"),
      "closed:", sum(1 for s in SPOTS if s["sun_class"] == "closed"))
