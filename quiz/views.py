from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import AnswerForm
from .models import Question
import json
from datetime import datetime,timedelta
import time
import pytz
# Create your views here.

#--------------Globals-------------------#
IST = pytz.timezone('Asia/Kolkata') 
starttime = IST.localize(datetime(2021,3,26,15,20,0,0))
endtime = IST.localize(datetime(2021,3,26,15,21,0,0))
#----------------------------------------#

@login_required
def answerView(request):
    if datetime.now(tz=IST) < starttime:
        return redirect(reverse_lazy('prestart'))
    elif datetime.now(tz=IST) > endtime:
        return redirect(reverse_lazy('conclude'))
    else:
        profile=request.user.profile
        old_id = profile.ques_id
        if request.is_ajax() and request.method=="POST":
            form=AnswerForm(request.POST)
            if form.is_valid():
                tempAnswer=form.cleaned_data.get('answer')
                actualAnswer=getObj(profile).answer
                if  tempAnswer.lower() == actualAnswer.lower():
                    profile.ques_id+=1
                    profile.correct+=1
                    profile.score+=10
                    profile.data+='<'+str(datetime.now(tz=IST).isoformat())+','+str(profile.score)+'>'
                    profile.save()
                winner=checkForWin(profile)
                if winner:
                    data={'winner':winner}
                else:
                    profileObj=getObj(profile)
                    question={'text':profileObj.question}
    
                    if(profile.ques_id == old_id):
                        data={'question':question,'winner':winner,'correct':False}
                    else:
                        data={'question':question,'winner':winner,'correct':True}
                return JsonResponse(data)
        else:
            if checkForWin(profile):
                return redirect(reverse_lazy('winner'))
            form=AnswerForm()
            profileObj=getObj(profile)
            question={'text':profileObj.question}
            return render(request,'quiz.html',{'question':question,'form':form})

@login_required
def getObj(profile):
    while True:
        try:
            quesObj=Question.objects.get(pk=profile.ques_id)
        except ObjectDoesNotExist:
            profile.ques_id+=1
            profile.save()
            continue
        else:
            break
    return quesObj
    
@login_required
def checkForWin(profile):
    if profile.correct == profile.total_ques:
        profile.winner=True
        profile.save()
        return True
    else:
        return False