from django.contrib import admin
from models import datewisedetailknownerrcounts,datewiseerrcounts
from ErrorsDict.models import ErrorsDict
from LogStatus.models import LogsAnalyzed
from LogConfiguration.models import CustomerProdLogsLoca,Error_Reporting_JIRA

#Display your models in admin page
class ErrorDictAdmin(admin.ModelAdmin):
    list_display = ["id","Error_name","Error_reportDate"]
    list_editable = ["Error_reportDate"]
    class Meta:
        model = ErrorsDict

class DetailErrCntsAdmin(admin.ModelAdmin):
    list_display = ["cust_name","err_name","month_name","date_date","appsrv_name","err_counts"]
    list_display_links = ["err_name"]
    list_filter = ["cust_name","month_name","appsrv_name"]
    search_fields = ["err_name"]


# Register your models here.
admin.site.register(datewiseerrcounts)
admin.site.register(datewisedetailknownerrcounts,DetailErrCntsAdmin)
admin.site.register(ErrorsDict,ErrorDictAdmin)
