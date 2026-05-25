package Assignment2;

public class Person {
    
    private static int count = 0; // Static variable to keep track of the number of User instances
    private String username; // Instance variable for username
    private String password; // Instance variable for password

    // Constructor to initialize username and password
    public Person(String username, String password) {
        this.username = username;
        this.password = password;
        count++; // Increment the count each time a new User is created
    }

    // Getter for username
    public String getUsername() {
        return username;
    }

    // Setter for username
    public void setUsername(String username) {
        this.username = username;
    }

    // Getter for password
    public String getPassword() {
        return password;
    }

    // Setter for password
    public void setPassword(String password) {
        this.password = password;
    }

    // Static method to get the count of User instances
    public static int getCount() {
        return count;
    }
    
    @Override
    public String toString() {
        return "User {" + "username='" + username + '\'' + '}';
    }
}