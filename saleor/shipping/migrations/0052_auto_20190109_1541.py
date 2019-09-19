# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-09 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0051_auto_20181221_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingmethodcountry',
            name='country_code',
            field=models.CharField(blank=True, choices=[('', 'Any country'), ('KP', "Korea (the Democratic People's Republic of)"), ('ET', 'Ethiopia'), ('LY', 'Libya'), ('BT', 'Bhutan'), ('EE', 'Estonia'), ('CC', 'Cocos (Keeling) Islands'), ('TW', 'Taiwan (Province of China)'), ('KM', 'Comoros'), ('BE', 'Belgium'), ('MF', 'Saint Martin (French part)'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('KN', 'Saint Kitts and Nevis'), ('TC', 'Turks and Caicos Islands'), ('SD', 'Sudan'), ('LT', 'Lithuania'), ('AF', 'Afghanistan'), ('SX', 'Sint Maarten (Dutch part)'), ('GE', 'Georgia'), ('SM', 'San Marino'), ('RW', 'Rwanda'), ('KR', 'Korea (the Republic of)'), ('GI', 'Gibraltar'), ('TL', 'Timor-Leste'), ('VN', 'Viet Nam'), ('ME', 'Montenegro'), ('CM', 'Cameroon'), ('MD', 'Moldova (the Republic of)'), ('MX', 'Mexico'), ('CI', "Côte d'Ivoire"), ('EH', 'Western Sahara'), ('SC', 'Seychelles'), ('CN', 'China'), ('SN', 'Senegal'), ('DK', 'Denmark'), ('AD', 'Andorra'), ('BZ', 'Belize'), ('NA', 'Namibia'), ('GY', 'Guyana'), ('MR', 'Mauritania'), ('RS', 'Serbia'), ('AX', 'Åland Islands'), ('QA', 'Qatar'), ('TO', 'Tonga'), ('BF', 'Burkina Faso'), ('TT', 'Trinidad and Tobago'), ('FR', 'France'), ('UA', 'Ukraine'), ('MY', 'Malaysia'), ('PK', 'Pakistan'), ('SJ', 'Svalbard and Jan Mayen'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('HM', 'Heard Island and McDonald Islands'), ('BH', 'Bahrain'), ('KH', 'Cambodia'), ('NG', 'Nigeria'), ('LR', 'Liberia'), ('DJ', 'Djibouti'), ('RE', 'Réunion'), ('LC', 'Saint Lucia'), ('ZW', 'Zimbabwe'), ('IO', 'British Indian Ocean Territory'), ('CR', 'Costa Rica'), ('DE', 'Germany'), ('GP', 'Guadeloupe'), ('JE', 'Jersey'), ('PG', 'Papua New Guinea'), ('CX', 'Christmas Island'), ('IS', 'Iceland'), ('GD', 'Grenada'), ('AM', 'Armenia'), ('IE', 'Ireland'), ('IL', 'Israel'), ('JO', 'Jordan'), ('AS', 'American Samoa'), ('TJ', 'Tajikistan'), ('AT', 'Austria'), ('VC', 'Saint Vincent and the Grenadines'), ('PL', 'Poland'), ('GN', 'Guinea'), ('KG', 'Kyrgyzstan'), ('MC', 'Monaco'), ('NO', 'Norway'), ('PW', 'Palau'), ('DZ', 'Algeria'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('CW', 'Curaçao'), ('MV', 'Maldives'), ('LB', 'Lebanon'), ('VI', 'Virgin Islands (U.S.)'), ('CL', 'Chile'), ('US', 'United States of America'), ('GR', 'Greece'), ('SO', 'Somalia'), ('MP', 'Northern Mariana Islands'), ('AO', 'Angola'), ('KE', 'Kenya'), ('CD', 'Congo (the Democratic Republic of the)'), ('AZ', 'Azerbaijan'), ('GH', 'Ghana'), ('VG', 'Virgin Islands (British)'), ('BL', 'Saint Barthélemy'), ('PM', 'Saint Pierre and Miquelon'), ('RU', 'Russian Federation'), ('AI', 'Anguilla'), ('AG', 'Antigua and Barbuda'), ('UM', 'United States Minor Outlying Islands'), ('SI', 'Slovenia'), ('PH', 'Philippines'), ('FI', 'Finland'), ('GG', 'Guernsey'), ('ER', 'Eritrea'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('SV', 'El Salvador'), ('GF', 'French Guiana'), ('GM', 'Gambia'), ('TV', 'Tuvalu'), ('HK', 'Hong Kong'), ('CZ', 'Czechia'), ('ZA', 'South Africa'), ('CU', 'Cuba'), ('BY', 'Belarus'), ('BB', 'Barbados'), ('CY', 'Cyprus'), ('CA', 'Canada'), ('JM', 'Jamaica'), ('HU', 'Hungary'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('TD', 'Chad'), ('GW', 'Guinea-Bissau'), ('IT', 'Italy'), ('SL', 'Sierra Leone'), ('BS', 'Bahamas'), ('SE', 'Sweden'), ('FJ', 'Fiji'), ('BV', 'Bouvet Island'), ('PA', 'Panama'), ('HT', 'Haiti'), ('FM', 'Micronesia (Federated States of)'), ('ID', 'Indonesia'), ('AU', 'Australia'), ('FO', 'Faroe Islands'), ('ML', 'Mali'), ('SK', 'Slovakia'), ('UG', 'Uganda'), ('FK', 'Falkland Islands  [Malvinas]'), ('EC', 'Ecuador'), ('AQ', 'Antarctica'), ('GT', 'Guatemala'), ('UY', 'Uruguay'), ('LS', 'Lesotho'), ('SZ', 'Swaziland'), ('GL', 'Greenland'), ('KZ', 'Kazakhstan'), ('IR', 'Iran (Islamic Republic of)'), ('DO', 'Dominican Republic'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('GQ', 'Equatorial Guinea'), ('MO', 'Macao'), ('NU', 'Niue'), ('TG', 'Togo'), ('NZ', 'New Zealand'), ('NF', 'Norfolk Island'), ('VA', 'Holy See'), ('TF', 'French Southern Territories'), ('MU', 'Mauritius'), ('NE', 'Niger'), ('AL', 'Albania'), ('NR', 'Nauru'), ('TN', 'Tunisia'), ('MQ', 'Martinique'), ('NL', 'Netherlands'), ('EG', 'Egypt'), ('AW', 'Aruba'), ('KW', 'Kuwait'), ('CH', 'Switzerland'), ('OM', 'Oman'), ('CV', 'Cabo Verde'), ('PR', 'Puerto Rico'), ('BD', 'Bangladesh'), ('BN', 'Brunei Darussalam'), ('SR', 'Suriname'), ('LV', 'Latvia'), ('SS', 'South Sudan'), ('MT', 'Malta'), ('NC', 'New Caledonia'), ('YE', 'Yemen'), ('LI', 'Liechtenstein'), ('IN', 'India'), ('MH', 'Marshall Islands'), ('LA', "Lao People's Democratic Republic"), ('MG', 'Madagascar'), ('KI', 'Kiribati'), ('DM', 'Dominica'), ('SA', 'Saudi Arabia'), ('SG', 'Singapore'), ('MW', 'Malawi'), ('CG', 'Congo'), ('BA', 'Bosnia and Herzegovina'), ('TM', 'Turkmenistan'), ('NP', 'Nepal'), ('PN', 'Pitcairn'), ('HR', 'Croatia'), ('WS', 'Samoa'), ('IM', 'Isle of Man'), ('ES', 'Spain'), ('ZM', 'Zambia'), ('AE', 'United Arab Emirates'), ('TZ', 'Tanzania, United Republic of'), ('HN', 'Honduras'), ('NI', 'Nicaragua'), ('CO', 'Colombia'), ('KY', 'Cayman Islands'), ('LK', 'Sri Lanka'), ('BO', 'Bolivia (Plurinational State of)'), ('GA', 'Gabon'), ('MA', 'Morocco'), ('UZ', 'Uzbekistan'), ('BW', 'Botswana'), ('BG', 'Bulgaria'), ('SY', 'Syrian Arab Republic'), ('LU', 'Luxembourg'), ('TK', 'Tokelau'), ('GU', 'Guam'), ('BI', 'Burundi'), ('JP', 'Japan'), ('PS', 'Palestine, State of'), ('PT', 'Portugal'), ('BJ', 'Benin'), ('CK', 'Cook Islands'), ('MZ', 'Mozambique'), ('YT', 'Mayotte'), ('GS', 'South Georgia and the South Sandwich Islands'), ('CF', 'Central African Republic'), ('VU', 'Vanuatu'), ('MN', 'Mongolia'), ('IQ', 'Iraq'), ('BR', 'Brazil'), ('TR', 'Turkey'), ('SB', 'Solomon Islands'), ('RO', 'Romania'), ('TH', 'Thailand'), ('MM', 'Myanmar'), ('WF', 'Wallis and Futuna'), ('ST', 'Sao Tome and Principe'), ('MS', 'Montserrat'), ('PF', 'French Polynesia'), ('BM', 'Bermuda'), ('AR', 'Argentina')], default='', max_length=2),
        ),
    ]