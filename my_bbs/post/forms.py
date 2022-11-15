from django import forms

from post.models import Topic


class TopicSearchForm(forms.Form):
    """
    Topic 表单
    """
    title = forms.CharField(label="Topic Title")

    def clean(self):
        """
        验证所有字段合法性
        :return:
        """
        super().clean()

    def clean_title(self):
        """
        验证指定字段合法性
        :return:
        """
        title = self.cleaned_data.get("title")
        if len(title) < 5:
            raise forms.ValidationError("字符串长度太短")
        return title


class TopicModelForm(forms.ModelForm):
    """
    ModelForm使用
    """
    class Meta:
        model = Topic
        exclude = ("is_online", "user")

