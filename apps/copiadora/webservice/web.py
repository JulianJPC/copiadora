from django.conf.urls import url
from django.views.decorators import http
from django.views.decorators import csrf

from wm.web.response.ErrorServiceResponse import ErrorServiceResponse
from wm.web.response.VoidServiceResponse import VoidServiceResponse
from wm.business.exception.ValidationException import ValidationException
from wm.web.response.BaseServiceResponse import BaseServiceResponse
from wm.apps import LoggerFactory

@http.require_POST
@csrf.csrf_exempt
def setFile(request, file):
    try:
        allsongs = copyservice.getsongs(file)
        return BaseServiceResponse("allsongs", allsongs).generate()
    except Exception, e:
        return ErrorServiceResponse(e).generate()

urlset = [
    url(__COPY_SCOPE.format(url=r"getsongs/"), setFile),

]