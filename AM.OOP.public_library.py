"""
AM OOP Design
Playing Card
https://algo.monster/problems/oop_public_library
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Set


class Book(ABC):
    """Abstract class representing a Book"""

    def __init__(self, book_id: str, title: str) -> None:
        super().__init__()
        self.__id: str = book_id
        self.__title: str = title
        self.__borrower_name: str = ""

    @property
    def title(self) -> str:
        """Property to access the title"""
        return self.__title

    @property
    def book_id(self) -> str:
        """Property to access the book id"""
        return self.__id

    @property
    def borrower_name(self) -> str:
        """Property to return the borrower name"""
        return self.__borrower_name

    @property
    def is_borrowed(self) -> bool:
        """Property to if the book is borrowed"""
        return bool(self.__borrower_name)

    def __str__(self) -> str:
        msg = f'"{self.__title}" {self._str_specific()}\nID: {self.__id}'
        if self.is_borrowed:
            msg += f"\nBorrowed by: {self.__borrower_name}"
        return msg

    @abstractmethod
    def _str_specific(self) -> str:
        """Return the str specific part of the Book"""
        raise NotImplementedError

    def borrow(self, borrower_name: str) -> None:
        """Method to borrow the book"""
        self.__borrower_name = borrower_name

    def release(self) -> None:
        """Method to release/return the book"""
        self.__borrower_name = ""


class TraditionalBook(Book):
    """Class representing a Traditional Book"""

    def __init__(self, book_id: str, title: str, author: str) -> None:
        super().__init__(book_id, title)
        self.__author: str = author

    @property
    def author(self) -> str:
        """Property to access the author"""
        return self.__author

    def _str_specific(self) -> str:
        """Return the str specific part of the TraditionalBook"""
        return f"by {self.__author}"


class Magazine(Book):
    """Class representing a Magazine"""

    def __init__(self, magazine_id: str, title: str, issue_nb: int) -> None:
        super().__init__(magazine_id, title)
        self.__issue_nb: str = issue_nb

    def _str_specific(self) -> str:
        """Return the str specific part of the TraditionalBook"""
        return f"Issue {self.__issue_nb}"


class Library:
    """Class representing a Library"""

    def __init__(self) -> None:
        self.__books_shelf: Dict[str, Book] = {}
        self.__titles_index: Dict[str, Set[str]] = {}
        self.__authors_index: Dict[str, Set[str]] = {}
        self.__borrowers: Dict[str, str] = {}

    def register_book(self, book: Book) -> bool:
        """Method to register a book in the library"""
        # Skip if book already in shelf
        if book.book_id in self.__books_shelf:
            return False

        # Add book in shelf
        self.__books_shelf[book.book_id] = book

        # Add book in title index
        if book.title not in self.__titles_index:
            self.__titles_index[book.title] = set()
        self.__titles_index[book.title].add(book.book_id)

        # Add book in author index if TraditionalBook
        if isinstance(book, TraditionalBook):
            if book.author not in self.__authors_index:
                self.__authors_index[book.author] = set()
            self.__authors_index[book.author].add(book.book_id)

        return True

    def lookup_id(self, book_id: str) -> str:
        """Lookup a book id and return its representation."""
        if book_id not in self.__books_shelf:
            return "No such book exists"
        return str(self.__books_shelf[book_id])

    def lookup_title(self, book_title: str) -> str:
        """Lookup books by their title."""
        if book_title not in self.__titles_index:
            return "No such book exists"

        if len(self.__titles_index[book_title]) == 1:
            return self.lookup_id(next(iter(self.__titles_index[book_title])))

        msg = f"{len(self.__titles_index[book_title])} books match the title: {book_title}"
        nb_available_books = len(self.__titles_index[book_title])
        for book_id in self.__titles_index[book_title]:
            if self.__books_shelf[book_id].is_borrowed:
                nb_available_books -= 1
        msg += f"\n{nb_available_books} book(s) available"
        return msg

    def lookup_author(self, book_author: str) -> str:
        """Lookup books by their author."""
        if book_author not in self.__authors_index:
            return "No such book exists"

        if len(self.__authors_index[book_author]) == 1:
            return self.lookup_id(
                next(iter(self.__authors_index[book_author]))
            )

        msg = f"{len(self.__authors_index[book_author])} books match the author: {book_author}"
        nb_available_books = len(self.__authors_index[book_author])
        for book_id in self.__authors_index[book_author]:
            if self.__books_shelf[book_id].is_borrowed:
                nb_available_books -= 1
        msg += f"\n{nb_available_books} book(s) available"

        return msg

    def borrow_book(self, book_id: str, borrower_name: str) -> bool:
        """Method to borrow a book"""
        if (
            book_id not in self.__books_shelf
            or borrower_name in self.__borrowers
            or self.__books_shelf[book_id].is_borrowed
        ):
            return False

        self.__books_shelf[book_id].borrow(borrower_name)
        self.__borrowers[borrower_name] = book_id
        return True

    def return_book(self, borrower_name: str) -> bool:
        """Method to borrow a book"""
        if borrower_name not in self.__borrowers:
            return False

        book_id: str = self.__borrowers[borrower_name]
        if book_id in self.__books_shelf:
            self.__books_shelf[book_id].release()

        self.__borrowers.pop(borrower_name, None)


def parse_register_command(instruction: str) -> Book:
    """Function to parse the instruction from a register command

    Returns
        The Book instantiated from the info found in the instruction
    """
    inst_params: List[str] = instruction.split()
    book_type: str = inst_params[1]
    book_id: str = inst_params[2]
    title: str = instruction.split('"')[1]
    if book_type == "book":
        author: str = instruction.split("by ")[-1]
        book: Book = TraditionalBook(
            book_id=book_id, title=title, author=author
        )
    elif book_type == "magazine":
        issue_nb: int = int(instruction[-1])
        book: Book = Magazine(
            magazine_id=book_id, title=title, issue_nb=issue_nb
        )
    else:
        raise ValueError(f"{book_type} is not a supported book type")
    return book


def simulate_library(instructions: List[str]) -> List[str]:
    """Application entry point function"""
    output: List[str] = []
    library = Library()
    for instruction in instructions:
        inst_params: List[str] = instruction.split()
        command: str = inst_params[0]
        if command == "register":
            book: Book = parse_register_command(instruction)
            library.register_book(book)
        elif command == "lookup":
            sub_command: str = inst_params[1]
            if sub_command == "id":
                book_id: str = inst_params[2]
                output.append(library.lookup_id(book_id))
            elif sub_command == "title":
                book_title: str = " ".join(inst_params[2:])
                output.append(library.lookup_title(book_title))
            elif sub_command == "author":
                book_author: str = " ".join(inst_params[2:])
                output.append(library.lookup_author(book_author))
        elif command == "borrow":
            book_id: str = inst_params[2]
            borrower_name: str = " ".join(inst_params[2:])
            library.borrow_book(book_id=book_id, borrower_name=borrower_name)
        elif command == "return":
            borrower_name: str = " ".join(inst_params[1:])
            library.return_book(borrower_name)
        else:
            raise ValueError(f"f{command} is not a valid command")
    return output


if __name__ == "__main__":
    instructions = [input() for _ in range(int(input()))]
    res = simulate_library(instructions)
    for line in res:
        print(line)
