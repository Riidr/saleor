# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-13 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0031_auto_20181213_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingmethodcountry',
            name='country_code',
            field=models.CharField(blank=True, choices=[('', 'Any country'), ('RU', 'Russian Federation'), ('PT', 'Portugal'), ('PW', 'Palau'), ('PM', 'Saint Pierre and Miquelon'), ('ER', 'Eritrea'), ('MZ', 'Mozambique'), ('LK', 'Sri Lanka'), ('IE', 'Ireland'), ('CF', 'Central African Republic'), ('CU', 'Cuba'), ('LC', 'Saint Lucia'), ('NL', 'Netherlands'), ('ES', 'Spain'), ('GQ', 'Equatorial Guinea'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('BL', 'Saint Barthélemy'), ('UA', 'Ukraine'), ('GP', 'Guadeloupe'), ('BV', 'Bouvet Island'), ('UZ', 'Uzbekistan'), ('BD', 'Bangladesh'), ('AL', 'Albania'), ('MT', 'Malta'), ('MM', 'Myanmar'), ('TH', 'Thailand'), ('PR', 'Puerto Rico'), ('AS', 'American Samoa'), ('PK', 'Pakistan'), ('NU', 'Niue'), ('KE', 'Kenya'), ('EC', 'Ecuador'), ('AO', 'Angola'), ('CM', 'Cameroon'), ('CZ', 'Czechia'), ('PN', 'Pitcairn'), ('BO', 'Bolivia (Plurinational State of)'), ('SY', 'Syrian Arab Republic'), ('CH', 'Switzerland'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('MO', 'Macao'), ('FM', 'Micronesia (Federated States of)'), ('MH', 'Marshall Islands'), ('FJ', 'Fiji'), ('CN', 'China'), ('SG', 'Singapore'), ('NG', 'Nigeria'), ('SL', 'Sierra Leone'), ('FK', 'Falkland Islands  [Malvinas]'), ('MD', 'Moldova (the Republic of)'), ('KM', 'Comoros'), ('KG', 'Kyrgyzstan'), ('AT', 'Austria'), ('TD', 'Chad'), ('LU', 'Luxembourg'), ('NP', 'Nepal'), ('VI', 'Virgin Islands (U.S.)'), ('BW', 'Botswana'), ('AQ', 'Antarctica'), ('KR', 'Korea (the Republic of)'), ('DM', 'Dominica'), ('ID', 'Indonesia'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('GI', 'Gibraltar'), ('GG', 'Guernsey'), ('GD', 'Grenada'), ('TT', 'Trinidad and Tobago'), ('ME', 'Montenegro'), ('AG', 'Antigua and Barbuda'), ('TM', 'Turkmenistan'), ('HM', 'Heard Island and McDonald Islands'), ('IT', 'Italy'), ('TV', 'Tuvalu'), ('SE', 'Sweden'), ('QA', 'Qatar'), ('UY', 'Uruguay'), ('CD', 'Congo (the Democratic Republic of the)'), ('US', 'United States of America'), ('SR', 'Suriname'), ('TK', 'Tokelau'), ('TR', 'Turkey'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('VU', 'Vanuatu'), ('SZ', 'Swaziland'), ('RS', 'Serbia'), ('CA', 'Canada'), ('LI', 'Liechtenstein'), ('ST', 'Sao Tome and Principe'), ('HT', 'Haiti'), ('IL', 'Israel'), ('BT', 'Bhutan'), ('EH', 'Western Sahara'), ('NI', 'Nicaragua'), ('MQ', 'Martinique'), ('SC', 'Seychelles'), ('AM', 'Armenia'), ('SO', 'Somalia'), ('BI', 'Burundi'), ('NZ', 'New Zealand'), ('UG', 'Uganda'), ('JO', 'Jordan'), ('TG', 'Togo'), ('GU', 'Guam'), ('GF', 'French Guiana'), ('KP', "Korea (the Democratic People's Republic of)"), ('NO', 'Norway'), ('VG', 'Virgin Islands (British)'), ('CG', 'Congo'), ('NR', 'Nauru'), ('PG', 'Papua New Guinea'), ('TW', 'Taiwan (Province of China)'), ('MF', 'Saint Martin (French part)'), ('BG', 'Bulgaria'), ('BY', 'Belarus'), ('AD', 'Andorra'), ('PS', 'Palestine, State of'), ('DK', 'Denmark'), ('ZA', 'South Africa'), ('DJ', 'Djibouti'), ('ET', 'Ethiopia'), ('SN', 'Senegal'), ('MW', 'Malawi'), ('HK', 'Hong Kong'), ('BA', 'Bosnia and Herzegovina'), ('OM', 'Oman'), ('WF', 'Wallis and Futuna'), ('GE', 'Georgia'), ('MP', 'Northern Mariana Islands'), ('GT', 'Guatemala'), ('SK', 'Slovakia'), ('GW', 'Guinea-Bissau'), ('CI', "Côte d'Ivoire"), ('RO', 'Romania'), ('TC', 'Turks and Caicos Islands'), ('MX', 'Mexico'), ('MR', 'Mauritania'), ('CX', 'Christmas Island'), ('PH', 'Philippines'), ('FO', 'Faroe Islands'), ('MU', 'Mauritius'), ('ZW', 'Zimbabwe'), ('LA', "Lao People's Democratic Republic"), ('SI', 'Slovenia'), ('PL', 'Poland'), ('DE', 'Germany'), ('RW', 'Rwanda'), ('MA', 'Morocco'), ('IS', 'Iceland'), ('KH', 'Cambodia'), ('AE', 'United Arab Emirates'), ('SD', 'Sudan'), ('GS', 'South Georgia and the South Sandwich Islands'), ('AF', 'Afghanistan'), ('BR', 'Brazil'), ('SB', 'Solomon Islands'), ('CK', 'Cook Islands'), ('GM', 'Gambia'), ('IR', 'Iran (Islamic Republic of)'), ('EG', 'Egypt'), ('FI', 'Finland'), ('MY', 'Malaysia'), ('GL', 'Greenland'), ('KW', 'Kuwait'), ('BM', 'Bermuda'), ('TJ', 'Tajikistan'), ('BS', 'Bahamas'), ('AW', 'Aruba'), ('ML', 'Mali'), ('EE', 'Estonia'), ('MV', 'Maldives'), ('SX', 'Sint Maarten (Dutch part)'), ('VN', 'Viet Nam'), ('PE', 'Peru'), ('CC', 'Cocos (Keeling) Islands'), ('TF', 'French Southern Territories'), ('SM', 'San Marino'), ('WS', 'Samoa'), ('MN', 'Mongolia'), ('TO', 'Tonga'), ('IQ', 'Iraq'), ('BF', 'Burkina Faso'), ('CY', 'Cyprus'), ('GH', 'Ghana'), ('FR', 'France'), ('GR', 'Greece'), ('IO', 'British Indian Ocean Territory'), ('SS', 'South Sudan'), ('LV', 'Latvia'), ('LT', 'Lithuania'), ('PY', 'Paraguay'), ('GN', 'Guinea'), ('BE', 'Belgium'), ('YE', 'Yemen'), ('SA', 'Saudi Arabia'), ('PF', 'French Polynesia'), ('VC', 'Saint Vincent and the Grenadines'), ('HR', 'Croatia'), ('HU', 'Hungary'), ('DO', 'Dominican Republic'), ('BN', 'Brunei Darussalam'), ('CV', 'Cabo Verde'), ('GY', 'Guyana'), ('BB', 'Barbados'), ('NF', 'Norfolk Island'), ('YT', 'Mayotte'), ('MC', 'Monaco'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('UM', 'United States Minor Outlying Islands'), ('KZ', 'Kazakhstan'), ('KY', 'Cayman Islands'), ('LS', 'Lesotho'), ('NE', 'Niger'), ('SV', 'El Salvador'), ('IN', 'India'), ('AX', 'Åland Islands'), ('PA', 'Panama'), ('TN', 'Tunisia'), ('CR', 'Costa Rica'), ('CL', 'Chile'), ('KI', 'Kiribati'), ('SJ', 'Svalbard and Jan Mayen'), ('AR', 'Argentina'), ('RE', 'Réunion'), ('LY', 'Libya'), ('CW', 'Curaçao'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('IM', 'Isle of Man'), ('NA', 'Namibia'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('LB', 'Lebanon'), ('NC', 'New Caledonia'), ('MG', 'Madagascar'), ('KN', 'Saint Kitts and Nevis'), ('TZ', 'Tanzania, United Republic of'), ('CO', 'Colombia'), ('AU', 'Australia'), ('HN', 'Honduras'), ('AI', 'Anguilla'), ('LR', 'Liberia'), ('JE', 'Jersey'), ('TL', 'Timor-Leste'), ('MS', 'Montserrat'), ('ZM', 'Zambia'), ('BH', 'Bahrain'), ('VA', 'Holy See'), ('GA', 'Gabon'), ('DZ', 'Algeria'), ('AZ', 'Azerbaijan')], default='', max_length=2),
        ),
    ]