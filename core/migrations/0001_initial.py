# Generated by Django 3.2.3 on 2021-06-12 03:43

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'Pharmacy Owner'), (2, ' Phermacist'), (3, 'Customer')], default=3, max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('delivered', models.IntegerField(default=1)),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('costofdelivery', models.IntegerField()),
                ('delivery_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOrders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_price', models.CharField(max_length=255)),
                ('coupon_code', models.CharField(max_length=255)),
                ('discount_amt', models.CharField(max_length=255)),
                ('product_status', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sender', models.CharField(max_length=255)),
                ('reciever', models.CharField(max_length=255)),
                ('subject', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='amount')),
                ('isFinished', models.BooleanField(default=False)),
                ('isSuccessFull', models.BooleanField(default=False)),
                ('trans_id', models.CharField(max_length=30)),
                ('order_id', models.CharField(max_length=200)),
                ('checkoutRequestID', models.CharField(max_length=100)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PharmacistProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=255)),
                ('profile_pic', models.FileField(upload_to='')),
                ('address', models.TextField()),
                ('country', models.CharField(default=None, max_length=255)),
                ('province', models.CharField(default=None, max_length=255)),
                ('district', models.CharField(default=None, max_length=255)),
                ('city', models.CharField(default=None, max_length=255)),
                ('zip_code', models.CharField(default=None, max_length=255)),
                ('phone_number', models.CharField(default=None, max_length=255)),
                ('education', models.CharField(default=None, max_length=255)),
                ('workplace', models.CharField(default=None, max_length=255)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('location_address', models.CharField(max_length=255)),
                ('country', models.CharField(default=None, max_length=255)),
                ('province', models.CharField(default=None, max_length=255)),
                ('district', models.CharField(default=None, max_length=255)),
                ('city', models.CharField(default=None, max_length=255)),
                ('zip_code', models.CharField(default=None, max_length=255)),
                ('phone_number', models.CharField(default=None, max_length=255)),
                ('license_no', models.CharField(max_length=255)),
                ('license_operate', models.FileField(upload_to='')),
                ('health_safety_code', models.CharField(max_length=255)),
                ('health_safety_code_doc', models.FileField(max_length=255, upload_to='')),
                ('about', models.TextField(max_length=150)),
                ('website', models.CharField(max_length=255)),
                ('contact_no', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PharmacyBranch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('license_no', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('contact_no', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('unit', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('gross', models.IntegerField()),
                ('size', models.CharField(max_length=255)),
                ('strength', models.CharField(max_length=255)),
                ('instock', models.IntegerField()),
                ('reader_limit', models.CharField(max_length=255)),
                ('expire_date', models.DateField()),
                ('mfg_date', models.DateField()),
                ('description', models.CharField(max_length=255)),
                ('attention', models.CharField(max_length=255)),
                ('frequecy', models.CharField(max_length=255)),
                ('composition', models.CharField(max_length=255)),
                ('notes', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now_add=True)),
                ('added_by_pharmacist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pharmacistprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False)),
                ('phone_number', models.CharField(max_length=30)),
                ('available_balance', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='available_balance')),
                ('actual_balance', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='actual_balance')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('pharmacy', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='core.pharmacybranch')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_product_count', models.IntegerField(default=1)),
                ('transaction_type', models.CharField(choices=[(1, 'BUY'), (2, 'SELL')], max_length=255)),
                ('transaction_description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReviews',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('review_image', models.FileField(upload_to='')),
                ('rating', models.CharField(default='5', max_length=255)),
                ('review', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductQuestions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductMedia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('media_type', models.CharField(max_length=255)),
                ('media_content', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=255)),
                ('patient', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('patient_contact', models.CharField(max_length=255)),
                ('presciber_name', models.CharField(max_length=255)),
                ('presciber_contact', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='core.product')),
            ],
        ),
        migrations.CreateModel(
            name='PharmacyPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='pharmacy/')),
                ('default', models.BooleanField(default=False)),
                ('photos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pharmacy')),
            ],
        ),
        migrations.CreateModel(
            name='PharmacyOwnerProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mobileNo', models.CharField(max_length=40)),
                ('cnic', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('shop_name', models.CharField(max_length=30)),
                ('user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDeliveryStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=255)),
                ('status_message', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customerorders')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationPharmacist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('pharmacist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pharmacistprofile')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationCustomer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customerprofile')),
            ],
        ),
        migrations.AddField(
            model_name='customerorders',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.product'),
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('pharmacy', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='core.pharmacybranch')),
            ],
        ),
    ]
