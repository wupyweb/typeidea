from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostAdminForm(forms.ModelForm):
    # desc = forms.CharField(widget=forms.Textarea, label="摘要", required=True)
    content = forms.CharField(widget=CKEditorUploadingWidget, label="正文", required=True)