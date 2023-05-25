from .forms import UserUpdateForm, ProfileUpdateForm, ClubUpdateForm

def form_generator(request, account_type):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if account_type == 'Gplayer':
            p_form = ProfileUpdateForm(request.POST, 
                                       request.FILES,
                                       instance=request.user.playerprofile)
        else:
            p_form = ClubUpdateForm(request.POST, 
                                       request.FILES,
                                       instance=request.user.clubprofile)
    else:
        u_form = UserUpdateForm(instance=request.user)
        if account_type == 'Gplayer':
            p_form = ProfileUpdateForm(instance=request.user.playerprofile)
        else:
            p_form = ClubUpdateForm(instance=request.user.clubprofile)
    return u_form, p_form