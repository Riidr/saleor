# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-01-29 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0002_auto_20160906_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingmethodcountry',
            name='country_code',
            field=models.CharField(blank=True, choices=[('', 'Any country'), ('JM', 'Jamaica'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('NF', 'Norfolk Island'), ('PE', 'Peru'), ('DO', 'Dominican Republic'), ('AS', 'American Samoa'), ('TR', 'Turkey'), ('MF', 'Saint Martin (French part)'), ('SO', 'Somalia'), ('EG', 'Egypt'), ('BS', 'Bahamas'), ('OM', 'Oman'), ('RE', 'Réunion'), ('BV', 'Bouvet Island'), ('TH', 'Thailand'), ('TW', 'Taiwan (Province of China)'), ('AZ', 'Azerbaijan'), ('DJ', 'Djibouti'), ('TL', 'Timor-Leste'), ('SV', 'El Salvador'), ('LI', 'Liechtenstein'), ('BR', 'Brazil'), ('PH', 'Philippines'), ('CD', 'Congo (the Democratic Republic of the)'), ('LU', 'Luxembourg'), ('TZ', 'Tanzania, United Republic of'), ('KI', 'Kiribati'), ('ME', 'Montenegro'), ('IT', 'Italy'), ('TM', 'Turkmenistan'), ('LV', 'Latvia'), ('SA', 'Saudi Arabia'), ('MG', 'Madagascar'), ('HR', 'Croatia'), ('TD', 'Chad'), ('PF', 'French Polynesia'), ('WS', 'Samoa'), ('CA', 'Canada'), ('HU', 'Hungary'), ('BN', 'Brunei Darussalam'), ('UA', 'Ukraine'), ('EH', 'Western Sahara'), ('AX', 'Åland Islands'), ('IQ', 'Iraq'), ('GI', 'Gibraltar'), ('PR', 'Puerto Rico'), ('RO', 'Romania'), ('NU', 'Niue'), ('MT', 'Malta'), ('GR', 'Greece'), ('GW', 'Guinea-Bissau'), ('FO', 'Faroe Islands'), ('FJ', 'Fiji'), ('AD', 'Andorra'), ('TO', 'Tonga'), ('IR', 'Iran (Islamic Republic of)'), ('ML', 'Mali'), ('AL', 'Albania'), ('KW', 'Kuwait'), ('PW', 'Palau'), ('GD', 'Grenada'), ('BM', 'Bermuda'), ('NO', 'Norway'), ('BD', 'Bangladesh'), ('MU', 'Mauritius'), ('ST', 'Sao Tome and Principe'), ('SD', 'Sudan'), ('LS', 'Lesotho'), ('VA', 'Holy See'), ('BY', 'Belarus'), ('SZ', 'Swaziland'), ('GG', 'Guernsey'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('RS', 'Serbia'), ('BZ', 'Belize'), ('YT', 'Mayotte'), ('TK', 'Tokelau'), ('GL', 'Greenland'), ('MN', 'Mongolia'), ('MS', 'Montserrat'), ('GN', 'Guinea'), ('KP', "Korea (the Democratic People's Republic of)"), ('SX', 'Sint Maarten (Dutch part)'), ('KE', 'Kenya'), ('NL', 'Netherlands'), ('PG', 'Papua New Guinea'), ('GM', 'Gambia'), ('GS', 'South Georgia and the South Sandwich Islands'), ('SK', 'Slovakia'), ('SG', 'Singapore'), ('BF', 'Burkina Faso'), ('AR', 'Argentina'), ('BT', 'Bhutan'), ('SB', 'Solomon Islands'), ('TG', 'Togo'), ('IM', 'Isle of Man'), ('KR', 'Korea (the Republic of)'), ('MP', 'Northern Mariana Islands'), ('MZ', 'Mozambique'), ('AO', 'Angola'), ('KN', 'Saint Kitts and Nevis'), ('MY', 'Malaysia'), ('NZ', 'New Zealand'), ('SN', 'Senegal'), ('MW', 'Malawi'), ('SL', 'Sierra Leone'), ('LT', 'Lithuania'), ('VG', 'Virgin Islands (British)'), ('SR', 'Suriname'), ('JO', 'Jordan'), ('WF', 'Wallis and Futuna'), ('LR', 'Liberia'), ('NA', 'Namibia'), ('DM', 'Dominica'), ('CY', 'Cyprus'), ('CM', 'Cameroon'), ('SE', 'Sweden'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('BE', 'Belgium'), ('FI', 'Finland'), ('CC', 'Cocos (Keeling) Islands'), ('GH', 'Ghana'), ('CO', 'Colombia'), ('IN', 'India'), ('AQ', 'Antarctica'), ('RW', 'Rwanda'), ('HN', 'Honduras'), ('TJ', 'Tajikistan'), ('NR', 'Nauru'), ('IE', 'Ireland'), ('SY', 'Syrian Arab Republic'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('ZW', 'Zimbabwe'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('KG', 'Kyrgyzstan'), ('CU', 'Cuba'), ('GE', 'Georgia'), ('CI', "Côte d'Ivoire"), ('TN', 'Tunisia'), ('AE', 'United Arab Emirates'), ('CL', 'Chile'), ('LB', 'Lebanon'), ('AI', 'Anguilla'), ('BJ', 'Benin'), ('BI', 'Burundi'), ('JP', 'Japan'), ('TV', 'Tuvalu'), ('FM', 'Micronesia (Federated States of)'), ('IL', 'Israel'), ('CH', 'Switzerland'), ('UZ', 'Uzbekistan'), ('AG', 'Antigua and Barbuda'), ('AU', 'Australia'), ('JE', 'Jersey'), ('BH', 'Bahrain'), ('SJ', 'Svalbard and Jan Mayen'), ('GP', 'Guadeloupe'), ('ER', 'Eritrea'), ('AF', 'Afghanistan'), ('SI', 'Slovenia'), ('PS', 'Palestine, State of'), ('MC', 'Monaco'), ('ID', 'Indonesia'), ('IO', 'British Indian Ocean Territory'), ('MM', 'Myanmar'), ('AM', 'Armenia'), ('KY', 'Cayman Islands'), ('CX', 'Christmas Island'), ('CK', 'Cook Islands'), ('FK', 'Falkland Islands  [Malvinas]'), ('US', 'United States of America'), ('ET', 'Ethiopia'), ('AT', 'Austria'), ('KM', 'Comoros'), ('HK', 'Hong Kong'), ('DK', 'Denmark'), ('PN', 'Pitcairn'), ('CN', 'China'), ('UG', 'Uganda'), ('EE', 'Estonia'), ('TC', 'Turks and Caicos Islands'), ('VU', 'Vanuatu'), ('PT', 'Portugal'), ('DZ', 'Algeria'), ('BA', 'Bosnia and Herzegovina'), ('KH', 'Cambodia'), ('BO', 'Bolivia (Plurinational State of)'), ('CR', 'Costa Rica'), ('NP', 'Nepal'), ('CG', 'Congo'), ('UY', 'Uruguay'), ('EC', 'Ecuador'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('CW', 'Curaçao'), ('BB', 'Barbados'), ('HT', 'Haiti'), ('PA', 'Panama'), ('MH', 'Marshall Islands'), ('LC', 'Saint Lucia'), ('PY', 'Paraguay'), ('KZ', 'Kazakhstan'), ('MD', 'Moldova (the Republic of)'), ('MX', 'Mexico'), ('DE', 'Germany'), ('MQ', 'Martinique'), ('AW', 'Aruba'), ('MV', 'Maldives'), ('GQ', 'Equatorial Guinea'), ('VC', 'Saint Vincent and the Grenadines'), ('BW', 'Botswana'), ('LK', 'Sri Lanka'), ('PM', 'Saint Pierre and Miquelon'), ('UM', 'United States Minor Outlying Islands'), ('QA', 'Qatar'), ('MR', 'Mauritania'), ('TF', 'French Southern Territories'), ('GA', 'Gabon'), ('BG', 'Bulgaria'), ('MO', 'Macao'), ('ES', 'Spain'), ('FR', 'France'), ('SS', 'South Sudan'), ('RU', 'Russian Federation'), ('ZA', 'South Africa'), ('GT', 'Guatemala'), ('LY', 'Libya'), ('GU', 'Guam'), ('PL', 'Poland'), ('NI', 'Nicaragua'), ('NC', 'New Caledonia'), ('GF', 'French Guiana'), ('GY', 'Guyana'), ('CV', 'Cabo Verde'), ('VN', 'Viet Nam'), ('PK', 'Pakistan'), ('NE', 'Niger'), ('HM', 'Heard Island and McDonald Islands'), ('VI', 'Virgin Islands (U.S.)'), ('SM', 'San Marino'), ('LA', "Lao People's Democratic Republic"), ('NG', 'Nigeria'), ('IS', 'Iceland'), ('CZ', 'Czech Republic'), ('BL', 'Saint Barthélemy'), ('SC', 'Seychelles'), ('MA', 'Morocco'), ('TT', 'Trinidad and Tobago'), ('CF', 'Central African Republic')], default='', max_length=2),
        ),
    ]
