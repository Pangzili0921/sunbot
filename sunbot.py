import discord
from discord.ext import commands
import asyncio, datetime, pytz
import urllib.request
import json
import requests
from requests.models import Response
from bs4 import BeautifulSoup
import os


client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
	await client.change_presence(status=discord.Status.online, activity=discord.Game("날씨 관측중"))
	

@client.event
async def on_message(message):
	if message.content.startswith("!날씨"):
		response = requests.get(' http://api.weatherapi.com/v1/current.json?key=c4e591bed51d4deeaa0110443210611&q=Daejeon&api=yes')
		jsonObj = json.loads(response.text)
		cityName = '대전'
		w1 = jsonObj['current']['temp_c']
		w2 = jsonObj['current']['condition']['text']
		embed = discord.Embed(title="오늘의 기상정보", description= "기상청 api를 활용했습니다.", color=0x00ff00)
		# w1 변수에 str 붙여야 되는 이유 str=숫자를 문자열로 바꿔줌 w2는 안바꿔줘도 문자 이기 때문에 str을 써서 문자열로 바꿀 필요x
		embed.add_field(name="기상정보", value=cityName + '의 기온은' + str(w1) + '도 입니다. 날씨는 ' + w2 + '입니다.')
		await message.channel.send(embed=embed)


	if message.content.startswith("!한강"):
		url = 'http://hangang.dkserver.wo.tc/'
		result = requests.get(url)
		js = json.loads(result.text)
		li = (js['time'])
		li2 = (js['temp'])
		o1 = li
		o2 = li2
		embed = discord.Embed(title="실시간 한강물 온도", description= "한강 api를 활용했습니다.", color=0x00ff00)
		embed.add_field(name="한강 온도",value=str(o1) +' 기준 한강의 온도는' + str(o2) + '입니다.')
		await message.channel.send(embed=embed)

access_token=os.environ["BOT_TOKEN"]

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run(access_token)



