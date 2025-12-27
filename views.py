from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from sanuapp.models import Contact,MembershipPlan,Trainer,Enrollment,Gallery,Attendance
# Create your views here.
def Home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def achivements(request):
    return render(request,"achivements.html")

def welcome(request):
    return render(request, "welcome.html")

def trainsamrter(request):
    return render(request, "train_samrter.html")

def seegymaction(request):
    return render(request, "see_gym_action.html")

def classes_pricing(request):
    return render(request, 'classes_pricing.html')

def hear_from_members(request):
    return render(request, 'hear_from_members.html')

def personal_training(request):
    return render(request, 'personal_training.html')

def group_fitness_classes(request):
    return render(request, 'group_fitness.html')

def cardio_strength_zone(request):
    return render(request, 'cardio_strength.html')

def wellness_recovery(request):
    return render(request, 'wellness_recovery.html')

def nutrition_bar(request):
    return render(request, 'nutrition_bar.html')

def fitness_tracking(request):
    return render(request, 'fitness_tracking.html')



def gallery(request):
    posts=Gallery.objects.all()
    context={"posts":posts}
    return render(request,"gallery.html",context)


def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    SelectTrainer=Trainer.objects.all()
    context={"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        phonenumber=request.POST.get('PhoneNumber')
        Login=request.POST.get('logintime')
        Logout=request.POST.get('loginout')
        SelectWorkout=request.POST.get('workout')
        TrainedBy=request.POST.get('trainer')
        query=Attendance(phonenumber=phonenumber,Login=Login,Logout=Logout,SelectWorkout=SelectWorkout,TrainedBy=TrainedBy)
        query.save()
        messages.warning(request,"Attendace Applied Success")
        return redirect('/attendance')
    return render(request,"attendance.html",context)

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    user_phone=request.user
    posts=Enrollment.objects.filter(PhoneNumber=user_phone)
    attendance=Attendance.objects.filter(phonenumber=user_phone)
    print(posts)
    context={"posts":posts,"attendance":attendance}
    return render(request,"profile.html",context)


def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
      
        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/signup')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
       
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/login')
        
        
    return render(request,"signup.html")



def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
            
        
    return render(request,"handlelogin.html")


def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('/login')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()       
        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/contact')
        
    return render(request,"contact.html")


def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')

    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={"Membership":Membership,"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        FullName=request.POST.get('FullName')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        PhoneNumber=request.POST.get('PhoneNumber')
        DOB=request.POST.get('DOB')
        member=request.POST.get('member')
        trainer=request.POST.get('trainer')
        reference=request.POST.get('reference')
        address=request.POST.get('address')
        query=Enrollment(FullName=FullName,Email=email,Gender=gender,PhoneNumber=PhoneNumber,DOB=DOB,SelectMembershipplan=member,SelectTrainer=trainer,Reference=reference,Address=address)
        query.save()
        messages.success(request,"Thanks For Enrollment")
        return redirect('/join')



    return render(request,"enroll.html",context)


def biceps_triceps(request):
    exercises = {
        'Biceps': [
            'Barbell Curl',
            'Dumbbell Curl',
            'Hammer Curl',
            'Preacher Curl',
            'Concentration Curl',
        ],
        'Triceps': [
            'Triceps Pushdown',
            'Overhead Triceps Extension',
            'Skull Crushers',
            'Close-Grip Bench Press',
            'Triceps Dips',
        ]
    }
    return render(request, 'biceps_triceps.html', {'exercises': exercises})

def back_exercises(request):
    back_exercises = [
        "Deadlift",
        "Pull-Ups",
        "Bent-Over Barbell Row",
        "T-Bar Row",
        "Seated Cable Row",
        "Lat Pulldown",
        "Single-Arm Dumbbell Row",
        "Face Pull",
        "Hyperextensions",
        "Inverted Row"
    ]
    return render(request, 'back_exercises.html', {'back_exercises': back_exercises})

def shoulder_exercises(request):
    shoulder_exercises = [
        "Overhead Press (Barbell or Dumbbell)",
        "Lateral Raises",
        "Front Raises",
        "Rear Delt Flys",
        "Arnold Press",
        "Upright Row",
        "Push Press",
        "Face Pulls",
        "Dumbbell Shoulder Press",
        "Cable Lateral Raise"
    ]
    return render(request, 'shoulder_exercises.html', {'shoulder_exercises': shoulder_exercises})

def chest_exercises(request):
    chest_exercises = [
        "Barbell Bench Press",
        "Incline Dumbbell Press",
        "Chest Dips",
        "Push-Ups",
        "Cable Crossover",
        "Pec Deck Machine",
        "Incline Bench Press",
        "Decline Bench Press",
        "Dumbbell Flyes",
        "Machine Chest Press"
    ]
    return render(request, 'chest_exercises.html', {'chest_exercises': chest_exercises})

def leg_exercises(request):
    leg_exercises = [
        "Barbell Back Squat",
        "Front Squat",
        "Leg Press",
        "Walking Lunges",
        "Romanian Deadlift",
        "Leg Curl Machine",
        "Leg Extension Machine",
        "Step-Ups",
        "Bulgarian Split Squat",
        "Calf Raises"
    ]
    return render(request, 'leg_exercises.html', {'leg_exercises': leg_exercises})

