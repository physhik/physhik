# ruff: noqa
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.urls import path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token
from physhik.blog.views import (
    BlogListView,
    BlogDetailView,
    blog_category,
    ContactFormView,
    ProjectListView,
    ProjectDetailView,
    PostCreateView,
    PostUpdateView,
    DraftListView,
    factoring_problems,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("drafts/", DraftListView.as_view(), name="drafts"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("physhik.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("post/<slug:slug>/", BlogDetailView.as_view(), name="blog-detail"),
    path("category/<slug:category>/", blog_category, name="categories"),
    path("project/", ProjectListView.as_view(), name="project"),
    path("project/<slug:slug>", ProjectDetailView.as_view(), name="project-details"),
    path("contact/", ContactFormView.as_view(), name="contact"),
    path('problems/', factoring_problems, name='factoring_problems'),
    path("post/<slug:slug>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("new/", PostCreateView.as_view(), name="post_new"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("api/auth-token/", obtain_auth_token),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
