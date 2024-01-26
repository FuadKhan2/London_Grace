from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from myschool.models import Class,Section,CustomUser,Student,Staff,Subject,Staff_Notification,Staff_leave,Staff_Feedback,Student_Notification,Student_Feedback,Student_leave,Attendance,Attendance_Report
from django.contrib import messages



@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    class_count = Class.objects.all().count()
    subject_count = Subject.objects.all().count()

    student_gender_male = Student.objects.filter(gender = 'Male').count()
    student_gender_female = Student.objects.filter(gender ='Female').count()

    context = {
        'student_count': student_count,
        'staff_count': staff_count,
        'class_count': class_count,
        'subject_count': subject_count,
        'student_gender_male': student_gender_male,
        'student_gender_female': student_gender_female,
    }
    return render(request,'Hod/home.html',context)

@login_required(login_url='/')
def ADD_STUDENT(request):
    global email, username
    classes = Class.objects.all()
    section = Section.objects.all()

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        profile_pic = request.FILES.get('profile_pic')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        class_id = request.POST.get('class_id')
        section_id = request.POST.get('section_id')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email Is Already Used')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username Is Already Used')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3,
                date_of_birth = date_of_birth,

            )
            user.set_password(password)
            user.save()

            classes = Class.objects.get(id=class_id)
            section = Section.objects.get(id=section_id)

            student = Student(
                admin = user,
                address = address,
                section_id = section,
                class_id = classes,
                gender = gender,
            )
            student.save()
            messages.success(request,user.first_name + " " + user.last_name + " Is Successfully Added ! ")
            return redirect('add_student')


    context = {
        'class': classes,
        'section':section,
    }
    return render(request,'Hod/add_student.html',context)

@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Student.objects.all()

    context = {
        'student':student,
    }
    return render(request,'Hod/view_student.html',context)

@login_required(login_url='/')
def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id = id)
    classes = Class.objects.all()
    section = Section.objects.all()

    context = {
        'student':student,
        'class': classes,
        'section': section,
    }
    return render(request,'Hod/edit_student.html',context)

@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        profile_pic = request.FILES.get('profile_pic')
        student_id = request.POST.get('student_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        class_id = request.POST.get('class_id')
        section_id = request.POST.get('section_id')
        address = request.POST.get('address')


        user = CustomUser.objects.get(id = student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.date_of_birth = date_of_birth

        if profile_pic !=None and profile_pic !="":
            user.profile_pic = profile_pic
        if password !=None and password !="":
            user.set_password(password)

        user.save()

        student = Student.objects.get(admin = student_id)
        student.address = address
        student.gender = gender

        classes = Class.objects.get(id = class_id)
        student.class_id = classes

        section = Section.objects.get(id = section_id)
        student.section_id = section

        student.save()
        messages.success(request,'Records Are Successfully Updated !')
        return  redirect('view_student')

    return render(request,'Hod/edit_student.html')

@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request,'Record is Successfully Deleted !')
    return redirect('view_student')

@login_required(login_url='/')
def ADD_CLASS(request):
    if request.method == "POST":
        class_name = request.POST.get('class_name')

        classes = Class(
            name = class_name,
        )
        classes.save()
        messages.success(request,'Class Is successfully Created !')
        return  redirect('add_class')
    return render(request,'Hod/add_class.html')

@login_required(login_url='/')
def VIEW_CLASS(request):
    classes = Class.objects.all()
    context = {
        'class':classes,
    }
    return render(request,'Hod/view_class.html',context)

@login_required(login_url='/')
def EDIT_CLASS(request,id):
    classes = Class.objects.get(id = id)

    context = {
        'class': classes,
    }
    return render(request,'Hod/edit_class.html',context)

@login_required(login_url='/')
def UPDATE_CLASS(request):
    if request.method == "POST":
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')

        classes = Class.objects.get(id=class_id)
        classes.name = name
        classes.save()
        messages.success(request, 'Class Is successfully Updated !')
        return redirect('view_class')

    return render(request,'Hod/edit_class.html')

@login_required(login_url='/')
def DELETE_CLASS(request,id):
    classes = Class.objects.get(id=id)
    classes.delete()
    messages.success(request, 'Class Is successfully Deleted !')

    return redirect('view_class')

@login_required(login_url='/')
def ADD_STAFF(request):
    global email, username

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        profile_pic = request.FILES.get('profile_pic')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email Is Already Used !')
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username Is Already Used !')
            return redirect('add_staff')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 2,
                date_of_birth = date_of_birth,

            )
            user.set_password(password)
            user.save()

            staff = Staff(
                admin = user,
                address = address,
                gender = gender,
            )
            staff.save()
            messages.success(request,user.first_name + " " + user.last_name + " Is Successfully Added ! ")
            return redirect('add_staff')

    return render(request,'Hod/add_staff.html')

@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()

    context = {
        'staff': staff,
    }
    return render(request,'Hod/view_staff.html',context)

@login_required(login_url='/')
def EDIT_STAFF(request,id):
    staff = Staff.objects.filter(id=id)

    context = {
        'staff': staff,
    }
    return render(request,'Hod/edit_staff.html',context)

@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        profile_pic = request.FILES.get('profile_pic')
        staff_id = request.POST.get('staff_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        address = request.POST.get('address')


        user = CustomUser.objects.get(id = staff_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.date_of_birth = date_of_birth

        if profile_pic !=None and profile_pic !="":
            user.profile_pic = profile_pic
        if password !=None and password !="":
            user.set_password(password)

        user.save()

        staff = Staff.objects.get(admin = staff_id)
        staff.address = address
        staff.gender = gender

        staff.save()
        messages.success(request,'Staff Record is Successfully Updated !')
        return redirect('view_staff')

    return render(request,'Hod/edit_staff.html')

@login_required(login_url='/')
def DELETE_STAFF(request,admin):
    staff = CustomUser.objects.get(id = admin)
    staff.delete()
    messages.success(request,'Record is Successfully Deleted !')
    return redirect('view_staff')

@login_required(login_url='/')
def ADD_SUBJECT(request):
    classes = Class.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        class_id = request.POST.get('class_id')
        staff_id = request.POST.get('staff_id')

        classes = Class.objects.get(id=class_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            name = subject_name,
            classes = classes,
            staff = staff,
        )
        subject.save()
        messages.success(request,"Subject Is Successfully Added ! ")
        return redirect('add_subject')

    context = {
        'class': classes,
        'staff': staff,
    }
    return render(request,'Hod/add_subject.html',context)

@login_required(login_url='/')
def VIEW_SUBJECT(request):
    subject = Subject.objects.all()

    context = {
        'subject': subject,
    }

    return render(request,'Hod/view_subject.html',context)

@login_required(login_url='/')
def EDIT_SUBJECT(request,id):
    subject = Subject.objects.get(id=id)
    classes = Class.objects.all()
    staff = Staff.objects.all()

    context = {
        'subject': subject,
        'class': classes,
        'staff': staff,
    }
    return render(request, 'Hod/edit_subject.html', context)

@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        class_id = request.POST.get('class_id')
        staff_id = request.POST.get('staff_id')

        classes = Class.objects.get(id=class_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            id=subject_id,
            name=subject_name,
            classes=classes,
            staff=staff,
        )
        subject.save()
        messages.success(request, 'Subject Is successfully Updated !')
        return redirect('view_subject')

    return render(request, 'Hod/edit_subject.html')

@login_required(login_url='/')
def DELETE_SUBJECT(request,id):
    subject = Subject.objects.filter(id=id)
    subject.delete()
    messages.success(request, 'Subject Is successfully Deleted !')

    return redirect('view_subject')

@login_required(login_url='/')
def STAFF_SEND_NOTIFICATION(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')[0:5]

    context = {
        'staff': staff,
        'see_notification': see_notification,
    }
    return render(request, 'Hod/staff_notification.html',context)

@login_required(login_url='/')
def STAFF_SAVE_NOTIFICATION(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(id = staff_id)

        notification = Staff_Notification(
            staff_id = staff,
            message = message,
        )
        notification.save()
        messages.success(request, 'Notification Is successfully Sent !')
        return redirect('staff_send_notification')

@login_required(login_url='/')
def STAFF_LEAVE_VIEW(request):
    staff_leave = Staff_leave.objects.all()
    context = {
        'staff_leave':staff_leave,
    }
    return render(request, 'Hod/staff_leave.html',context)

@login_required(login_url='/')
def STAFF_APPROVE_LEAVE(request,id):
    leave = Staff_leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view')

@login_required(login_url='/')
def STAFF_DECLINE_LEAVE(request,id):
    leave = Staff_leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_view')

@login_required(login_url='/')
def STAFF_FEEDBACK_REPLY(request):
    feedback = Staff_Feedback.objects.all()
    feedback_history = Staff_Feedback.objects.all()

    context = {
        'feedback': feedback,
        'feedback_history': feedback_history,
    }
    return render(request, 'Hod/staff_feedback_reply.html',context)

@login_required(login_url='/')
def STAFF_FEEDBACK_REPLY_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Staff_Feedback.objects.get(id = feedback_id)
        feedback.feedback_reply  = feedback_reply
        feedback.status = 1
        feedback.save()
        messages.success(request, 'Thank You For Your Reply !')
        return redirect('staff_feedback_reply')

@login_required(login_url='/')
def STUDENT_SEND_NOTIFICATION(request):
    student = Student.objects.all()
    see_student_notification = Student_Notification.objects.all().order_by('-id')[0:5]


    context = {
        'student': student,
        'see_student_notification': see_student_notification,
    }
    return render(request, 'Hod/student_notification.html', context)

@login_required(login_url='/')
def STUDENT_SAVE_NOTIFICATION(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        message = request.POST.get('message')

        student = Student.objects.get(admin = student_id)

        stud_notification = Student_Notification(
            student_id = student,
            message = message,
        )
        stud_notification.save()
        messages.success(request, 'Notification Is successfully Sent !')
        return redirect('student_send_notification')

@login_required(login_url='/')
def STUDENT_FEEDBACK_REPLY(request):
    feedback = Student_Feedback.objects.all()
    feedback_history = Student_Feedback.objects.all().order_by('-id')[0:5]

    context = {
        'feedback': feedback,
        'feedback_history': feedback_history,
    }
    return render(request, 'Hod/student_feedback_reply.html',context)
@login_required(login_url='/')
def STUDENT_FEEDBACK_REPLY_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Student_Feedback.objects.get(id = feedback_id)
        feedback.feedback_reply  = feedback_reply
        feedback.status = 1
        feedback.save()
        messages.success(request, 'Thank You For Your Reply !')
        return redirect('student_feedback_reply')

@login_required(login_url='/')
def STUDENT_LEAVE_VIEW(request):
    student_leave = Student_leave.objects.all()
    context = {
        'student_leave':student_leave,
    }
    return render(request, 'Hod/student_leave.html',context)

@login_required(login_url='/')
def STUDENT_APPROVE_LEAVE(request,id):
    leave = Student_leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('student_leave_view')

@login_required(login_url='/')
def STUDENT_DECLINE_LEAVE(request,id):
    leave = Student_leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('student_leave_view')


def VIEW_ATTENDANCE(request):
    subject = Subject.objects.all()
    classes = Class.objects.all()
    section = Section.objects.all()
    action = request.GET.get('action')

    students = None
    get_subject = None
    get_class = None
    get_section = None
    attendance_date = None
    attendance_report = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            class_id = request.POST.get('class_id')
            section_id = request.POST.get('section_id')
            attendance_date = request.POST.get('attendance_date')

            get_subject = Subject.objects.get(id=subject_id)
            get_class = Class.objects.get(id=class_id)
            get_section = Section.objects.get(id=section_id)

            attendance = Attendance.objects.filter(subject_id=get_subject, attendance_date=attendance_date)
            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(attendance_id=attendance_id)

    context = {
        'subject': subject,
        'class': classes,
        'section': section,
        'get_subject': get_subject,
        'get_class': get_class,
        'get_section': get_section,
        'action': action,
        'students': students,
        'attendance_date': attendance_date,
        'attendance_report': attendance_report,
    }
    return render(request, 'Hod/view_attendance.html',context)