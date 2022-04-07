from django.contrib.auth.forms import AuthenticationForm 

# ログイン用 (ユーザー名／パスワード)
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'