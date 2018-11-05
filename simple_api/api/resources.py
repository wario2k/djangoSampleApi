from tastypie.resources import ModelResource
from api.models import President
class PresidentResource(ModelResource):
    class Meta:
        queryset = President.objects.all()
        resource_name = 'president'