
# Hotel Booking Website (BlueSkyBooking)

**Final Assignment**

BlueSkyBooking is a comprehensive hotel booking system developed using Django REST Framework, featuring user authentication, hotel and booking management, payment processing, and review functionalities. This application supports CRUD operations for hotels and bookings, secure payments via SSLCommerz, and integrates email notifications for booking confirmations.

- **Frontend GitHub:** [Hotel-Booking-Frontend](https://github.com/ramim141/Hotel-Booking-Management-frontend)
- **Backend GitHub:** [Hotel-Booking-Website-Backend](https://github.com/ramim141/Hotel-Booking-Management-Backend)

### User Access Information
- **Admin Role:**
```
Username: manager
Password: manager2004
```



## API Endpoints

### Account App
| Action                | Endpoint                                                               |
|-----------------------|------------------------------------------------------------------------|
| All Users             | [`/user/allUser/`](https://hotel-booking-website-backend.vercel.app/user/allUser/) |
| Account View          | [`/user/account/`](https://hotel-booking-website-backend.vercel.app/user/account/) |
| Register              | [`/user/register/`](https://hotel-booking-website-backend.vercel.app/user/register/) |
| Login                 | [`/user/login/`](https://hotel-booking-website-backend.vercel.app/user/login/) |
| Logout                | [`/user/logout/`](https://hotel-booking-website-backend.vercel.app/user/logout/) |
| Deposit               | [`/user/deposit/`](https://hotel-booking-website-backend.vercel.app/user/deposit/) |
| Check User Role       | [`/user/is_users_staff/`](https://hotel-booking-website-backend.vercel.app/user/is_users_staff/) |
| Contact Admin         | [`/user/admin-messages/`](https://hotel-booking-website-backend.vercel.app/user/admin-messages/) |

### Hotel App
| Action                | Endpoint                                                               |
|-----------------------|------------------------------------------------------------------------|
| All Districts         | [`/hotel/districts/`](https://hotel-booking-website-backend.vercel.app/hotel/districts/) |
| District Details      | [`/hotel/districts/1/`](https://hotel-booking-website-backend.vercel.app/hotel/districts/1/) |
| All Hotels            | [`/hotel/hotels/`](https://hotel-booking-website-backend.vercel.app/hotel/hotels/) |
| Hotel Details         | [`/hotel/hotels/1`](https://hotel-booking-website-backend.vercel.app/hotel/hotels/1) |
| All Reviews           | [`/hotel/reviews/`](https://hotel-booking-website-backend.vercel.app/hotel/reviews/) |
| Add Review            | [`/hotel/review_add/`](https://hotel-booking-website-backend.vercel.app/hotel/review_add/) |
| Review Update/Delete  | [`/hotel/review_add/1/`](https://hotel-booking-website-backend.vercel.app/hotel/review_add/1/) |
| All Bookings          | [`/hotel/bookings/`](https://hotel-booking-website-backend.vercel.app/hotel/bookings/) |
| Book a Hotel          | [`/hotel/book/`](https://hotel-booking-website-backend.vercel.app/hotel/book/) |
| Download Booking PDF  | [`/hotel/download-booking-pdf/1/`](https://hotel-booking-website-backend.vercel.app/hotel/download-booking-pdf/1/) |

### Payment App
| Action                | Endpoint                                                               |
|-----------------------|------------------------------------------------------------------------|
| Payment Booking       | [`/payment/payment-booking/`](https://hotel-booking-website-backend.vercel.app/payment/payment-booking/) |
| Payment Success       | [`/payment/success/`](https://hotel-booking-website-backend.vercel.app/payment/success/) |
| Payment Failed        | [`/payment/fail/`](https://hotel-booking-website-backend.vercel.app/payment/fail/) |
| Payment Cancel        | [`/payment/cancel/`](https://hotel-booking-website-backend.vercel.app/payment/cancel/) |

---

## Key Features
- **User Authentication** via Gmail OAuth
- **CRUD Operations** for hotel and booking management
- **Email Notifications** for booking confirmations
- **SSLCommerz Payment Integration** for secure payments
- **Hotel Review System** for customer feedback
- **Scalable PostgreSQL Database** with Django Rest Framework API

---

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** OAuth2 via Gmail
- **Payment Gateway:** SSLCommerz


---

## Installation and Setup

1. **Clone the repository:**
 ```bash
 
git clone https://github.com/ramim141/Hotel-Booking-Management-Backend.git

```

Install dependencies:
```
pip install -r requirements.txt

```
Run migrations:
```
 python manage.py migrate
```

Create a superuser:
```
python manage.py createsuperuser
```
Run the server:
```
python manage.py runserver
```

Run Tests:

```
python manage.py runserver
```


License
This project is licensed under the MIT License.
You can save this code as `README.md` in your project repository. It includes all the necessary information for users and developers to understand your project.






