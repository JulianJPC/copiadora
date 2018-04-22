from django.http import FileResponse
from django.conf.urls.static import static
from django.conf.urls import url
from copiadora.apps import CopiadoraConfig

def base(request, *dummy):
    """
    :param request:
    :return:
    """
    data = None
    with open(CopiadoraConfig.static_dirs.get('/'), "rb") as foundfile:
        data = foundfile.read()
    return FileResponse(data)

urlpatterns = [
]
#urlpatterns += WebWs.urlset


# Agrega los directorios estaticos
for prefix in CopiadoraConfig.static_dirs.keys():
    # Valida que entre siempre al inicio
    if prefix == '/':
        urlpatterns += [url(r"^$", base)]
    else:
        urlpatterns += static(prefix, document_root=CopiadoraConfig.static_dirs.get(prefix))