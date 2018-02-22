from django.core.exceptions import PermissionDeniedfrom django.contrib.auth.decorators import login_required, user_passes_testfrom django.http import HttpResponse, Http404from django.template import loaderfrom .models import *from .utils import *def is_coordinator(usr):    user = get_FSJ_user(usr)    if not isinstance(user, Coordinator):        raise PermissionDenied    return True@login_required@user_passes_test(is_coordinator)def coordinator_home(request, FSJ_user):    context = get_standard_context(FSJ_user)       template = loader.get_template("FSJ/coord_home.html")    return HttpResponse(template.render(context, request))@login_required@user_passes_test(is_coordinator)def coordinator_studentlist(request):    FSJ_user = get_FSJ_user(request.user.username)    student_list = Student.objects.all()    template = loader.get_template("FSJ/coord_student_list.html")    context = get_standard_context(FSJ_user)    context["student_list"] = student_list    return HttpResponse(template.render(context, request))         @login_required@user_passes_test(is_coordinator)def coordinator_studentdetail(request, usr_ccid):    FSJ_user = get_FSJ_user(request.user.username)    try:        student = Student.objects.get(ccid = usr_ccid)    except Student.DoesNotExist:        raise Http404("Student does not exist")    context = get_standard_context(FSJ_user)    context["student"] = student      template = loader.get_template("FSJ/coord_student_view.html")    return HttpResponse(template.render(context, request))@login_required@user_passes_test(is_coordinator)def coordinator_awards(request, FSJ_user):	awards_list = Award.objects.all()	template = loader.get_template("FSJ/coord_awards_list.html")	context = get_standard_context(FSJ_user)	context["awards_list"] = awards_list	return HttpResponse(template.render(context,request))# @login_required# @user_passes_test(is_coordinator)# def coordinator_add_awards(request):# 	FSJ_user = get_FSJ_user(request.user.username)# 	template = loader.get_template("FSJ/add_award.html")# 	context = get_standard_context(FSJ_user)# 	return HttpResponse(template.render(context,request))