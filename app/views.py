from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# indexにフォームを追加して動かす
from django.views.generic.edit import FormView
from . import forms
from .forms import TextForm

class IndexView(LoginRequiredMixin, TemplateView, FormView):
    form_class = forms.TextForm
    template_name = 'app/index.html'

    def form_valid(self, form):
        # form.cleaned_dataにフォームの入力内容が入っています
        data = form.cleaned_data
        text = data["text"]
        search = data["search"]
        replace = data["replace"]
        
        # ここで変換
        new_text = text.replace(search, replace)
        
        # テンプレートに渡す
        ctxt = self.get_context_data(new_text=new_text, form=form)
        return self.render_to_response(ctxt)







