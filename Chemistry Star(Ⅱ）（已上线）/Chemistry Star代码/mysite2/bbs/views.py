import random

from django.utils import timezone
from django.shortcuts import HttpResponse
from django.shortcuts import render
from datetime import datetime,timedelta
from .models import Users, GkQuestion, Shoucangt, papers,paperquestion,Statistic,quesrecord

# Users.objects.create(name="wym1", age=21)
# Users.objects(name="wym").update(age=19)
# return HttpResponse(a)

ctx={}

# 接收请求数据
def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
        Search.objects.create(Searcher=request.GET['q'])
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

def search_post(request):
    i=0
    if request.POST['m'].isdigit()==False and request.POST['m']!='':
        ctx['n'] = "请输入数字"
        return render(request, "旧/runoob2.html", ctx)


    if request.POST['m']:
        mark = request.POST['m']
        ques = Question.objects(mark=mark)
        for que in ques:
            ctx['m'] = mark
            ctx['q'] = que.question
            ctx['a'] = que.answer_a
            ctx['b'] = que.answer_b
            ctx['c'] = que.answer_c
            ctx['d'] = que.answer_d
            ctx['n'] = ""
    else:
        for question in Question.objects:
           i=i+1
        mark = random.randint(0,i)
        ques = Question.objects(mark=mark)
        for que in ques:
            ctx['m'] = mark
            ctx['q'] = que.question
            ctx['a'] = que.answer_a
            ctx['b'] = que.answer_b
            ctx['c'] = que.answer_c
            ctx['d'] = que.answer_d
            ctx['n'] = ""

    return render(request, "旧/runoob.html", ctx)





def zhuce(request):
    ctx1 = {}
    request.encoding = 'utf-8'
    if request.GET['er']:
        ctx1['er'] = ''
    else:
        ctx1['er'] = '请输入用户名'

    if request.GET['a']:
        ctx1['w'] = ''
    else:
        ctx1['w'] = '请设置密码'

    if request.GET['b']:
        ctx1['e'] = ''
        if request.GET['a']!=request.GET['b']:
            ctx1['e']='两次密码不一样'

    else:
        ctx1['e'] = '请再次输入密码'

    student = Users.objects(name=request.GET['er'])

    if len(student)!=0:
        ctx1['er'] = '用户名已被使用'

    if ctx1['er'] == '' and ctx1['w'] == '' and ctx1['e'] == '':
        Users.objects.create(name=request.GET['er'], password=request.GET['a'])
        Statistic.objects.create(name=request.GET['er'])

        ctx1['p'] = '注册成功'



    return render(request, "zhuce.html", ctx1)

def zhu(request):

    return render(request, "zhuce.html")

def log(request):
    ctx_log = {}
    ctx_log['i'] = ''
    return render(request, "login.html",ctx_log)




def login(request):
    request.encoding='utf-8'
    if request.GET['tg'] and request.GET['a']:
        name = request.GET['tg']
        password = request.GET['a']

        student = Users.objects(name=name)

        l=len(student)

        if l==1:
            if password==student[0].password:
                uname['uname'] = name
                ct={}
                ct['n']=uname['uname']
                u = Users.objects(name=uname['uname'])
                for u in u:
                    ct['s'] = u.status
                return render(request, "index.html", ct)

    ctx_log={}
    ctx_log['i']='用户名或密码错误'
    return render(request, "login.html", ctx_log)

def web1(request):
     ct={}
     ct['n']=uname['uname']
     u = Users.objects(name=uname['uname'])
     for u in u:
         ct['s'] = u.status

     return render(request, "index.html", ct)


def gaokao(request):
    ct = {}
    ct['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        ct['s'] = u.status
    return render(request, "gaokao.html", ct)


inf={'question_mark':0,'paper_mark':'','right_answer':'','jiexi':'','nian':''}

def sd2020(request):

    inf['paper_mark'] ='2020sd'
    inf['question_mark'] = 1
    inf['nian']=2020
    return render(request, "子页面/2020-sd.html", inf)

def sd2019(request):

    inf['paper_mark'] ='2019sd'
    inf['question_mark'] = 1
    inf['nian'] = 2019
    return render(request, "子页面/2020-sd.html", inf)

def sd2018(request):

    inf['paper_mark'] ='2018sd'
    inf['question_mark'] = 1
    inf['nian'] = 2018
    return render(request, "子页面/2020-sd.html", inf)

def sd2017(request):

    inf['paper_mark'] ='2017sd'
    inf['question_mark'] = 1
    inf['nian'] = 2017
    return render(request, "子页面/2020-sd.html", inf)

def sd2016(request):

    inf['paper_mark'] ='2016sd'
    inf['question_mark'] = 1
    inf['nian'] = 2016
    return render(request, "子页面/2020-sd.html", inf)



ctxgk = {}

def gktest(request,papermark,nian):
    inf['paper_mark']=papermark
    inf['question_mark'] = 1
    inf['nian'] = nian
    question = GkQuestion.objects(papermark=inf['paper_mark'],mark=inf['question_mark'])
    for que in question:
        ctxgk['m'] = que.mark
        ctxgk['q'] = que.question
        ctxgk['a'] = que.answer_a
        ctxgk['b'] = que.answer_b
        ctxgk['c'] = que.answer_c
        ctxgk['d'] = que.answer_d
        inf['right_answer'] = que.r_answer
        inf['jiexi'] = que.jiexi
        ctxgk['an'] = ''
        ctxgk['bn'] = ''
        ctxgk['cn'] = ''
        ctxgk['jx'] = ''
        ctxgk['nian'] = inf["nian"]
    ctxgk['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        ctxgk['s'] = u.status

    return render(request, "gkdati.html", ctxgk)

smark={'smark':1}

def sctest(request):
    ctxsc={}
    smark['smark']=1
    i=0
    cancel['cancel'] = 0
    question = Shoucangt.objects(name=uname['uname'])
    for que in question:
        i=i+1
        if i==smark['smark']:
            qu = GkQuestion.objects( mark=que.questionmark, papermark=que.papermark)
            for qu in qu:
                ctxgk['y'] = que.papermark
                ctxgk['m'] = qu.mark
                ctxgk['q'] = qu.question
                ctxgk['a'] = qu.answer_a
                ctxgk['b'] = qu.answer_b
                ctxgk['c'] = qu.answer_c
                ctxgk['d'] = qu.answer_d
                inf['right_answer'] = qu.r_answer
                inf['jiexi'] = qu.jiexi
                ctxgk['an'] = ''
                ctxgk['bn'] = ''
                ctxgk['jx'] = ''
                ctxgk['n'] = uname['uname']
                u = Users.objects(name=uname['uname'])
                for u in u:
                    ctxgk['s'] = u.status
            return render(request, "scdati.html", ctxgk)
    ctxsc['r']='您没有已收藏的题目'
    ctxsc['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        ctxsc['s'] = u.status
    return render(request, "scdati.html", ctxsc)


def gkhandin(request):
    try:
        x = request.POST['t1']
    except KeyError:
        x = None

    if x:
        ans = x
        na = Statistic.objects(name=uname['uname'])
        for n in na:
            n.total = n.total+1
            n.save()


        if ans == inf['right_answer']:
            ctxgk['an']="回答正确"
            ctxgk['jx'] = inf['jiexi']
            quesrecord.objects.create(name=uname['uname'], papermark=inf['paper_mark'],mark=inf['question_mark'],pubtime=datetime.today(),tf='right')
            for n in na:
                n.right = n.right + 1
                n.save()

        else:
            ctxgk['an'] = "回答错误"
            ctxgk['jx'] = inf['jiexi']
            quesrecord.objects.create(name=uname['uname'], papermark=inf['paper_mark'],mark=inf['question_mark'],pubtime=datetime.today(),tf='wrong')

    else:
        ctxgk['an'] = "您没有答题"

    ctxgk['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        ctxgk['s'] = u.status
    return render(request, "gkdati.html", ctxgk)

def schandin(request):
    try:
        x = request.POST['t1']
    except KeyError:
        x = None

    if x:
        ans = x
        na = Statistic.objects(name=uname['uname'])
        for n in na:
            n.total = n.total + 1
            n.save()

        if ans == inf['right_answer']:
            ctxgk['an']="回答正确"
            ctxgk['jx'] = inf['jiexi']
            quesrecord.objects.create(name=uname['uname'], papermark=ctxgk['y'],mark=ctxgk['m'],pubtime=datetime.today(),tf='right')

            for n in na:
                n.right = n.right + 1
                n.save()
        else:
            ctxgk['an'] = "回答错误"
            ctxgk['jx'] = inf['jiexi']
            quesrecord.objects.create(name=uname['uname'], papermark=ctxgk['y'],mark=ctxgk['m'],pubtime=datetime.today(),tf='wrong')

    else:
        ctxgk['an'] = "您没有答题"


    return render(request, "scdati.html", ctxgk)

def summitgk(request):
    request.encoding='utf-8'
    cont={}
    cont['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        cont['s'] = u.status
    if uname['uname']!= 'WangYiMai':
        cont['fankui'] = '您无权限'
        return render(request, "tmluru.html", cont)

    qu = GkQuestion.objects(mark=request.POST['n'], papermark=request.POST['y'])
    i=0
    for qu in qu:
        i=i+1

    if i==1:
        cont['fankui'] = '题目已存在'
        return render(request, "tmluru.html", cont)

    if 'tg' in request.POST and request.POST['tg'] and 'a' in request.POST and request.POST['a'] and 'b' in request.POST and request.POST['b'] and 'c' in request.POST and request.POST['c'] and 'd' in request.POST and request.POST['d'] and 'e' in request.POST and request.POST['e'] and 'y' in request.POST and request.POST['y'] and 'n' in request.POST and request.POST['n']:
       cont['fankui'] = '题目录入成功'
       GkQuestion.objects.create(question=request.POST['tg'],answer_a=request.POST['a'],
                                               answer_b=request.POST['b'],answer_c=request.POST['c'],
                                               answer_d=request.POST['d'],r_answer=request.POST['e'],mark=request.POST['n'],
                                               papermark=request.POST['y'],jiexi=request.POST['jiexi'])
       return render(request, "tmluru.html", cont)
    else:
        cont['fankui']='输入有空'
    return render(request, "tmluru.html", cont)

def summitgk0(request):
    c={}
    c['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        c['s'] = u.status

    return render(request, "tmluru.html",c)

def nextgk(request):
    inf['question_mark'] = inf['question_mark']+1
    c = len(GkQuestion.objects(papermark=inf['paper_mark']))
    if c<inf['question_mark']:
        inf['question_mark'] = inf['question_mark']-1
        ctxgk['an']='这已经是最后一道题'
        ctxgk['n'] = uname['uname']
        u = Users.objects(name=uname['uname'])
        for u in u:
            ctxgk['s'] = u.status
        return render(request, "gkdati.html", ctxgk)
    question = GkQuestion.objects(papermark=inf['paper_mark'], mark=inf['question_mark'])
    for que in question:

        ctxgk['m'] = que.mark
        ctxgk['q'] = que.question
        ctxgk['a'] = que.answer_a
        ctxgk['b'] = que.answer_b
        ctxgk['c'] = que.answer_c
        ctxgk['d'] = que.answer_d
        inf['right_answer'] = que.r_answer
        inf['jiexi'] = que.jiexi
        ctxgk['an']=''
        ctxgk['bn'] = ''
        ctxgk['cn'] = ''
        ctxgk['jx'] = ''
    ctxgk['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        ctxgk['s'] = u.status
    return render(request, "gkdati.html", ctxgk)

def lastgk(request):
    inf['question_mark'] = inf['question_mark']-1
    c = len(GkQuestion.objects(papermark=inf['paper_mark']))
    if inf['question_mark']==0:
        inf['question_mark'] = inf['question_mark']+1
        ctxgk['an']='这已经是第一道题'
        ctxgk['n'] = uname['uname']
        u = Users.objects(name=uname['uname'])
        for u in u:
            ctxgk['s'] = u.status
        return render(request, "gkdati.html", ctxgk)
    question = GkQuestion.objects(papermark=inf['paper_mark'], mark=inf['question_mark'])
    for que in question:

        ctxgk['m'] = que.mark
        ctxgk['q'] = que.question
        ctxgk['a'] = que.answer_a
        ctxgk['b'] = que.answer_b
        ctxgk['c'] = que.answer_c
        ctxgk['d'] = que.answer_d
        inf['right_answer'] = que.r_answer
        inf['jiexi'] = que.jiexi
        ctxgk['an']=''
        ctxgk['bn'] = ''
        ctxgk['cn'] = ''
        ctxgk['jx'] = ''
    ctxgk['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        ctxgk['s'] = u.status
    return render(request, "gkdati.html", ctxgk)

def nextsc(request):
    smark['smark']= smark['smark'] + 1
    i = 0
    question = Shoucangt.objects(name=uname['uname'])
    for que in question:
        i = i + 1
        if i == smark['smark']:
            qu = GkQuestion.objects(mark=que.questionmark, papermark=que.papermark)
            for qu in qu:
                ctxgk['y'] = que.papermark
                ctxgk['m'] = qu.mark
                ctxgk['q'] = qu.question
                ctxgk['a'] = qu.answer_a
                ctxgk['b'] = qu.answer_b
                ctxgk['c'] = qu.answer_c
                ctxgk['d'] = qu.answer_d
                inf['right_answer'] = qu.r_answer
                inf['jiexi'] = qu.jiexi
                ctxgk['an'] = ''
                ctxgk['bn'] = ''
                ctxgk['jx'] = ''
                cancel['cancel'] = 0
            return render(request, "scdati.html", ctxgk)
    ctxgk['an'] = '这是最后一道题'
    smark['smark'] = smark['smark'] - 1
    if cancel['cancel']==1:
        return render(request, "scdati2.html", ctxgk)

    return render(request, "scdati.html", ctxgk)

def lastsc(request):
    smark['smark']= smark['smark'] - 1
    i = 0
    question = Shoucangt.objects(name=uname['uname'])
    if smark['smark']==0 or smark['smark']== -1:
        ctxgk['an'] = '这是第一道题'
        smark['smark'] = smark['smark'] + 1
        if cancel['cancel'] == 1:
            return render(request, "scdati2.html", ctxgk)
        return render(request, "scdati.html", ctxgk)

    for que in question:
        i = i + 1
        if i == smark['smark']:
            qu = GkQuestion.objects(mark=que.questionmark, papermark=que.papermark)
            for qu in qu:
                ctxgk['y'] = que.papermark
                ctxgk['m'] = qu.mark
                ctxgk['q'] = qu.question
                ctxgk['a'] = qu.answer_a
                ctxgk['b'] = qu.answer_b
                ctxgk['c'] = qu.answer_c
                ctxgk['d'] = qu.answer_d
                inf['right_answer'] = qu.r_answer
                inf['jiexi'] = qu.jiexi
                ctxgk['an'] = ''
                ctxgk['bn'] = ''
                ctxgk['jx'] = ''
                cancel['cancel'] = 0
            return render(request, "scdati.html", ctxgk)




def shoucang(request):
    return render(request, "子页面/shoucang.html")

uname={'uname':''}

def gkshoucang(request):

    if len(Shoucangt.objects(papermark=inf['paper_mark'], questionmark=inf['question_mark'], name=uname['uname']) )==1:
        ctxgk['an'] = '您已收藏'
        ctxgk['n'] = uname['uname']
        u = Users.objects(name=uname['uname'])
        for u in u:
            ctxgk['s'] = u.status
        return render(request, "gkdati.html", ctxgk)


    i = 0
    shoucang = Shoucangt.objects()
    for s in shoucang:
        i = i + 1

    Shoucangt.objects.create(papermark=inf['paper_mark'], questionmark=inf['question_mark'],number=i,name=uname['uname'])
    ctxgk['an']='收藏成功'
    ctxgk['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        ctxgk['s'] = u.status
    return render(request, "gkdati.html", ctxgk)

cancel={'cancel':0}

def quxiaosc(request):

    smark['smark']
    i = 0
    question = Shoucangt.objects(name=uname['uname'])
    for que in question:
        i = i + 1
        if i == smark['smark']:
            que.delete()
            smark['smark']=smark['smark']-1
            ctxgk['an']='已取消'
            cancel['cancel']=1
            return render(request, "scdati2.html", ctxgk)

def fanhuisy(request):
    ct = {}
    ct['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        ct['s'] = u.status

    return render(request, "index.html", ct)

def zujuan(request):
    ct = {}
    ct['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        ct['s'] = u.status
    return render(request, 'zujuan.html',ct)

def get_questions(request):
    questions = GkQuestion.objects.all().order_by('papermark')
    return render(request, 'zujuan2.html', {'questions': questions})

paperinfor={'name':'','author':'','intro':'','quesflag':0}

paperques=dict()

zj_already=[]




def startzujuan(request):
    ctxzj = {}
    paperinfor['quesflag'] = 0
    zj_already[:] = []
    paperques.clear()
    request.encoding = 'utf-8'
    user = Users.objects(name=uname['uname'])
    for u in user:
        if u.status=='stu':
            ctxzj['fankui'] = '您无权限'

            ctxzj['n'] = uname['uname']
            u = Users.objects(name=uname['uname'])
            for u in u:
                ctxzj['s'] = u.status
            return render(request, "zujuan.html", ctxzj)
    if request.GET['n']:
        ctxzj['fankui'] = ''
    else:
        ctxzj['fankui'] = '请输入试卷名称'
        ctxzj['n'] = uname['uname']
        u = Users.objects(name=uname['uname'])
        for u in u:
            ctxzj['s'] = u.status
        return render(request, "zujuan.html", ctxzj)

    paper = papers.objects(name=request.GET['n'])

    if len(paper)!=0:
        ctxzj['fankui'] = '试卷名称已被使用'
        ctxzj['n'] = uname['uname']
        u = Users.objects(name=uname['uname'])
        for u in u:
            ctxzj['s'] = u.status
        return render(request, "zujuan.html", ctxzj)

    if ctxzj['fankui'] == '' :
        paperinfor['name']=request.GET['n']
        paperinfor['author']=uname['uname']
        paperinfor['intro'] = request.GET['s']
        questions = GkQuestion.objects.all().order_by('papermark')
        ctxzj['questions']=questions
        ctxzj['n'] = uname['uname']
        u = Users.objects(name=uname['uname'])
        for u in u:
            ctxzj['s'] = u.status
        return render(request, 'zujuanxt.html', ctxzj)

def zjhandin(request,papermark,mark,num_ber):
    zj_already.append(int(num_ber))
    questions = GkQuestion.objects.all().order_by('papermark')
    paperques.update({paperinfor['quesflag']: {'name': papermark}})
    paperques[paperinfor['quesflag']].update({'mark': mark})
    paperinfor['quesflag']=paperinfor['quesflag']+1
    ctxzj={'questions': questions,'zj_already': zj_already}
    ctxzj['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        ctxzj['s'] = u.status
    return render(request, 'zujuanxt.html', ctxzj)

def scpaper(request):
    ctxzj={}
    if paperinfor['quesflag']==0 :
        ctxzj['questions'] = GkQuestion.objects.all().order_by('papermark')
        ctxzj['fk'] = '您还没有添加试题'
        return render(request, "zujuan2.html", ctxzj)
    ctxzj['fankui']='组卷成功'
    pubtime = datetime.today()
    papers.objects.create(name=paperinfor['name'], author=paperinfor['author'],intro=paperinfor['intro'],pubtime=pubtime)

    for i in range(paperinfor['quesflag']):
        paperquestion.objects.create(papername=paperinfor['name'], papermark=paperques[i]['name'],mark=paperques[i]['mark'])
    paperinfor['quesflag']=0
    zj_already[:]=[]
    paperques.clear()
    ctxzj['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        ctxzj['s'] = u.status

    return render(request, "zujuan.html", ctxzj)

def jszjk(request):
    ct = {}
    p_apers = papers.objects.all().order_by('pubtime')
    ct['n'] = uname['uname']
    ct['papers'] = p_apers
    u = Users.objects(name=uname['uname'])
    for u in u:
        ct['s'] = u.status
    return render(request, 'zujuanku.html', ct)

zmark={'zmark':1}

paperzj={'paperzj':''}

ctxzj = {}
def zujuandt(request,paper):

    smark['smark'] = 1
    i = 0
    question = paperquestion.objects(papername=paper)
    paperzj['paperzj']=paper
    for que in question:
        i = i + 1
        if i == smark['smark']:
            qu = GkQuestion.objects(mark=que.mark, papermark=que.papermark)
            for qu in qu:
                ctxzj['y'] = que.papermark
                ctxzj['m'] = qu.mark
                ctxzj['q'] = qu.question
                ctxzj['a'] = qu.answer_a
                ctxzj['b'] = qu.answer_b
                ctxzj['c'] = qu.answer_c
                ctxzj['d'] = qu.answer_d
                inf['right_answer'] = qu.r_answer
                inf['jiexi'] = qu.jiexi
                inf['paper_mark'] = que.papermark
                inf['question_mark'] = qu.mark
                ctxzj['an'] = ''
                ctxzj['bn'] = ''
                ctxzj['jx'] = ''
                ctxzj['cn'] = ''
            ctxzj['n'] = uname['uname']
            u = Users.objects(name=uname['uname'])
            for u in u:
                ctxzj['s'] = u.status
            return render(request, "zjdati.html", ctxzj)

def zjdthandin(request):
    try:
        x = request.POST['t1']
    except KeyError:
        x = None

    if x:
        ans = x
        na = Statistic.objects(name=uname['uname'])
        for n in na:
            n.total = n.total + 1
            n.save()
        if ans == inf['right_answer']:
            ctxzj['an']="正确"
            ctxzj['jx'] = inf['jiexi']
            quesrecord.objects.create(name=uname['uname'], papermark=ctxzj['y'],mark=ctxzj['m'],pubtime=datetime.today(),tf='right')

            for n in na:
                n.right = n.right + 1
                n.save()
        else:
            ctxzj['an'] = "错误"
            ctxzj['jx'] = inf['jiexi']
            quesrecord.objects.create(name=uname['uname'], papermark=ctxzj['y'],mark=ctxzj['m'],pubtime=datetime.today(),tf='wrong')

    else:
        ctxzj['an'] = "您没有答题"

    return render(request, "zjdati.html", ctxzj)

def nextzj(request):
    smark['smark']= smark['smark'] + 1
    i = 0
    question = paperquestion.objects(papername=paperzj['paperzj'])
    for que in question:
        i = i + 1
        if i == smark['smark']:
            qu = GkQuestion.objects(mark=que.mark, papermark=que.papermark)
            for qu in qu:
                ctxzj['y'] = que.papermark
                ctxzj['m'] = qu.mark
                ctxzj['q'] = qu.question
                ctxzj['a'] = qu.answer_a
                ctxzj['b'] = qu.answer_b
                ctxzj['c'] = qu.answer_c
                ctxzj['d'] = qu.answer_d
                inf['right_answer'] = qu.r_answer
                inf['jiexi'] = qu.jiexi
                inf['paper_mark']=que.papermark
                inf['question_mark']=qu.mark
                ctxzj['an'] = ''
                ctxzj['bn'] = ''
                ctxzj['jx'] = ''
                ctxzj['cn'] = ''

            return render(request, "zjdati.html", ctxzj)
    ctxzj['an'] = '这是最后一道题'
    smark['smark'] = smark['smark'] - 1

    return render(request, "zjdati.html", ctxzj)

def lastzj(request):
    smark['smark']= smark['smark'] - 1
    i = 0
    question = paperquestion.objects(papername=paperzj['paperzj'])
    if smark['smark']==0 or smark['smark']== -1:
        ctxzj['an'] = '这是第一道题'
        smark['smark'] = smark['smark'] + 1
        return render(request, "zjdati.html", ctxzj)

    for que in question:
        i = i + 1
        if i == smark['smark']:
            qu = GkQuestion.objects(mark=que.mark, papermark=que.papermark)
            for qu in qu:
                ctxzj['y'] = que.papermark
                ctxzj['m'] = qu.mark
                ctxzj['q'] = qu.question
                ctxzj['a'] = qu.answer_a
                ctxzj['b'] = qu.answer_b
                ctxzj['c'] = qu.answer_c
                ctxzj['d'] = qu.answer_d
                inf['right_answer'] = qu.r_answer
                inf['jiexi'] = qu.jiexi
                inf['paper_mark'] = que.papermark
                inf['question_mark'] = qu.mark
                ctxzj['an'] = ''
                ctxzj['bn'] = ''
                ctxzj['jx'] = ''
                ctxzj['cn'] = ''
            return render(request, "zjdati.html", ctxzj)

def zjshoucang(request):

    if len(Shoucangt.objects(papermark=inf['paper_mark'], questionmark=inf['question_mark'], name=uname['uname']) )==1:
        print(Shoucangt.objects(papermark=inf['paper_mark'], questionmark=inf['question_mark'], name=uname['uname']))
        ctxzj['an'] = '您已收藏'
        return render(request, "zjdati.html", ctxzj)


    i = 0
    shoucang = Shoucangt.objects()
    for s in shoucang:
        i = i + 1

    Shoucangt.objects.create(papermark=inf['paper_mark'], questionmark=inf['question_mark'],number=i,name=uname['uname'])
    ctxzj['an']='收藏成功'
    return render(request, "zjdati.html", ctxzj)

def teacherrz(request):
    c={}
    if uname['uname'] == 'WangYiMai':
        name = request.GET['n']
        users = Users.objects(name=name)
        if len(users)==0:
            c['fankui'] = "没有此用户"

            c['n'] = uname['uname']
            u = Users.objects(name=uname['uname'])
            for u in u:
                c['s'] = u.status
            return render(request, "jsrz.html", c)
        for u in users:
            u.status = 'teacher'
            u.save()
        c['fankui'] = "认证成功"

        c['n'] = uname['uname']
        u = Users.objects(name=uname['uname'])
        for u in u:
            c['s'] = u.status
        return render(request, "jsrz.html", c)
    c['fankui'] = '无权限'
    c['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        c['s'] = u.status
    c['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        c['s'] = u.status
    return render(request, "jsrz.html", c)

def jsrz(request):
    c={}
    c['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        c['s'] = u.status
    return render(request, "jsrz.html",c)

def statistic(request):
    ctxs={}
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    user = Statistic.objects(name=uname['uname'])
    for u in user:
        if u.total == 0:
            ctxs['i']='您未答题无数据'

            ctxs['n'] = uname['uname']
            u = Users.objects(name=uname['uname'])
            for u in u:
                ctxs['s'] = u.status
            return render(request, "statistic.html", ctxs)
        ctxs['a']=u.total
        ctxs['b']=u.right/u.total
        ctxs['b']=format(ctxs['b'], '.2%')

    now = datetime.today()
    lastday = datetime(now.year, now.month, now.day)
    lastweek =datetime(now.year, now.month, now.day) - timedelta(days=now.weekday())
    lastmonth = datetime(now.year, now.month, 1)
    lastyear =datetime(now.year, 1, 1)
    ques = quesrecord.objects(name=uname['uname'])
    for ques in ques:
        if(ques.pubtime>lastday and ques.tf=="right"):
            d=d+1
            c=c+1
        elif(ques.pubtime>lastday):
            c=c+1
        if(ques.pubtime>lastweek and ques.tf=="right"):
            e=e+1
            f=f+1
        elif (ques.pubtime >lastweek):
            e=e+1
        if(ques.pubtime>lastmonth and ques.tf=="right"):
            g=g+1
            h=h+1
        elif (ques.pubtime > lastmonth):
            g=g+1
    if (c!=0):
        ctxs['c']=c
        ctxs['d']=format(d/c, '.2%')
    if (f!=0):
        ctxs['e'] = e
        ctxs['f'] = format(f/e, '.2%')
    if (g!=0):
        ctxs['g'] = g
        ctxs['h'] = format(h/g, '.2%')
    ctxs['n'] = uname['uname']
    u = Users.objects(name=uname['uname'])
    for u in u:
        ctxs['s'] = u.status
    return render(request, "statistic.html", ctxs)





def zujuanxt(request):
    return render(request, "zujuanxt.html")











