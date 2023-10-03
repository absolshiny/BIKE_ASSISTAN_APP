from django.shortcuts import render
import openai, os
from dataenv import load_dotenv
load_dotenv()

api_key=os.getenv("OPENAI_KEY", None)

def chetbot