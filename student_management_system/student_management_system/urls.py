
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views,Hod_views,Staff_views,Student_views

admin.site.site_header = "LONDON GRACE ADMINISTRATION"
admin.site.site_title = "London Grace Admin Portal"
admin.site.index_title = "Welcome to London Grace Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),

    #login-path
    path('',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),

    # Profile Update
    path('Profile',views.PROFILE,name='profile'),
    path('Profile/update',views.PROFILE_UPDATE,name = 'profile_update'),

    #contact
    path('Contact',views.CONTACT,name='contact'),

    #ABOUT
    path('About',views.ABOUT,name='about'),

    #This is HOD panel url
    path('Hod/Home',Hod_views.HOME,name='hod_home'),
    path('Hod/Student/Add',Hod_views.ADD_STUDENT,name = 'add_student'),
    path('Hod/Student/View',Hod_views.VIEW_STUDENT,name = 'view_student'),
    path('Hod/Student/Edit/<str:id>',Hod_views.EDIT_STUDENT,name = 'edit_student'),
    path('Hod/Student/Update',Hod_views.UPDATE_STUDENT,name = 'update_student'),
    path('Hod/Student/Delete/<str:admin>',Hod_views.DELETE_STUDENT, name='delete_student'),

    path('Hod/Staff/Add',Hod_views.ADD_STAFF,name = 'add_staff'),
    path('Hod/Staff/View',Hod_views.VIEW_STAFF,name = 'view_staff'),
    path('Hod/Staff/Edit/<str:id>',Hod_views.EDIT_STAFF,name = 'edit_staff'),
    path('Hod/Staff/Update',Hod_views.UPDATE_STAFF, name='update_staff'),
    path('Hod/Staff/Delete/<str:admin>',Hod_views.DELETE_STAFF, name='delete_staff'),

    path('Hod/Class/Add',Hod_views.ADD_CLASS, name='add_class'),
    path('Hod/Class/View',Hod_views.VIEW_CLASS, name='view_class'),
    path('Hod/Class/Edit/<str:id>',Hod_views.EDIT_CLASS, name='edit_class'),
    path('Hod/Class/Update',Hod_views.UPDATE_CLASS, name='update_class'),
    path('Hod/Class/Delete/<str:id>',Hod_views.DELETE_CLASS, name='delete_class'),

    path('Hod/Subject/Add', Hod_views.ADD_SUBJECT, name='add_subject'),
    path('Hod/Subject/View', Hod_views.VIEW_SUBJECT, name='view_subject'),
    path('Hod/Subject/Edit/<str:id>',Hod_views.EDIT_SUBJECT,name = 'edit_subject'),
    path('Hod/Subject/Update',Hod_views.UPDATE_SUBJECT, name='update_subject'),
    path('Hod/Subject/Delete/<str:id>',Hod_views.DELETE_SUBJECT, name='delete_subject'),

    path('Hod/Staff/Send_Notification',Hod_views.STAFF_SEND_NOTIFICATION, name='staff_send_notification'),
    path('Hod/Staff/Save_Notification',Hod_views.STAFF_SAVE_NOTIFICATION, name='save_staff_notification'),
    path('Hod/Student/Send_Notification',Hod_views.STUDENT_SEND_NOTIFICATION, name='student_send_notification'),
    path('Hod/Student/Save_Notification',Hod_views.STUDENT_SAVE_NOTIFICATION, name='save_student_notification'),

    path('Hod/Staff/Leave_view',Hod_views.STAFF_LEAVE_VIEW,name = 'staff_leave_view'),
    path('Hod/Staff/approve_leave/<str:id>',Hod_views.STAFF_APPROVE_LEAVE,name = 'staff_approve_leave'),
    path('Hod/Staff/decline_leave/<str:id>',Hod_views.STAFF_DECLINE_LEAVE,name = 'staff_decline_leave'),
    path('Hod/Student/Leave_view',Hod_views.STUDENT_LEAVE_VIEW,name = 'student_leave_view'),
    path('Hod/Student/approve_leave/<str:id>',Hod_views.STUDENT_APPROVE_LEAVE,name = 'student_approve_leave'),
    path('Hod/Student/decline_leave/<str:id>',Hod_views.STUDENT_DECLINE_LEAVE,name = 'student_decline_leave'),

    path('Hod/Staff/feedback', Hod_views.STAFF_FEEDBACK_REPLY, name ='staff_feedback_reply'),
    path('Hod/Staff/feedback/save', Hod_views.STAFF_FEEDBACK_REPLY_SAVE, name ='staff_feedback_reply_save'),
    path('Hod/Student/feedback', Hod_views.STUDENT_FEEDBACK_REPLY, name ='student_feedback_reply'),
    path('Hod/Student/feedback/save', Hod_views.STUDENT_FEEDBACK_REPLY_SAVE, name ='student_feedback_reply_save'),

    path('Hod/View_Attendance',Hod_views.VIEW_ATTENDANCE, name='view_attendance'),

    #this is staff urls
    path('Staff/Home',Staff_views.HOME,name='staff_home'),


    path('Staff/Notification',Staff_views.NOTIFICATION, name='notifications'),
    path('Staff/mark_as_done/<str:status>',Staff_views.STAFF_NOTIFICATION_MARK_AS_DONE, name='staff_notification_mark_as_done'),
    path('Staff/Apply_leave',Staff_views.STAFF_APPLY_LEAVE, name='staff_apply_leave'),
    path('Staff/Apply_leave_save',Staff_views.STAFF_APPLY_LEAVE_SAVE, name='staff_apply_leave_save'),

    path('Staff/Feedback',Staff_views.STAFF_FEEDBACK, name='staff_feedback'),
    path('Staff/Feedback/Save',Staff_views.STAFF_FEEDBACK_SAVE, name='staff_feedback_save'),

    path('Staff/Take_Attendance',Staff_views.STAFF_TAKE_ATTENDANCE, name='staff_take_attendance'),
    path('Staff/Save_Attendance',Staff_views.STAFF_SAVE_ATTENDANCE, name='staff_save_attendance'),
    path('Staff/View_Attendance',Staff_views.STAFF_VIEW_ATTENDANCE, name='staff_view_attendance'),

    path('Staff/Add/Result',Staff_views.STAFF_ADD_RESULT, name='staff_add_result'),
    path('Staff/Save/Result',Staff_views.STAFF_SAVE_RESULT, name='staff_save_result'),

#this is student urls
    path('Student/Home',Student_views.HOME,name='student_home'),

    path('Student/Notification',Student_views.STUDENT_NOTIFICATION, name='student_notification'),
    path('Student/mark_as_done/<str:status>',Student_views.STUDENT_NOTIFICATION_MARK_AS_DONE, name='student_notification_mark_as_done'),

    path('Student/Feedback',Student_views.STUDENT_FEEDBACK, name='student_feedback'),
    path('Student/Feedback/Save',Student_views.STUDENT_FEEDBACK_SAVE, name='student_feedback_save'),
    path('Student/Apply_leave',Student_views.STUDENT_APPLY_LEAVE, name='student_apply_leave'),
    path('Student/Apply_leave_save',Student_views.STUDENT_APPLY_LEAVE_SAVE, name='student_apply_leave_save'),

    path('Student/View_Attendance',Student_views.STUDENT_VIEW_ATTENDANCE, name='student_view_attendance'),

    path('Student/View_Result',Student_views.VIEW_RESULT, name='view_result'),



] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)












