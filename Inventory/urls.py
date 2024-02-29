from .views import *
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('supplier_info',Supplierview,basename='supplier_view')
router.register('Inventory_info',InvetoryItemview,basename='Inventory_items')

urlpatterns = [
    
]+router.urls
