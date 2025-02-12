module Abstract

// Zadanie 1
open System
// Book
type Book(title: string, author: string, pages: int) =
    member this.Title = title
    member this.Author = author
    member this.Pages = pages

    // Metoda
    member this.GetInfo() =
        sprintf "Tytuł: %s, Autor: %s, Liczba stron: %d" this.Title this.Author this.Pages
        // printfn - wypisywanie na konsole
        // sprintf - wypisanie ciągu znaków


// User
type User(name: string) =

    // Lista książek
    let borrowBooks = System.Collections.Generic.List<Book>()
    member this.Name = name

    member this.BorrowedBook(book: Book) =
        // BorrowBook
        borrowBooks.Add(book)
        printfn "%s wypożyczył książke: \"%s\"" this.Name book.Title // Jan Nowak wypożyczył książke: "Tytuł"

    member this.ReturnBook(book: Book) =
        if borrowBooks.Contains(book) then
            borrowBooks.Remove(book)
            printfn "%s zwrócił książke: \"%s\"" this.Name book.Title
        else
            printfn "%s nie ma książki do zwrócenia \"%s\"" this.Name book.Title

    // metoda do wyświetlenie listy książek wypożyczonych
    member this.ListBorrowBooks() =
        if borrowBooks.Count > 0 then
            borrowBooks
            |> Seq.map (fun book -> book.GetInfo())
            |> String.concat "\n"
            |> printfn "Książki wypożyczone przez %s:\n%s" this.Name
        else
            printfn "%s nie ma wypożyczonych książek" this.Name

type Library() =
    let mutable books = System.Collections.Generic.List<Book>()

    member this.AddBook(book: Book) =
        books.Add(book)
        printfn "Książka \"%s\" została dodana" book.Title
    
    member this.RemoveBook(book: Book) =
        if books.Contains(book) then
            books.Remove(book)
            printfn "Książka \"%s\" została usunięta" book.Title
        else
            printfn "Nie znaleziono książki"

     member this.ListBooks() =
        if books.Count > 0 then
            books
            |> Seq.map (fun book -> book.GetInfo())
            |> String.concat "\n"
            |> printfn "Książki w bibliotece: \n%s"
        else
            printfn "W bibliotece nie ma książek"

let main() =
    // Obiekty klas
    let library = Library()
    let user = User("Jan")

    // Książki
    let book1 = Book("Książka 1", "Autor 1", 123)
    let book2 = Book("Książka 2", "Autor 2", 1234)
    let book3 = Book("Książka 3", "Autor 3", 12335)
    let book4 = Book("Książka 4", "Autor 4", 12367)

    // Dodanie do biblioteki
    library.AddBook(book1)
    library.AddBook(book2)
    library.AddBook(book3)
    library.AddBook(book4)

    // Wyświetlenie ksiażek w bibliotece
    library.ListBooks()

    user.ListBorrowBooks()

    // Zwrot książki
    user.ReturnBook(book1)
    user.ListBorrowBooks()

main()