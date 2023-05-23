import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain import LLMChain
from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp as youtube_dl

def get_title_id(url):
	options = {}
	with youtube_dl.YoutubeDL(options) as ydl:
		info_dict = ydl.extract_info(url, download=False)
		video_title = info_dict.get('title', None)
		video_id = info_dict.get('id', None)
	return [video_title, video_id]

def get_transcript(video_id):
	translist = YouTubeTranscriptApi.get_transcript(video_id)
	transcript_text = video_title
	for item in translist:
		transcript_text += item['text']	
	return transcript_text

video_title, video_id = get_title_id('https://www.youtube.com/watch?v=UF8uR6Z6KLc')
template = "Can you summarize {this}?"
llm = OpenAI(model_name="text-davinci-003")
prompt = PromptTemplate(template=template, input_variables=['this'])
chain = LLMChain(llm=llm, prompt=prompt)
input = {'this': get_transcript(video_id)}
print(chain.run(input))