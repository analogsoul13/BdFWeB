from django.contrib import admin

from .models import * #import all at once

# Register your models here.

admin.site.register(Donor)
admin.site.register(BloodDonation)
admin.site.register(ReqBlood)
admin.site.register(DonorAppointment)
admin.site.register(ReqCampaign)
