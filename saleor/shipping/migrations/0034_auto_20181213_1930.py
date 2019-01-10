# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-13 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0033_auto_20181213_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingmethodcountry',
            name='country_code',
            field=models.CharField(blank=True, choices=[('', 'Any country'), ('CR', 'Costa Rica'), ('KM', 'Comoros'), ('SA', 'Saudi Arabia'), ('SI', 'Slovenia'), ('TJ', 'Tajikistan'), ('BJ', 'Benin'), ('ML', 'Mali'), ('AX', 'Åland Islands'), ('BM', 'Bermuda'), ('TK', 'Tokelau'), ('KH', 'Cambodia'), ('UM', 'United States Minor Outlying Islands'), ('KZ', 'Kazakhstan'), ('NP', 'Nepal'), ('PF', 'French Polynesia'), ('CN', 'China'), ('VN', 'Viet Nam'), ('CD', 'Congo (the Democratic Republic of the)'), ('HR', 'Croatia'), ('CY', 'Cyprus'), ('DE', 'Germany'), ('CM', 'Cameroon'), ('IN', 'India'), ('EG', 'Egypt'), ('DM', 'Dominica'), ('FK', 'Falkland Islands  [Malvinas]'), ('PL', 'Poland'), ('SZ', 'Swaziland'), ('IL', 'Israel'), ('BA', 'Bosnia and Herzegovina'), ('EC', 'Ecuador'), ('HM', 'Heard Island and McDonald Islands'), ('LS', 'Lesotho'), ('RW', 'Rwanda'), ('ES', 'Spain'), ('ID', 'Indonesia'), ('BV', 'Bouvet Island'), ('RS', 'Serbia'), ('KE', 'Kenya'), ('CZ', 'Czechia'), ('NG', 'Nigeria'), ('GD', 'Grenada'), ('SY', 'Syrian Arab Republic'), ('CH', 'Switzerland'), ('KI', 'Kiribati'), ('GP', 'Guadeloupe'), ('HU', 'Hungary'), ('CO', 'Colombia'), ('JP', 'Japan'), ('AQ', 'Antarctica'), ('UA', 'Ukraine'), ('SV', 'El Salvador'), ('MD', 'Moldova (the Republic of)'), ('BR', 'Brazil'), ('MZ', 'Mozambique'), ('TW', 'Taiwan (Province of China)'), ('VI', 'Virgin Islands (U.S.)'), ('WS', 'Samoa'), ('VA', 'Holy See'), ('BT', 'Bhutan'), ('ST', 'Sao Tome and Principe'), ('CG', 'Congo'), ('AL', 'Albania'), ('TN', 'Tunisia'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('LT', 'Lithuania'), ('LR', 'Liberia'), ('ER', 'Eritrea'), ('BL', 'Saint Barthélemy'), ('AE', 'United Arab Emirates'), ('GT', 'Guatemala'), ('SG', 'Singapore'), ('IS', 'Iceland'), ('PT', 'Portugal'), ('GI', 'Gibraltar'), ('EE', 'Estonia'), ('AD', 'Andorra'), ('BI', 'Burundi'), ('ZM', 'Zambia'), ('NC', 'New Caledonia'), ('BN', 'Brunei Darussalam'), ('RU', 'Russian Federation'), ('AR', 'Argentina'), ('DJ', 'Djibouti'), ('ZW', 'Zimbabwe'), ('MM', 'Myanmar'), ('PM', 'Saint Pierre and Miquelon'), ('PS', 'Palestine, State of'), ('TR', 'Turkey'), ('SL', 'Sierra Leone'), ('AW', 'Aruba'), ('FR', 'France'), ('SB', 'Solomon Islands'), ('IR', 'Iran (Islamic Republic of)'), ('LU', 'Luxembourg'), ('CF', 'Central African Republic'), ('MA', 'Morocco'), ('TZ', 'Tanzania, United Republic of'), ('SM', 'San Marino'), ('UG', 'Uganda'), ('PR', 'Puerto Rico'), ('CA', 'Canada'), ('BW', 'Botswana'), ('OM', 'Oman'), ('PW', 'Palau'), ('TO', 'Tonga'), ('VG', 'Virgin Islands (British)'), ('QA', 'Qatar'), ('LK', 'Sri Lanka'), ('TH', 'Thailand'), ('MU', 'Mauritius'), ('TV', 'Tuvalu'), ('KP', "Korea (the Democratic People's Republic of)"), ('SN', 'Senegal'), ('JM', 'Jamaica'), ('SC', 'Seychelles'), ('LB', 'Lebanon'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('RO', 'Romania'), ('PE', 'Peru'), ('GS', 'South Georgia and the South Sandwich Islands'), ('SS', 'South Sudan'), ('WF', 'Wallis and Futuna'), ('FO', 'Faroe Islands'), ('AM', 'Armenia'), ('CW', 'Curaçao'), ('TL', 'Timor-Leste'), ('ET', 'Ethiopia'), ('GW', 'Guinea-Bissau'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('PA', 'Panama'), ('CX', 'Christmas Island'), ('LI', 'Liechtenstein'), ('MV', 'Maldives'), ('TD', 'Chad'), ('MN', 'Mongolia'), ('YE', 'Yemen'), ('AZ', 'Azerbaijan'), ('BZ', 'Belize'), ('DO', 'Dominican Republic'), ('AU', 'Australia'), ('EH', 'Western Sahara'), ('PG', 'Papua New Guinea'), ('BO', 'Bolivia (Plurinational State of)'), ('IE', 'Ireland'), ('HT', 'Haiti'), ('LV', 'Latvia'), ('CU', 'Cuba'), ('BE', 'Belgium'), ('JO', 'Jordan'), ('KR', 'Korea (the Republic of)'), ('CI', "Côte d'Ivoire"), ('FM', 'Micronesia (Federated States of)'), ('SE', 'Sweden'), ('BH', 'Bahrain'), ('TF', 'French Southern Territories'), ('GE', 'Georgia'), ('NI', 'Nicaragua'), ('MG', 'Madagascar'), ('GL', 'Greenland'), ('AS', 'American Samoa'), ('AF', 'Afghanistan'), ('BS', 'Bahamas'), ('MX', 'Mexico'), ('IM', 'Isle of Man'), ('GQ', 'Equatorial Guinea'), ('LY', 'Libya'), ('AG', 'Antigua and Barbuda'), ('SR', 'Suriname'), ('UZ', 'Uzbekistan'), ('MQ', 'Martinique'), ('KY', 'Cayman Islands'), ('CL', 'Chile'), ('BY', 'Belarus'), ('GM', 'Gambia'), ('MF', 'Saint Martin (French part)'), ('BB', 'Barbados'), ('FI', 'Finland'), ('GY', 'Guyana'), ('TG', 'Togo'), ('NL', 'Netherlands'), ('UY', 'Uruguay'), ('SJ', 'Svalbard and Jan Mayen'), ('CV', 'Cabo Verde'), ('ME', 'Montenegro'), ('JE', 'Jersey'), ('MS', 'Montserrat'), ('MT', 'Malta'), ('CC', 'Cocos (Keeling) Islands'), ('AI', 'Anguilla'), ('GU', 'Guam'), ('RE', 'Réunion'), ('HK', 'Hong Kong'), ('ZA', 'South Africa'), ('NU', 'Niue'), ('SK', 'Slovakia'), ('GF', 'French Guiana'), ('SD', 'Sudan'), ('VU', 'Vanuatu'), ('AT', 'Austria'), ('TM', 'Turkmenistan'), ('SO', 'Somalia'), ('TC', 'Turks and Caicos Islands'), ('GN', 'Guinea'), ('KG', 'Kyrgyzstan'), ('AO', 'Angola'), ('VC', 'Saint Vincent and the Grenadines'), ('SX', 'Sint Maarten (Dutch part)'), ('IO', 'British Indian Ocean Territory'), ('NZ', 'New Zealand'), ('YT', 'Mayotte'), ('DK', 'Denmark'), ('GA', 'Gabon'), ('KW', 'Kuwait'), ('IQ', 'Iraq'), ('GR', 'Greece'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('MP', 'Northern Mariana Islands'), ('GH', 'Ghana'), ('NA', 'Namibia'), ('BF', 'Burkina Faso'), ('TT', 'Trinidad and Tobago'), ('PY', 'Paraguay'), ('MR', 'Mauritania'), ('US', 'United States of America'), ('PH', 'Philippines'), ('NF', 'Norfolk Island'), ('MH', 'Marshall Islands'), ('HN', 'Honduras'), ('MY', 'Malaysia'), ('MC', 'Monaco'), ('FJ', 'Fiji'), ('IT', 'Italy'), ('CK', 'Cook Islands'), ('MW', 'Malawi'), ('MO', 'Macao'), ('BG', 'Bulgaria'), ('GG', 'Guernsey'), ('PK', 'Pakistan'), ('NO', 'Norway'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('DZ', 'Algeria'), ('NR', 'Nauru'), ('BD', 'Bangladesh'), ('PN', 'Pitcairn'), ('LA', "Lao People's Democratic Republic"), ('NE', 'Niger')], default='', max_length=2),
        ),
    ]
