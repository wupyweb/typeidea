from django import forms
import mistune

from .models import Comment


class CommentForm(forms.ModelForm):
    """
    评论表单
    """
    nickname = forms.CharField(
        label='昵称',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'whidth: 60%;'}),
        error_messages={'required': '请输入昵称'}
    )
    email = forms.EmailField(
        label='邮箱',
        max_length=50,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'style': 'whidth: 60%;'}),
        error_messages={'required': '请输入邮箱'}
    )
    website = forms.URLField(
        label='网站',
        max_length=100,
        widget=forms.URLInput(attrs={'class': 'form-control', 'style': 'whidth: 60%;'}),
        required=False
    )
    content = forms.CharField(
        label='内容',
        max_length=500,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 60}),
        error_messages={'required': '请输入内容'}
    )

    def clean_content(self):
        """
        验证评论内容
        """
        content = self.cleaned_data['content']
        if len(content) < 5:
            raise forms.ValidationError('内容太短')
        content = mistune.markdown(content)
        return content
    

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']