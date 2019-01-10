# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-13 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0030_auto_20181213_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingmethodcountry',
            name='country_code',
            field=models.CharField(blank=True, choices=[('', 'Any country'), ('TD', 'Chad'), ('PF', 'French Polynesia'), ('BJ', 'Benin'), ('MS', 'Montserrat'), ('DO', 'Dominican Republic'), ('CC', 'Cocos (Keeling) Islands'), ('CL', 'Chile'), ('GM', 'Gambia'), ('NC', 'New Caledonia'), ('GA', 'Gabon'), ('SB', 'Solomon Islands'), ('CD', 'Congo (the Democratic Republic of the)'), ('GE', 'Georgia'), ('MH', 'Marshall Islands'), ('DK', 'Denmark'), ('KY', 'Cayman Islands'), ('CG', 'Congo'), ('VG', 'Virgin Islands (British)'), ('TR', 'Turkey'), ('IQ', 'Iraq'), ('PE', 'Peru'), ('MC', 'Monaco'), ('GN', 'Guinea'), ('RO', 'Romania'), ('VU', 'Vanuatu'), ('CF', 'Central African Republic'), ('GG', 'Guernsey'), ('JO', 'Jordan'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('MZ', 'Mozambique'), ('CA', 'Canada'), ('PG', 'Papua New Guinea'), ('SV', 'El Salvador'), ('UY', 'Uruguay'), ('SX', 'Sint Maarten (Dutch part)'), ('PT', 'Portugal'), ('GD', 'Grenada'), ('FJ', 'Fiji'), ('AZ', 'Azerbaijan'), ('GR', 'Greece'), ('LR', 'Liberia'), ('BS', 'Bahamas'), ('GF', 'French Guiana'), ('YE', 'Yemen'), ('PN', 'Pitcairn'), ('SN', 'Senegal'), ('GP', 'Guadeloupe'), ('MR', 'Mauritania'), ('TV', 'Tuvalu'), ('MM', 'Myanmar'), ('CV', 'Cabo Verde'), ('TW', 'Taiwan (Province of China)'), ('ET', 'Ethiopia'), ('KN', 'Saint Kitts and Nevis'), ('BF', 'Burkina Faso'), ('SZ', 'Swaziland'), ('AL', 'Albania'), ('NU', 'Niue'), ('EH', 'Western Sahara'), ('MY', 'Malaysia'), ('BT', 'Bhutan'), ('SM', 'San Marino'), ('BY', 'Belarus'), ('TM', 'Turkmenistan'), ('AW', 'Aruba'), ('NA', 'Namibia'), ('TK', 'Tokelau'), ('SD', 'Sudan'), ('PL', 'Poland'), ('IN', 'India'), ('WS', 'Samoa'), ('SC', 'Seychelles'), ('PK', 'Pakistan'), ('UM', 'United States Minor Outlying Islands'), ('AU', 'Australia'), ('HM', 'Heard Island and McDonald Islands'), ('PR', 'Puerto Rico'), ('BB', 'Barbados'), ('RS', 'Serbia'), ('AM', 'Armenia'), ('JM', 'Jamaica'), ('NO', 'Norway'), ('MW', 'Malawi'), ('SJ', 'Svalbard and Jan Mayen'), ('VA', 'Holy See'), ('ER', 'Eritrea'), ('CR', 'Costa Rica'), ('KZ', 'Kazakhstan'), ('FR', 'France'), ('CX', 'Christmas Island'), ('IS', 'Iceland'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('NE', 'Niger'), ('MN', 'Mongolia'), ('TN', 'Tunisia'), ('LY', 'Libya'), ('BE', 'Belgium'), ('PY', 'Paraguay'), ('QA', 'Qatar'), ('LK', 'Sri Lanka'), ('MO', 'Macao'), ('NZ', 'New Zealand'), ('CM', 'Cameroon'), ('IT', 'Italy'), ('MD', 'Moldova (the Republic of)'), ('NG', 'Nigeria'), ('JE', 'Jersey'), ('UZ', 'Uzbekistan'), ('EG', 'Egypt'), ('LS', 'Lesotho'), ('KI', 'Kiribati'), ('TF', 'French Southern Territories'), ('HU', 'Hungary'), ('EC', 'Ecuador'), ('PS', 'Palestine, State of'), ('AE', 'United Arab Emirates'), ('AT', 'Austria'), ('ME', 'Montenegro'), ('SR', 'Suriname'), ('BR', 'Brazil'), ('NL', 'Netherlands'), ('TH', 'Thailand'), ('TT', 'Trinidad and Tobago'), ('SG', 'Singapore'), ('ZM', 'Zambia'), ('RU', 'Russian Federation'), ('MV', 'Maldives'), ('VN', 'Viet Nam'), ('UG', 'Uganda'), ('GU', 'Guam'), ('DE', 'Germany'), ('UA', 'Ukraine'), ('HK', 'Hong Kong'), ('IR', 'Iran (Islamic Republic of)'), ('GL', 'Greenland'), ('US', 'United States of America'), ('LU', 'Luxembourg'), ('MQ', 'Martinique'), ('ZW', 'Zimbabwe'), ('PA', 'Panama'), ('AX', 'Åland Islands'), ('IO', 'British Indian Ocean Territory'), ('CI', "Côte d'Ivoire"), ('IE', 'Ireland'), ('GH', 'Ghana'), ('MF', 'Saint Martin (French part)'), ('CO', 'Colombia'), ('JP', 'Japan'), ('KG', 'Kyrgyzstan'), ('HR', 'Croatia'), ('ES', 'Spain'), ('LC', 'Saint Lucia'), ('AF', 'Afghanistan'), ('AR', 'Argentina'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('KP', "Korea (the Democratic People's Republic of)"), ('BZ', 'Belize'), ('BW', 'Botswana'), ('BD', 'Bangladesh'), ('KR', 'Korea (the Republic of)'), ('RW', 'Rwanda'), ('AO', 'Angola'), ('TL', 'Timor-Leste'), ('TO', 'Tonga'), ('LT', 'Lithuania'), ('FM', 'Micronesia (Federated States of)'), ('GI', 'Gibraltar'), ('AS', 'American Samoa'), ('MT', 'Malta'), ('ML', 'Mali'), ('GW', 'Guinea-Bissau'), ('BI', 'Burundi'), ('SS', 'South Sudan'), ('BH', 'Bahrain'), ('PM', 'Saint Pierre and Miquelon'), ('YT', 'Mayotte'), ('NP', 'Nepal'), ('SL', 'Sierra Leone'), ('IM', 'Isle of Man'), ('BG', 'Bulgaria'), ('SA', 'Saudi Arabia'), ('TG', 'Togo'), ('RE', 'Réunion'), ('BA', 'Bosnia and Herzegovina'), ('LI', 'Liechtenstein'), ('SO', 'Somalia'), ('BO', 'Bolivia (Plurinational State of)'), ('PH', 'Philippines'), ('SK', 'Slovakia'), ('LA', "Lao People's Democratic Republic"), ('GT', 'Guatemala'), ('AQ', 'Antarctica'), ('ST', 'Sao Tome and Principe'), ('TJ', 'Tajikistan'), ('CW', 'Curaçao'), ('KM', 'Comoros'), ('BM', 'Bermuda'), ('TC', 'Turks and Caicos Islands'), ('AG', 'Antigua and Barbuda'), ('KW', 'Kuwait'), ('GQ', 'Equatorial Guinea'), ('MX', 'Mexico'), ('MP', 'Northern Mariana Islands'), ('DM', 'Dominica'), ('KE', 'Kenya'), ('FK', 'Falkland Islands  [Malvinas]'), ('VI', 'Virgin Islands (U.S.)'), ('BN', 'Brunei Darussalam'), ('VC', 'Saint Vincent and the Grenadines'), ('SE', 'Sweden'), ('HN', 'Honduras'), ('GS', 'South Georgia and the South Sandwich Islands'), ('WF', 'Wallis and Futuna'), ('DZ', 'Algeria'), ('NF', 'Norfolk Island'), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('MU', 'Mauritius'), ('SI', 'Slovenia'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('AI', 'Anguilla'), ('OM', 'Oman'), ('CK', 'Cook Islands'), ('CZ', 'Czechia'), ('AD', 'Andorra'), ('BV', 'Bouvet Island'), ('SY', 'Syrian Arab Republic'), ('CN', 'China'), ('NR', 'Nauru'), ('CU', 'Cuba'), ('PW', 'Palau'), ('CY', 'Cyprus'), ('CH', 'Switzerland'), ('ID', 'Indonesia'), ('NI', 'Nicaragua'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('MG', 'Madagascar'), ('BL', 'Saint Barthélemy'), ('GY', 'Guyana'), ('KH', 'Cambodia'), ('TZ', 'Tanzania, United Republic of'), ('DJ', 'Djibouti'), ('FI', 'Finland'), ('MA', 'Morocco'), ('ZA', 'South Africa'), ('HT', 'Haiti'), ('IL', 'Israel'), ('FO', 'Faroe Islands'), ('EE', 'Estonia')], default='', max_length=2),
        ),
    ]
