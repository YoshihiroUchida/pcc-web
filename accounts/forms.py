from django.contrib.auth.forms import AuthenticationForm 

# ログイン用 (ユーザ名／パスワード)
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control' # class属性へ指定
            field.widget.attrs['placeholder'] = field.label # label属性の指定
