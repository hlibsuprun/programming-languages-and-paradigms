open System
open System.Collections.Generic

// Zadanie 2
// BankAccount
type BankAccount(accountNumber: string, initialBalance: decimal) =
    let mutable balance = initialBalance

    member this.AccountNumber = accountNumber
    member this.Balance = balance

    member this.Deposit(amount: decimal) =
        if amount > 0m then
            balance <- balance + amount
            printfn "Wpłacono %.2f na konto %s" amount this.AccountNumber
        else
            printfn "Kwota wpłaty musi być większa niż 0"

    member this.Withdraw(amount: decimal) =
        if amount > 0m && amount <= balance then
            balance <- balance - amount
            printfn "Wypłacono %.2f z konta %s" amount this.AccountNumber
        elif amount > balance then
            printfn "Nie wystarczające środki na koncie %s" this.AccountNumber
        else
            printfn "Kwota wypłaty musi być większa niż 0"

    member this.GetInfo() =
        sprintf "Konto: %s, Saldo: %.2f" this.AccountNumber this.Balance

// Bank
type Bank() =
    let accounts = Dictionary<string, BankAccount>()
    // Stworzyć konto
    member this.CreateAccount(accountNumber: string, initialBalance: decimal) =
        if not (accounts.ContainsKey(accountNumber)) then
            let account = BankAccount(accountNumber, initialBalance)
            accounts.Add(accountNumber, account)
            printfn "Utworzono konto %s z początkowym saldem %.2f" accountNumber initialBalance
        else
            printfn "Konto o numerze %s już istnieje" accountNumber
            
            member this.GetAccount(accountNumber: string) =
        if accounts.ContainsKey(accountNumber) then
            Some(accounts.[accountNumber])
        else
            printfn "Konto o numerze %s nie znaleziono" accountNumber
            None

    member this.UpdateAccount(accountNumber: string, amount: decimal, isDeposit: bool) =
        match this.GetAccount(accountNumber) with
        | Some(account) ->
            if isDeposit then
                account.Deposit(amount)
            else
                account.Withdraw(amount)
        | None -> ()

    member this.DeleteAccount(accountNumber: string) =
        if accounts.Remove(accountNumber) then
            printfn "Konto %s zostało usunięte" accountNumber
        else
            printfn "Konto o numerze %s nie znaleziono" accountNumber
            // metoda do wyświetlenie listy utworzonych kontów
    member this.ListAccounts() =
        if accounts.Count > 0 then
            accounts.Values
            |> Seq.map (fun account -> account.GetInfo())
            |> String.concat "\n"
            |> printfn "Lista kont:\n%s"
        else
            printfn "Brak dostępnych kont"

// Program główny
let main() =
    let bank = Bank()
    let mutable exitProgram = false
    // zarządzanie aplikacją
    while not exitProgram do
        printfn "\nMenu:"
        printfn "1. Utwórz konto"
        printfn "2. Wyświetl konto"
        printfn "3. Wpłać środki"
        printfn "4. Wypłać środki"
        printfn "5. Usuń konto"
        printfn "6. Pokaż wszystkie konta"
        printfn "0. Wyjdź"

        printf "Wybierz opcję: "
        match Console.ReadLine() with
        | "1" ->
            printf "Podaj numer konta: "
            let accountNumber = Console.ReadLine()
            printf "Podaj początkowe saldo: "
            match Decimal.TryParse(Console.ReadLine()) with
            | (true, initialBalance) ->
                bank.CreateAccount(accountNumber, initialBalance)
            | _ ->
                printfn "Nieprawidłowa kwota"
        | "2" ->
            printf "Podaj numer konta: "
            let accountNumber = Console.ReadLine()
            match bank.GetAccount(accountNumber) with
            | Some(account) -> printfn "%s" (account.GetInfo())
            | None -> ()
        | "3" ->
            printf "Podaj numer konta: "
            let accountNumber = Console.ReadLine()
            printf "Podaj kwotę wpłaty: "
            match Decimal.TryParse(Console.ReadLine()) with
            | (true, amount) -> bank.UpdateAccount(accountNumber, amount, true)
            | _ -> printfn "Nieprawidłowa kwota"
        | "4" ->
            printf "Podaj numer konta: "
            let accountNumber = Console.ReadLine()
            printf "Podaj kwotę wypłaty: "
            match Decimal.TryParse(Console.ReadLine()) with
            | (true, amount) -> bank.UpdateAccount(accountNumber, amount, false)
            | _ -> printfn "Nieprawidłowa kwota"
        | "5" ->
            printf "Podaj numer konta: "
            let accountNumber = Console.ReadLine()
            bank.DeleteAccount(accountNumber)
        | "6" -> bank.ListAccounts()
        | "0" -> exitProgram <- true
        | _ -> printfn "Nieprawidłowa opcja. Spróbuj ponownie."

main()
