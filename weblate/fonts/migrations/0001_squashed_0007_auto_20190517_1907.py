# Generated by Django 2.2 on 2019-05-22 12:35

import django.core.files.storage
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import weblate.fonts.validators
import weblate.trans.mixins
from weblate.utils.data import data_dir


class Migration(migrations.Migration):

    replaces = [
        ("fonts", "0001_initial"),
        ("fonts", "0002_fontgroup_fontoverride"),
        ("fonts", "0003_auto_20190517_1249"),
        ("fonts", "0004_auto_20190517_1421"),
        ("fonts", "0005_auto_20190517_1450"),
        ("fonts", "0006_auto_20190517_1900"),
        ("fonts", "0007_auto_20190517_1907"),
    ]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("trans", "0026_alert_change"),
        ("trans", "0027_auto_20190517_1125"),
        ("lang", "0002_auto_20190516_1245"),
    ]

    operations = [
        migrations.CreateModel(
            name="Font",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "family",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Font family"
                    ),
                ),
                (
                    "style",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Font style"
                    ),
                ),
                (
                    "font",
                    models.FileField(
                        help_text="OpenType and TrueType fonts are supported.",
                        storage=django.core.files.storage.FileSystemStorage(
                            location=data_dir("fonts")
                        ),
                        upload_to="",
                        validators=[weblate.fonts.validators.validate_font],
                        verbose_name="Font file",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="trans.Project"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"unique_together": {("family", "style", "project")}},
            bases=(models.Model, weblate.trans.mixins.UserDisplayMixin),
        ),
        migrations.CreateModel(
            name="FontGroup",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.SlugField(
                        help_text="Identifier you will use in checks to select this font group. Avoid whitespace or special chars.",
                        max_length=100,
                        verbose_name="Font group name",
                    ),
                ),
                (
                    "font",
                    models.ForeignKey(
                        help_text="Default font is used unless per language override matches.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fonts.Font",
                        verbose_name="Default font",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="trans.Project"
                    ),
                ),
            ],
            options={"unique_together": {("name", "project")}},
        ),
        migrations.CreateModel(
            name="FontOverride",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "font",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fonts.Font",
                        verbose_name="Font",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fonts.FontGroup",
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lang.Language",
                        verbose_name="Language",
                    ),
                ),
            ],
            options={"unique_together": {("group", "language")}},
        ),
    ]
