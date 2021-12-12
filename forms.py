# ######################################################################################################################
# ########################################                               ###############################################
# ########################################          FLASK FORMS          ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, PasswordField, FloatField, DateTimeField
from wtforms.validators import Length, InputRequired, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[InputRequired()]
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired()]
    )
    remember_me = BooleanField('Remember Me')

    submit = SubmitField("Sign In")


class LoginRegistrationForm():
    username = StringField(
        "Username",
        validators=[InputRequired()]
    )
    email = StringField(
        "Email",
        validators=[InputRequired(), Email()]
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired()]
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[InputRequired(), EqualTo(password, message="Passwords must match.")]
    )

    submit = SubmitField("Register")


class AirplaneRegistrationForm(FlaskForm):
    airplane_type = IntegerField(
        'Airplane Type',
        validators=[InputRequired()]
    )

    submit = SubmitField('Add Airplane')


class AirplaneTypeRegistrationForm(FlaskForm):
    type_id = IntegerField(
        'Type ID',
        validators=[InputRequired()]
    )
    max_capacity = IntegerField(
        "Max Capacity",
        validators=[InputRequired()]
    )

    submit = SubmitField('Add Airplane Type')


class AirportRegistrationForm(FlaskForm):
    iata_id = StringField(
        'IATA ID',
        validators=[Length(min=3, max=3)]
    )
    city = StringField(
        'City',
        validators=[Length(min=3, max=40)]
    )
    name = StringField(
        'Name',
        validators=[Length(min=3, max=40)]
    )
    longitude = IntegerField(
        'Longitude',
        validators=[]
    )
    latitude = IntegerField(
        'Latitude',
        validators=[]
    )
    elevation = IntegerField(
        'Elevation',
        validators=[]
    )

    submit = SubmitField('Add Airport')


class BookingRegistrationForm(FlaskForm):
    id = IntegerField(
        'Booking ID',
        validators=[InputRequired()]
    )
    is_active = BooleanField(
        'Is Active',
        validators=[InputRequired()]
    )
    confirmation_code = StringField(
        'Confirmation Code',
        validators=[InputRequired()]
    )

    submit = SubmitField('Add Booking')


class BookingGuestRegistrationForm(FlaskForm):
    booking_id = IntegerField(
        'Booking ID',
        validators=[InputRequired()]
    )
    contact_email = StringField(
        'Contact Email',
        validators=[Email()]
    )
    contact_phone = StringField(
        'Contact Phone'
    )

    submit = SubmitField('Add Booking Guest')


class BookingPaymentRegistrationForm(FlaskForm):
    booking_id = IntegerField(
        'Booking ID',
        validators=[InputRequired()]
    )
    stripe_id = StringField(
        'Stripe ID'
    )
    refunded = BooleanField(
        'Refunded?'
    )

    submit = SubmitField('Add Booking Payment')


class RouteRegistrationForm(FlaskForm):
    origin_id = StringField(
        'Origin',
        validators=[Length(min=3, max=3)]
    )
    destination_id = StringField(
        'Destination',
        validators=[Length(min=3, max=3)]
    )

    submit = SubmitField('Add Route')


class FlightRegistrationForm(FlaskForm):
    id = IntegerField(
        'Flight ID',
        validators=[InputRequired()]
    )
    route_id = IntegerField(
        'Route ID',
        validators=[InputRequired()]
    )
    airplane_id = IntegerField(
        'Airplane ID',
        validators=[InputRequired()]
    )
    departure_time = DateTimeField(
        'Departure Time',
        validators=[InputRequired()]
    )
    reserved_seats = IntegerField(
        'Reserved Seats',
        validators=[]
    )
    seat_price = FloatField(
        'Airplane ID',
        validators=[InputRequired()]
    )

    submit = SubmitField('Add Flight')


class PassengerRegistrationForm(FlaskForm):
    id = IntegerField(
        'Flight ID',
        validators=[InputRequired()]
    )
    route_id = IntegerField(
        'Route ID',
        validators=[InputRequired()]
    )
    airplane_id = IntegerField(
        'Airplane ID',
        validators=[InputRequired()]
    )
    departure_time = DateTimeField(
        'Departure Time',
        validators=[InputRequired()]
    )
    reserved_seats = IntegerField(
        'Reserved Seats',
        validators=[]
    )
    seat_price = FloatField(
        'Airplane ID',
        validators=[InputRequired()]
    )

    submit = SubmitField('Add Flight')


class UserRoleRegistrationForm(FlaskForm):
    id = IntegerField(
        "Role ID",
        validators=[InputRequired()]
    )
    name = StringField(
        "Role Name",
        validators=[InputRequired()]
    )

    submit = SubmitField("Add User Role")


class UserRegistrationForm(FlaskForm):
    id = IntegerField(
        "User ID",
        validators=[InputRequired()]
    )
    role_id = IntegerField(
        "Role ID",
        validators=[InputRequired()]
    )
    given_name = StringField(
        "First Name",
        validators=[InputRequired()]
    )
    family_name = StringField(
        "Family Name",
        validators=[InputRequired()]
    )
    username = StringField(
        "Username",
        validators=[InputRequired()]
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired()]
    )
    email = StringField(
        "Email",
        validators=[InputRequired(), Email()]
    )
    phone = StringField(
        "Phone",
        validators=[InputRequired(), Length(min=10)]
    )

    submit = SubmitField("Add User")

