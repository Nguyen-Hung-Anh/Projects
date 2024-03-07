/*
Product Struct: A struct named "product" is created with fields for product 
name, department, quantity, SKU, and price.

Main Function: The main function prompts the user to input information for 3 products 
and creates instances of the product struct with the provided information. 
It then passes these instances to the manage_inventory function.

Manage Inventory Function: A void function named manage_inventory is implemented, 
which calls the order_more function for each product and prints "Order more" 
if the return value is TRUE. It also calls the is_grocery function for each product 
and prints grocery item details if the return value is TRUE.

Order More Function: The order_more function checks if the quantity of a product 
is greater than 5 and returns TRUE if it is, otherwise returns FALSE.

Is Grocery Function: The is_grocery function checks if the department of a product 
is "grocery" and returns TRUE if it is, otherwise returns FALSE.
*/

#include<stdio.h>

#define FALSE 0
#define TRUE 1

// Define a structure to represent a product
struct product {
    char product_name[32];
    char department[16];
    int quantity;
    int SKU;
    float price;
};

// Function prototypes
void manage_inventory(struct product p1, struct product p2, struct product p3);
int order_more(struct product item);
int is_grocery(struct product item);

int main() {

    // Declare variables to store product information
    struct product product1, product2, product3;
		
    // Input information for product 1
    printf("Enter information for product 1:\n");
    printf("Product Name: ");
    scanf("%31s", product1.product_name);
    printf("Department: ");
    scanf("%15s", product1.department);
    printf("Quantity: ");
    scanf("%d", &product1.quantity);
    printf("SKU: ");
    scanf("%d", &product1.SKU);
    printf("Price: ");
    scanf("%f", &product1.price);

    // Input information for product 2
    printf("\nEnter information for product 2:\n");
    printf("Product Name: ");
    scanf("%31s", product2.product_name);
    printf("Department: ");
    scanf("%15s", product2.department);
    printf("Quantity: ");
    scanf("%d", &product2.quantity);
    printf("SKU: ");
    scanf("%d", &product2.SKU);
    printf("Price: ");
    scanf("%f", &product2.price);

    // Input information for product 3
    printf("\nEnter information for product 3:\n");
    printf("Product Name: ");
    scanf("%31s", product3.product_name);
    printf("Department: ");
    scanf("%15s", product3.department);
    printf("Quantity: ");
    scanf("%d", &product3.quantity);
    printf("SKU: ");
    scanf("%d", &product3.SKU);
    printf("Price: ");
    scanf("%f", &product3.price);

    // Call manage_inventory function with the products as arguments
    manage_inventory(product1, product2, product3);

    return 0;
}

// Function to manage inventory, takes three product structures as input
void manage_inventory(struct product p1, struct product p2, struct product p3) {
    // Check if each product needs to be reordered
    if (order_more(p1) == TRUE) {
        printf("Order more:\n");
        printf("SKU: %d\n", p1.SKU);
        printf("Product Name: %s\n", p1.product_name);
        printf("\n");
    }
    if (order_more(p2) == TRUE) {
        printf("Order more:\n");
        printf("SKU: %d\n", p2.SKU);
        printf("Product Name: %s\n", p2.product_name);
        printf("\n");
    }
    if (order_more(p3) == TRUE) {
        printf("Order more:\n");
        printf("SKU: %d\n", p3.SKU);
        printf("Product Name: %s\n", p3.product_name);
        printf("\n");
    }

    // Check if each product is a grocery item
    if (is_grocery(p1) == TRUE) {
        printf("Grocery\n=======\n");
        printf("Item Name: %s\n", p1.product_name);
        printf("SKU: %d\n", p1.SKU);
        printf("Quantity: %d\n", p1.quantity);
        printf("Price: %g\n", p1.price);
    }
    if (is_grocery(p2) == TRUE) {
        printf("Grocery\n=======\n");
        printf("Item Name: %s\n", p2.product_name);
        printf("SKU: %d\n", p2.SKU);
        printf("Quantity: %d\n", p2.quantity);
        printf("Price: %g\n", p2.price);
    }
    if (is_grocery(p3) == TRUE) {
        printf("Grocery\n=======\n");
        printf("Item Name: %s\n", p3.product_name);
        printf("SKU: %d\n", p3.SKU);
        printf("Quantity: %d\n", p3.quantity);
        printf("Price: %g\n", p3.price);
    }
}	
	

// Function to check if quantity of an item is low
int order_more(struct product item) {
    if(item.quantity > 5) {
        return FALSE;
    } else {
        return TRUE;
    }	
}

// Function to check if an item belongs to the grocery department
int is_grocery(struct product item) {
    int index = 0;
    // Compare department string with "grocery" string
    while (item.department[index] != '\0' || index < 8) {
        if (item.department[index] != "grocery"[index])
            return FALSE;
        index++;
    }
    return TRUE;
}