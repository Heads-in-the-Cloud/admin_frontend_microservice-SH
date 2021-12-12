import requests
from flask import render_template, jsonify
from app import app
from forms import *


@app.route('/')
@app.route('/about')
def hello():
    return render_template('about.html', title='About Page')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Sign In", form=form)


@app.route('/register')
def register():
    form = LoginRegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/airport')
def airport():
    airports = requests.get('http://flights:5000/api/airport/all')
    form = AirportRegistrationForm()
    return render_template('airport.html', title="Airport Management", form=form, airports=airports)


@app.route('/airplane')
def airplane():
    # airplanes = requests.get('http://flights:5000/api/airplane/all')
    airplanes = [
        {
            'id': 1,
            'type_id': 747
        },
        {
            'id': 2,
            'type_id': 858
        },
        {
            'id': 3,
            'type_id': 969
        }
    ]
    form = AirplaneRegistrationForm()
    return render_template('airplane.html', title="Airplane Management", form=form, airplanes=airplanes)


@app.route('/airplane_type')
def airplane_type():
    airplane_types = requests.get('http://flights:5000/api/airplane_type/all')
    form = AirplaneTypeRegistrationForm()
    return render_template('airplane_type.html', title="Airplane Type Management", form=form, airplane_types=airplane_types)


@app.route('/booking')
def booking():
    bookings = requests.get('http://bookings:5000/api/booking/all')
    form = BookingRegistrationForm()
    return render_template('booking.html', title="Bookings Management", form=form, bookings=bookings)


@app.route('/booking_guest')
def booking_guest():
    booking_guests = requests.get('http://bookings:5000/api/booking_guest/all')
    form = BookingGuestRegistrationForm()
    return render_template('booking_guest.html', title="Booking Guest Management", form=form, booking_guests=booking_guests)


@app.route('/booking_payment')
def booking_payment():
    booking_payments = requests.get('http://bookings:5000/api/booking_payment/all')
    form = BookingPaymentRegistrationForm()
    return render_template('booking_payment.html', title="Booking Payment Management", form=form, booking_payments=booking_payments)


@app.route('/flight')
def flight():
    flights = requests.get('http://flights:5000/api/flight/all')
    form = FlightRegistrationForm()
    return render_template('flight.html', title="Flight Management", form=form, flights=flights)


@app.route('/user')
def user():
    users = requests.get('http://users:5000/api/user/all')
    form = UserRegistrationForm()
    return render_template('user.html', title="User Management", form=form, users=users)


@app.route('/user_role')
def user_role():
    # user_roles = requests.get('http://users:5000/api/user_role/all')
    user_roles = [
        {
            'id': 1,
            'name': 'admin'
        },
        {
            'id': 2,
            'name': 'agent'
        },
        {
            'id': 3,
            'name': 'user'
        }
    ]
    form = UserRoleRegistrationForm()
    return render_template('user_role.html', title="User Role Management", form=form, user_roles=user_roles)


@app.route('/passenger')
def passenger():
    passengers = requests.get('http://bookings:5000/api/passenger/all')
    form = PassengerRegistrationForm()
    return render_template('passenger.html', title="Passenger Management", form=form, passengers=passengers)


@app.route('/route')
def route():
    routes = requests.get('http://flights:5000/api/route/all')
    form = RouteRegistrationForm()
    return render_template('route.html', title="Route Management", form=form, routes=routes)
