from django.urls import path
from Baloncesto import views


urlpatterns = [

# Jugadores
	path('detallar/<int:jugador_id>', views.detallar, name="detallar_jugador"),
    path('agregar', views.agregar, name="agregar_jugador"),
    path('listar', views.listar, name="listar_jugador"),
    path('editar/<int:jugador_id>', views.editar, name="editar_jugador"),
    path('eliminar/<int:jugador_id>', views.eliminar, name="eliminar_jugador"),

    # Entrenador
    path('agregarentrenador', views.agregarentrenador, name="agregar_entrenador"),
    path('listarentrenador', views.listarentrenador, name="listar_entrenador"),
    path('detallarentrenador/<int:entrenador_id>', views.detallarentrenador, name="detallar_entrenador"),
    path('editarentrenador/<int:entrenador_id>', views.editarentrenador, name="editar_entrenador"),
    path('eliminarentrenador/<int:entrenador_id>', views.eliminarentrenador, name="eliminar_entrenador"),

    #Equipo
    path('agregarequipo', views.agregarequipo, name="agregar_equipo"),
    path('listarequipo', views.listarequipo, name="listar_equipo"),
    path('detallarequipo/<int:equipo_id>', views.detallarequipo, name="detallar_equipo"),
    path('editarequipo/<int:equipo_id>', views.editarequipo, name="editar_equipo"),
    path('eliminarequipo/<int:equipo_id>', views.eliminarequipo, name="eliminar_equipo"),

    #Nomina
    path('listarnomina', views.listarnomina, name="listar_nomina"),
    path('agregarnomina', views.agregarnomina, name="agregar_nomina"),

	
]