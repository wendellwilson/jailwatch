from django.contrib.gis.db import models
from django.core.validators import RegexValidator

PHONE_REGEX = RegexValidator(
    regex=r'^\d{10}$',
    message="Phone number must be entered in the format: '9999999999'"
)
YEAR_REGEX = RegexValidator(
    regex=r'^\d{4}$',
    message="Year must be entered in the format: '2222'"
)

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('B', 'Both')
)
POPULATION_DENSITY_CHOICES = (
    ('MR', 'Mostly Rural'),
    ('CR', 'Completely Rural'),
    ('MU', 'Mostly Urban'),
    ('CU', 'Completely Urban'),
)


class PIO(models.Model):  # Public Information Officer
    first_name = models.CharField('PIO First Name', max_length=20)
    last_name = models.CharField('PIO Last Name', max_length=20)
    middle_name = models.CharField('PIO Middle Name or Initial', max_length=20)
    email = models.EmailField('PIO Office Email', max_length=50)
    phone = models.CharField('PIO Phone Number', validators=[PHONE_REGEX], max_length=10)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Sheriff(models.Model):
    first_name = models.CharField('Sheriff First Name', max_length=20)
    last_name = models.CharField('Sheriff Last Name', max_length=20)
    middle_name = models.CharField('Sheriff Middle Name or Initial', max_length=20)
    office_email = models.EmailField('Sheriff Office Email', max_length=50)
    office_phone = models.CharField('Sheriff Office Phone Number',validators=[PHONE_REGEX], max_length=10)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Jail(models.Model):
    name = models.CharField('Jail Name', max_length=50)
    city = models.CharField('Jail City', max_length=20)
    capacity = models.PositiveIntegerField('Capacity')
    phone_number = models.CharField('Main Jail Phone Number', validators=[PHONE_REGEX], max_length=10)
    search_url = models.URLField('Inmate Search URL')
    opened_year = models.CharField('Year of Jail Opening', validators=[YEAR_REGEX], max_length=4)
    renovated_year = models.CharField('Year of Most Recent Renovations', validators=[YEAR_REGEX], max_length=4)
    daily_pop = models.PositiveIntegerField('Average Daily Population')
    staff = models.PositiveIntegerField('Number of Staff')
    gender = models.CharField('Genders in Prison', max_length=1, choices=GENDER_CHOICES)
    loc_pop_den = models.CharField('Census Information on Location of Prison Urban vs Rural',
                                   max_length=2, choices=POPULATION_DENSITY_CHOICES)
    address = models.CharField('Jail Address', max_length=255)
    budget = models.PositiveIntegerField('Budget')
    email = models.EmailField('Jail Office Email')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class County(models.Model):
    name = models.CharField('County Name', max_length=20, unique=True)
    fips = models.CharField('FIPS Code', max_length=3)
    border = models.PolygonField('County Border for Mapping', srid=900914)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
