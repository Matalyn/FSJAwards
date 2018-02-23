from django.core.exceptions import PermissionDeniedfrom django.views.decorators.csrf import csrf_exemptfrom django.contrib.auth.decorators import login_required, user_passes_testfrom django.http import HttpResponse, Http404from django.template import loaderfrom django.shortcuts import redirectfrom .models import *from .utils import *from .forms import *def is_coordinator(usr):    user = get_FSJ_user(usr)    if not isinstance(user, Coordinator):        raise PermissionDenied    return True@login_required@user_passes_test(is_coordinator)def coordinator_home(request, FSJ_user):    context = get_standard_context(FSJ_user)       template = loader.get_template("FSJ/home.html")    return HttpResponse(template.render(context, request))@login_required@user_passes_test(is_coordinator)def coordinator_studentlist(request):    FSJ_user = get_FSJ_user(request.user.username)    student_list = Student.objects.all()    template = loader.get_template("FSJ/coord_student_list.html")    context = get_standard_context(FSJ_user)    context["student_list"] = student_list    return HttpResponse(template.render(context, request)) @login_required@user_passes_test(is_coordinator)def coordinator_adjudicatorlist(request):    FSJ_user = get_FSJ_user(request.user.username)    adjudicator_list = Adjudicator.objects.all()    template = loader.get_template("FSJ/coord_adjudicator_list.html")    context = get_standard_context(FSJ_user)    context["adjudicator_list"] = adjudicator_list    return HttpResponse(template.render(context, request))         @login_required@user_passes_test(is_coordinator)def coordinator_studentdetail(request, usr_ccid):    FSJ_user = get_FSJ_user(request.user.username)    try:        student = Student.objects.get(ccid = usr_ccid)    except Student.DoesNotExist:        raise Http404("Student does not exist")        if request.method == "POST":        form = StudentForm(request.POST, instance=student)        if form.is_valid():            form.save()            return redirect('studentlist')        else:            raise ValueError    else:        form = StudentForm(instance=student)        context = get_standard_context(FSJ_user)        context["student"] = student        context["form"] = form        url = "/studentlist/" + student.ccid + "/"        context["url"] = url        template = loader.get_template("FSJ/profile.html")        return HttpResponse(template.render(context, request))@login_required@user_passes_test(is_coordinator)def coordinator_adjudicatordetail(request, usr_ccid):    FSJ_user = get_FSJ_user(request.user.username)    try:        adjudicator = Adjudicator.objects.get(ccid = usr_ccid)    except Adjudicator.DoesNotExist:        raise Http404("Adjudicator does not exist")        if request.method == "POST":        form = AdjudicatorForm(request.POST, instance=adjudicator)        if form.is_valid():            form.save()            return redirect('adjudicatorlist')        else:            raise ValueError    else:        form = AdjudicatorForm(instance=adjudicator)        context = get_standard_context(FSJ_user)        context["adjudicator"] = adjudicator        context["form"] = form        url = "/adjudicatorlist/" + adjudicator.ccid + "/"        context["url"] = url        template = loader.get_template("FSJ/profile.html")        return HttpResponse(template.render(context, request))@login_required@user_passes_test(is_coordinator)def coordinator_addstudent(request):    FSJ_user = get_FSJ_user(request.user.username)    if request.method == "POST":        form = StudentForm(request.POST)        if form.is_valid:            form.save()            return redirect('studentlist')    else:        form = StudentForm()        context = get_standard_context(FSJ_user)        template = loader.get_template("FSJ/profile.html")        context["form"] = form        url = "/studentlist/add/"        context["url"] = url        return HttpResponse(template.render(context, request))@login_required@user_passes_test(is_coordinator)def coordinator_addadjudicator(request):    FSJ_user = get_FSJ_user(request.user.username)    if request.method == "POST":        form = AdjudicatorForm(request.POST)        if form.is_valid:            form.save()            return redirect('adjudicatorlist')    else:        form = AdjudicatorForm()                   context = get_standard_context(FSJ_user)        template = loader.get_template("FSJ/profile.html")        context["form"] = form        url = "/adjudicatorlist/add/"        context["url"] = url        return HttpResponse(template.render(context, request))@login_required@user_passes_test(is_coordinator)def coordinator_deletestudent(request):    if request.method == 'POST':        id_list = request.POST.getlist('instance')        for usr_ccid in id_list:            Student.objects.get(ccid=usr_ccid).delete()                    return redirect('studentlist')        @login_required@user_passes_test(is_coordinator)def coordinator_deleteadjudicator(request):    if request.method == 'POST':        id_list = request.POST.getlist('instance')        for usr_ccid in id_list:            Adjudicator.objects.get(ccid=usr_ccid).delete()                    return redirect('adjudicatorlist')