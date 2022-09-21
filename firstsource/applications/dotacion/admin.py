from re import search
from django.contrib import admin
from .models import Dotacion, User, Talla, Entrega, Cliente, Factura, Producto_factura, Producto_factura, Devolucion, Tipo
from import_export import resources
from django.apps import apps
from import_export.admin import ImportExportModelAdmin
from django.db import models
import tablib
import collections

class DotacionResource(resources.ModelResource):
    def __init__(self):
        super(DotacionResource, self).__init__()
        # Obtenga todos los campos en el modelo Libro en la aplicación de tablas, cambie las tablas de acuerdo con su aplicación
        field_list = apps.get_model('dotacion', 'Dotacion')._meta.fields
        self.vname_dict = {}
        self.fkey = []
        for i in field_list:
            self.vname_dict[i.name] = i.verbose_name    # Obtenga el verbose_name de todos los campos y guárdelos en el diccionario
            if(isinstance(i, models.ForeignKey)):
                self.fkey.append(i.name)    # Obtenga los nombres de todos los campos ForeignKey almacenados en la lista

    def export(self, queryset=None, *args, **kwargs):
        self.before_export(queryset, *args, **kwargs)

        if queryset is None:
            queryset = self.get_queryset()

        headers = self.get_export_headers()
        data = tablib.Dataset(headers=headers)

        # Obtener la posición de todos los nombres de claves externas en los encabezados
        fk_index = {}
        for fk in self.fkey:
            fk_index[fk] = headers.index(fk)

        iterable = queryset
        for obj in iterable:
            # Obtenga los datos de origen para exportar, donde export_resource devuelve una lista para una fácil modificación. Reemplazado por el valor de la clave externa
            res = self.export_resource(obj)
            """
                         Aquí está la clave, obtenga el objeto correspondiente del valor del propietario al Usuario e intercepte el nombre de usuario legible,
                         Aquí está get, por lo que el nombre de usuario debe ser único en el modelo de usuario
            """
            res[fk_index['Producto']] = User.objects.get(id=res[fk_index['Producto']]).username
            data.append(res)
        self.after_export(queryset, data, *args, **kwargs)
        return data

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        dict = []
        for row in dataset.dict:
            tmp = collections.OrderedDict()
            Dotacion = Dotacion.objects.all()
            for item in row:
                if item == 'Producto':
                    """
                                         Aquí está la clave, encuentre la identificación correspondiente en la tabla Usuario a través del nombre legible y agréguela a los datos importados
                    """
                    tmp[item] = User.objects.get(username=row[item]).id
                else:
                    tmp[item] = row[item]
            """
                         La clave aquí es comparar los datos. Si los datos son los mismos, agregue la identificación original en la tabla del Libro a los datos que se importarán.
                         Esto no agregará los mismos datos que el original, similar al método create_or_update
            """
            for Dotacion in Dotacion:
                if row['name'] == Dotacion.name:
                    tmp['id'] = Dotacion.id
            dict.append(tmp)
        dataset.dict = dict
        return dataset

    class Meta:
        model = Dotacion

class DotacionAdmin(ImportExportModelAdmin):
    resource_class = DotacionResource

class DotacionAdmin(ImportExportModelAdmin):
    resource_class = DotacionResource
    list_display = ['Producto', 'Talla', 'Sucursal', 'cantidad', 'stock_usado', 'total_dotacion', 'valor_promedio']
    list_filter = ('Producto', 'Talla', 'Sucursal', 'cantidad', 'Producto__categoria')
    search_fields = ['cantidad']
    exclude = ('valor_promedio',)
    raw_id_fields = ('Producto',)

class UserResource(resources.ModelResource):
    class Meta:
        model = User

from django.db.models import Sum
from django.db.models import Count
from django.db.models import F

class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    list_display = ['username', 'stock_nuevo', 'stock_usado', 'stock_total', 'promedio_total']
    search_fields = ['username']
    list_filter = ('categoria',)

    def stock_usado(self, obj):
        return obj.post_count
    
    def stock_nuevo(self, obj):
        return obj.post_counts

    def stock_total(self, obj):
        return obj.post_total
    
    def promedio_total(self, obj):
        return obj.post_promedio

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(post_counts=Sum("dotacion__cantidad"))
        queryset = queryset.annotate(post_count=Sum("dotacion__stock_usado"))
        queryset = queryset.annotate(post_total=Sum("dotacion__total_dotacion"))

        queryset = queryset.annotate(post_promedio=Sum("dotacion__valor_promedio"))
        return queryset


    # @admin.display(empty_value='???')
    # def view_birth_date(self, obj):
    #     # lista = 
    #     return obj.dotacion_ropa.count()
    
class EntregaAdmin(ImportExportModelAdmin):
    list_display = ('id', 't_dotacion', 'sucursal')

class FacturaInline(admin.TabularInline):
    model = Producto_factura
    extra = 2

class productoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'numero_factura', 'fecha', 'total_factura')
    search_fields = ('numero_factura', 'cliente__nombre')
    date_hierarchy = ('fecha')
    inlines = [
        FacturaInline,
    ]

class DevolucionAdmin(admin.ModelAdmin):
    list_display = ('dotacion', 'cantidad', 'fecha')
    date_hierarchy = ('fecha')

admin.site.register(Dotacion, DotacionAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Talla)
admin.site.register(Entrega, EntregaAdmin)
admin.site.register(Cliente)
admin.site.register(Factura, productoAdmin)
admin.site.register(Producto_factura)
admin.site.register(Devolucion, DevolucionAdmin)
admin.site.register(Tipo)
