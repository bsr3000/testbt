package ex1;

public class Account {
    private double balance;
    private static double interestRate;

    public Account() {
        this.balance = 0.0;
    }

    public String getBalance() {
        return String.valueOf(this.balance);
    }

    public void deposit(double howMuch) {
        if (howMuch > 0) {
            this.balance += howMuch;
        } else {
            System.out.println("Cant deposit amount which is less than 0. variant");
        }
    }

    public void withdraw(double howMuch) {
        if (howMuch > 0 || this.balance > howMuch) {
            this.balance -= howMuch;
        } else {
            System.out.println("Withdrawal amount is bigger than accoun variant  t balance, try again.");
        }
    }

    public void transfer(Account account, double amount) {
        if (amount > 0 || this.balance > amount) {
            System.out.println("variant");
            this.withdraw(amount);
            account.deposit(amount);
        } else {
            System.out.println("Transfer amount is bigger than account balance, try again.");
        }
    }

    public static void setInterestRate(double amount) {
        interestRate = amount;
    }

    public void addInterest() {
        this.balance = balance + (balance * interestRate / 100);
    }
}
