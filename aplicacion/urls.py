from django.urls import path, include
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from .models import Cliente, Ascensor, OrdenTrabajo
from rest_framework import routers, serializers, viewsets


from . import views



class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('url', 'Nombre', 'Apellido', 'Direccion', 'Ciudad', 'Comuna', 'Telefono', 'Correo')

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AscensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ascensor
        fields = ('url', 'id_ascensor', 'Modelo')

class AscensorViewSet(viewsets.ModelViewSet):
    queryset = Ascensor.objects.all()
    serializer_class = AscensorSerializer

class OrdenTrabajoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrdenTrabajo
        fields = ('url', 'Cliente', 'Ascensor')

class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'tecnicos', UserViewSet)
router.register(r'ascensores', AscensorViewSet)
router.register(r'ordenes de trabajo', OrdenTrabajoViewSet)

urlpatterns = [
    path('inicio/', views.cargarInicio, name='cargarInicio'),
    path('inicio/login', views.cargarLogin, name='cargarLogin'),
    path('inicio/orden', views.cargarOrden, name='cargarOrden'),
    path('inicio/listado', views.cargarListado, name='cargarListado'),
    path('salir', views.logout, name='logout'),
    path('', include('social_django.urls', namespace='social')),
    path('api-ascensores/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  
    path('cambiar-contraseña/', auth_views.PasswordChangeView.as_view()),

]