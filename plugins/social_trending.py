import requests

HN_URL = "https://github.com/RoCry/social-trending/releases/download/latest/hackernews.json"
def get_hn_info():
    resp = requests.get(HN_URL)
    item = resp.json()[0]
    pespective = item["ai_perspective"]
    return {
        "title": item["title"],
        "subtitle": pespective["title"],
        "summary": pespective["summary"],
        "viewpoints": pespective["viewpoints"],
    }
    

if __name__ == "__main__":
    import json
    print(json.dumps(get_hn_info()))