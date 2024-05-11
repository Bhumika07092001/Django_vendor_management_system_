
# Django Vendor Performance API

The Django Vendor Performance API is a RESTful web service built with Django and Django REST Framework that allows users to track and manage vendor performance metrics, such as on-time delivery rate, quality rating average, average response time, and fulfillment rate.

## Features

- Create, retrieve, update, and delete purchase orders.
- Track vendor performance metrics over time.
- Generate reports and insights based on performance data.

## Installation

To set up the Django Vendor Performance API on your local machine, follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your-username/Django_vendor_management_system_with_performance_metrics.git
   ```

2. Navigate to the project directory:
   ```
   cd vendor_system
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Apply database migrations:
   ```
   python manage.py migrate
   ```

7. Create a superuser account (for accessing the Django admin):
   ```
   python manage.py createsuperuser
   ```

8. Start the development server:
   ```
   python manage.py runserver
   ```

9. Access the API at `http://127.0.0.1:8000/api/`.

## API Endpoints

- `GET /api/vendors/`: List all vendors.
- `POST /api/vendors/`: Create a new vendor.
- `GET /api/vendors/<int:pk>/`: Retrieve details of a specific vendor.
- `PUT /api/vendors/<int:pk>/`: Update a vendor's information.
- `DELETE /api/vendors/<int:pk>/`: Delete a vendor.
- `GET /api/vendors/{vendor_id}/performance/`: Retrieve historical performance metrics for a specific vendor.



## Testing

To run the test suite and verify the functionality of the API endpoints, execute the following command:
```
python manage.py test
```
