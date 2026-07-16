import json

file_path = "E:/miniproject/Line Flexmessage/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# find the start and end of flexMessageJson
start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if "const flexMessageJson = {" in line:
        start_idx = i
    if "};" in line and start_idx != -1 and i > start_idx:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    new_json_str = '''            const flexMessageJson = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://res.cloudinary.com/dr13kpsqg/image/upload/v1780906367/jamine_store/products/f61q0pi0za5txez077b2.jpg"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "Arm Chair, White",
            "wrap": true,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "$49",
                "wrap": true,
                "weight": "bold",
                "size": "xl",
                "flex": 0
              },
              {
                "type": "text",
                "text": ".99",
                "wrap": true,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ]
          }
        ],
        "background": {
          "type": "linearGradient",
          "angle": "0deg",
          "startColor": "#a0d2eb",
          "endColor": "#ffffff"
        }
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "Buy Now!",
              "uri": "https://project-jamine.vercel.app/product/6a26797f946e76767a426f87"
            }
          }
        ],
        "background": {
          "type": "linearGradient",
          "angle": "0deg",
          "startColor": "#a0d2eb",
          "endColor": "#a0d2eb"
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "url": "https://res.cloudinary.com/dr13kpsqg/image/upload/v1782199356/jamine_store/products/kwc1tmuyjwypvv34y83x.jpg"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "GEFORCE RTX 5050",
            "wrap": true,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "flex": 1,
            "contents": [
              {
                "type": "text",
                "text": "$11",
                "wrap": true,
                "weight": "bold",
                "size": "xl",
                "flex": 0
              },
              {
                "type": "text",
                "text": ".99",
                "wrap": true,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ]
          }
        ],
        "background": {
          "type": "linearGradient",
          "angle": "0deg",
          "startColor": "#a0d2eb",
          "endColor": "#ffffff"
        }
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "Buy Now!",
              "uri": "https://project-jamine.vercel.app/product/6a3a343d893e790d74369aac"
            }
          }
        ],
        "background": {
          "type": "linearGradient",
          "angle": "0deg",
          "startColor": "#a0d2eb",
          "endColor": "#a0d2eb"
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://images.unsplash.com/photo-1550009158-9effb66233d9?auto=format&fit=crop&w=600&q=80"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "More Products",
            "wrap": true,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "Discover",
                "wrap": true,
                "weight": "bold",
                "size": "xl",
                "flex": 0,
                "color": "#666666"
              }
            ]
          }
        ],
        "background": {
          "type": "linearGradient",
          "angle": "0deg",
          "startColor": "#a0d2eb",
          "endColor": "#ffffff"
        }
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "See more",
              "uri": "https://project-jamine.vercel.app/"
            }
          }
        ],
        "background": {
          "type": "linearGradient",
          "angle": "0deg",
          "startColor": "#a0d2eb",
          "endColor": "#a0d2eb"
        }
      }
    }
  ]
};\n'''
    lines[start_idx:end_idx+1] = [new_json_str]
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("Success")
else:
    print("Could not find start or end index.")
