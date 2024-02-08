# Generated by Django 4.2 on 2023-05-27 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(max_length=50)),
                ('division', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=50)),
                ('exp_date', models.DateField(blank=True, null=True)),
                ('available_days', models.IntegerField(blank=True, null=True)),
                ('rate', models.IntegerField(default=1)),
                ('ci_stock', models.IntegerField()),
                ('avail_stock', models.PositiveIntegerField()),
                ('ci_stock_price', models.IntegerField()),
                ('avail_stock_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=255, null=True)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='usertable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('cno', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=False)),
                ('is_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.items')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='app.OrderItem', to='app.items'),
        ),
    ]