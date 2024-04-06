from openai import OpenAI
client = OpenAI(
    base_url="http://140.127.74.249:8000/v1",
    api_key="nknusumlab",
)

completion = client.chat.completions.create(
  model="Breeze-7B-Instruct-v1_0",
  messages=[
    #   在content中輸入要問的事情
    {"role": "user", "content": "請幫我將以下的問答集轉乘10個不同提問方式的問題集，格式不便 {\"id\": 1, \"paragraph\": [{\"q\": \"價值型投資法如何選股?\", \"a\": \"價值型投資法選股時需考慮以下幾點:1. 股價淨值比<1 2. 本益比適中 3. 穩定發放股利 4. 營收成長率>0 等,找出被低估的優質股票。\"}]} "}]
)

print(completion.choices[0].message)
