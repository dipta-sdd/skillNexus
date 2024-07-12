
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(blank=True)
    mobile = models.TextField(blank=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    role = models.CharField(max_length=50, choices=[
        ('Employer', 'Employer'),
        ('Student', 'Student'),
        ('Freelancer', 'Freelancer'),
        ('Educator', 'Educator'),
        ('University', 'University'),
        ('Admin', 'Admin')
    ])
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Category(models.Model):
    name = models.CharField(max_length=255)


class Subcategory(models.Model):
    name = models.CharField(max_length=255)


class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategories = models.ManyToManyField(Subcategory, blank=True)


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    skills_required = models.ManyToManyField(Skill)
    status = models.CharField(max_length=20, choices=[(
        'open', 'Open'), ('closed', 'Closed'), ('in_progress', 'In Progress')])
    # participants = models.ManyToManyField(
    #     User, related_name='projects_participated', blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()


class Review(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='reviews_given', null=True)
    subject = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='reviews_received', null=True)
    rating = models.PositiveIntegerField()
    description = models.TextField()
    date = models.DateField()


class Program(models.Model):
    university = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='programs')
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)


class Course(models.Model):
    program = models.ForeignKey(
        Program, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()


class PersonalDetails(models.Model):
    id = models.OneToOneField("data.user", verbose_name=(
        "Id of user"), on_delete=models.CASCADE, primary_key=True)
    father_name = models.CharField(max_length=200, blank=True, null=True)
    mother_name = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ])
    date_of_birth = models.DateField(blank=True, null=True)
    religion = models.CharField(max_length=200, blank=True, null=True)
    marital_status = models.CharField(max_length=7, blank=True, null=True, choices=[
        ('Married', 'Married'),
        ('Single', 'Single')
    ])


class Edu_level(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Edu_degree(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    level = models.ForeignKey(
        Edu_level, on_delete=models.CASCADE, null=True)


class Edu_group_or_major(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    degree = models.ForeignKey(
        Edu_degree, on_delete=models.CASCADE, null=True)


class Education(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False)
    level = models.ForeignKey(
        Edu_level, on_delete=models.CASCADE,  blank=False)
    degree = models.ForeignKey(
        Edu_degree, on_delete=models.CASCADE, blank=False)
    group = models.ForeignKey(
        Edu_group_or_major, on_delete=models.CASCADE, blank=False)
    result_type = models.CharField(max_length=8, blank=False, choices=[
        ('Grade', 'Grade'),
        ('Class', 'Class'),
        ('Division', 'Division')
    ])
    result = models.IntegerField(null=True, blank=True)
    gpa = models.DecimalField(
        decimal_places=2, max_digits=3, null=True, blank=True)
    gpa_scale = models.DecimalField(
        decimal_places=2, max_digits=3, null=True, blank=True)
    institute = models.CharField(max_length=255, blank=False, null=False)
    passing_year = models.PositiveIntegerField(blank=False)
    # start_date = models.DateField()


class Training(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    title = models.CharField(max_length=250, blank=False)
    institution_name = models.CharField(max_length=300, blank=False)
    country = models.CharField(max_length=50, blank=False)
    duration_year = models.IntegerField(blank=False)
    duration_month = models.IntegerField(blank=False)
    duration_day = models.IntegerField(blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    designation = models.CharField(max_length=250, blank=False)
    department = models.CharField(max_length=250, blank=False)
    organisation_name = models.CharField(max_length=300, blank=False)
    location = models.CharField(max_length=50, blank=False)
    duration_year = models.IntegerField(blank=False)
    duration_month = models.IntegerField(blank=False)
    duration_day = models.IntegerField(blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
