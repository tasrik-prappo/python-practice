public class Main {
    public static void main(String args[]) {
        Staff s = new Staff("Messi", 253, 5);
        Supervisor sv = new Supervisor("Neymar", 263, 8, 63000.0);
        Passenger p[] = new Passenger[5];
        p[0] = new Passenger("Alice", "Economy", 4500);
        p[1] = new Passenger("Brian", "Buisness", 12000);
        p[2] = new Passenger("Catherine", "Economy", 4500);
        p[3] = new Passenger("David", "First Class", 18000);
        p[4] = new Passenger("Emma", "Buisness", 12000);
        System.out.println(s.getSalary());
        System.out.println(s.getBonus());
        s.setSalary(50000);
        System.out.println(s.getSalary());
        System.out.println(s.getBonus());
        sv.setSalary(s, 48000);
        System.out.println(s.getSalary());
        System.out.println(s.getBonus());
        sv.setSalary(100000);
        System.out.println(sv.getSalary());
        System.out.println(sv.getBonus());
        Passenger.BuisnessPassengers(p);
    }
}

class Staff {
    String name;
    int staffId;
    int yearsOfService;
    private double baseSalary;

    public Staff() {
    }

    public Staff(String n, int id, int y) {
        this.name = n;
        this.staffId = id;
        this.yearsOfService = y;
    }

    public double getSalary() {
        return this.baseSalary;
    }

    public void setSalary(double amount) {
        this.baseSalary = amount;
    }

    public double getBonus() {
        return (5.0 / 100.0) * this.baseSalary;
    }
}

class Supervisor extends Staff {
    public Supervisor() {
    }

    public Supervisor(String n, int id, int y, double sal) {
        super(n, id, y);
        super.setSalary(sal);
    }

    public void setSalary(double ammount) {
        super.setSalary(ammount);
    }

    public void setSalary(Staff staff, double amount) {
        staff.setSalary(amount);
    }

    @Override
    public double getBonus() {
        return (yearsOfService / 100.0) * getSalary();
    }
}

class Passenger {
    String pasName;
    String ticType;
    int fare;

    public Passenger(String n, String t, int f) {
        this.pasName = n;
        this.ticType = t;
        this.fare = f;
    }

    public static void BuisnessPassengers(Passenger passengers[]) {
        for (int i = 0; i < passengers.length; i++) {
            if (passengers[i].ticType.equals("Buisness")) {
                System.out.println("Name: " + passengers[i].pasName);
            }
        }
    }
}