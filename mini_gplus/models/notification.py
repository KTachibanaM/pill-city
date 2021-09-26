from enum import Enum
from mongoengine import Document, LazyReferenceField, StringField, EnumField, BooleanField, CASCADE
from .created_at_mixin import CreatedAtMixin
from .user import User


class NotifyingAction(Enum):
    Comment = "comment"
    Mention = "mention"
    Reaction = "reaction"
    Reshare = "reshare"


class Notification(Document, CreatedAtMixin):
    eid = StringField(required=True)
    notifying_action = EnumField(NotifyingAction, required=True)  # type: NotifyingAction
    unread = BooleanField(required=False, default=True)

    notifier = LazyReferenceField(User, required=True, reverse_delete_rule=CASCADE)  # type: User
    notifying_href = StringField(required=True)
    notifying_summary = StringField(required=False, default='')  # todo: backfilled by backfill_notification_href_summaries

    owner = LazyReferenceField(User, required=True, reverse_delete_rule=CASCADE)  # type: User
    notified_href = StringField(required=True)
    notified_summary = StringField(required=False, default='')  # todo: backfill_notification_href_summaries
