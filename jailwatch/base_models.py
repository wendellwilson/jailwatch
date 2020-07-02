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
    city = models.CharField('Jail City', max_length=20, null=True)
    capacity = models.PositiveIntegerField('Capacity', null=True)
    phone_number = models.CharField('Main Jail Phone Number', validators=[PHONE_REGEX], max_length=10, null=True)
    search_url = models.URLField('Inmate Search URL', null=True)
    opened_year = models.CharField('Year of Jail Opening', validators=[YEAR_REGEX], max_length=4, null=True)
    renovated_year = models.CharField('Year of Most Recent Renovations', validators=[YEAR_REGEX], max_length=4, null=True)
    daily_pop = models.PositiveIntegerField('Average Daily Population', null=True)
    staff = models.PositiveIntegerField('Number of Staff', null=True)
    gender = models.CharField('Genders in Prison', max_length=1, choices=GENDER_CHOICES, null=True)
    loc_pop_den = models.CharField('Census Information on Location of Prison Urban vs Rural',
                                   max_length=2, choices=POPULATION_DENSITY_CHOICES, null=True)
    address = models.CharField('Jail Address', max_length=255, null=True)
    budget = models.PositiveIntegerField('Budget', null=True)
    email = models.EmailField('Jail Office Email', null=True)
    location = models.PointField("Lat Long Location of Jail for Map")
    annex_location = models.PointField("Lat Long Location of Jail Annex for Map")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class County(models.Model):
    name = models.CharField('County Name', max_length=20, unique=True)
    fips = models.CharField('FIPS Code', max_length=3)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
