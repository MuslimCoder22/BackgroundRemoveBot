import requests
import logging

url = "https://background-removal.p.rapidapi.com/remove"

payload = { "image_url": "https://objectcut.com/assets/img/raven.jpg" }
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": " Your API KEY",
	"X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}
async def remove_backgraund(img_url):
	payload = f"image_url={img_url}"
	response = requests.request("POST",url, data=payload, headers=headers)
	logging.info(response.json()['response']['image_url'])
	return response.json()['response']['image_url']





