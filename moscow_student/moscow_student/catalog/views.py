from django.shortcuts import render
from .forms import AuthorizationForm
import vk_api


def autolike(request):
    # Если данный запрос типа POST, тогда
    # Создаем экземпляр формы и заполняем данными из запроса (связывание, binding):
    form = AuthorizationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # Обработка данных из form.cleaned_data
            N = 15  # Количество постов
            groups_owner_id = -492221  # id группы студент москвы -133029999
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            vk_session = vk_api.VkApi(login, password)
            vk_session.auth()

            vk = vk_session.get_api()
            # Получаем id N постов
            results = vk.wall.get(owner_id=groups_owner_id, count=N)
            # Цикл, который простовляет лайки, если их нет
            for i in range(len(results['items'])):
                if not vk.likes.isLiked(type="post", owner_id=groups_owner_id, item_id=results['items'][i]['id'])['liked']:
                    vk.likes.add(type="post", owner_id=groups_owner_id, item_id=results['items'][i]['id'])

    return render(request, 'autolike.html', {'form': form, })