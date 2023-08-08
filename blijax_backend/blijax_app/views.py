from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Text

from generate.generate import Blijax

def retrieveNews(company_name: str) -> str: pass
def retrieveStocks(company_name: str) -> str: pass
def questionsAboutCurrent(input: str) -> str: pass
def generalConversation(input: str) -> str: pass

functionList = [retrieveNews, retrieveStocks, questionsAboutCurrent, generalConversation]

blijax_model = Blijax("gpt-4", "in 5 sentences")
blijax_model.setUpChain(functionList)

# says that this function can do handle POST requests
@api_view(["POST"])
def summarize_view(request):
	
	# handle data inputs
	if request.method == "POST":
		
		# get the data and provide No value if not given
		text = request.data.get("text", None)
		
		# add it to the database and save
		new_addition = Text(text=text)
		new_addition.save()
		
		# pull the text and summarize it
		summary = blijax_model.generate(new_addition.text)
		
		# return answer & status 200 (meaning everything worked!) 
		return Response(summary, status=200)