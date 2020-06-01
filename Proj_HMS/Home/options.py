from django.contrib.auth.models import Group

def grp(user, grpn):
    try:
        group = Group.objects.get(name=grpn)
        return True if group in user.groups.all() else False
    except:
        return False

def action(request):
    actions = {}
    user = request.user
    if grp(user, 'Doctors'):
        actions['Appointments'] = '/appointments'
        actions['Reports'] = '/reports'
        actions['Generate Report'] = '/reports/new                                                                                                                                                                                                             '
        
        
    elif grp(user, 'Patients'):
        actions['Reports'] = '/reports/'+str(user.username)+'/'
        actions['Bills'] = '/bills/'+str(user.username)
        

    elif grp(user, 'Receptionist'):
        actions['New Patient'] = '/register'
        actions['New Appointment'] = '/appointments/book'
        actions['Bills'] = '/bills'
        
    return actions