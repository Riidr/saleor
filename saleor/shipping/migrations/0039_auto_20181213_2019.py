# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-13 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0038_auto_20181213_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingmethodcountry',
            name='country_code',
            field=models.CharField(blank=True, choices=[('', 'Any country'), ('ES', 'Spain'), ('CW', 'Curaçao'), ('CA', 'Canada'), ('CK', 'Cook Islands'), ('ZM', 'Zambia'), ('ET', 'Ethiopia'), ('VC', 'Saint Vincent and the Grenadines'), ('SJ', 'Svalbard and Jan Mayen'), ('NE', 'Niger'), ('CY', 'Cyprus'), ('PT', 'Portugal'), ('AS', 'American Samoa'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('GI', 'Gibraltar'), ('MZ', 'Mozambique'), ('BW', 'Botswana'), ('TJ', 'Tajikistan'), ('PK', 'Pakistan'), ('MQ', 'Martinique'), ('SD', 'Sudan'), ('CH', 'Switzerland'), ('GU', 'Guam'), ('HK', 'Hong Kong'), ('SY', 'Syrian Arab Republic'), ('LB', 'Lebanon'), ('DE', 'Germany'), ('ST', 'Sao Tome and Principe'), ('LV', 'Latvia'), ('UM', 'United States Minor Outlying Islands'), ('GL', 'Greenland'), ('CV', 'Cabo Verde'), ('MP', 'Northern Mariana Islands'), ('SK', 'Slovakia'), ('TN', 'Tunisia'), ('AM', 'Armenia'), ('TV', 'Tuvalu'), ('AX', 'Åland Islands'), ('TM', 'Turkmenistan'), ('GT', 'Guatemala'), ('HT', 'Haiti'), ('HM', 'Heard Island and McDonald Islands'), ('RU', 'Russian Federation'), ('SI', 'Slovenia'), ('BM', 'Bermuda'), ('WF', 'Wallis and Futuna'), ('MS', 'Montserrat'), ('GW', 'Guinea-Bissau'), ('AZ', 'Azerbaijan'), ('IN', 'India'), ('JE', 'Jersey'), ('AR', 'Argentina'), ('TG', 'Togo'), ('IT', 'Italy'), ('PR', 'Puerto Rico'), ('IM', 'Isle of Man'), ('US', 'United States of America'), ('LT', 'Lithuania'), ('VI', 'Virgin Islands (U.S.)'), ('BO', 'Bolivia (Plurinational State of)'), ('YE', 'Yemen'), ('GF', 'French Guiana'), ('FJ', 'Fiji'), ('DZ', 'Algeria'), ('BH', 'Bahrain'), ('KM', 'Comoros'), ('NO', 'Norway'), ('TF', 'French Southern Territories'), ('BG', 'Bulgaria'), ('SL', 'Sierra Leone'), ('SZ', 'Swaziland'), ('IS', 'Iceland'), ('GQ', 'Equatorial Guinea'), ('GP', 'Guadeloupe'), ('BB', 'Barbados'), ('MA', 'Morocco'), ('CC', 'Cocos (Keeling) Islands'), ('JP', 'Japan'), ('MC', 'Monaco'), ('KG', 'Kyrgyzstan'), ('TT', 'Trinidad and Tobago'), ('NU', 'Niue'), ('LK', 'Sri Lanka'), ('VG', 'Virgin Islands (British)'), ('TR', 'Turkey'), ('CN', 'China'), ('PS', 'Palestine, State of'), ('NR', 'Nauru'), ('EC', 'Ecuador'), ('FM', 'Micronesia (Federated States of)'), ('AQ', 'Antarctica'), ('TD', 'Chad'), ('MU', 'Mauritius'), ('FR', 'France'), ('CZ', 'Czechia'), ('AF', 'Afghanistan'), ('GM', 'Gambia'), ('GY', 'Guyana'), ('TC', 'Turks and Caicos Islands'), ('MW', 'Malawi'), ('LC', 'Saint Lucia'), ('SG', 'Singapore'), ('BR', 'Brazil'), ('JO', 'Jordan'), ('BS', 'Bahamas'), ('LS', 'Lesotho'), ('SS', 'South Sudan'), ('KY', 'Cayman Islands'), ('NF', 'Norfolk Island'), ('LR', 'Liberia'), ('TK', 'Tokelau'), ('TH', 'Thailand'), ('HU', 'Hungary'), ('OM', 'Oman'), ('BD', 'Bangladesh'), ('MX', 'Mexico'), ('MD', 'Moldova (the Republic of)'), ('NL', 'Netherlands'), ('GA', 'Gabon'), ('RS', 'Serbia'), ('ZA', 'South Africa'), ('FI', 'Finland'), ('RE', 'Réunion'), ('GS', 'South Georgia and the South Sandwich Islands'), ('PA', 'Panama'), ('MO', 'Macao'), ('SB', 'Solomon Islands'), ('AE', 'United Arab Emirates'), ('QA', 'Qatar'), ('KH', 'Cambodia'), ('GG', 'Guernsey'), ('PN', 'Pitcairn'), ('SN', 'Senegal'), ('AG', 'Antigua and Barbuda'), ('BI', 'Burundi'), ('BF', 'Burkina Faso'), ('FO', 'Faroe Islands'), ('DK', 'Denmark'), ('EG', 'Egypt'), ('PM', 'Saint Pierre and Miquelon'), ('NA', 'Namibia'), ('IL', 'Israel'), ('LY', 'Libya'), ('KW', 'Kuwait'), ('RW', 'Rwanda'), ('SO', 'Somalia'), ('BZ', 'Belize'), ('SX', 'Sint Maarten (Dutch part)'), ('CR', 'Costa Rica'), ('TL', 'Timor-Leste'), ('SE', 'Sweden'), ('PY', 'Paraguay'), ('CU', 'Cuba'), ('EE', 'Estonia'), ('BJ', 'Benin'), ('BE', 'Belgium'), ('KN', 'Saint Kitts and Nevis'), ('BT', 'Bhutan'), ('CD', 'Congo (the Democratic Republic of the)'), ('KZ', 'Kazakhstan'), ('BA', 'Bosnia and Herzegovina'), ('AW', 'Aruba'), ('TO', 'Tonga'), ('MY', 'Malaysia'), ('KI', 'Kiribati'), ('KE', 'Kenya'), ('DO', 'Dominican Republic'), ('UZ', 'Uzbekistan'), ('WS', 'Samoa'), ('AI', 'Anguilla'), ('JM', 'Jamaica'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('CM', 'Cameroon'), ('AD', 'Andorra'), ('PH', 'Philippines'), ('PG', 'Papua New Guinea'), ('ME', 'Montenegro'), ('BY', 'Belarus'), ('UG', 'Uganda'), ('EH', 'Western Sahara'), ('PF', 'French Polynesia'), ('BN', 'Brunei Darussalam'), ('IO', 'British Indian Ocean Territory'), ('VU', 'Vanuatu'), ('CI', "Côte d'Ivoire"), ('CF', 'Central African Republic'), ('MN', 'Mongolia'), ('MF', 'Saint Martin (French part)'), ('ML', 'Mali'), ('MV', 'Maldives'), ('ID', 'Indonesia'), ('KR', 'Korea (the Republic of)'), ('IQ', 'Iraq'), ('MH', 'Marshall Islands'), ('NC', 'New Caledonia'), ('LI', 'Liechtenstein'), ('LA', "Lao People's Democratic Republic"), ('DJ', 'Djibouti'), ('VN', 'Viet Nam'), ('CG', 'Congo'), ('TW', 'Taiwan (Province of China)'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('CL', 'Chile'), ('MG', 'Madagascar'), ('DM', 'Dominica'), ('GE', 'Georgia'), ('NG', 'Nigeria'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('LU', 'Luxembourg'), ('VA', 'Holy See'), ('PL', 'Poland'), ('GD', 'Grenada'), ('NI', 'Nicaragua'), ('UA', 'Ukraine'), ('AO', 'Angola'), ('SM', 'San Marino'), ('TZ', 'Tanzania, United Republic of'), ('NP', 'Nepal'), ('HN', 'Honduras'), ('RO', 'Romania'), ('AL', 'Albania'), ('BL', 'Saint Barthélemy'), ('YT', 'Mayotte'), ('GH', 'Ghana'), ('AT', 'Austria'), ('SA', 'Saudi Arabia'), ('AU', 'Australia'), ('ZW', 'Zimbabwe'), ('MM', 'Myanmar'), ('MT', 'Malta'), ('MR', 'Mauritania'), ('BV', 'Bouvet Island'), ('ER', 'Eritrea'), ('IR', 'Iran (Islamic Republic of)'), ('NZ', 'New Zealand'), ('CO', 'Colombia'), ('PE', 'Peru'), ('SV', 'El Salvador'), ('UY', 'Uruguay'), ('GN', 'Guinea'), ('IE', 'Ireland'), ('PW', 'Palau'), ('KP', "Korea (the Democratic People's Republic of)"), ('HR', 'Croatia'), ('CX', 'Christmas Island'), ('SC', 'Seychelles'), ('SR', 'Suriname'), ('GR', 'Greece'), ('FK', 'Falkland Islands  [Malvinas]')], default='', max_length=2),
        ),
    ]