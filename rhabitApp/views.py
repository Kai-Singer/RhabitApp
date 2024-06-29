from django.shortcuts import render

def home(request):
  if 'user' in request.session:
    user = request.session['user']
    return render(request, 'rhabitApp/home.html', { 'name': user })
  else:
    return render(request, 'rhabitApp/home.html', { 'name': 'Bitte einloggen!' })

def login(request):
  request.session['user'] = 'User1'
  return render(request, 'rhabitApp/home.html', { 'name': 'Login Page' })

def logout(request):
  user = ''
  try:
    user = request.session['user']
    del request.session['user']
  except:
    return render(request, 'rhabitApp/home.html', { 'name': 'Bitte einloggen!' })
  return render(request, 'rhabitApp/home.html', { 'name': user + ' wurde ausgeloggt!' })