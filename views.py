from django.shortcuts import render
import requests

def hello(request):
    requests.post("https://api.groupme.com/v3/bots/post","",{"text" : "karandeep help me", "bot_id" : "28052c90156a26b1f5e499297c"})
    return render(request, "templates/hello.html", {})
