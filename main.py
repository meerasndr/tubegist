import os
import sys
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp as youtube_dl
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain import LLMChain

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this list based on your requirements
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
	return {"message": "Hello"}
@app.post("/video_url/")
async def send_url(url:str):
	video_title, video_id = get_title_id(url)	
	template = "Can you summarize {this}?"
	llm = OpenAI(model_name="text-davinci-003")
	prompt = PromptTemplate(template=template, input_variables=['this'])
	chain = LLMChain(llm=llm, prompt=prompt)
	input = {'this': get_transcript(video_id, video_title)}
	try:
		return {"message" : chain.run(input)}
	except:
		return {"message": "There's an unforeseen error. \nA likely cause is the video length being high. \nWe are working on supporting this. Thanks for your patience. "}

def get_title_id(url):
	options = {}
	try:
		with youtube_dl.YoutubeDL(options) as ydl:
			info_dict = ydl.extract_info(url, download=False)
			video_title = info_dict.get('title', None)
			video_id = info_dict.get('id', None)
	except:
		return "Enter a valid YouTube URL"
	return [video_title, video_id]

def get_transcript(video_id, video_title):
	try: 
		translist = YouTubeTranscriptApi.get_transcript(video_id)
		transcript_text = video_title
		for item in translist:
			transcript_text += item['text']
	except:
		return "This YouTube video does not have a transcript. It is probably a music video or uses a non-English language."
	return transcript_text

if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8000)