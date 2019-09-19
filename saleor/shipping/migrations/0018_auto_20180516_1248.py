# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-05-16 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0017_auto_20180516_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingmethodcountry',
            name='country_code',
            field=models.CharField(blank=True, choices=[('', 'Any country'), ('EC', 'Ecuador'), ('BA', 'Bosnia and Herzegovina'), ('KW', 'Kuwait'), ('RO', 'Romania'), ('FR', 'France'), ('IS', 'Iceland'), ('BO', 'Bolivia (Plurinational State of)'), ('AD', 'Andorra'), ('MA', 'Morocco'), ('HR', 'Croatia'), ('KE', 'Kenya'), ('SN', 'Senegal'), ('DE', 'Germany'), ('HK', 'Hong Kong'), ('AG', 'Antigua and Barbuda'), ('CX', 'Christmas Island'), ('AQ', 'Antarctica'), ('LR', 'Liberia'), ('IE', 'Ireland'), ('MD', 'Moldova (the Republic of)'), ('CI', "Côte d'Ivoire"), ('SX', 'Sint Maarten (Dutch part)'), ('GP', 'Guadeloupe'), ('BS', 'Bahamas'), ('AE', 'United Arab Emirates'), ('JO', 'Jordan'), ('UZ', 'Uzbekistan'), ('CG', 'Congo'), ('LA', "Lao People's Democratic Republic"), ('BJ', 'Benin'), ('PG', 'Papua New Guinea'), ('GR', 'Greece'), ('EG', 'Egypt'), ('JE', 'Jersey'), ('IR', 'Iran (Islamic Republic of)'), ('NO', 'Norway'), ('TK', 'Tokelau'), ('ET', 'Ethiopia'), ('TJ', 'Tajikistan'), ('PF', 'French Polynesia'), ('IT', 'Italy'), ('GH', 'Ghana'), ('IN', 'India'), ('BD', 'Bangladesh'), ('TD', 'Chad'), ('UY', 'Uruguay'), ('NF', 'Norfolk Island'), ('MR', 'Mauritania'), ('SD', 'Sudan'), ('SO', 'Somalia'), ('AF', 'Afghanistan'), ('NU', 'Niue'), ('ER', 'Eritrea'), ('GU', 'Guam'), ('VI', 'Virgin Islands (U.S.)'), ('MQ', 'Martinique'), ('BG', 'Bulgaria'), ('CA', 'Canada'), ('VG', 'Virgin Islands (British)'), ('UM', 'United States Minor Outlying Islands'), ('GL', 'Greenland'), ('CR', 'Costa Rica'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('SC', 'Seychelles'), ('YE', 'Yemen'), ('DM', 'Dominica'), ('TO', 'Tonga'), ('BN', 'Brunei Darussalam'), ('RU', 'Russian Federation'), ('SA', 'Saudi Arabia'), ('TR', 'Turkey'), ('JP', 'Japan'), ('GG', 'Guernsey'), ('NZ', 'New Zealand'), ('BM', 'Bermuda'), ('BY', 'Belarus'), ('MS', 'Montserrat'), ('OM', 'Oman'), ('AL', 'Albania'), ('LU', 'Luxembourg'), ('KI', 'Kiribati'), ('VA', 'Holy See'), ('CK', 'Cook Islands'), ('BB', 'Barbados'), ('EE', 'Estonia'), ('CY', 'Cyprus'), ('TC', 'Turks and Caicos Islands'), ('DO', 'Dominican Republic'), ('PW', 'Palau'), ('LT', 'Lithuania'), ('KN', 'Saint Kitts and Nevis'), ('SE', 'Sweden'), ('RW', 'Rwanda'), ('NG', 'Nigeria'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('UA', 'Ukraine'), ('KZ', 'Kazakhstan'), ('SB', 'Solomon Islands'), ('FI', 'Finland'), ('LY', 'Libya'), ('HN', 'Honduras'), ('IL', 'Israel'), ('MH', 'Marshall Islands'), ('BF', 'Burkina Faso'), ('KY', 'Cayman Islands'), ('TZ', 'Tanzania, United Republic of'), ('MO', 'Macao'), ('FJ', 'Fiji'), ('SK', 'Slovakia'), ('IM', 'Isle of Man'), ('LC', 'Saint Lucia'), ('QA', 'Qatar'), ('SY', 'Syrian Arab Republic'), ('PT', 'Portugal'), ('GF', 'French Guiana'), ('SM', 'San Marino'), ('MM', 'Myanmar'), ('WS', 'Samoa'), ('DJ', 'Djibouti'), ('BR', 'Brazil'), ('GW', 'Guinea-Bissau'), ('LI', 'Liechtenstein'), ('MU', 'Mauritius'), ('LV', 'Latvia'), ('SZ', 'Swaziland'), ('SI', 'Slovenia'), ('CH', 'Switzerland'), ('SS', 'South Sudan'), ('PN', 'Pitcairn'), ('MG', 'Madagascar'), ('ZW', 'Zimbabwe'), ('BL', 'Saint Barthélemy'), ('PM', 'Saint Pierre and Miquelon'), ('SG', 'Singapore'), ('TG', 'Togo'), ('JM', 'Jamaica'), ('CW', 'Curaçao'), ('MV', 'Maldives'), ('KR', 'Korea (the Republic of)'), ('NC', 'New Caledonia'), ('ES', 'Spain'), ('RE', 'Réunion'), ('MZ', 'Mozambique'), ('LK', 'Sri Lanka'), ('RS', 'Serbia'), ('ML', 'Mali'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('FO', 'Faroe Islands'), ('SJ', 'Svalbard and Jan Mayen'), ('ZM', 'Zambia'), ('WF', 'Wallis and Futuna'), ('SR', 'Suriname'), ('TV', 'Tuvalu'), ('VC', 'Saint Vincent and the Grenadines'), ('HT', 'Haiti'), ('MC', 'Monaco'), ('TL', 'Timor-Leste'), ('BT', 'Bhutan'), ('SV', 'El Salvador'), ('LB', 'Lebanon'), ('MP', 'Northern Mariana Islands'), ('HU', 'Hungary'), ('AI', 'Anguilla'), ('ID', 'Indonesia'), ('PL', 'Poland'), ('SL', 'Sierra Leone'), ('TF', 'French Southern Territories'), ('FM', 'Micronesia (Federated States of)'), ('GT', 'Guatemala'), ('IQ', 'Iraq'), ('CM', 'Cameroon'), ('GD', 'Grenada'), ('AR', 'Argentina'), ('GY', 'Guyana'), ('AX', 'Åland Islands'), ('TT', 'Trinidad and Tobago'), ('KH', 'Cambodia'), ('PK', 'Pakistan'), ('GM', 'Gambia'), ('GA', 'Gabon'), ('UG', 'Uganda'), ('MX', 'Mexico'), ('CU', 'Cuba'), ('BH', 'Bahrain'), ('AZ', 'Azerbaijan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('TH', 'Thailand'), ('PA', 'Panama'), ('GS', 'South Georgia and the South Sandwich Islands'), ('AS', 'American Samoa'), ('KM', 'Comoros'), ('CL', 'Chile'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('GI', 'Gibraltar'), ('ST', 'Sao Tome and Principe'), ('DZ', 'Algeria'), ('PS', 'Palestine, State of'), ('PR', 'Puerto Rico'), ('GN', 'Guinea'), ('NA', 'Namibia'), ('AW', 'Aruba'), ('US', 'United States of America'), ('CC', 'Cocos (Keeling) Islands'), ('CD', 'Congo (the Democratic Republic of the)'), ('NE', 'Niger'), ('DK', 'Denmark'), ('BI', 'Burundi'), ('PH', 'Philippines'), ('GQ', 'Equatorial Guinea'), ('KG', 'Kyrgyzstan'), ('MT', 'Malta'), ('AO', 'Angola'), ('MY', 'Malaysia'), ('BE', 'Belgium'), ('NP', 'Nepal'), ('LS', 'Lesotho'), ('CN', 'China'), ('VN', 'Viet Nam'), ('NL', 'Netherlands'), ('FK', 'Falkland Islands  [Malvinas]'), ('BV', 'Bouvet Island'), ('MW', 'Malawi'), ('AU', 'Australia'), ('YT', 'Mayotte'), ('GE', 'Georgia'), ('KP', "Korea (the Democratic People's Republic of)"), ('CZ', 'Czech Republic'), ('ME', 'Montenegro'), ('TM', 'Turkmenistan'), ('TW', 'Taiwan (Province of China)'), ('MF', 'Saint Martin (French part)'), ('BZ', 'Belize'), ('NR', 'Nauru'), ('CV', 'Cabo Verde'), ('CO', 'Colombia'), ('IO', 'British Indian Ocean Territory'), ('EH', 'Western Sahara'), ('HM', 'Heard Island and McDonald Islands'), ('ZA', 'South Africa'), ('NI', 'Nicaragua'), ('AM', 'Armenia'), ('CF', 'Central African Republic'), ('AT', 'Austria'), ('BW', 'Botswana'), ('MN', 'Mongolia'), ('PE', 'Peru'), ('PY', 'Paraguay'), ('TN', 'Tunisia')], default='', max_length=2),
        ),
    ]