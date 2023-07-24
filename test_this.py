#!/usr/bin/env python3

import json
import subprocess
import html

import requests
import pyjokes
from googletrans import Translator

url = "http://192.168.122.55"

def get_joke() -> str:
  translator = Translator()
  joke = pyjokes.get_joke()
  joke_result = translator.translate(joke, dest='ru')
  return [joke, joke_result.text]

def start_opera():
  command_deploy = ["opera deploy service.yaml -i ins.json -v"]

  p = subprocess.run(command_deploy, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  with open('logs_deploy', 'wb') as file:
    file.write(p.stdout)

def stop_opera():
  command_undeploy = ["opera undeploy"]

  p = subprocess.run(command_undeploy, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  with open('logs_undeploy', 'wb') as file:
    file.write(p.stdout)

joke_texts = get_joke()

get_text = '\n\n'.join(joke_texts)
print(f"Generated :\n{get_text}")

html_text = "<br>".join(map(lambda x: f"<div>{x}</div>", joke_texts))
with open('ins.json', 'w') as file:
    json.dump({"site_text":html_text}, file)
 
start_opera()

r = requests.get(url)

r.encoding = 'utf-8'

print(f"Anekdot is in docker: {all([anek in html.unescape(r.text) for anek in joke_texts])}")

#print(html.unescape(r.text))

input(f"You can check youself: {url}"+"\nWhen you are done, press enter")

stop_opera()









