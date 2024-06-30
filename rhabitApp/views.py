from django.shortcuts import render, redirect
from datetime import date
import os, json

def user_page(request):
  return render(request, 'rhabitApp/user_page.html', {})

def profile_page(request):
  if 'uid' in request.session:
    uid = request.session['uid']
    vars = { 'private': True }
    with open(f'data/users/{uid}.json', 'r') as file:
      vars.update(json.load(file))
    return render(request, 'rhabitApp/user_page.html', vars)
  else:
    return redirect(login_page)

def home_page(request):
  return render(request, 'rhabitApp/home_page.html', {})

def search_page(request):
  return render(request, 'rhabitApp/search_page.html', {})

def login_page(request):
  if len(request.GET) > 0:
    uname = request.GET.get('uname', '')
    pwd = request.GET.get('pwd', '')
    uid = ''
    for file in os.listdir(f'data/users/'):
      with open(f'data/users/{file}', 'r') as fileContents:
        fileContents = json.load(fileContents)
        if fileContents['name'] == uname and fileContents['pwd'] == pwd:
          uid = file.split('.')[0]
    if uid != '':
      request.session['uid'] = uid
      return redirect(profile_page)
    else:
      return render(request, 'rhabitApp/error_page.html', { 'error': 'login' })
  else:
    return render(request, 'rhabitApp/login_page.html', { 'mode': 'login'})

def signup_page(request):
  if len(request.GET) > 0:
    uname = request.GET.get('uname', '')
    email = request.GET.get('email', '')
    pwd = request.GET.get('pwd', '')
    duplicate = False
    for file in os.listdir(f'data/users/'):
      with open(f'data/users/{file}', 'r') as fileContents:
        fileContents = json.load(fileContents)
        if fileContents['name'] == uname or fileContents['email'] == email:
          duplicate = True
    if not duplicate:
      uid = 0
      for item in os.listdir('data/users'):
        item_uid = int((item.split('.')[0])[1:])
        if item_uid > uid:
          uid = item_uid
      uid = 'u' + f'000{uid + 1}'[-4:]
      newData = {
        'name': uname,
        'email': email,
        'pwd': pwd,
        'creation': date.today().strftime('%Y-%m-%d'),
        'bio': '',
        'picture': False,
        'followers': [],
        'following': [],
        'habits': [],
        'currentHabit': False
      }
      with open(f'data/users/{uid}.json', 'w') as file:
        file.write(json.dumps(newData, indent = 2))
      request.session['uid'] = uid
      return redirect(profile_page)
    else:
      return render(request, 'rhabitApp/error_page.html', { 'error': 'signup' })
  else:
    return render(request, 'rhabitApp/login_page.html', { 'mode': 'signup'})

# def home(request):
#   if 'user' in request.session:
#     user = request.session['user']
#     return render(request, 'rhabitApp/home.html', { 'name': user })
#   else:
#     return render(request, 'rhabitApp/home.html', { 'name': 'Bitte einloggen!' })

# def login(request):
#   request.session['user'] = 'User1'
#   return render(request, 'rhabitApp/home.html', { 'name': 'Login Page' })

# def logout(request):
#   user = ''
#   try:
#     user = request.session['user']
#     del request.session['user']
#   except:
#     return render(request, 'rhabitApp/home.html', { 'name': 'Bitte einloggen!' })
#   return render(request, 'rhabitApp/home.html', { 'name': user + ' wurde ausgeloggt!' })