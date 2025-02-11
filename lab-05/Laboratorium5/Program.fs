// Laboratorium 5
// Zadanie 1. Rekurencyjne generowanie ciągu Fibonacciego
// Napisz funkcję rekurencyjną, która oblicza n-ty wyraz ciągu Fibonacciego. Następnie zoptymalizuj ją,
// stosując funkcję z ogonową rekurencją.

// Zadanie 2. Wyszukiwanie elementu w drzewie binarnym
// Zaimplementuj funkcję rekurencyjną do wyszukiwania elementu w drzewie binarnym. Napisz też
// iteracyjną wersję tej funkcji z użyciem stosu symulowanego za pomocą listy

module Funkcje =
    //open System
    // Laboratorium 5

    // Funkcja iteracyjna
    let sumaIter n = 
        let mutable suma = 0
        for i in 1..n do
            suma <- suma + i
        suma

    let wynik = sumaIter 5
    printf "Suma iteracyjnie: %d\n" wynik

    // Funkcja rekurencyjna
    let rec sumaRek n =
        if n <= 0 then 0
        else n + sumaRek (n - 1)

    let wynik1 = sumaRek 5
    printf "Suma rekurencyjna: %d\n" wynik1

    // Rekurencja ogonowa
    let rec silniaOgonowa n acc =
        if n <= 1 then acc
        else silniaOgonowa (n - 1) (n + acc)

    let wynik2 = silniaOgonowa 5 1
    printf "5! = %d\n" wynik2

    // Zadanie 1
    let rec fibRek n =
        if n <= 0 then 0
        elif n = 1 then 1
        else fibRek (n - 1) + fibRek (n - 2)

    let rec fibRekTail n a b =
        if n = 0 then a
        elif n = 1 then b
        else fibRekTail (n - 1) b (a + b)

    // Zadanie 2
    type Tree<'T> =
        | Empty
        | Node of 'T * Tree<'T> * Tree<'T>


    let rec findRecursive tree value =
        match tree with
        | Empty -> false
        | Node (v, left, right) ->
            if v = value then true
            else
                findRecursive left value || findRecursive right value


    let findIterative tree value =
        let rec loop stack =
            match stack with
            | [] -> false
            | Empty :: rest -> loop rest
            | Node (v, left, right) :: rest ->
                if v = value then true
                else loop (left :: right :: rest)

        loop [tree]

    let tree =
        Node (5,
            Node (3, Node (1, Empty, Empty), Node (4, Empty, Empty)),
            Node (8, Node (7, Empty, Empty), Node (9, Empty, Empty)))


    let resultRecursive = findRecursive tree 4
    let resultIterative = findIterative tree 4

    printfn "Wersja rekurencyjna: %b" resultRecursive
    printfn "Wersja iteracyjna: %b" resultIterative


    [<EntryPoint>]
    let wynikEntryPoint args =
        printfn "Arguments passed to function : %A" args
        0
            