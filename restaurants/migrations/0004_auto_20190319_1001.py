# Generated by Django 2.1.7 on 2019-03-19 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20190317_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='operatingday',
            name='restaurant',
        ),
        migrations.AlterModelOptions(
            name='queue',
            options={'ordering': ['-position']},
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='_type',
        ),
        migrations.AddField(
            model_name='operatingtime',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='operatingtime',
            name='day',
            field=models.ManyToManyField(to='restaurants.Day'),
        ),
        migrations.AlterField(
            model_name='queue',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='restaurants.Restaurant'),
        ),
        migrations.RenameModel(
            old_name='Menu',
            new_name='Category',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.DeleteModel(
            name='OperatingDay',
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Category'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='foodtype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurants.RestaurantType'),
            preserve_default=False,
        ),
    ]
