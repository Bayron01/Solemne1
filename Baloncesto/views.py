from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
#Nomina
from Baloncesto.models import Nomina
from Baloncesto.forms import NominaForm
#Jugador
from Baloncesto.models import Jugador
from Baloncesto.forms import JugadorForm
#Entrenador
from Baloncesto.models import Entrenador
from Baloncesto.forms import EntrenadorForm
#Equipo
from Baloncesto.models import Equipo
from Baloncesto.forms import EquipoForm



#Jugador

@login_required(login_url='/auth/login')
def detallar(request, jugador_id):
    data = {}
    data['jugador'] = Jugador.objects.get(pk=jugador_id)
    template_name = 'jugador/detallar_jugador.html'
    return render(request, template_name, data)



@login_required(login_url='/auth/login')
def listar(request):
    data = {}

    object_list = Jugador.objects.all().order_by('id')
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    
    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'jugador/listar_jugador.html'
    return render(request, template_name, data)


@login_required(login_url='/auth/login')
def agregar(request):
    data = {}
    if request.method == "POST":
        data['form'] = JugadorForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('listar_jugador')

    else:
        data['form'] = JugadorForm()
   

    template_name = 'jugador/agregar_jugador.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def editar(request, jugador_id):
    data = {}
    jugador = Jugador.objects.get(pk=jugador_id)
    if request.method == "GET":
        data['form'] = JugadorForm(instance= jugador)

    else:
        data['form'] = JugadorForm(request.POST, request.FILES, instance= jugador)  
        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()
            return redirect('listar_jugador') 

    template_name = 'jugador/editar_jugador.html'
    return render(request, template_name, data)



@login_required(login_url='/auth/login')
def eliminar(request, jugador_id):
    data = {}
    jugador = Jugador.objects.get(pk=jugador_id)
    if request.method == "POST":
        jugador.delete()
        return redirect('listar_jugador')


    template_name = 'jugador/eliminar_jugador.html'
    return render(request, template_name, data)


# Entrenador

@login_required(login_url='/auth/login')
def agregarentrenador(request):
    data = {}
    if request.method == "POST":
        data['form'] = EntrenadorForm(request.POST)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('listar_entrenador')

    else:
        data['form'] = EntrenadorForm()
   

    template_name = 'entrenador/agregar_entrenador.html'
    return render(request, template_name, data)


@login_required(login_url='/auth/login')
def listarentrenador(request):
    data = {}

    object_list = Entrenador.objects.all().order_by('id')
    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'entrenador/listar_entrenador.html'
    return render(request, template_name, data)


@login_required(login_url='/auth/login')
def detallarentrenador(request, entrenador_id):
    data = {}
    data['entrenador'] = Entrenador.objects.get(pk=entrenador_id)
    template_name = 'entrenador/detallar_entrenador.html'
    return render(request, template_name, data)



@login_required(login_url='/auth/login')
def editarentrenador(request, entrenador_id):
    data = {}
    entrenador = Entrenador.objects.get(pk=entrenador_id)
    if request.method == "GET":
        data['form'] = EntrenadorForm(instance= entrenador)

    else:
        data['form'] = EntrenadorForm(request.POST, instance= entrenador)  
        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()
            return redirect('listar_entrenador') 

    template_name = 'entrenador/editar_entrenador.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def eliminarentrenador(request, entrenador_id):
    data = {}
    entrenador = Entrenador.objects.get(pk=entrenador_id)
    if request.method == "POST":
        entrenador.delete()
        return redirect('listar_entrenador')


    template_name = 'entrenador/eliminar_entrenador.html'
    return render(request, template_name, data)



#Equipo


@login_required(login_url='/auth/login')
def agregarequipo(request):
    data = {}
    if request.method == "POST":
        data['form'] = EquipoForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('listar_equipo')

    else:
        data['form'] = EquipoForm()
   

    template_name = 'equipo/agregar_equipo.html'
    return render(request, template_name, data)


@login_required(login_url='/auth/login')
def listarequipo(request):
    data = {}

    object_list = Equipo.objects.all().order_by('id')
    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'equipo/listar_equipo.html'
    return render(request, template_name, data)


@login_required(login_url='/auth/login')
def detallarequipo(request, equipo_id):
    data = {}
    data['equipo'] = Equipo.objects.get(pk=equipo_id)
    template_name = 'equipo/detallar_equipo.html'
    return render(request, template_name, data)


@login_required(login_url='/auth/login')
def editarequipo(request, equipo_id):
    data = {}
    equipo = Equipo.objects.get(pk=equipo_id)
    if request.method == "GET":
        data['form'] = EquipoForm(instance= equipo)

    else:
        data['form'] = EquipoForm(request.POST, request.FILES, instance= equipo)  
        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()
            return redirect('listar_equipo') 

    template_name = 'equipo/editar_equipo.html'
    return render(request, template_name, data)


@login_required(login_url='/auth/login')
def eliminarequipo(request, equipo_id):
    data = {}
    equipo = Equipo.objects.get(pk=equipo_id)
    if request.method == "POST":
        equipo.delete()
        return redirect('listar_equipo')


    template_name = 'equipo/eliminar_equipo.html'
    return render(request, template_name, data)


#Nomina


@login_required(login_url='/auth/login')
def listarnomina(request):
    data = {}

    object_list = Nomina.objects.all().order_by('id')
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'nomina/listar_nomina.html'
    return render(request, template_name, data)


@login_required(login_url='/auth/login')
def agregarnomina(request):
    data = {}
    if request.method == "POST":
        data['form'] = NominaForm(request.POST)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('listar_nomina')

    else:
        data['form'] = NominaForm()
   

    template_name = 'nomina/agregar_nomina.html'
    return render(request, template_name, data)