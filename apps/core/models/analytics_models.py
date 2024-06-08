from django.db import models


class AssetSummary(models.Model):
    total_assets = models.IntegerField()
    allocated_assets = models.IntegerField()
    unallocated_assets = models.IntegerField()


class AssetCategorySummary(models.Model):
    total_categories = models.IntegerField()


class MaintenanceRequestSummary(models.Model):
    total_requests = models.IntegerField()
    pending_requests = models.IntegerField()
    approved_requests = models.IntegerField()
    rejected_requests = models.IntegerField()


class AssetRequestSummary(models.Model):
    total_requests = models.IntegerField()
    pending_requests = models.IntegerField()
    approved_requests = models.IntegerField()
    rejected_requests = models.IntegerField()


class ProfileSummary(models.Model):
    total_profiles = models.IntegerField()


class Summary(models.Model):
    asset_summary = models.OneToOneField(AssetSummary, on_delete=models.CASCADE)
    asset_category_summary = models.OneToOneField(AssetCategorySummary, on_delete=models.CASCADE)
    maintenance_request_summary = models.OneToOneField(MaintenanceRequestSummary, on_delete=models.CASCADE)
    asset_request_summary = models.OneToOneField(AssetRequestSummary, on_delete=models.CASCADE)
    profile_summary = models.OneToOneField(ProfileSummary, on_delete=models.CASCADE)
