"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from bbs.views import search,search_post,zhu,zhuce,log,login,web1,sd2020 ,summitgk0,summitgk,gkhandin,nextgk,shoucang,gkshoucang,schandin,nextsc,quxiaosc,fanhuisy,sd2019,sd2018,sd2016,sd2017,lastgk,lastsc,startzujuan,get_questions,zujuan,zjhandin,scpaper,jszjk,zujuandt,zjdthandin,nextzj,lastzj,zjshoucang,teacherrz,jsrz,statistic,gaokao,gktest,sctest,zujuanxt

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search-post$', search_post),
    path('zhuce/', zhu),
    url(r'^zhuce$', zhuce),
    path('', log),
    url(r'^login$', login),
    path('web1/', web1),
    path('gaokao/', gaokao),
    path('sd2020/', sd2020),
    path('sd2019/', sd2019),
    path('sd2018/', sd2018),
    path('sd2017/', sd2017),
    path('sd2016/', sd2016),
    path('gktest/<papermark>/<nian>/', gktest),
    path('gk/', summitgk0),
    url(r'^summitgk$', summitgk),
    url(r'^gkhandin$', gkhandin),
    url(r'^nextgk$', nextgk),
    url(r'^lastgk$', lastgk),
    url(r'^gkshoucang$', gkshoucang),
    path('shoucang/', sctest),
    url(r'^schandin$', schandin),
    url(r'^nextsc$', nextsc),
    url(r'^lastsc$', lastsc),
    url(r'^quxiaosc$', quxiaosc),
    url(r'^fanhuisy$', fanhuisy),
    path('zujuan/', zujuan),
    url(r'^startzujuan$', startzujuan),
    path('zjhandin/<papermark>/<mark>/<num_ber>/', zjhandin, name='urlName'),
    url(r'^scpaper', scpaper),
    path('jszjk/', jszjk),
    path('zujuandt/<paper>/', zujuandt, name='startzjdt'),
    url(r'^zjdthandin', zjdthandin),
    url(r'^nextzj', nextzj),
    url(r'^lastzj', lastzj),
    url(r'^zjshoucang', zjshoucang),
    url(r'^teacherrz', teacherrz),
    path('jsrz/', jsrz),
    path('statistic/', statistic),
    path('zujuanxt/', zujuanxt),




]

