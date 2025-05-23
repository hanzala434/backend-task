# E-commerce Admin API

A backend API that powers a web admin dashboard for e-commerce managers, providing insights into sales, revenue, and inventory status.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- MySQL database

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Backend_Task
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn sqlalchemy mysqlclient
```

4. Configure the database:
- Create a MySQL database
- Update the database connection string in `app/database.py`

5. Run the demo data script:
```bash
mysql -u your_username -p your_database < demo_data/seed.sql
```

6. Start the server:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

### Sales Endpoints

#### GET /sales/
- Retrieves all sales records

#### POST /sales/
- Creates a new sale record
- Body: Sale details including product_id, quantity, price

#### GET /sales/filter
- Filters sales by date range, product, and category
- Query Parameters:
  - start_date: Start date (YYYY-MM-DD)
  - end_date: End date (YYYY-MM-DD)


#### GET /sales/revenue/aggregate
- Analyzes revenue for different time periods
- Query Parameters:
  - mode: One of "daily", "weekly", "monthly", "yearly"

#### GET /sales/revenue/compare
- Compares revenue between two periods
- Query Parameters:
  - period1_start: First period start date
  - period1_end: First period end date
  - period2_start: Second period start date
  - period2_end: Second period end date

### Inventory Endpoints

#### GET /inventory/
- Lists current inventory status

#### POST /inventory/
- Updates inventory levels
- Body: Inventory details including product_id, quantity

#### GET /inventory/low-stock
- Retrieves products with low stock levels 