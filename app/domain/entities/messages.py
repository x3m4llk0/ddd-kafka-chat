from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from domain.entities.base import BaseEntity
from domain.values.messages import Text, Title


@dataclass(eq=False)
class Message(BaseEntity):
    text: Text

    def __hash__(self) -> int:
        return hash(self.oid)


@dataclass(eq=False)
class Chat(BaseEntity):
    title: Title
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True,
    )

    def add_message(self, message: Message):
        self.messages.add(message)
