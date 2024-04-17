#!/bin/python3
from math import radians, pi, log, tan

regions = {
    'Abkhazia': {
        'nom': 'Abkhazia',
        'capitale': 'Sukhumi',
        'latitude': 43.001525,
        'longitude': 41.023415
    },
    'Afghanistan': {
        'nom': 'Afghanistan',
        'capitale': 'Kabul',
        'latitude': 34.575503,
        'longitude': 69.240073
    },
    'Aland Islands': {
        'nom': 'Aland Islands',
        'capitale': 'Mariehamn',
        'latitude': 60.1,
        'longitude': 19.933333
    },
    'Albania': {
        'nom': 'Albania',
        'capitale': 'Tirana',
        'latitude': 41.327546,
        'longitude': 19.818698
    },
    'Algeria': {
        'nom': 'Algeria',
        'capitale': 'Algiers',
        'latitude': 36.752887,
        'longitude': 3.042048
    },
    'American Samoa': {
        'nom': 'American Samoa',
        'capitale': 'Pago Pago',
        'latitude': -14.275632,
        'longitude': -170.702036
    },
    'Andorra': {
        'nom': 'Andorra',
        'capitale': 'Andorra la Vella',
        'latitude': 42.506317,
        'longitude': 1.521835
    },
    'Angola': {
        'nom': 'Angola',
        'capitale': 'Luanda',
        'latitude': -8.839988,
        'longitude': 13.289437
    },
    'Anguilla': {
        'nom': 'Anguilla',
        'capitale': 'The Valley',
        'latitude': 18.214813,
        'longitude': -63.057441
    },
    'Antarctica': {
        'nom': 'Antarctica',
        'capitale': 'South Pole',
        'latitude': -90.0,
        'longitude': 0.0
    },
    'Antigua and Barbuda': {
        'nom': 'Antigua and Barbuda',
        'capitale': "St. John's",
        'latitude': 17.12741,
        'longitude': -61.846772
    },
    'Argentina': {
        'nom': 'Argentina',
        'capitale': 'Buenos Aires',
        'latitude': -34.603684,
        'longitude': -58.381559
    },
    'Armenia': {
        'nom': 'Armenia',
        'capitale': 'Yerevan',
        'latitude': 40.179186,
        'longitude': 44.499103
    },
    'Aruba': {
        'nom': 'Aruba',
        'capitale': 'Oranjestad',
        'latitude': 12.509204,
        'longitude': -70.008631
    },
    'Australia': {
        'nom': 'Australia',
        'capitale': 'Canberra',
        'latitude': -35.282,
        'longitude': 149.128684
    },
    'Austria': {
        'nom': 'Austria',
        'capitale': 'Vienna',
        'latitude': 48.208174,
        'longitude': 16.373819
    },
    'Azerbaijan': {
        'nom': 'Azerbaijan',
        'capitale': 'Baku',
        'latitude': 40.409262,
        'longitude': 49.867092
    },
    'Bahamas': {
        'nom': 'Bahamas',
        'capitale': 'Nassau',
        'latitude': 25.047984,
        'longitude': -77.355413
    },
    'Bahrain': {
        'nom': 'Bahrain',
        'capitale': 'Manama',
        'latitude': 26.228516,
        'longitude': 50.58605
    },
    'Bangladesh': {
        'nom': 'Bangladesh',
        'capitale': 'Dhaka',
        'latitude': 23.810332,
        'longitude': 90.412518
    },
    'Barbados': {
        'nom': 'Barbados',
        'capitale': 'Bridgetown',
        'latitude': 13.113222,
        'longitude': -59.598809
    },
    'Belarus': {
        'nom': 'Belarus',
        'capitale': 'Minsk',
        'latitude': 53.90454,
        'longitude': 27.561524
    },
    'Belgium': {
        'nom': 'Belgium',
        'capitale': 'Brussels',
        'latitude': 50.85034,
        'longitude': 4.35171
    },
    'Belize': {
        'nom': 'Belize',
        'capitale': 'Belmopan',
        'latitude': 17.251011,
        'longitude': -88.75902
    },
    'Benin': {
        'nom': 'Benin',
        'capitale': 'Porto-Novo',
        'latitude': 6.496857,
        'longitude': 2.628852
    },
    'Bermuda': {
        'nom': 'Bermuda',
        'capitale': 'Hamilton',
        'latitude': 32.294816,
        'longitude': -64.781375
    },
    'Bhutan': {
        'nom': 'Bhutan',
        'capitale': 'Thimphu',
        'latitude': 27.472792,
        'longitude': 89.639286
    },
    'Bolivia': {
        'nom': 'Bolivia',
        'capitale': 'La Paz',
        'latitude': -16.489689,
        'longitude': -68.119294
    },
    'Bosnia and Herzegovina': {
        'nom': 'Bosnia and Herzegovina',
        'capitale': 'Sarajevo',
        'latitude': 43.856259,
        'longitude': 18.413076
    },
    'Botswana': {
        'nom': 'Botswana',
        'capitale': 'Gaborone',
        'latitude': -24.628208,
        'longitude': 25.923147
    },
    'Bouvet Island': {
        'nom': 'Bouvet Island',
        'capitale': 'Bouvet Island',
        'latitude': -54.43,
        'longitude': 3.38
    },
    'Brazil': {
        'nom': 'Brazil',
        'capitale': 'Brasília',
        'latitude': -15.794229,
        'longitude': -47.882166
    },
    'British Indian Ocean Territory': {
        'nom': 'British Indian Ocean Territory',
        'capitale': 'Camp Justice',
        'latitude': 21.3419,
        'longitude': 55.4778
    },
    'British Virgin Islands': {
        'nom': 'British Virgin Islands',
        'capitale': 'Road Town',
        'latitude': 18.428612,
        'longitude': -64.618466
    },
    'Brunei': {
        'nom': 'Brunei',
        'capitale': 'Bandar Seri Begawan',
        'latitude': 4.903052,
        'longitude': 114.939821
    },
    'Bulgaria': {
        'nom': 'Bulgaria',
        'capitale': 'Sofia',
        'latitude': 42.697708,
        'longitude': 23.321868
    },
    'Burkina Faso': {
        'nom': 'Burkina Faso',
        'capitale': 'Ouagadougou',
        'latitude': 12.371428,
        'longitude': -1.51966
    },
    'Burundi': {
        'nom': 'Burundi',
        'capitale': 'Bujumbura',
        'latitude': -3.361378,
        'longitude': 29.359878
    },
    'Cambodia': {
        'nom': 'Cambodia',
        'capitale': 'Phnom Penh',
        'latitude': 11.544873,
        'longitude': 104.892167
    },
    'Cameroon': {
        'nom': 'Cameroon',
        'capitale': 'Yaoundé',
        'latitude': 3.848033,
        'longitude': 11.502075
    },
    'Canada': {
        'nom': 'Canada',
        'capitale': 'Ottawa',
        'latitude': 45.42153,
        'longitude': -75.697193
    },
    'Cape Verde': {
        'nom': 'Cape Verde',
        'capitale': 'Praia',
        'latitude': 14.93305,
        'longitude': -23.513327
    },
    'Cayman Islands': {
        'nom': 'Cayman Islands',
        'capitale': 'George Town',
        'latitude': 19.286932,
        'longitude': -81.367439
    },
    'Central African Republic': {
        'nom': 'Central African Republic',
        'capitale': 'Bangui',
        'latitude': 4.394674,
        'longitude': 18.55819
    },
    'Chad': {
        'nom': 'Chad',
        'capitale': "N'Djamena",
        'latitude': 12.134846,
        'longitude': 15.055742
    },
    'Chile': {
        'nom': 'Chile',
        'capitale': 'Santiago',
        'latitude': -33.44889,
        'longitude': -70.669265
    },
    'China': {
        'nom': 'China',
        'capitale': 'Beijing',
        'latitude': 39.904211,
        'longitude': 116.407395
    },
    'Christmas Island': {
        'nom': 'Christmas Island',
        'capitale': 'Flying Fish Cove',
        'latitude': -10.420686,
        'longitude': 105.679379
    },
    'Cocos (Keeling) Islands': {
        'nom': 'Cocos (Keeling) Islands',
        'capitale': 'West Island',
        'latitude': -12.188834,
        'longitude': 96.829316
    },
    'Colombia': {
        'nom': 'Colombia',
        'capitale': 'Bogotá',
        'latitude': 4.710989,
        'longitude': -74.072092
    },
    'Comoros': {
        'nom': 'Comoros',
        'capitale': 'Moroni',
        'latitude': -11.717216,
        'longitude': 43.247315
    },
    'Congo (DRC)': {
        'nom': 'Congo (DRC)',
        'capitale': 'Kinshasa',
        'latitude': -4.441931,
        'longitude': 15.266293
    },
    'Congo (Republic)': {
        'nom': 'Congo (Republic)',
        'capitale': 'Brazzaville',
        'latitude': -4.26336,
        'longitude': 15.242885
    },
    'Cook Islands': {
        'nom': 'Cook Islands',
        'capitale': 'Avarua',
        'latitude': -21.212901,
        'longitude': -159.782306
    },
    'Costa Rica': {
        'nom': 'Costa Rica',
        'capitale': 'San José',
        'latitude': 9.928069,
        'longitude': -84.090725
    },
    "Côte d'Ivoire": {
        'nom': "Côte d'Ivoire",
        'capitale': 'Yamoussoukro',
        'latitude': 6.827623,
        'longitude': -5.289343
    },
    'Croatia': {
        'nom': 'Croatia',
        'capitale': 'Zagreb ',
        'latitude': 45.815011,
        'longitude': 15.981919
    },
    'Cuba': {
        'nom': 'Cuba',
        'capitale': 'Havana',
        'latitude': 23.05407,
        'longitude': -82.345189
    },
    'Curaçao': {
        'nom': 'Curaçao',
        'capitale': 'Willemstad',
        'latitude': 12.122422,
        'longitude': -68.882423
    },
    'Cyprus': {
        'nom': 'Cyprus',
        'capitale': 'Nicosia',
        'latitude': 35.185566,
        'longitude': 33.382276
    },
    'Czech Republic': {
        'nom': 'Czech Republic',
        'capitale': 'Prague',
        'latitude': 50.075538,
        'longitude': 14.4378
    },
    'Denmark': {
        'nom': 'Denmark',
        'capitale': 'Copenhagen',
        'latitude': 55.676097,
        'longitude': 12.568337
    },
    'Djibouti': {
        'nom': 'Djibouti',
        'capitale': 'Djibouti',
        'latitude': 11.572077,
        'longitude': 43.145647
    },
    'Dominica': {
        'nom': 'Dominica',
        'capitale': 'Roseau',
        'latitude': 15.309168,
        'longitude': -61.379355
    },
    'Dominican Republic': {
        'nom': 'Dominican Republic',
        'capitale': 'Santo Domingo',
        'latitude': 18.486058,
        'longitude': -69.931212
    },
    'Ecuador': {
        'nom': 'Ecuador',
        'capitale': 'Quito',
        'latitude': -0.180653,
        'longitude': -78.467838
    },
    'Egypt': {
        'nom': 'Egypt',
        'capitale': 'Cairo',
        'latitude': 30.04442,
        'longitude': 31.235712
    },
    'El Salvador': {
        'nom': 'El Salvador',
        'capitale': 'San Salvador',
        'latitude': 13.69294,
        'longitude': -89.218191
    },
    'Equatorial Guinea': {
        'nom': 'Equatorial Guinea',
        'capitale': 'Malabo',
        'latitude': 3.750412,
        'longitude': 8.737104
    },
    'Eritrea': {
        'nom': 'Eritrea',
        'capitale': 'Asmara',
        'latitude': 15.322877,
        'longitude': 38.925052
    },
    'Estonia': {
        'nom': 'Estonia',
        'capitale': 'Tallinn',
        'latitude': 59.436961,
        'longitude': 24.753575
    },
    'Ethiopia': {
        'nom': 'Ethiopia',
        'capitale': 'Addis Ababa',
        'latitude': 8.980603,
        'longitude': 38.757761
    },
    'Falkland Islands (Islas Malvinas)': {
        'nom': 'Falkland Islands (Islas Malvinas)',
        'capitale': 'Stanley',
        'latitude': -51.697713,
        'longitude': -57.851663
    },
    'Faroe Islands': {
        'nom': 'Faroe Islands',
        'capitale': 'Tórshavn',
        'latitude': 62.007864,
        'longitude': -6.790982
    },
    'Fiji': {
        'nom': 'Fiji',
        'capitale': 'Suva',
        'latitude': -18.124809,
        'longitude': 178.450079
    },
    'Finland': {
        'nom': 'Finland',
        'capitale': 'Helsinki',
        'latitude': 60.173324,
        'longitude': 24.941025
    },
    'France': {
        'nom': 'France',
        'capitale': 'Paris',
        'latitude': 48.856614,
        'longitude': 2.352222
    },
    'French Guiana': {
        'nom': 'French Guiana',
        'capitale': 'Cayenne',
        'latitude': 4.92242,
        'longitude': -52.313453
    },
    'French Polynesia': {
        'nom': 'French Polynesia',
        'capitale': 'Papeete',
        'latitude': -17.551625,
        'longitude': -149.558476
    },
    'French Southern Territories': {
        'nom': 'French Southern Territories',
        'capitale': 'Saint-Pierre ',
        'latitude': -21.3419,
        'longitude': 55.4778
    },
    'Gabon': {
        'nom': 'Gabon',
        'capitale': 'Libreville',
        'latitude': 0.416198,
        'longitude': 9.467268
    },
    'Gambia': {
        'nom': 'Gambia',
        'capitale': 'Banjul',
        'latitude': 13.454876,
        'longitude': -16.579032
    },
    'Georgia': {
        'nom': 'Georgia',
        'capitale': 'Tbilisi',
        'latitude': 41.715138,
        'longitude': 44.827096
    },
    'Germany': {
        'nom': 'Germany',
        'capitale': 'Berlin',
        'latitude': 52.520007,
        'longitude': 13.404954
    },
    'Ghana': {
        'nom': 'Ghana',
        'capitale': 'Accra',
        'latitude': 5.603717,
        'longitude': -0.186964
    },
    'Gibraltar': {
        'nom': 'Gibraltar',
        'capitale': 'Gibraltar',
        'latitude': 36.140773,
        'longitude': -5.353599
    },
    'Greece': {
        'nom': 'Greece',
        'capitale': 'Athens',
        'latitude': 37.983917,
        'longitude': 23.72936
    },
    'Greenland': {
        'nom': 'Greenland',
        'capitale': 'Nuuk',
        'latitude': 64.18141,
        'longitude': -51.694138
    },
    'Grenada': {
        'nom': 'Grenada',
        'capitale': "St. George's",
        'latitude': 12.056098,
        'longitude': -61.7488
    },
    'Guadeloupe': {
        'nom': 'Guadeloupe',
        'capitale': 'Basse-Terre',
        'latitude': 16.014453,
        'longitude': -61.706411
    },
    'Guam': {
        'nom': 'Guam',
        'capitale': 'Hagåtña',
        'latitude': 13.470891,
        'longitude': 144.751278
    },
    'Guatemala': {
        'nom': 'Guatemala',
        'capitale': 'Guatemala City',
        'latitude': 14.634915,
        'longitude': -90.506882
    },
    'Guernsey': {
        'nom': 'Guernsey',
        'capitale': 'St. Peter Port',
        'latitude': 49.455443,
        'longitude': -2.536871
    },
    'Guinea': {
        'nom': 'Guinea',
        'capitale': 'Conakry',
        'latitude': 9.641185,
        'longitude': -13.578401
    },
    'Guinea-Bissau': {
        'nom': 'Guinea-Bissau',
        'capitale': 'Bissau',
        'latitude': 11.881655,
        'longitude': -15.617794
    },
    'Guyana': {
        'nom': 'Guyana',
        'capitale': 'Georgetown',
        'latitude': 6.801279,
        'longitude': -58.155125
    },
    'Haiti': {
        'nom': 'Haiti',
        'capitale': 'Port-au-Prince',
        'latitude': 18.594395,
        'longitude': -72.307433
    },
    'Honduras': {
        'nom': 'Honduras',
        'capitale': 'Tegucigalpa',
        'latitude': 14.072275,
        'longitude': -87.192136
    },
    'Hong Kong': {
        'nom': 'Hong Kong',
        'capitale': 'Hong Kong',
        'latitude': 22.396428,
        'longitude': 114.109497
    },
    'Hungary': {
        'nom': 'Hungary',
        'capitale': 'Budapest',
        'latitude': 47.497912,
        'longitude': 19.040235
    },
    'Iceland': {
        'nom': 'Iceland',
        'capitale': 'Reykjavík',
        'latitude': 64.126521,
        'longitude': -21.817439
    },
    'India': {
        'nom': 'India',
        'capitale': 'New Delhi',
        'latitude': 28.613939,
        'longitude': 77.209021
    },
    'Indonesia': {
        'nom': 'Indonesia',
        'capitale': 'Jakarta',
        'latitude': -6.208763,
        'longitude': 106.845599
    },
    'Iran': {
        'nom': 'Iran',
        'capitale': 'Tehran',
        'latitude': 35.689198,
        'longitude': 51.388974
    },
    'Iraq': {
        'nom': 'Iraq',
        'capitale': 'Baghdad',
        'latitude': 33.312806,
        'longitude': 44.361488
    },
    'Ireland': {
        'nom': 'Ireland',
        'capitale': 'Dublin',
        'latitude': 53.349805,
        'longitude': -6.26031
    },
    'Isle of Man': {
        'nom': 'Isle of Man',
        'capitale': 'Douglas',
        'latitude': 54.152337,
        'longitude': -4.486123
    },
    'Israel': {
        'nom': 'Israel',
        'capitale': 'Tel Aviv',
        'latitude': 32.0853,
        'longitude': 34.781768
    },
    'Italy': {
        'nom': 'Italy',
        'capitale': 'Rome',
        'latitude': 41.902784,
        'longitude': 12.496366
    },
    'Jamaica': {
        'nom': 'Jamaica',
        'capitale': 'Kingston',
        'latitude': 18.042327,
        'longitude': -76.802893
    },
    'Japan': {
        'nom': 'Japan',
        'capitale': 'Tokyo',
        'latitude': 35.709026,
        'longitude': 139.731992
    },
    'Jersey': {
        'nom': 'Jersey',
        'capitale': 'St. Helier',
        'latitude': 49.186823,
        'longitude': -2.106568
    },
    'Jordan': {
        'nom': 'Jordan',
        'capitale': 'Amman',
        'latitude': 31.956578,
        'longitude': 35.945695
    },
    'Kazakhstan': {
        'nom': 'Kazakhstan',
        'capitale': 'Astana',
        'latitude': 51.160523,
        'longitude': 71.470356
    },
    'Kenya': {
        'nom': 'Kenya',
        'capitale': 'Nairobi',
        'latitude': -1.292066,
        'longitude': 36.821946
    },
    'Kiribati': {
        'nom': 'Kiribati',
        'capitale': 'Tarawa Atoll',
        'latitude': 1.451817,
        'longitude': 172.971662
    },
    'Kosovo': {
        'nom': 'Kosovo',
        'capitale': 'Pristina',
        'latitude': 42.662914,
        'longitude': 21.165503
    },
    'Kuwait': {
        'nom': 'Kuwait',
        'capitale': 'Kuwait City',
        'latitude': 29.375859,
        'longitude': 47.977405
    },
    'Kyrgyzstan': {
        'nom': 'Kyrgyzstan',
        'capitale': 'Bishkek',
        'latitude': 42.874621,
        'longitude': 74.569762
    },
    'Laos': {
        'nom': 'Laos',
        'capitale': 'Vientiane',
        'latitude': 17.975706,
        'longitude': 102.633104
    },
    'Latvia': {
        'nom': 'Latvia',
        'capitale': 'Riga',
        'latitude': 56.949649,
        'longitude': 24.105186
    },
    'Lebanon': {
        'nom': 'Lebanon',
        'capitale': 'Beirut',
        'latitude': 33.888629,
        'longitude': 35.495479
    },
    'Lesotho': {
        'nom': 'Lesotho',
        'capitale': 'Maseru',
        'latitude': -29.363219,
        'longitude': 27.51436
    },
    'Liberia': {
        'nom': 'Liberia',
        'capitale': 'Monrovia',
        'latitude': 6.290743,
        'longitude': -10.760524
    },
    'Libya': {
        'nom': 'Libya',
        'capitale': 'Tripoli',
        'latitude': 32.887209,
        'longitude': 13.191338
    },
    'Liechtenstein': {
        'nom': 'Liechtenstein',
        'capitale': 'Vaduz',
        'latitude': 47.14103,
        'longitude': 9.520928
    },
    'Lithuania': {
        'nom': 'Lithuania',
        'capitale': 'Vilnius',
        'latitude': 54.687156,
        'longitude': 25.279651
    },
    'Luxembourg': {
        'nom': 'Luxembourg',
        'capitale': 'Luxembourg',
        'latitude': 49.611621,
        'longitude': 6.131935
    },
    'Macau': {
        'nom': 'Macau',
        'capitale': 'Macau',
        'latitude': 22.166667,
        'longitude': 113.55
    },
    'Macedonia': {
        'nom': 'Macedonia',
        'capitale': 'Skopje',
        'latitude': 41.997346,
        'longitude': 21.427996
    },
    'Madagascar': {
        'nom': 'Madagascar',
        'capitale': 'Antananarivo',
        'latitude': -18.87919,
        'longitude': 47.507905
    },
    'Malawi': {
        'nom': 'Malawi',
        'capitale': 'Lilongwe',
        'latitude': -13.962612,
        'longitude': 33.774119
    },
    'Malaysia': {
        'nom': 'Malaysia',
        'capitale': 'Kuala Lumpur',
        'latitude': 3.139003,
        'longitude': 101.686855
    },
    'Maldives': {
        'nom': 'Maldives',
        'capitale': 'Malé',
        'latitude': 4.175496,
        'longitude': 73.509347
    },
    'Mali': {
        'nom': 'Mali',
        'capitale': 'Bamako',
        'latitude': 12.639232,
        'longitude': -8.002889
    },
    'Malta': {
        'nom': 'Malta',
        'capitale': 'Valletta',
        'latitude': 35.898909,
        'longitude': 14.514553
    },
    'Marshall Islands': {
        'nom': 'Marshall Islands',
        'capitale': 'Majuro',
        'latitude': 7.116421,
        'longitude': 171.185774
    },
    'Martinique': {
        'nom': 'Martinique',
        'capitale': 'Fort-de-France',
        'latitude': 14.616065,
        'longitude': -61.05878
    },
    'Mauritania': {
        'nom': 'Mauritania',
        'capitale': 'Nouakchott',
        'latitude': 18.07353,
        'longitude': -15.958237
    },
    'Mauritius': {
        'nom': 'Mauritius',
        'capitale': 'Port Louis',
        'latitude': -20.166896,
        'longitude': 57.502332
    },
    'Mayotte': {
        'nom': 'Mayotte',
        'capitale': 'Mamoudzou',
        'latitude': -12.780949,
        'longitude': 45.227872
    },
    'Mexico': {
        'nom': 'Mexico',
        'capitale': 'Mexico City',
        'latitude': 19.432608,
        'longitude': -99.133208
    },
    'Micronesia': {
        'nom': 'Micronesia',
        'capitale': 'Palikir',
        'latitude': 6.914712,
        'longitude': 158.161027
    },
    'Moldova': {
        'nom': 'Moldova',
        'capitale': 'Chisinau',
        'latitude': 47.010453,
        'longitude': 28.86381
    },
    'Monaco': {
        'nom': 'Monaco',
        'capitale': 'Monaco',
        'latitude': 43.737411,
        'longitude': 7.420816
    },
    'Mongolia': {
        'nom': 'Mongolia',
        'capitale': 'Ulaanbaatar',
        'latitude': 47.886399,
        'longitude': 106.905744
    },
    'Montenegro': {
        'nom': 'Montenegro',
        'capitale': 'Podgorica',
        'latitude': 42.43042,
        'longitude': 19.259364
    },
    'Montserrat': {
        'nom': 'Montserrat',
        'capitale': 'Plymouth',
        'latitude': 16.706523,
        'longitude': -62.215738
    },
    'Morocco': {
        'nom': 'Morocco',
        'capitale': 'Rabat',
        'latitude': 33.97159,
        'longitude': -6.849813
    },
    'Mozambique': {
        'nom': 'Mozambique',
        'capitale': 'Maputo',
        'latitude': -25.891968,
        'longitude': 32.605135
    },
    'Myanmar': {
        'nom': 'Myanmar',
        'capitale': 'Naypyidaw',
        'latitude': 19.763306,
        'longitude': 96.07851
    },
    'Nagorno-Karabakh Republic': {
        'nom': 'Nagorno-Karabakh Republic',
        'capitale': 'Stepanakert',
        'latitude': 39.826385,
        'longitude': 46.763595
    },
    'Namibia': {
        'nom': 'Namibia',
        'capitale': 'Windhoek',
        'latitude': -22.560881,
        'longitude': 17.065755
    },
    'Nauru': {
        'nom': 'Nauru',
        'capitale': 'Yaren',
        'latitude': -0.546686,
        'longitude': 166.921091
    },
    'Nepal': {
        'nom': 'Nepal',
        'capitale': 'Kathmandu',
        'latitude': 27.717245,
        'longitude': 85.323961
    },
    'Netherlands': {
        'nom': 'Netherlands',
        'capitale': 'Amsterdam',
        'latitude': 52.370216,
        'longitude': 4.895168
    },
    'Netherlands Antilles': {
        'nom': 'Netherlands Antilles',
        'capitale': 'Willemstad ',
        'latitude': 12.1091242,
        'longitude': -68.9316546
    },
    'New Caledonia': {
        'nom': 'New Caledonia',
        'capitale': 'Nouméa',
        'latitude': -22.255823,
        'longitude': 166.450524
    },
    'New Zealand': {
        'nom': 'New Zealand',
        'capitale': 'Wellington',
        'latitude': -41.28646,
        'longitude': 174.776236
    },
    'Nicaragua': {
        'nom': 'Nicaragua',
        'capitale': 'Managua',
        'latitude': 12.114993,
        'longitude': -86.236174
    },
    'Niger': {
        'nom': 'Niger',
        'capitale': 'Niamey',
        'latitude': 13.511596,
        'longitude': 2.125385
    },
    'Nigeria': {
        'nom': 'Nigeria',
        'capitale': 'Abuja',
        'latitude': 9.076479,
        'longitude': 7.398574
    },
    'Niue': {
        'nom': 'Niue',
        'capitale': 'Alofi',
        'latitude': -19.055371,
        'longitude': -169.917871
    },
    'Norfolk Island': {
        'nom': 'Norfolk Island',
        'capitale': 'Kingston',
        'latitude': -29.056394,
        'longitude': 167.959588
    },
    'North Korea': {
        'nom': 'North Korea',
        'capitale': 'Pyongyang',
        'latitude': 39.039219,
        'longitude': 125.762524
    },
    'Northern Cyprus': {
        'nom': 'Northern Cyprus',
        'capitale': 'Nicosia',
        'latitude': 35.185566,
        'longitude': 33.382276
    },
    'Northern Mariana Islands': {
        'nom': 'Northern Mariana Islands',
        'capitale': 'Saipan',
        'latitude': 15.177801,
        'longitude': 145.750967
    },
    'Norway': {
        'nom': 'Norway',
        'capitale': 'Oslo',
        'latitude': 59.913869,
        'longitude': 10.752245
    },
    'Oman': {
        'nom': 'Oman',
        'capitale': 'Muscat',
        'latitude': 23.58589,
        'longitude': 58.405923
    },
    'Pakistan': {
        'nom': 'Pakistan',
        'capitale': 'Islamabad',
        'latitude': 33.729388,
        'longitude': 73.093146
    },
    'Palau': {
        'nom': 'Palau',
        'capitale': 'Ngerulmud',
        'latitude': 7.500384,
        'longitude': 134.624289
    },
    'Palestine': {
        'nom': 'Palestine',
        'capitale': 'Ramallah',
        'latitude': 31.9073509,
        'longitude': 35.5354719
    },
    'Panama': {
        'nom': 'Panama',
        'capitale': 'Panama City',
        'latitude': 9.101179,
        'longitude': -79.402864
    },
    'Papua New Guinea': {
        'nom': 'Papua New Guinea',
        'capitale': 'Port Moresby',
        'latitude': -9.4438,
        'longitude': 147.180267
    },
    'Paraguay': {
        'nom': 'Paraguay',
        'capitale': 'Asuncion',
        'latitude': -25.26374,
        'longitude': -57.575926
    },
    'Peru': {
        'nom': 'Peru',
        'capitale': 'Lima',
        'latitude': -12.046374,
        'longitude': -77.042793
    },
    'Philippines': {
        'nom': 'Philippines',
        'capitale': 'Manila',
        'latitude': 14.599512,
        'longitude': 120.98422
    },
    'Pitcairn Islands': {
        'nom': 'Pitcairn Islands',
        'capitale': 'Adamstown',
        'latitude': -25.06629,
        'longitude': -130.100464
    },
    'Poland': {
        'nom': 'Poland',
        'capitale': 'Warsaw',
        'latitude': 52.229676,
        'longitude': 21.012229
    },
    'Portugal': {
        'nom': 'Portugal',
        'capitale': 'Lisbon',
        'latitude': 38.722252,
        'longitude': -9.139337
    },
    'Puerto Rico': {
        'nom': 'Puerto Rico',
        'capitale': 'San Juan',
        'latitude': 18.466334,
        'longitude': -66.105722
    },
    'Qatar': {
        'nom': 'Qatar',
        'capitale': 'Doha',
        'latitude': 25.285447,
        'longitude': 51.53104
    },
    'Réunion': {
        'nom': 'Réunion',
        'capitale': 'Saint-Denis',
        'latitude': -20.882057,
        'longitude': 55.450675
    },
    'Romania': {
        'nom': 'Romania',
        'capitale': 'Bucharest',
        'latitude': 44.426767,
        'longitude': 26.102538
    },
    'Russia': {
        'nom': 'Russia',
        'capitale': 'Moscow',
        'latitude': 55.755826,
        'longitude': 37.6173
    },
    'Rwanda': {
        'nom': 'Rwanda',
        'capitale': 'Kigali',
        'latitude': -1.957875,
        'longitude': 30.112735
    },
    'Saint Pierre and Miquelon': {
        'nom': 'Saint Pierre and Miquelon',
        'capitale': 'St. Pierre',
        'latitude': 46.775846,
        'longitude': -56.180636
    },
    'Saint Vincent and the Grenadines': {
        'nom': 'Saint Vincent and the Grenadines',
        'capitale': 'Kingstown',
        'latitude': 13.160025,
        'longitude': -61.224816
    },
    'Samoa': {
        'nom': 'Samoa',
        'capitale': 'Apia',
        'latitude': -13.850696,
        'longitude': -171.751355
    },
    'San Marino': {
        'nom': 'San Marino',
        'capitale': 'San Marino',
        'latitude': 43.935591,
        'longitude': 12.447281
    },
    'São Tomé and Príncipe': {
        'nom': 'São Tomé and Príncipe',
        'capitale': 'São Tomé',
        'latitude': 0.330192,
        'longitude': 6.733343
    },
    'Saudi Arabia': {
        'nom': 'Saudi Arabia',
        'capitale': 'Riyadh',
        'latitude': 24.749403,
        'longitude': 46.902838
    },
    'Senegal': {
        'nom': 'Senegal',
        'capitale': 'Dakar',
        'latitude': 14.764504,
        'longitude': -17.366029
    },
    'Serbia': {
        'nom': 'Serbia',
        'capitale': 'Belgrade',
        'latitude': 44.786568,
        'longitude': 20.448922
    },
    'Seychelles': {
        'nom': 'Seychelles',
        'capitale': 'Victoria',
        'latitude': -4.619143,
        'longitude': 55.451315
    },
    'Sierra Leone': {
        'nom': 'Sierra Leone',
        'capitale': 'Freetown',
        'latitude': 8.465677,
        'longitude': -13.231722
    },
    'Singapore': {
        'nom': 'Singapore',
        'capitale': 'Singapore',
        'latitude': 1.280095,
        'longitude': 103.850949
    },
    'Slovakia': {
        'nom': 'Slovakia',
        'capitale': 'Bratislava',
        'latitude': 48.145892,
        'longitude': 17.107137
    },
    'Slovenia': {
        'nom': 'Slovenia',
        'capitale': 'Ljubljana',
        'latitude': 46.056947,
        'longitude': 14.505751
    },
    'Solomon Islands': {
        'nom': 'Solomon Islands',
        'capitale': 'Honiara',
        'latitude': -9.445638,
        'longitude': 159.9729
    },
    'Somalia': {
        'nom': 'Somalia',
        'capitale': 'Mogadishu',
        'latitude': 2.046934,
        'longitude': 45.318162
    },
    'South Africa': {
        'nom': 'South Africa',
        'capitale': 'Pretoria',
        'latitude': -25.747868,
        'longitude': 28.229271
    },
    'South Georgia and the South Sandwich Islands': {
        'nom': 'South Georgia and the South Sandwich Islands',
        'capitale': 'King Edward Point',
        'latitude': -54.28325,
        'longitude': -36.493735
    },
    'South Korea': {
        'nom': 'South Korea',
        'capitale': 'Seoul',
        'latitude': 37.566535,
        'longitude': 126.977969
    },
    'South Ossetia': {
        'nom': 'South Ossetia',
        'capitale': 'Tskhinvali',
        'latitude': 42.22146,
        'longitude': 43.964405
    },
    'South Sudan': {
        'nom': 'South Sudan',
        'capitale': 'Juba',
        'latitude': 4.859363,
        'longitude': 31.57125
    },
    'Spain': {
        'nom': 'Spain',
        'capitale': 'Madrid',
        'latitude': 40.416775,
        'longitude': -3.70379
    },
    'Sri Lanka': {
        'nom': 'Sri Lanka',
        'capitale': 'Sri Jayawardenepura Kotte',
        'latitude': 6.89407,
        'longitude': 79.902478
    },
    'St. Barthélemy': {
        'nom': 'St. Barthélemy',
        'capitale': 'Gustavia',
        'latitude': 17.896435,
        'longitude': -62.852201
    },
    'St. Kitts and Nevis': {
        'nom': 'St. Kitts and Nevis',
        'capitale': 'Basseterre',
        'latitude': 17.302606,
        'longitude': -62.717692
    },
    'St. Lucia': {
        'nom': 'St. Lucia',
        'capitale': 'Castries',
        'latitude': 14.010109,
        'longitude': -60.987469
    },
    'St. Martin': {
        'nom': 'St. Martin',
        'capitale': 'Marigot',
        'latitude': 18.067519,
        'longitude': -63.082466
    },
    'Sudan': {
        'nom': 'Sudan',
        'capitale': 'Khartoum',
        'latitude': 15.500654,
        'longitude': 32.559899
    },
    'Suriname': {
        'nom': 'Suriname',
        'capitale': 'Paramaribo',
        'latitude': 5.852036,
        'longitude': -55.203828
    },
    'Svalbard and Jan Mayen': {
        'nom': 'Svalbard and Jan Mayen',
        'capitale': 'Longyearbyen ',
        'latitude': 78.062,
        'longitude': 22.055
    },
    'Swaziland': {
        'nom': 'Swaziland',
        'capitale': 'Mbabane',
        'latitude': -26.305448,
        'longitude': 31.136672
    },
    'Sweden': {
        'nom': 'Sweden',
        'capitale': 'Stockholm',
        'latitude': 59.329323,
        'longitude': 18.068581
    },
    'Switzerland': {
        'nom': 'Switzerland',
        'capitale': 'Bern',
        'latitude': 46.947974,
        'longitude': 7.447447
    },
    'Syria': {
        'nom': 'Syria',
        'capitale': 'Damascus',
        'latitude': 33.513807,
        'longitude': 36.276528
    },
    'Taiwan': {
        'nom': 'Taiwan',
        'capitale': 'Taipei',
        'latitude': 25.032969,
        'longitude': 121.565418
    },
    'Tajikistan': {
        'nom': 'Tajikistan',
        'capitale': 'Dushanbe',
        'latitude': 38.559772,
        'longitude': 68.787038
    },
    'Tanzania': {
        'nom': 'Tanzania',
        'capitale': 'Dodoma',
        'latitude': -6.162959,
        'longitude': 35.751607
    },
    'Thailand': {
        'nom': 'Thailand',
        'capitale': 'Bangkok',
        'latitude': 13.756331,
        'longitude': 100.501765
    },
    'Timor-Leste': {
        'nom': 'Timor-Leste',
        'capitale': 'Dili',
        'latitude': -8.556856,
        'longitude': 125.560314
    },
    'Togo': {
        'nom': 'Togo',
        'capitale': 'Lomé',
        'latitude': 6.172497,
        'longitude': 1.231362
    },
    'Tokelau': {
        'nom': 'Tokelau',
        'capitale': 'Nukunonu',
        'latitude': -9.2005,
        'longitude': -171.848
    },
    'Tonga': {
        'nom': 'Tonga',
        'capitale': 'Nukuʻalofa',
        'latitude': -21.139342,
        'longitude': -175.204947
    },
    'Transnistria': {
        'nom': 'Transnistria',
        'capitale': 'Tiraspol',
        'latitude': 46.848185,
        'longitude': 29.596805
    },
    'Trinidad and Tobago': {
        'nom': 'Trinidad and Tobago',
        'capitale': 'Port of Spain',
        'latitude': 10.654901,
        'longitude': -61.501926
    },
    'Tristan da Cunha': {
        'nom': 'Tristan da Cunha',
        'capitale': 'Edinburgh of the Seven Seas',
        'latitude': -37.068042,
        'longitude': -12.311315
    },
    'Tunisia': {
        'nom': 'Tunisia',
        'capitale': 'Tunis',
        'latitude': 36.806495,
        'longitude': 10.181532
    },
    'Turkey': {
        'nom': 'Turkey',
        'capitale': 'Ankara',
        'latitude': 39.933364,
        'longitude': 32.859742
    },
    'Turkmenistan': {
        'nom': 'Turkmenistan',
        'capitale': 'Ashgabat',
        'latitude': 37.960077,
        'longitude': 58.326063
    },
    'Turks and Caicos Islands': {
        'nom': 'Turks and Caicos Islands',
        'capitale': 'Cockburn Town',
        'latitude': 21.467458,
        'longitude': -71.13891
    },
    'Tuvalu': {
        'nom': 'Tuvalu',
        'capitale': 'Funafuti',
        'latitude': -8.520066,
        'longitude': 179.198128
    },
    'U.S. Virgin Islands': {
        'nom': 'U.S. Virgin Islands',
        'capitale': 'Charlotte Amalie',
        'latitude': 18.3419,
        'longitude': -64.930701
    },
    'Uganda': {
        'nom': 'Uganda',
        'capitale': 'Kampala',
        'latitude': 0.347596,
        'longitude': 32.58252
    },
    'Ukraine': {
        'nom': 'Ukraine',
        'capitale': 'Kiev',
        'latitude': 50.4501,
        'longitude': 30.5234
    },
    'United Arab Emirates': {
        'nom': 'United Arab Emirates',
        'capitale': 'Abu Dhabi',
        'latitude': 24.299174,
        'longitude': 54.697277
    },
    'United Kingdom': {
        'nom': 'United Kingdom',
        'capitale': 'London',
        'latitude': 51.507351,
        'longitude': -0.127758
    },
    'United States': {
        'nom': 'United States',
        'capitale': 'Washington',
        'latitude': 38.907192,
        'longitude': -77.036871
    },
    'Uruguay': {
        'nom': 'Uruguay',
        'capitale': 'Montevideo',
        'latitude': -34.901113,
        'longitude': -56.164531
    },
    'Uzbekistan': {
        'nom': 'Uzbekistan',
        'capitale': 'Tashkent',
        'latitude': 41.299496,
        'longitude': 69.240073
    },
    'Vanuatu': {
        'nom': 'Vanuatu',
        'capitale': 'Port Vila',
        'latitude': -17.733251,
        'longitude': 168.327325
    },
    'Vatican City': {
        'nom': 'Vatican City',
        'capitale': 'Vatican City',
        'latitude': 41.902179,
        'longitude': 12.453601
    },
    'Venezuela': {
        'nom': 'Venezuela',
        'capitale': 'Caracas',
        'latitude': 10.480594,
        'longitude': -66.903606
    },
    'Vietnam': {
        'nom': 'Vietnam',
        'capitale': 'Hanoi',
        'latitude': 21.027764,
        'longitude': 105.83416
    },
    'Wallis and Futuna': {
        'nom': 'Wallis and Futuna',
        'capitale': 'Mata-Utu',
        'latitude': -13.282509,
        'longitude': -176.176447
    },
    'Western Sahara': {
        'nom': 'Western Sahara',
        'capitale': 'El Aaiún',
        'latitude': 27.125287,
        'longitude': -13.1625
    },
    'Yemen': {
        'nom': 'Yemen',
        'capitale': "Sana'a",
        'latitude': 15.369445,
        'longitude': 44.191007
    },
    'Zambia': {
        'nom': 'Zambia',
        'capitale': 'Lusaka',
        'latitude': -15.387526,
        'longitude': 28.322817
    },
    'Zimbabwe': {
        'nom': 'Zimbabwe',
        'capitale': 'Harare',
        'latitude': -17.825166,
        'longitude': 31.03351
    }
}


def convert_lat_long(latitude, longitude, map_width, map_height):

    false_easting = 180
    radius = map_width / (2 * pi)
    latitude = radians(latitude)
    longitude = radians(longitude + false_easting)

    x_coord = longitude * radius

    y_dist_from_equator = radius * log(tan(pi / 4 + latitude / 2))
    y_coord = map_height / 2 - y_dist_from_equator

    coords = {'x': x_coord, 'y': y_coord}

    return coords


def get_available_regions():
    return regions.keys()


def get_region_coords(region, map_width=991, map_height=768):
    coords = None

    try:
        lookup = regions[region]
        coords = convert_lat_long(
            lookup['latitude'], lookup['longitude'], map_width, map_height)
        return coords
    except KeyError:
        print('Region not recognised: ', region)
