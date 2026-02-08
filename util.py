from typing import Iterable, Optional, Set

class CommandPermissionHelper:
    def __init__(
        self,
        owner_ids: Optional[Iterable[int]] = None,
        allowed_user_ids: Optional[Iterable[int]] = None,
        allowed_role_ids: Optional[Iterable[int]] = None,
    ):
        self.owner_ids: Set[int] = set(owner_ids or [])
        self.allowed_user_ids: Set[int] = set(allowed_user_ids or [])
        self.allowed_role_ids: Set[int] = set(allowed_role_ids or [])

    def can_run(self, user_id: int, role_ids: Iterable[int]) -> bool:
        if user_id in self.owner_ids:
            return True

        if user_id in self.allowed_user_ids:
            return True

        if self.allowed_role_ids.intersection(role_ids):
            return True

        return False
