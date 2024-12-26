from django.shortcuts import redirect

def Auth_Middleware(get_response):


    def middleware(request):
        returnurl = request.META['PATH_INFO']
        if not request.session.get('customer'):
             return redirect(f'login?return_url={returnurl}')
        response = get_response(request)
        return response

    return middleware