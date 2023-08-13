from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .forms import CommentForm

# Create your views here.

class CommentView(TemplateView):
    http_method_names = ['post']
    template_name = 'comment/result.html'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        target = request.POST.get('target')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.target = target
            instance.save()
            succeeded = True
            return redirect(target)
        else:
            succeeded = False

        context = {
              "succeed": succeeded,
              "form": form,
              "target": target,
        }
        return self.render_to_response(context)
