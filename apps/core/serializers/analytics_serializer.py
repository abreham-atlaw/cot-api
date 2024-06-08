from rest_framework import serializers
from apps.core.models import AssetSummary, AssetCategorySummary, MaintenanceRequestSummary, AssetRequestSummary, \
    ProfileSummary, Summary


class AssetSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetSummary
        fields = ['total_assets', 'allocated_assets', 'unallocated_assets']


class AssetCategorySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCategorySummary
        fields = ['total_categories']


class MaintenanceRequestSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRequestSummary
        fields = ['total_requests', 'pending_requests', 'approved_requests', 'rejected_requests']


class AssetRequestSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetRequestSummary
        fields = ['total_requests', 'pending_requests', 'approved_requests', 'rejected_requests']

class ProfileSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileSummary
        fields = ['total_profiles']

class SummarySerializer(serializers.ModelSerializer):
    asset_summary = AssetSummarySerializer()
    asset_category_summary = AssetCategorySummarySerializer()
    maintenance_request_summary = MaintenanceRequestSummarySerializer()
    asset_request_summary = AssetRequestSummarySerializer()
    profile_summary = ProfileSummarySerializer()

    class Meta:
        model = Summary
        fields = ['asset_summary', 'asset_category_summary', 'maintenance_request_summary', 'asset_request_summary', 'profile_summary']
