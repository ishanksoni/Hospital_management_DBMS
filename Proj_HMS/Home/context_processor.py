from django.contrib.auth.models import Group

def hasGroup(user, groupName):
    try:
        group = Group.objects.get(name=groupName)
        return True if group in user.groups.all() else False
    except:
        return False

def menu_processor(request):
    menu = {}
    user = request.user
    if hasGroup(user, 'Doctors'):
        menu['Appointments'] = '/appointments'
        menu['Reports'] = '/reports'
        menu['Generate Report'] = '/reports/generate'
        
    elif hasGroup(user, 'Patients'):
        menu['Reports'] = '/reports'
        menu['Appointments'] = '/appointments'
        menu['Medication'] = '/bill/medicines'
        menu['Bills'] = '/bill'

    elif hasGroup(user, 'Receptionist'):
        menu['New Patient'] = '/register'
        menu['Manage Appointments'] = '/appointments'
        menu['New Appointment'] = '/appointments/book'
        menu['Bills'] = '/bill'
    
    elif hasGroup(user, 'inventory_manager'):
        menu['All Stock'] = ''
        menu['Stock Details'] = ''

    return {'menu': menu}