from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('frase', models.TextField()),
                ('inspirador', models.CharField(blank=True, max_length=255, null=True)),
                ('criado_em', models.DateTimeField(default=django.utils.timezone.now)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]