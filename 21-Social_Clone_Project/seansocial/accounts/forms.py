from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    #THE METACLASS CONNECTS THE FORM TO THE MODEL
    class Meta:
        fields = ('username','email','password1','password2')
        #the model comes from the baked in model given to you by the contrib.auth library
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init(*args,**kwargs)
        #THIS SETS UP THE LABELS FOR THE FORM FIELDS BASED ON THE MODEL FIELDS
        self.fields['username'].label = "Display Name"
        self.fields['email'].label = "Email Address"
