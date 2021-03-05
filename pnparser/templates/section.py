from typing import TYPE_CHECKING
from ..templates.common import *
from ..dragon import Dragon

if TYPE_CHECKING:
    from .border import Border


class Section:
    """=={title}=="""
    def __init__(self, id: int, title: str) -> None:
        self.id: int = id
        self.title: str = title
        self.borders: 'list[Border]' = []

    def print_toc(self) -> str:
        result: str = f"|group{self.id}={self.title}"
        
        if not self.title == "Champions" or "Items" or "Runes":
            return result + NEW_LINE
        else:
            icons: str = ""
            result = result[:-1] + NEW_LINE
            result += f"|group{self.id}images="
            
            for border in self.borders:
                for change in border.changes:
                    if self.title == "Champions":
                        if any(x["name"] == change.name for x in Dragon.champions):
                            icons += f"{change.name}, "
                    elif self.title == "Items":
                        if any(x["name"] == change.name for x in Dragon.items):
                            icons += f"{change.name}, "
                        else:
                            for inner_change in change.changes:
                                if any(x["name"] == inner_change.name for x in Dragon.items):
                                    icons += f"{inner_change.name}, "
                    elif self.title == "Runes":
                        if any(x["name"] == change.name for x in Dragon.runes):
                            icons += f"{change.name}, "
            if icons and not icons.isspace():
                result += icons[:-2] + NEW_LINE
            return result
    
    def print(self) -> str:
        return TITLE.format(self.title)