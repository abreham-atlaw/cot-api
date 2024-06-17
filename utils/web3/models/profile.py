from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Department:
    id: Optional[str] = None
    name: str = ""
    # Add other fields as needed


@dataclass
class Profile:
    id: Optional[str] = None
    name: str = ""
    role: int = 0
    user_key: str = ""
    email: str = ""
    organization_id: Optional[str] = None

    def has_organization(self) -> bool:
        return self.organization_id is not None
