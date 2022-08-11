from django.http import HttpResponse,JsonResponse
from .models import  People,Parties,Employee,Election,Candidates
import json 
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def sara(request):
    return HttpResponse("Hello, sara")

def question(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


@csrf_exempt
def getcandidates_All(request):
     c=list(Candidates.objects.values()) 
     return JsonResponse(c,safe=False)


@csrf_exempt
def getelection_All(request):
     e=list(Election.objects.values()) 
     return JsonResponse(e,safe=False)


@csrf_exempt
def ok(request):
    return JsonResponse({'result':'0'})
       


@csrf_exempt
def getelectioncount(request):
    try:
        count={
        "4030039716":Election.objects.filter(C_id="4030039716").count(),
        "4030039715":Election.objects.filter(C_id="4030039715").count(),
        "4030039714":Election.objects.filter(C_id="4030039714").count()}
        print(count)
        return JsonResponse(count,safe=False)

    except Exception as el:
        print(el)
        return JsonResponse({'result':'notfound'})   



@csrf_exempt
def getparties_All(request):
     p=list(Parties.objects.values()) 
     return JsonResponse(p,safe=False)

@csrf_exempt
def getpeople_All(request):
     pe=list(People.objects.values()) 
     return JsonResponse(pe,safe=False)



@csrf_exempt
def login_user(request):
    body=request.body.decode('utf-8')
    print(body)
    bodyjson=json.loads(body)
    P_id=bodyjson['P_id']
    print(P_id)
    try:
        per=People.objects.get(P_id=P_id)
        print(per)
        perjson=toJson(per)
        del perjson['_state']
        perjson['result']='success'
        return JsonResponse({'Password':perjson['Password']},safe=False)
    except Exception as e :
        print(e)
        return JsonResponse({'result':'notfound'})

@csrf_exempt
def election(request):
    body=request.body.decode('utf-8')
    print(body)
    bodyjson=json.loads(body)
    try:
        P_id=bodyjson['P_id']
        C_id=bodyjson['C_id']
        print(P_id)
        pe=People.objects.get(P_id=P_id)
        ca=Candidates.objects.get(C_id=C_id)
        #Election.P_id=pepole
        data1=Election(P_id=pe,C_id=ca)
        print(data1)
        data1.save()
        return JsonResponse({'result':'success'})
    except Exception as e:
        print(e)
        return JsonResponse({'result':'notfound'})






@csrf_exempt
def register(request):
    if request.method=='POST':
        body=request.body.decode('utf-8')
        print(body)
        bodyjson=json.loads(body)
        Fname=bodyjson['Fname']
        Mname=bodyjson['Mname']
        Lname=bodyjson['Lname']
        P_id=bodyjson['P_id']
        MobilePhone=bodyjson['MobilePhone']
        Email=bodyjson['Email']
        Password=bodyjson['Password']
        Sex=bodyjson['Sex']
        print(Sex)
        data=People( Fname=Fname , Mname=Mname , Lname=Lname , P_id=P_id , MobilePhone =MobilePhone, Email=Email , Password =Password , Sex =Sex)
        data.save()
        return JsonResponse({'result':'success'})

@csrf_exempt
def login(request):
    body=request.body.decode('utf-8')
    print(body)
    bodyjson=json.loads(body)
    Username=bodyjson['Username']
    Password=bodyjson['Password']
    try:
        per=Employee.objects.get(Username=Username,Password=Password)
        perjson=toJson(per)
        del perjson['_state']
        perjson['result']='success'
        return JsonResponse(perjson['result'],safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'result':'notfound'})



def toJson(p):
    return json.loads(json.dumps(p,default=lambda o: o.__dict__))
