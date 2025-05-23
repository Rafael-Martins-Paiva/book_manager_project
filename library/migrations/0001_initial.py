
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
