from django.shortcuts import render , redirect
from django.http import HttpResponse
from mainapp.models import User_auth , Winemag

import csv , io
from django.contrib import messages


def index(request):
	val = True

	try :
		uname = request.session['uname']
	except:
		val = False

	if val :
		qs = Winemag.objects.all()
		return render(request , 'dashboard.html' , {'wine_list' : qs ,'tot_wines' : len(qs) , 'uname':uname})

	return render(request, 'index.html')

def signUp(request):
	return render(request,'signup.html')

def login(request):
   uname = "anonymous"
   if request.method == 'POST':
   		tempUser = request.POST.get("username")
   		password = request.POST.get("password")
   		valid = False
   		qs = User_auth.objects.filter(username = tempUser)
   		if len(qs) > 0 :
   			if qs[0].password == password:
   				valid = True
   		if valid :
   			request.session['uname'] = tempUser
   			uname = tempUser
   		else :
   			return redirect('../signup/')
   return redirect('../home/')

def home(request):
 	
 	val = True
 	uname = ""

 	try:
 		uname = request.session['uname']
 	except:
 		val = False

 	if(not val):
 		return redirect('../')
 	qs = Winemag.objects.all()

 	return render(request , 'dashboard.html' , {'wine_list' : qs ,'tot_wines' : len(qs) , 'uname' : uname})

def addUser(request):
 	uname = request.POST.get("username")
 	pwd = request.POST.get("password")
 	eml = request.POST.get("email")

 	User_auth.objects.create(username = uname , password = pwd , email = eml)

 	return HttpResponse("Your account has been created Successfully")

def upload_csv(request):
	return render(request,"upload_csv.html")

def import_csv(request):
	csv_file = request.FILES['file']

	if not csv_file.name.endswith('.csv'):
		messages.error(request,'not a csv file!')

	data_set = csv_file.read().decode('UTF-8')

	io_string = io.StringIO(data_set)
	next(io_string)

	for col in csv.reader(io_string ):
		try:
			_ , created = Winemag.objects.update_or_create(
				country = col[1],
				description = col[2],
				designation = col[3],
				points = col[4],
				price = col[5],
				province = col[6],
				region_1 = col[7],
				region_2 = col[8],
				variety = col[9],
				winery = col[10]
			)
		except:
			continue
	return HttpResponse("done")



def sortbyprice(request):
	res = "<table class = 'table'>"
	qs = Winemag.objects.order_by('price')

	for i in qs :
	  res += "<tr class='success lisitem'><td><a name = '"+str(i.winery)+"'>"
	  res += str(i.winery)
	  res += "</a></td> <td id = 'alrt'>"
	  res += str(i.price)
	  res += "</td></tr>"
	 
	res += "</table>"

	return HttpResponse(res)

def sortbypoints(request):
	res = "<table class = 'table'>"
	qs = Winemag.objects.order_by('-points')

	for i in qs :
	  res += "<tr class='success lisitem'><td><a name = '"+str(i.winery)+"'>"
	  res += str(i.winery)
	  res += "</a></td> <td id = 'alrt'>"
	  res += str(i.price)
	  res += "</td></tr>"
	  
	res += "</table>"

	return HttpResponse(res)

def getDesc(request):
	nam = request.GET.get('name')

	qs = Winemag.objects.filter(winery = nam)

	res = "<h3> Country : "
	res += str(qs[0].country)
	res += "</h3><br>"
	res = "<h3> Designation: "
	res += str(qs[0].designation)
	res += "</h3><br>"
	res = "<h3><b> Variety :</b> "
	res += str(qs[0].variety)
	res += "</h3><br>"
	res += "<div class = 'desc_detail'>"
	res += "<h3><u>" + str(qs[0].winery) + "</u></h3>"
	res += str(qs[0].description)
	res += "</div>"

	res += "<div class = 'row'> <div class = 'col-sm-6' bcgreen>"
	res += "<h3> Points :</h3><h1>"
	res += str(qs[0].points)
	res += "</h1></div>"

	res += "<div class = 'col-sm-6' bcred><h3> Price :</h3><h1>"
	res += str(qs[0].price)
	res += "</h1></div></div>"

	res += "<br> Regions : "
	res += str(qs[0].region_1) +" | "+ str(qs[0].region_2)

	return HttpResponse(res)

def logout(request):
	del request.session['uname']
	return redirect('../')