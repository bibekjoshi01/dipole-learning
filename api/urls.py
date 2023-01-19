from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import (
    TagViewset,
    CategoryViewset,
    PostViewset,
    CommentViewset,
    SubjectViewset,
    UnitViewset,
    ChapterViewset,
    HeadingViewset,
    Sub_HeadingViewset,
)

router = DefaultRouter()

#blog routers
router.register('post', PostViewset)
router.register('tag', TagViewset)
router.register('category', CategoryViewset)
router.register('comment', CommentViewset)

#Core_app routers
router.register('subject', SubjectViewset)
router.register('unit', UnitViewset)
router.register('chapter', ChapterViewset)
router.register('heading', HeadingViewset)
router.register('sub-heading', Sub_HeadingViewset)



urlpatterns = [
    path('', include(router.urls)),
]




