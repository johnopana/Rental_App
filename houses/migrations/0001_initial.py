
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('owner_pic', models.ImageField(default='images/avatar.png', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('profile_pic', models.ImageField(blank=True, default='images/avatar.png', upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.CharField(max_length=50)),
                ('registry_no', models.CharField(max_length=100)),
                ('house_location', models.CharField(max_length=50)),
                ('house_pic', models.ImageField(upload_to='media/')),
                ('house_type', models.CharField(max_length=100)),
                ('no_of_rooms', models.CharField(max_length=5)),
                ('year_built', models.CharField(max_length=5)),
                ('price', models.CharField(default=0, max_length=100)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.Owner')),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]
