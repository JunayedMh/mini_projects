## A small shop wants to manage inventory using tuples.
Each product is stored as a TUPLE: (product_id, name, price, quantity).
Tuples are used here because product data should not change accidentally.


**Rules**:
- Start with 5 pre-loaded product tuples.
- Menu:
1. View all products (neat table)
2. Search by name (partial, case-insensitive)
3. Show low stock items (quantity < 5)
4. Show total inventory value (price x quantity for all items)
5. Restock any product if needed
6. Exit
