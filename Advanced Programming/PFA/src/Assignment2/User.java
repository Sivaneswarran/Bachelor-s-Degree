package Assignment2;

import java.util.Objects;

public class User {

    private static int count = 0; // Static variable to track the number of instances
    private String name;          // Person's name
    private double income;        // Person's income
    private double expenses;      // Person's expenses
    private double savings;       // Percentage of income saved
    private double monthly;       // Monthly contribution
    private double amount;        // Cost of the item to be purchased
    private String item;          // Name of the item to be bought

    // Constructor to initialize all fields
    public User(String name, double income, double expenses, double savings, double monthly, double amount, String item) {
        this.name = name;
        this.income = income;
        this.expenses = expenses;
        this.savings = savings;
        this.monthly = monthly;
        this.amount = amount;
        this.item = item;
        count++; // Increment the instance count
    }

    // Getter and Setter methods

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getIncome() {
        return income;
    }

    public void setIncome(double income) {
        this.income = income;
    }

    public double getExpenses() {
        return expenses;
    }

    public void setExpenses(double expenses) {
        this.expenses = expenses;
    }

    public double getSavings() {
        return savings;
    }

    public void setSavings(double savings) {
        this.savings = savings;
    }

    public double getMonthly() {
        return monthly;
    }

    public void setMonthly(double monthly) {
        this.monthly = monthly;
    }

    public double getAmount() {
        return amount;
    }

    public void setAmount(double amount) {
        this.amount = amount;
    }

    public String getItem() {
        return item;
    }

    public void setItem(String item) {
        this.item = item;
    }

    // Static method to get the count of User instances
    public static int getCount() {
        return count;
    }

    // Override toString() method to provide a string representation of the User object
    @Override
    public String toString() {
        return "User [name=" + name + ", income=" + income + ", expenses=" + expenses + ", savings=" + savings
                + ", monthly=" + monthly + ", amount=" + amount + ", item=" + item + "]";
    }

    
    // Override equals() method to compare two User objects
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        User user = (User) obj;
        return Double.compare(user.income, income) == 0 &&
                Double.compare(user.expenses, expenses) == 0 &&
                Double.compare(user.savings, savings) == 0 &&
                Double.compare(user.monthly, monthly) == 0 &&
                Double.compare(user.amount, amount) == 0 &&
                Objects.equals(name, user.name) &&
                Objects.equals(item, user.item);
    }

    // Override hashCode() method to return a hash code for the User object
    @Override
    public int hashCode() {
        return Objects.hash(name, income, expenses, savings, monthly, amount, item);
    }
    
}