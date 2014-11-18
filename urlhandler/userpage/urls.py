from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
                       url(r'^$', 'userpage.views.home'),
                       url(r'^validate/try/$', 'userpage.views.validate_post'),
                       url(r'^validate/(?P<openid>\S+)/$', 'userpage.views.validate_view'),
                       url(r'^activity/(?P<activityid>\d+)/$','userpage.views.details_view'),
                       url(r'^ticket/(?P<uid>\S+)/$','userpage.views.ticket_view'),
                       url(r'^help/$','userpage.views.help_view'),
                       url(r'^helpact/$','userpage.views.helpact_view'),
                       url(r'^helpclub/$','userpage.views.helpclub_view'),
                       url(r'^helplecture/$','userpage.views.helplecture_view'),
                       url(r'^activity/(?P<actid>\d+)/menu/$', 'userpage.views.activity_menu_view'),
					   #以下为选座的url--刘博格,刘峻琳
					   url(r'^ticket/mainseat/(?P<uid>\S+)/$','userpage.views.choose_seat_mainmenu',name='mainmenu'),
					   url(r'^ticket/subseat/(?P<uid>\S+)/(?P<block_id>\d+)/$','userpage.views.choose_seat_submenu',name='submenu'),
                       )