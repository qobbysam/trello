



from .models import UserHandInput, UserFileUpload


def handle_user_input_get(user):
    try:

        objs = UserHandInput.objects.filter(user=user)

        return objs, True
    except Exception as e:
        print(e)
        return None, False
def handle_user_file_get(user):
    try:

        objs = UserFileUpload.objects.filter(file_user=user)

        return objs, True
    except Exception as e:
        print(e)
        return None, False

def handle_user_input_post(user , form):

    userhandinput = UserHandInput( age= form.cleaned_data['age'], user=user)
    try:
        userhandinput.save()
        return True
    except:
        return False

    

def handle_user_file_input_post(user, form):

    userfileupload = UserFileUpload(
           file_name = form.cleaned_data['file_name'],
            file_type = form.cleaned_data['file_type'],
            file = form.cleaned_data['file'],
            file_user = user
            )

    try:
        userfileupload.save()

        return True
    except Exception as e:
        print(e)
        return False




