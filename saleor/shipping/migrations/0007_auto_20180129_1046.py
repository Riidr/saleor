# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-01-29 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0006_auto_20180129_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingmethodcountry',
            name='country_code',
            field=models.CharField(blank=True, choices=[('', 'Any country'), ('SY', 'Syrian Arab Republic'), ('LK', 'Sri Lanka'), ('NA', 'Namibia'), ('BF', 'Burkina Faso'), ('EG', 'Egypt'), ('TL', 'Timor-Leste'), ('YE', 'Yemen'), ('TN', 'Tunisia'), ('WS', 'Samoa'), ('IN', 'India'), ('SK', 'Slovakia'), ('IO', 'British Indian Ocean Territory'), ('TW', 'Taiwan (Province of China)'), ('CK', 'Cook Islands'), ('HM', 'Heard Island and McDonald Islands'), ('PK', 'Pakistan'), ('LT', 'Lithuania'), ('BN', 'Brunei Darussalam'), ('MO', 'Macao'), ('PY', 'Paraguay'), ('FR', 'France'), ('HR', 'Croatia'), ('KI', 'Kiribati'), ('CV', 'Cabo Verde'), ('ID', 'Indonesia'), ('CC', 'Cocos (Keeling) Islands'), ('GN', 'Guinea'), ('HK', 'Hong Kong'), ('BB', 'Barbados'), ('FM', 'Micronesia (Federated States of)'), ('PN', 'Pitcairn'), ('SN', 'Senegal'), ('OM', 'Oman'), ('MM', 'Myanmar'), ('TD', 'Chad'), ('NP', 'Nepal'), ('TF', 'French Southern Territories'), ('GL', 'Greenland'), ('PF', 'French Polynesia'), ('KR', 'Korea (the Republic of)'), ('HT', 'Haiti'), ('MD', 'Moldova (the Republic of)'), ('ST', 'Sao Tome and Principe'), ('PG', 'Papua New Guinea'), ('CI', "Côte d'Ivoire"), ('TR', 'Turkey'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('CZ', 'Czech Republic'), ('MH', 'Marshall Islands'), ('BG', 'Bulgaria'), ('VU', 'Vanuatu'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BJ', 'Benin'), ('NU', 'Niue'), ('AD', 'Andorra'), ('GD', 'Grenada'), ('KE', 'Kenya'), ('IR', 'Iran (Islamic Republic of)'), ('NZ', 'New Zealand'), ('GQ', 'Equatorial Guinea'), ('GS', 'South Georgia and the South Sandwich Islands'), ('MC', 'Monaco'), ('RE', 'Réunion'), ('CH', 'Switzerland'), ('PE', 'Peru'), ('AR', 'Argentina'), ('KG', 'Kyrgyzstan'), ('SX', 'Sint Maarten (Dutch part)'), ('MF', 'Saint Martin (French part)'), ('DE', 'Germany'), ('NC', 'New Caledonia'), ('NO', 'Norway'), ('TZ', 'Tanzania, United Republic of'), ('ZW', 'Zimbabwe'), ('SR', 'Suriname'), ('AO', 'Angola'), ('UA', 'Ukraine'), ('LI', 'Liechtenstein'), ('BR', 'Brazil'), ('MU', 'Mauritius'), ('CU', 'Cuba'), ('MG', 'Madagascar'), ('AL', 'Albania'), ('JP', 'Japan'), ('PH', 'Philippines'), ('PM', 'Saint Pierre and Miquelon'), ('CO', 'Colombia'), ('LY', 'Libya'), ('TM', 'Turkmenistan'), ('EC', 'Ecuador'), ('CG', 'Congo'), ('IT', 'Italy'), ('RO', 'Romania'), ('MY', 'Malaysia'), ('CL', 'Chile'), ('ZA', 'South Africa'), ('IM', 'Isle of Man'), ('BY', 'Belarus'), ('AU', 'Australia'), ('NR', 'Nauru'), ('NF', 'Norfolk Island'), ('FO', 'Faroe Islands'), ('PA', 'Panama'), ('DO', 'Dominican Republic'), ('IS', 'Iceland'), ('PW', 'Palau'), ('AI', 'Anguilla'), ('KN', 'Saint Kitts and Nevis'), ('KP', "Korea (the Democratic People's Republic of)"), ('YT', 'Mayotte'), ('TO', 'Tonga'), ('GW', 'Guinea-Bissau'), ('LU', 'Luxembourg'), ('MN', 'Mongolia'), ('FI', 'Finland'), ('IE', 'Ireland'), ('TC', 'Turks and Caicos Islands'), ('FK', 'Falkland Islands  [Malvinas]'), ('GF', 'French Guiana'), ('LV', 'Latvia'), ('GY', 'Guyana'), ('CX', 'Christmas Island'), ('SG', 'Singapore'), ('MS', 'Montserrat'), ('TT', 'Trinidad and Tobago'), ('AG', 'Antigua and Barbuda'), ('HU', 'Hungary'), ('GA', 'Gabon'), ('VN', 'Viet Nam'), ('AE', 'United Arab Emirates'), ('MX', 'Mexico'), ('GM', 'Gambia'), ('AX', 'Åland Islands'), ('BD', 'Bangladesh'), ('DK', 'Denmark'), ('BW', 'Botswana'), ('TK', 'Tokelau'), ('MR', 'Mauritania'), ('AF', 'Afghanistan'), ('UG', 'Uganda'), ('CN', 'China'), ('KM', 'Comoros'), ('BS', 'Bahamas'), ('BL', 'Saint Barthélemy'), ('RS', 'Serbia'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('SV', 'El Salvador'), ('LC', 'Saint Lucia'), ('DJ', 'Djibouti'), ('UM', 'United States Minor Outlying Islands'), ('MT', 'Malta'), ('BZ', 'Belize'), ('WF', 'Wallis and Futuna'), ('SC', 'Seychelles'), ('IL', 'Israel'), ('CF', 'Central African Republic'), ('SA', 'Saudi Arabia'), ('VC', 'Saint Vincent and the Grenadines'), ('KZ', 'Kazakhstan'), ('CM', 'Cameroon'), ('BA', 'Bosnia and Herzegovina'), ('AM', 'Armenia'), ('RW', 'Rwanda'), ('SL', 'Sierra Leone'), ('TH', 'Thailand'), ('MP', 'Northern Mariana Islands'), ('MZ', 'Mozambique'), ('PR', 'Puerto Rico'), ('SE', 'Sweden'), ('AW', 'Aruba'), ('EH', 'Western Sahara'), ('GT', 'Guatemala'), ('PS', 'Palestine, State of'), ('JO', 'Jordan'), ('ME', 'Montenegro'), ('SB', 'Solomon Islands'), ('AZ', 'Azerbaijan'), ('KW', 'Kuwait'), ('VA', 'Holy See'), ('UY', 'Uruguay'), ('JM', 'Jamaica'), ('US', 'United States of America'), ('NE', 'Niger'), ('SO', 'Somalia'), ('DZ', 'Algeria'), ('NG', 'Nigeria'), ('SS', 'South Sudan'), ('MV', 'Maldives'), ('FJ', 'Fiji'), ('HN', 'Honduras'), ('UZ', 'Uzbekistan'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('GR', 'Greece'), ('GI', 'Gibraltar'), ('BH', 'Bahrain'), ('GE', 'Georgia'), ('NL', 'Netherlands'), ('GP', 'Guadeloupe'), ('ZM', 'Zambia'), ('LB', 'Lebanon'), ('BI', 'Burundi'), ('BM', 'Bermuda'), ('ET', 'Ethiopia'), ('SD', 'Sudan'), ('CA', 'Canada'), ('LA', "Lao People's Democratic Republic"), ('VG', 'Virgin Islands (British)'), ('DM', 'Dominica'), ('KH', 'Cambodia'), ('RU', 'Russian Federation'), ('AQ', 'Antarctica'), ('ML', 'Mali'), ('SJ', 'Svalbard and Jan Mayen'), ('NI', 'Nicaragua'), ('ER', 'Eritrea'), ('CR', 'Costa Rica'), ('PL', 'Poland'), ('GU', 'Guam'), ('LR', 'Liberia'), ('SZ', 'Swaziland'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('GG', 'Guernsey'), ('GH', 'Ghana'), ('ES', 'Spain'), ('BV', 'Bouvet Island'), ('CD', 'Congo (the Democratic Republic of the)'), ('TJ', 'Tajikistan'), ('CW', 'Curaçao'), ('EE', 'Estonia'), ('QA', 'Qatar'), ('LS', 'Lesotho'), ('MW', 'Malawi'), ('CY', 'Cyprus'), ('JE', 'Jersey'), ('BE', 'Belgium'), ('AS', 'American Samoa'), ('SI', 'Slovenia'), ('KY', 'Cayman Islands'), ('BT', 'Bhutan'), ('MQ', 'Martinique'), ('MA', 'Morocco'), ('TG', 'Togo'), ('VI', 'Virgin Islands (U.S.)'), ('BO', 'Bolivia (Plurinational State of)'), ('PT', 'Portugal'), ('AT', 'Austria'), ('IQ', 'Iraq'), ('SM', 'San Marino'), ('TV', 'Tuvalu')], default='', max_length=2),
        ),
    ]