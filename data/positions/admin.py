from django.contrib import admin
# from .models import PositionsType
from .models import Positions
#
#
@admin.register(Positions)
class PositionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'cate_name', 'job_name', 'salary_range', 'working_city', 'experience_required', 'education_required', 'job_type', 'position_label', 'publish_time', 'working_address', 'company_name', 'company_field', 'financing_status', 'company_size')

#
# #
# # @admin.register(PositionsType)
# # class PositionsTypeAdmin(admin.ModelAdmin):
# #     list_display = ('id', 'type_name')