import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class BillSplitterApp {
    public static void main(String[] args) {
        
        JFrame frame = new JFrame("Bill Splitter");
        frame.setLayout(new BorderLayout());
        frame.setSize(400, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(6, 2));
        
        JTextField nameField = new JTextField();
        JTextField priceField = new JTextField();
        JTextField peopleField = new JTextField("1"); 
        
        String[] type = {"Shared Item", "Individual Item"};
        JComboBox<String> typeComboBox = new JComboBox<>(type);
        
        String[] tip = {"15%", "18%", "20%"};
        JComboBox<String> tipComboBox = new JComboBox<>(tip);
        
        panel.add(new JLabel("Item Name:"));
        panel.add(nameField);
        panel.add(new JLabel("Price:"));
        panel.add(priceField);
        panel.add(new JLabel("Type:"));
        panel.add(typeComboBox);
        panel.add(new JLabel("Total People:"));
        panel.add(peopleField);
        panel.add(new JLabel("Tip:"));
        panel.add(tipComboBox);
        
        JButton addButton = new JButton("Add Item");
        JButton calcButton = new JButton("Calculate");
        panel.add(addButton);
        panel.add(calcButton);
        
        JTextArea resultArea = new JTextArea();
        resultArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(resultArea);
        
        ArrayList<BillItem> items = new ArrayList<>();
        
        addButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String name = nameField.getText().trim();
                if (name.isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Please enter an item name.", "Input Error", JOptionPane.WARNING_MESSAGE);
                    return; 
                }

                try {
                    double price = Double.parseDouble(priceField.getText());
                    
                    if (price < 0) {
                        JOptionPane.showMessageDialog(frame, "Price cannot be negative.", "Input Error", JOptionPane.WARNING_MESSAGE);
                        return;
                    }

                    String selectedType = (String) typeComboBox.getSelectedItem();
                    
                    BillItem item;
                    if(selectedType.equals("Shared Item")) {
                        item = new SharedAppetizer(name, price);
                    } else {
                        item = new IndividualEntree(name, price);
                    }
                    
                    items.add(item);
                    
                    resultArea.append(String.format("%s (%s) - $%.2f%n", name, selectedType, price));
                    
                    nameField.setText("");
                    priceField.setText("");
                    
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(frame, "Please enter a valid number for the price.", "Input Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });
        
        calcButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (items.isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Please add at least one item first.", "Empty Bill", JOptionPane.WARNING_MESSAGE);
                    return;
                }

                try {
                    int people = Integer.parseInt(peopleField.getText());
                    
                    if (people <= 0) {
                        JOptionPane.showMessageDialog(frame, "Total people must be at least 1.", "Input Error", JOptionPane.WARNING_MESSAGE);
                        return;
                    }

                    String selectedTip = (String) tipComboBox.getSelectedItem();
                    double tipPercent = Double.parseDouble(selectedTip.replace("%", ""));
                    
                    double mySubtotalShare = 0;
                    for (BillItem item : items) {
                        mySubtotalShare += item.calculateCostPerPerson(people); 
                    }
                    
                    Taxable tax = new TaxCalculator(5);
                    double myTaxedShare = tax.applyTax(mySubtotalShare);
                    double myTipShare = myTaxedShare * (tipPercent / 100);
                    double myFinalOwed = myTaxedShare + myTipShare;
                    
                    resultArea.setText("");
                    resultArea.append("\n--- Your Personal Bill Share ---\n");
                    resultArea.append(String.format("Your Subtotal: $%.2f%n", mySubtotalShare));
                    resultArea.append(String.format("With Tax (5%%): $%.2f%n", myTaxedShare));
                    resultArea.append(String.format("Your Tip Share: $%.2f%n", myTipShare));
                    resultArea.append(String.format("YOU OWE: $%.2f%n", myFinalOwed));
                    
                    items.clear(); 
                    
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(frame, "Please enter a valid whole number for Total People.", "Input Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });
        
        frame.add(panel, BorderLayout.NORTH);
        frame.add(scrollPane, BorderLayout.CENTER);
        
        frame.setVisible(true);
    }
}

interface Taxable {
    double applyTax(double subtotal);
}

class TaxCalculator implements Taxable {
    private double taxRate;
    
    public TaxCalculator(double taxRate) {
        this.taxRate = taxRate;
    }
    
    @Override
    public double applyTax(double subtotal) {
        return subtotal + (subtotal * taxRate / 100);
    }
}

abstract class BillItem {
    private String name;
    private double price;
    
    public BillItem(String n, double p) {
        this.name = n;
        this.price = p;
    }
    
    public double getPrice() { return this.price; }
    public String getName() { return this.name; }
    
    public abstract double calculateCostPerPerson(int totalPeople);
}

class SharedAppetizer extends BillItem {
    
    public SharedAppetizer(String name, double price) {
        super(name, price);
    }
    
    @Override
    public double calculateCostPerPerson(int totalPeople) {
        return super.getPrice() / totalPeople;
    }
}

class IndividualEntree extends BillItem {
    
    public IndividualEntree(String name, double price) {
        super(name, price);
    }
    
    @Override
    public double calculateCostPerPerson(int totalPeople) {
        return super.getPrice();
    }
}