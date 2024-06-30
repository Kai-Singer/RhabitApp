from django.shortcuts import render
import os, json

def user_page(request):
  return render(request, 'rhabitApp/user_page.html', {})

def profile_page(request):
  return render(request, 'rhabitApp/user_page.html', { 'private': True })

def home_page(request):
  return render(request, 'rhabitApp/home_page.html', {})

def search_page(request):
  return render(request, 'rhabitApp/search_page.html', {})

def login_page(request):
  if len(request.GET) > 0:
    uname = request.GET.get('uname', '')
    pwd = request.GET.get('pwd', '')
    uid = ''
    for file in os.listdir(f"data/users/"):
      with open(f"data/users/{file}", "r") as fileContents:
        fileContents = json.load(fileContents)
        if fileContents['name'] == uname and fileContents['pwd'] == pwd:
          uid = os.path.splitext()[0]
    if uid != '':
      request.session['uid'] = uid
      user_page(request)
    else:
      return render(request, 'rhabitApp/wrongpwd_page.html', {})
  else:
    return render(request, 'rhabitApp/login_page.html', {})

def signup_page(request):
  return render(request, 'rhabitApp/signup_page.html', {})

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