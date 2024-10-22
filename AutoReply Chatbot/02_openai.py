from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<Your Key Here>",
)
 
command = '''
[9:24 pm, 04/09/2024] Tahur: Ok okk
[9:25 pm, 04/09/2024] Parthiv Koli: https://www.codsoft.in/
[9:25 pm, 04/09/2024] Parthiv Koli: Maja barobar Prathamesh pan internship karat aahe
[9:25 pm, 04/09/2024] Parthiv Koli: Me Ai ghetla, Tyne Python ghetla
[10:05 pm, 04/09/2024] Tahur: Achaa okk
[12:46 pm, 06/10/2024] Tahur: Hechi link patv na bhaii
[12:54 pm, 06/10/2024] Parthiv Koli: https://prodigyinfotech.dev/
[8:08 pm, 06/10/2024] Parthiv Koli: https://internship.aicte-india.org/
[8:09 pm, 06/10/2024] Parthiv Koli: Me ya var atta internship apply kele aahe
[8:21 pm, 06/10/2024] Tahur: Achaa
[8:23 pm, 06/10/2024] Parthiv Koli: Shortlist jhala var mail yeto
[8:23 pm, 06/10/2024] Parthiv Koli: Pan ya madhe Kai Kai Internship la Interview pan lagto
[8:24 pm, 06/10/2024] Parthiv Koli: Kai Kai government wale madhe Stipend pan aahe
[8:25 pm, 06/10/2024] Tahur: Ohh achhaa
[8:25 pm, 06/10/2024] Tahur: Tu shortlist zala ahe naa
[8:26 pm, 06/10/2024] Parthiv Koli: 3 madhe shortlist jhalo, 2 madhun call aale hote
[8:26 pm, 06/10/2024] Tahur: Interview zala kay
[8:26 pm, 06/10/2024] Parthiv Koli: Nahi, te nantar ghenar bole
[8:26 pm, 06/10/2024] Tahur: Achaa okk
[8:26 pm, 06/10/2024] Parthiv Koli: Mag me dusre apply kele
[8:27 pm, 06/10/2024] Tahur: Ok okk
[8:27 pm, 06/10/2024] Parthiv Koli: 3rd madhe shortlist jhalo aahe, tya madhe interview nahi aahe, tar te karel
[8:27 pm, 06/10/2024] Tahur: All domains wal??
[8:28 pm, 06/10/2024] Parthiv Koli: 1st wala aahe na, tya madhe Data Analyst cha aahe
[8:28 pm, 06/10/2024] Tahur: Acha
[8:29 pm, 06/10/2024] Tahur: Hechya mde ahe kay te
[8:29 pm, 06/10/2024] Parthiv Koli: Ho
[8:29 pm, 06/10/2024] Tahur: Ok okk
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Tahur who speaks hindi, marathi as well as english. He is from India and is a coder. You analyze chat history and respond like Tahur"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)
