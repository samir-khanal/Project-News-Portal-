from .models import Category, Setting
def data_pass(request):
    data = {
        'title':"News Portal",
        'settingData':Setting.objects.first(),
        'menuCategory':Category.objects.all(),
    }
    return data