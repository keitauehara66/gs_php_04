from typing import Text
from django import forms
from django.core.exceptions import ValidationError

widget_textarea = forms.Textarea(
    attrs={
        "class": "form-control"
    }
)

widget_textinput = forms.TextInput(
    attrs={
        "class": "form-control"
    }
)

class TextForm(forms.Form):
    text = forms.CharField(label="", widget=widget_textarea)
    search = forms.CharField(label="検索", widget=widget_textinput)
    replace = forms.CharField(label="置換", widget=widget_textinput)

    # 文字数でバリデーション
    def clean(self):
        # djangoもともとのバリデーションを実行してデータを取得
        data = super().clean()
        text = data["text"]
        if len(text) <= 5:
            raise ValidationError("テキストが短すぎます。")
            
        # 最後は必ずデータ全体を返します
        return data

