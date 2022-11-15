from django import forms


class TopicSearchForm(forms.Form):
    """
    Topic 表单
    """
    title = forms.CharField(label="Topic Title")