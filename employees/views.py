from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import loginmodel,employemodel
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

#............using get method i loaded the html page for signup..................#
def emp_signup(request):
    return render(request,'employee_signup.html')






#............using post method i insert the value to database..................#
def lg(request):
    if request.method=="POST":

        a = request.POST["textfield"]
        b = request.POST["textfield2"]
        c = request.POST["ph"]
        # upload_file = request.FILES['img']
        # fs = FileSystemStorage()
        # name = fs.save(upload_file.name, upload_file)
        # url = "/media/" + upload_file.name
        # print(url)


        upload_file=request.FILES['img']
        fs=FileSystemStorage()
        fs.save(upload_file.name,upload_file)
        url2="/media/"+upload_file.name





        import random
        n = random.randint(00000000, 99999999)
        print(n)
        b1 = loginmodel(uname=a, password=n)
        b1.save()
        print(b1.id)
        m=b1.id
        print(m)
        a1 = employemodel(name=a, age=b, gen22=fs.url(url2), contact=c)
        a1.save()

        return render(request, "Homepage.html")
    else:
        return 'invalid'

def emp_home(request):
    return render(request, 'Homepage.html')

#....................after signup doing login........................
def emp_login(request):
    return render(request, 'login.html')


#........using post method cheacking the value if the value is in database.................
def empdologin(request):

        username = request.POST["textfield"]
        password = request.POST["textfield2"]

        if loginmodel.objects.filter(uname=username, password=password).exists():
            yy=loginmodel.objects.get(uname=username, password=password)
            # request["lid"]=yy.id
            print("kooyi=",yy.id)
            request.session["lid"]=yy.id
            return render(request,"Homepage.html")
        else:
            print("no")

            return render(request, "login.html")


#........using get method trying to view all employess(selecting all employeeees............)
def show(request):
    res = employemodel.objects.all()
    return render(request, "view_all_employees.html", {'res': res})


#.................editing values after viewing datas..........#
def edit(request,id):
    print("kkkkkkkkkkkkkkkkkkkkkkk")
    res = employemodel.objects.get(id=id)
    print(res)
    request.session["id"]=id
    return render(request,'emp_edit.html', {'res':res})


#....................now want an post method for editing values.........................

@csrf_exempt
def edit_post(request):
    id =  request.session["id"]

    ##date format
    # import datetime
    # yy=datetime.datetime.now().strftime("%Y-%m-%d")
    ##date with time format
    # import datetime
    # datetime.date.today()  # Returns 2018-01-15
    # showtime=datetime.datetime.now()  # Returns 2018-01-15 09:00

    na1=request.POST["nm"]
    ag1 = request.POST['ag']

    gen1 = request.POST['cn']
    res = employemodel.objects.get(id=id)

    if request.method == "POST":

        if request.FILES is not  None:

            if 'pics' in request.FILES:

                if request.FILES['pics']!='':

                    upload_file = request.FILES['pics']
                    fs = FileSystemStorage()

                    names = fs.save(upload_file.name, upload_file)
                    url = upload_file.name

                    res.name=na1
                    res.age=ag1
                    res.contact=gen1
                    res.gen22=fs.url(names)
                    res.save()
                else:

                    res.name = na1
                    res.age = ag1
                    res.contact = gen1
                    # res.gen22 = fs.url(names)
                    res.save()
            else:
                res.name = na1
                res.age = ag1
                res.contact = gen1
                # res.gen22 = fs.url(names)
                res.save()
        else:
            res.name = na1
            res.age = ag1
            res.contact = gen1
            # res.gen22 = fs.url(names)
            res.save()


        return render(request,"Homepage.html")
    return render(request, 'emp_edit.html', {'res': res})

#..........................deleting an employee details.............................

def emp_del(request, id):
    res = employemodel.objects.get(id=id)
    res.delete()
    return  render(request,"Homepage.html")


def sendemail(request,id):
    print("========================")
    db=Db()
    a=request.json['to']
    qry="INSERT INTO `aa`(`name`) VALUES ('"+a+"')"
    res=db.insert(qry)
    return jsonify(status="ok")
# Create your views here.
