from django.shortcuts import render,redirect
from .models import Area,PublicoAlvo,Curso
from .forms import AreaForm,PublicoAlvoForm,CursoForm


# Create your views here.

def inicio(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

# def perfil(request):
#     return render(request,'perfil.html')

def cadastro(request):
    return render(request,'cadastro.html')

def curso_detalhe(request):
    return render(request,'curso_detalhe.html')

def curso_galeria(request):
    return render(request,'curso_galeria.html')

def contato(request):
    return render(request,'contato.html')

def areas(request):
    areas=Area.objects.all()
    context = {
        'areas': areas
    }

    #return render(request,'areas.html',context)
    return render(request,'privado/areas.html',context)


def publico_alvo(request):
    areas=PublicoAlvo.objects.all()
    context = {
        'areas': areas
    }

    #return render(request,'areas.html',context)
    return render(request,'privado/publico_alvo.html',context)


def area_cadastrar(request):
    form = AreaForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('area_listar')    
    context = {
        'form': form
    }
    # return render(request,'area_cadastrar.html',context)
    return render(request,'privado/area_cadastrar.html',context)

def area_editar(request,id):
    area = Area.objects.get(pk=id)
    form = AreaForm(request.POST or None,instance=area)
    
    if form.is_valid():
        form.save()
        return redirect('area_listar')    
    context = {
        'form': form
    }
    return render(request,'privado/publico_cadastrar.html',context)

def area_remover(request,id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('area_listar')



def publico_alvo_cadastrar(request):
    form = PublicoAlvoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('publicoalvo')    
    context = {
        'form': form
    }
    # return render(request,'area_cadastrar.html',context)
    return render(request,'privado/publico_cadastrar.html',context)



def publico_alvo_editar(request,id):
    area = PublicoAlvo.objects.get(pk=id)
    form = PublicoAlvoForm(request.POST or None,instance=area)
    
    if form.is_valid():
        form.save()
        return redirect('publicoalvo')    
    context = {
        'form': form
    }
    return render(request,'privado/publico_cadastrar.html',context)

def publico_alvo_remover(request,id):
    area = PublicoAlvo.objects.get(pk=id)
    area.delete()
    return redirect('publicoalvo')

def curso_listar(request):
    cursos = Curso.objects.all()
    context = {
        'cursos' : cursos
    }
    return render(request,'privado/Cursos.html',context)


def curso_cadastrar(request):
    form = CursoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('cursos')    
    context = {
        'form': form
    }
    return render(request,'privado/curso_cadastrar.html',context)