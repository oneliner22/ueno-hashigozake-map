# -*- coding: utf-8 -*-
"""Google Places (New) で各スポットの曜日別営業時間を引き、土日の行を tools/weekend_hours_log.json に書く。
build_spots.py の sat/sun を埋める・見直すための下調べ用（spots.json は書き換えない）。
使い方（リポ直下）:
  export PLACES_API_KEY=$(gcloud secrets versions access latest --secret=places-api-key --project central-bulwark-427114-j7)
  python tools/fetch_weekend_hours.py
"""
import io, json, math, os
import requests

API_KEY = os.environ["PLACES_API_KEY"]
FIELDS = ("places.id,places.displayName,places.formattedAddress,places.location,"
          "places.businessStatus,places.regularOpeningHours.weekdayDescriptions")

def dist_m(a_lat, a_lng, b_lat, b_lng):
    dy = (a_lat - b_lat) * 111000
    dx = (a_lng - b_lng) * 111000 * math.cos(math.radians(a_lat))
    return math.hypot(dx, dy)

spots = json.load(io.open("data/spots.json", encoding="utf-8"))["spots"]
out = []
for s in spots:
    r = requests.post(
        "https://places.googleapis.com/v1/places:searchText",
        headers={"X-Goog-Api-Key": API_KEY, "X-Goog-FieldMask": FIELDS},
        json={"textQuery": s["name"] + " 台東区", "languageCode": "ja", "maxResultCount": 3,
              "locationBias": {"circle": {"center": {"latitude": s["lat"], "longitude": s["lng"]},
                                          "radius": 500.0}}},
        timeout=30)
    r.raise_for_status()
    cands = []
    for p in r.json().get("places", []):
        loc = p.get("location", {})
        wk = (p.get("regularOpeningHours") or {}).get("weekdayDescriptions") or []
        cands.append({
            "name": p.get("displayName", {}).get("text"),
            "address": p.get("formattedAddress"),
            "status": p.get("businessStatus"),
            "dist_m": round(dist_m(s["lat"], s["lng"], loc.get("latitude", 0), loc.get("longitude", 0))),
            "sat": next((w for w in wk if w.startswith("土曜日")), None),
            "sun": next((w for w in wk if w.startswith("日曜日")), None),
        })
    out.append({"slug": s["slug"], "name": s["name"], "cur_sun": s.get("sun"),
                "cur_sun_note": s.get("sun_note"), "candidates": cands})
    print(s["slug"], "->", cands[0]["name"] if cands else None, flush=True)

json.dump(out, io.open("tools/weekend_hours_log.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrote tools/weekend_hours_log.json", len(out))
