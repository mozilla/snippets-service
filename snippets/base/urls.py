from django.urls import path

from watchman import views as watchman_views

from snippets.base import feed, views


urlpatterns = [
    path('', views.HomeView.as_view()),

    # ASRSnippets
    path('<int:startpage_version>/<name>/<version>/<appbuildid>/<build_target>/'
         '<locale>/<channel>/<os_version>/<distribution>/<distribution_version>/',
         views.fetch_snippets, name='base.fetch_snippets'),
    path('list/jobs/', views.JobListView.as_view(), name='base.list_jobs'),
    path('feeds/snippets.ics', feed.JobsFeed(), name='ical-feed'),

    path('preview-asr/<str:uuid>/', views.preview_asr_snippet, name='asr-preview'),
    # Application
    path('csp-violation-capture', views.csp_violation_capture, name='csp-violation-capture'),
    path('healthz/', watchman_views.ping, name='watchman.ping'),
    path('readiness/', watchman_views.status, name='watchman.status'),
]
