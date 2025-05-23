# Database Documentation

## Database Schema

### Products Table
- Primary key: `id` (INT, AUTO_INCREMENT)
- `name` (VARCHAR(255)) - Name of the product
- `category` (VARCHAR(100)) - Product category
- `description` (TEXT) - Product description
- `price` (DECIMAL(10,2)) - Current product price

### Sales Table
- Primary key: `id` (INT, AUTO_INCREMENT)
- `product_id` (INT) - Foreign key referencing Products table
- `quantity` (INT) - Number of units sold
- `price` (DECIMAL(10,2)) - Price at the time of sale
- `sale_date` (DATETIME) - Date and time of the sale
- Foreign key constraint: `product_id` references `Products(id)`

### Inventory Table
- Primary key: `id` (INT, AUTO_INCREMENT)
- `product_id` (INT) - Foreign key referencing Products table
- `quantity` (INT) - Current stock quantity
- `last_updated` (DATETIME) - Last inventory update timestamp
- Foreign key constraint: `product_id` references `Products(id)`

## Relationships

1. Products to Sales (One-to-Many):
   - One product can have multiple sales records
   - Each sale record belongs to one product
   - Relationship maintained through `product_id` in Sales table

2. Products to Inventory (One-to-One):
   - Each product has one inventory record
   - Each inventory record belongs to one product
   - Relationship maintained through `product_id` in Inventory table

## Indexing
- Primary keys are automatically indexed
- Foreign keys (`product_id`) are indexed for faster joins
- `sale_date` in Sales table is indexed for efficient date-based queries
- `category` in Products table is indexed for category-based filtering

## Data Integrity
- Foreign key constraints ensure referential integrity
- `NOT NULL` constraints on essential fields
- `DEFAULT` values where appropriate
- `UNIQUE` constraint on product names to prevent duplicates 