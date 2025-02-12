open System
open System.Collections.Generic

(*Zadanie 1. Liczba słów i znaków
Napisz program, który pobiera tekst od użytkownika, a następnie oblicza i wyświetla:
• Liczbę słów w podanym tekście.
• Liczbę znaków (bez spacji).*)
let countWordsAndCharacters (text: string) =
    let words = text.Split([|' '; '\t'; '\n'|], StringSplitOptions.RemoveEmptyEntries)
    let charCount = text.Replace(" ", "").Length
    printfn "Liczba słów: %d" words.Length
    printfn "Liczba znaków (bez spacji): %d" charCount

(*Zadanie 2. Sprawdzenie palindromu
Stwórz funkcję, która sprawdza, czy podany ciąg znaków jest palindromem (czytany od przodu i od tyłu
jest taki sam). Program powinien pobierać tekst od użytkownika i wyświetlać odpowiedni komunikat.
*)
let isPalindrome (text: string) =
    let cleanedText = text.ToLower().Replace(" ", "")
    cleanedText = new string(cleanedText.ToCharArray() |> Array.rev)

let checkPalindrome () =
    printf "Wprowadź tekst do sprawdzenia: "
    let input: string = Console.ReadLine()
    if isPalindrome input then
        printfn "Podany tekst jest palindromem."
    else
        printfn "Podany tekst nie jest palindromem."

(*Zadanie 3: Usuwanie duplikatów
Napisz funkcję, która przyjmuje listę ciągów (np. słów) i zwraca nową listę, w której usunięte są
duplikaty. Użytkownik powinien mieć możliwość wprowadzenia słów oddzielonych spacjami, a program
powinien wyświetlić listę unikalnych słów.*)
let removeDuplicates (words: string list) =
    words |> List.distinct

let getUniqueWords () =
    printf "Wprowadź słowa oddzielone spacjami: "
    let input: string = Console.ReadLine()
    let words = input.Split(' ') |> List.ofArray
    let uniqueWords = removeDuplicates words
    printfn "Unikalne słowa: %s" (String.Join(" ", uniqueWords))

(*Zadanie 4: Zmiana formatu tekstu
Stwórz program, który przyjmuje tekst w formacie "imię; nazwisko; wiek" i przekształca go na format
"Nazwisko, Imię (wiek lat)". Użytkownik powinien móc wprowadzić dowolną liczbę takich wpisów, a
program powinien je przetworzyć i wyświetlić w nowym formacie.*)
let formatEntries () =
    let mutable entries: string list = []
    let mutable continueInput = true
    while continueInput do
        printf "Wprowadź dane w formacie \"imię; nazwisko; wiek\" (lub wpisz 'stop' aby zakończyć): "
        let input: string = Console.ReadLine()
        if input.ToLower() = "stop" then
            continueInput <- false
        else
            entries <- input :: entries

    let formattedEntries = 
        entries
        |> List.map (fun entry ->
            let parts = entry.Split(';')
            if parts.Length = 3 then
                let name = parts.[0].Trim()
                let surname = parts.[1].Trim()
                let age = parts.[2].Trim()
                sprintf "%s, %s (%s lat)" surname name age
            else
                "Nieprawidłowy format")
    
    printfn "\nPrzetworzone dane:"
    formattedEntries |> List.iter (fun formatted -> printfn "%s" formatted)

(*Zadanie 5: Znajdowanie najdłuższego słowa*)
let findLongestWord (text: string) =
    let words = text.Split([|' '; '\t'; '\n'|], StringSplitOptions.RemoveEmptyEntries)
    let longestWord = words |> Array.maxBy (fun word -> word.Length)
    longestWord, longestWord.Length

let displayLongestWord () =
    printf "Wprowadź tekst: "
    let input: string = Console.ReadLine()
    let word, length = findLongestWord input
    printfn "Najdłuższe słowo: %s (długość: %d)" word length

// Zadanie 6: Wyszukiwanie i zamiana
let replaceWordInText (text: string) (wordToFind: string) (wordToReplace: string) =
    text.Replace(wordToFind, wordToReplace)

let searchAndReplace () =
    printf "Wprowadź tekst: "
    let input: string = Console.ReadLine()
    printf "Podaj słowo do wyszukania: "
    let wordToFind: string = Console.ReadLine()
    printf "Podaj słowo do zamiany: "
    let wordToReplace: string = Console.ReadLine()
    let modifiedText = replaceWordInText input wordToFind wordToReplace
    printfn "Zmodyfikowany tekst: %s" modifiedText

// Zarządzanie całą aplikacją
let main () =
    let mutable exitProgram = false
    while not exitProgram do
        printfn "\nMenu:"
        printfn "1. Liczba słów i znaków"
        printfn "2. Sprawdzenie palindromu"
        printfn "3. Usuwanie duplikatów"
        printfn "4. Zmiana formatu tekstu"
        printfn "5. Znajdowanie najdłuższego słowa"
        printfn "6. Wyszukiwanie i zamiana"
        printfn "0. Wyjście"
        printf "Wybierz opcję: "
        match Console.ReadLine() with
        | "1" ->
            printf "Wprowadź tekst: "
            let input: string = Console.ReadLine()
            countWordsAndCharacters input
        | "2" -> checkPalindrome ()
        | "3" -> getUniqueWords ()
        | "4" -> formatEntries ()
        | "5" -> displayLongestWord ()
        | "6" -> searchAndReplace ()
        | "0" -> exitProgram <- true
        | _ -> printfn "Nieprawidłowa opcja. Spróbuj ponownie."

main ()
