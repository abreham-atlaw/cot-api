import typing

from django.db import models


class Contracts:
    profile = "profile"
    asset = "asset"
    asset_maintenance = "asset_maintenance"
    asset_request = "asset_request"
    department = "department"
    invitation = "invitation"

    all = [profile, asset, asset_maintenance, asset_request, department, invitation]


PERMISSION_MAP = {
    -1: [Contracts.profile],
    0: Contracts.all,
    1: [Contracts.profile, Contracts.department],
    2: [Contracts.profile, Contracts.department, Contracts.asset],
    3: Contracts.all,
    4: Contracts.all,
    5: Contracts.all
}


class OrganizationKeys(models.Model):

    organization_id = models.CharField(primary_key=True, max_length=512)

    def __str__(self):
        return self.organization_id

    @property
    def keys(self) -> typing.List['SymmetricKey']:
        return SymmetricKey.objects.filter(organization_key=self)


class SymmetricKey(models.Model):
    organization_key: str = models.ForeignKey(OrganizationKeys, on_delete=models.CASCADE)
    key: str = models.CharField(max_length=512)
    contract = models.CharField(max_length=512)
