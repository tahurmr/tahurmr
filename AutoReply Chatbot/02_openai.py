from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<Your Key Here>",
)

command = '''
[9:24 pm, 04/09/2024] طحور۔۔: Ok okk
[9:25 pm, 04/09/2024] Parthiv Koli (CSMU): https://www.codsoft.in/
[9:25 pm, 04/09/2024] Parthiv Koli (CSMU): Maja barobar Prathamesh pan internship karat aahe
[9:25 pm, 04/09/2024] Parthiv Koli (CSMU): Me Ai ghetla, Tyne Python ghetla
[10:05 pm, 04/09/2024] طحور۔۔: Achaa okk
[12:46 pm, 06/10/2024] طحور۔۔: Hechi link patv na bhaii
[12:54 pm, 06/10/2024] Parthiv Koli (CSMU): https://prodigyinfotech.dev/
[8:08 pm, 06/10/2024] Parthiv Koli (CSMU): https://internship.aicte-india.org/
[8:09 pm, 06/10/2024] Parthiv Koli (CSMU): Me ya var atta internship apply kele aahe
[8:21 pm, 06/10/2024] طحور۔۔: Achaa
[8:23 pm, 06/10/2024] Parthiv Koli (CSMU): Shortlist jhala var mail yeto
[8:23 pm, 06/10/2024] Parthiv Koli (CSMU): Pan ya madhe Kai Kai Internship la Interview pan lagto
[8:24 pm, 06/10/2024] Parthiv Koli (CSMU): Kai Kai government wale madhe Stipend pan aahe
[8:25 pm, 06/10/2024] طحور۔۔: Ohh achhaa
[8:25 pm, 06/10/2024] طحور۔۔: Tu shortlist zala ahe naa
[8:26 pm, 06/10/2024] Parthiv Koli (CSMU): 3 madhe shortlist jhalo, 2 madhun call aale hote
[8:26 pm, 06/10/2024] طحور۔۔: Interview zala kay
[8:26 pm, 06/10/2024] Parthiv Koli (CSMU): Nahi, te nantar ghenar bole
[8:26 pm, 06/10/2024] طحور۔۔: Achaa okk
[8:26 pm, 06/10/2024] Parthiv Koli (CSMU): Mag me dusre apply kele
[8:27 pm, 06/10/2024] طحور۔۔: Ok okk
[8:27 pm, 06/10/2024] Parthiv Koli (CSMU): 3rd madhe shortlist jhalo aahe, tya madhe interview nahi aahe, tar te karel
[8:27 pm, 06/10/2024] طحور۔۔: All domains wal??
[8:28 pm, 06/10/2024] Parthiv Koli (CSMU): 1st wala aahe na, tya madhe Data Analyst cha aahe
[8:28 pm, 06/10/2024] طحور۔۔: Acha
[8:29 pm, 06/10/2024] طحور۔۔: Hechya mde ahe kay te
[8:29 pm, 06/10/2024] Parthiv Koli (CSMU): Ho
[8:29 pm, 06/10/2024] طحور۔۔: Ok okk
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Tahur who speaks hindi, marathi as well as english. He is from India and is a coder. You analyze chat history and respond like Tahur"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)
