from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from myschool.models import Staff,Staff_Notification,Staff_leave,Staff_Feedback,Class,Section,Subject,Student,Attendance,Attendance_Report,StudentResult
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    return render(request,'Staff/staffHome.html')

@login_required(login_url='/')
def NOTIFICATION(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id
    notification = Staff_Notification.objects.filter(staff_id = staff_id)

    context = {
        'notification' : notification,
    }
    return render(request,'Staff/notification.html',context)

@login_required(login_url='/')
def STAFF_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Staff_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('notifications')

@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id

        staff_leave_history = Staff_leave.objects.filter(staff_id=staff_id)

        context = {
            'staff_leave_history':staff_leave_history,
        }
        return render(request,'Staff/apply_leave.html',context)

@login_required(login_url='/')
def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        staff = Staff.objects.get(admin = request.user.id)

        leave = Staff_leave(
            staff_id = staff,
            date = leave_date,
            message = leave_message,
        )
        leave.save()
        messages.success(request, 'Leave Application is Successfully Sent !')
        return redirect('staff_apply_leave')

@login_required(login_url='/')
def STAFF_FEEDBACK(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    feedback_history = Staff_Feedback.objects.filter(staff_id=staff_id)

    context = {
        'feedback_history': feedback_history,
    }
    return render(request,'Staff/feedback.html',context)

@login_required(login_url='/')
def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')

        staff = Staff.objects.get(admin = request.user.id)

        feedback = Staff_Feedback(
            staff_id = staff,
            feedback = feedback,
            feedback_reply = '',
        )
        feedback.save()
        messages.success(request, 'Thank You For Your Feedback !')
        return redirect('staff_feedback')

@login_required(login_url='/')
def STAFF_TAKE_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)

    subject = Subject.objects.filter(staff=staff_id)
    classes = Class.objects.all()
    section = Section.objects.all()
    action = request.GET.get('action')

    students = None
    get_subject = None
    get_class = None
    get_section = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            class_id = request.POST.get('class_id')
            section_id = request.POST.get('section_id')

            get_subject = Subject.objects.get(id=subject_id)
            get_class = Class.objects.get(id=class_id)
            get_section = Section.objects.get(id=section_id)

            subject = Subject.objects.filter(id=subject_id)
            for i in subject:
                student_id = i.classes.id
                students = Student.objects.filter(class_id=student_id)

    context = {
        'subject': subject,
        'class': classes,
        'section': section,
        'get_subject': get_subject,
        'get_class': get_class,
        'get_section': get_section,
        'action': action,
        'students': students,
    }
    return render(request,'Staff/take_attendance.html',context)

@login_required(login_url='/')
def STAFF_SAVE_ATTENDANCE(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        class_id = request.POST.get('class_id')
        section_id = request.POST.get('section_id')
        attendance_date = request.POST.get('attendance_date')
        student_id = request.POST.getlist('student_id')

        get_subject = Subject.objects.get(id=subject_id)
        get_class = Class.objects.get(id=class_id)
        get_section = Section.objects.get(id=section_id)

        attendance = Attendance(
            subject_id=get_subject,
            class_id=get_class,
            section_id=get_section,
            attendance_date=attendance_date,
        )
        attendance.save()
        for i in student_id:
            stud_id = i
            int_stud = int(stud_id)

            p_students = Student.objects.get(id = int_stud)
            attendance_report = Attendance_Report(
                student_id = p_students,
                attendance_id = attendance,
            )
            attendance_report.save()
    messages.success(request, 'Attendance Successfully Taken !')
    return redirect('staff_take_attendance')


def STAFF_VIEW_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)

    subject = Subject.objects.filter(staff_id=staff_id)
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

            attendance = Attendance.objects.filter(subject_id=get_subject,attendance_date=attendance_date)
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
        'attendance_report' : attendance_report,
    }
    return render(request,'Staff/view_attendance.html',context)


def STAFF_ADD_RESULT(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff_id=staff_id)
    classes = Class.objects.all()
    section = Section.objects.all()
    action = request.GET.get('action')

    get_subject = None
    get_class = None
    get_section = None
    students = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            class_id = request.POST.get('class_id')
            section_id = request.POST.get('section_id')

            get_subject = Subject.objects.get(id=subject_id)
            get_class = Class.objects.get(id=class_id)
            get_section = Section.objects.get(id=section_id)

            subject = Subject.objects.filter(id=subject_id)
            for i in subject:
                student_id = i.classes.id
                students = Student.objects.filter(class_id=student_id)

    context = {
        'subject': subject,
        'class': classes,
        'section': section,
        'action': action,
        'get_subject': get_subject,
        'get_class': get_class,
        'get_section': get_section,
        'students': students,
    }
    return render(request,'Staff/add_result.html',context)


def STAFF_SAVE_RESULT(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        class_id = request.POST.get('class_id')
        section_id = request.POST.get('section_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        Exam_mark = request.POST.get('Exam_mark')

        get_subject = Subject.objects.get(id=subject_id)
        get_student = Student.objects.get(admin = student_id)

        check_exist = StudentResult.objects.filter(subject_id=get_subject, student_id=get_student).exists()
        if check_exist:
            result = StudentResult.objects.get(subject_id=get_subject, student_id=get_student)
            result.assignment_mark = assignment_mark
            result.exam_mark = Exam_mark
            result.save()
            messages.success(request, "Result is Successfully Updated !")
            return redirect('staff_add_result')
        else:
            result = StudentResult(
                student_id=get_student,
                subject_id=get_subject,
                exam_mark=Exam_mark,
                assignment_mark=assignment_mark,
            )
            result.save()
            messages.success(request, "Successfully Added Result")
            return redirect('staff_add_result')