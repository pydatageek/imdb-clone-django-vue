"""Views are so thin because no need to serve anything from server"""
from django.views.generic import TemplateView


class MovieCommentList(TemplateView):
    pass


class MovieCommentDetail(TemplateView):
    pass


class CelebCommentList(TemplateView):
    pass


class CelebCommentDetail(TemplateView):
    pass
