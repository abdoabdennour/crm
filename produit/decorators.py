from django.shortcuts import redirect




def loginrequis(view_fonction):
    def wraper_foction(request, *args,**kwargs):
        if request.user.is_authenticated:
            return redirect('produit:produit')
        else:
            return view_fonction(request, *args,**kwargs)    
    return wraper_foction        