from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        self.fields['username'].disabled = True
        #부모클래스와 다 동일하게하고, username이라는 특성에 disabled를 True
        #개발자도구에서 아이디 변경이 가능하지만 위 기능을 사용함으로 이 기능을 막음.