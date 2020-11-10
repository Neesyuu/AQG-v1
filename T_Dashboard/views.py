from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from aqg.decorators import teacher_only
from question.models import Subject, AllQues, MathQues, PhysicsQues, EnglishQues, ChemistryQues
from django.utils.timezone import now
from django.contrib import messages
import re
from builtins import zip


# Create your views here.

def timeCal(mr, le):
    if int(mr) == 1:
        if int(le) == 3:
            t = 1.5
        elif int(le) == 2:
            t = 1
        else:
            t = 0.5
    elif int(mr) == 2:
        if int(le) == 3:
            t = 3
        elif int(le) == 2:
            t = 2
        else:
            t = 1
    return t


@login_required
@teacher_only
def dashboardTView(request):
    return render(request, 'dashboard/teacher/Dashboard.html')


@login_required
@teacher_only
def selsub(request):
    return render(request, 'dashboard/teacher/TselSub.html')


@login_required
@teacher_only
def selsubforReview(request):
    return render(request, 'dashboard/teacher/TselSubReview.html')


# ------------------------------------ MATH ------------------------------------------

def mathCount():
    allMathQues = MathQues.objects.all()
    count = allMathQues.count()
    sno = allMathQues[count-1].pk
    # print(MathQues.objects.get(pk=5))
    return sno + 1



@login_required
@teacher_only
def mathSel(request):
    if request.method == 'POST':
        question = request.POST.get('questionArea')
        optA = request.POST.get('optA')
        optB = request.POST.get('optB')
        optC = request.POST.get('optC')
        optD = request.POST.get('optD')
        ans = request.POST.get('answer')
        mark = request.POST.get('mark')
        level = request.POST.get('level')

        if ans == 'optA':
            ans = optA
        elif ans == 'optB':
            ans = optB
        elif ans == 'optC':
            ans = optC
        elif ans == 'optD':
            ans = optD

        timeToSolve = timeCal(mark, level)

        teacherName = request.user.first_name + ' ' + request.user.last_name
        teacherID = request.user.id
        mathID = str(teacherID) + 'M' + str(mathCount())
        mathModel = 'M' + 'mk' + str(mark) + 'le' + str(level) + 'v' + str(mathCount())

        into_all = AllQues(subID='M', Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark,
                           level=level, teacherName=teacherName, subjID=mathID,
                           timeStamp=now(), subjModel=mathModel, timeToSolve=timeToSolve, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        into_all.save()
        intQusId = AllQues.objects.get(pk=into_all.pk)
        add = MathQues(intQuesID= intQusId, Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark, level=level,
                       teacherName=teacherName, timeStamp=now(), mathID=mathID, mathModel=mathModel,
                       timeToSolve=timeToSolve, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        add.save()

        messages.success(request, 'Question is added success')
    return render(request, 'dashboard/teacher/AddQuestion/addMath.html')


# ------------------------------------ PHYSICS ------------------------------------------

def physicsCount():
    allPhysicsQues = PhysicsQues.objects.all()
    count = allPhysicsQues.count()
    sno = allPhysicsQues[count - 1].pk
    return sno + 1


@login_required
@teacher_only
def physicsSel(request):
    if request.method == 'POST':
        question = request.POST.get('questionArea')
        optA = request.POST.get('optA')
        optB = request.POST.get('optB')
        optC = request.POST.get('optC')
        optD = request.POST.get('optD')
        ans = request.POST.get('answer')
        mark = request.POST.get('mark')
        level = request.POST.get('level')

        if ans == 'optA':
            ans = optA
        elif ans == 'optB':
            ans = optB
        elif ans == 'optC':
            ans = optC
        elif ans == 'optD':
            ans = optD

        timeToSolve = timeCal(mark, level)

        teacherName = request.user.first_name + ' ' + request.user.last_name
        teacherID = request.user.id
        physicsID = str(teacherID) + 'P' + str(physicsCount())
        physicsModel = 'P' + 'mk' + str(mark) + 'le' + str(level) + 'v' + str(physicsCount())

        into_all = AllQues(subID='P', Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark,
                           level=level, teacherName=teacherName,
                           subjID=physicsID, timeStamp=now(), subjModel=physicsModel, timeToSolve=timeToSolve, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        into_all.save()
        intQusId = AllQues.objects.get(pk=into_all.pk)
        add = PhysicsQues(intQuesID= intQusId, Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark,
                          level=level,
                          teacherName=teacherName, timeStamp=now(), physicsID=physicsID, physicsModel=physicsModel, timeToSolve=timeToSolve, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        add.save()



    messages.success(request, 'Question is added success')
    return render(request, 'dashboard/teacher/AddQuestion/addPhysics.html')


# ------------------------------------ CHEMISTRY ------------------------------------------

def chemistryCount():
    allChemistryQues = ChemistryQues.objects.all()
    count = allChemistryQues.count()
    sno = allChemistryQues[count-1].pk
    return sno + 1


@login_required
@teacher_only
def chemistrySel(request):
    if request.method == 'POST':
        question = request.POST.get('questionArea')
        optA = request.POST.get('optA')
        optB = request.POST.get('optB')
        optC = request.POST.get('optC')
        optD = request.POST.get('optD')
        ans = request.POST.get('answer')
        mark = request.POST.get('mark')
        level = request.POST.get('level')

        if ans == 'optA':
            ans = optA
        elif ans == 'optB':
            ans = optB
        elif ans == 'optC':
            ans = optC
        elif ans == 'optD':
            ans = optD

        timeToSolve = timeCal(mark,level)

        teacherName = request.user.first_name + ' ' + request.user.last_name
        teacherID = request.user.id
        chemistryID = str(teacherID) + 'C' + str(chemistryCount())
        chemistryModel = 'C' + 'mk' + str(mark) + 'le' + str(level) + 'v' + str(chemistryCount())

        into_all = AllQues(subID='C', Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark,
                           level=level, teacherName=teacherName,
                           subjID=chemistryID, timeStamp=now(), subjModel=chemistryModel, timeToSolve=timeToSolve, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        into_all.save()
        intQusId = AllQues.objects.get(pk=into_all.pk)
        add = ChemistryQues(intQuesID=intQusId, Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark,
                            level=level, timeToSolve=timeToSolve,
                            teacherName=teacherName, timeStamp=now(), chemistryID=chemistryID,
                            chemistryModel=chemistryModel, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        add.save()

    messages.success(request, 'Question is added success')
    return render(request, 'dashboard/teacher/AddQuestion/addChemistry.html')


# ------------------------------------ ENGLISH ------------------------------------------

def englishCount():
    allEnglishQues = EnglishQues.objects.all()
    count = allEnglishQues.count()
    sno = allEnglishQues[count-1].pk
    return sno + 1


@login_required
@teacher_only
def englishSel(request):
    if request.method == 'POST':
        question = request.POST.get('questionArea')
        optA = request.POST.get('optA')
        optB = request.POST.get('optB')
        optC = request.POST.get('optC')
        optD = request.POST.get('optD')
        ans = request.POST.get('answer')
        mark = request.POST.get('mark')
        level = request.POST.get('level')

        if ans == 'optA':
            ans = optA
        elif ans == 'optB':
            ans = optB
        elif ans == 'optC':
            ans = optC
        elif ans == 'optD':
            ans = optD

        timeToSolve = timeCal(mark, level)

        teacherName = request.user.first_name + ' ' + request.user.last_name
        teacherID = request.user.id
        englishID = str(teacherID) + 'E' + str(englishCount())
        englishModel = 'E' + 'mk' + str(mark) + 'le' + str(level) + 'v' + str(englishCount())

        into_all = AllQues(subID='E', Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark,
                           level=level, teacherName=teacherName, timeToSolve=timeToSolve,
                           subjID=englishID, timeStamp=now(), subjModel=englishModel, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        into_all.save()
        intQusId = AllQues.objects.get(pk=into_all.pk)
        add = EnglishQues(intQuesID=intQusId, Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark,
                          level=level, timeToSolve=timeToSolve,
                          teacherName=teacherName, timeStamp=now(), englishID=englishID, englishModel=englishModel, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        add.save()


    messages.success(request, 'Question is added success')

    return render(request, 'dashboard/teacher/AddQuestion/addEnglish.html')


# ------------------------------------ SHOW ONLY MINE ------------------------------------------

@login_required
@teacher_only
def allMyPhysics(request):
    new = []
    idd = request.user.id
    pattern = f'^{idd}P[0-9]+$'
    all = PhysicsQues.objects.all()
    print('all:')
    print(all)
    for x in all:
        if re.match(pattern, x.physicsID):
            print('x:')
            print(x)
            new.append(x)
    data = {'all': new}
    print('New:')
    print(new)
    return render(request, 'dashboard/teacher/ReviewQuestion/physics.html', data)


@login_required
@teacher_only
def allMyChemistry(request):
    new = []
    idd = request.user.id
    pattern = f'^{idd}C[0-9]+$'
    all = ChemistryQues.objects.all()
    for x in all:
        if re.match(pattern, x.chemistryID):
            new.append(x)
    data = {'all': new}
    return render(request, 'dashboard/teacher/ReviewQuestion/chemistry.html', data)


@login_required
@teacher_only
def allMyMath(request):
    new = []
    idd = request.user.id
    pattern = f'^{idd}M[0-9]+$'
    all = MathQues.objects.all()
    for x in all:
        if re.match(pattern, x.mathID):
            new.append(x)
    data = {'all': new}
    return render(request, 'dashboard/teacher/ReviewQuestion/math.html', data)


@login_required
@teacher_only
def allMyEnglish(request):
    new = []
    idd = request.user.id
    pattern = f'^{idd}E[0-9]+$'
    all = EnglishQues.objects.all()
    for x in all:
        if re.match(pattern, x.englishID):
            new.append(x)
    data = {'all': new}
    return render(request, 'dashboard/teacher/ReviewQuestion/english.html', data)


@login_required
@teacher_only
def allMyQues(request):
    new = []
    idd = request.user.id
    pattern = f'^{idd}[P, M, C, E][0-9]+$'
    all = AllQues.objects.all()
    for x in all:
        if re.match(pattern, x.subjID):
            new.append(x)
    data = {'all': new}
    return render(request, 'dashboard/teacher/ReviewQuestion/ownQues.html', data)


# ------------------------------------ ALL QUESTIONS ------------------------------------------

@login_required
@teacher_only
def allQues(request):
    all = AllQues.objects.all()
    c = all.count()
    zipping = zip(range(1,c+1), all)
    data = {'all': all, 'count': c, 'zip':zipping}
    return render(request, 'dashboard/teacher/ReviewQuestion/allQuesColl.html', data)