#!/bin/python3
from math import radians, pi, log, tan

regios = {
    'Abkhazia': {
        'name': 'Abkhazia',
        'capital': 'Sukhumi',
        'breedtegraad': 43.001525,
        'lengtegraad': 41.023415
    },
    'Afghanistan': {
        'name': 'Afghanistan',
        'capital': 'Kabul',
        'breedtegraad': 34.575503,
        'lengtegraad': 69.240073
    },
    'Aland Islands': {
        'name': 'Aland Islands',
        'capital': 'Mariehamn',
        'breedtegraad': 60.1,
        'lengtegraad': 19.933333
    },
    'Albania': {
        'name': 'Albania',
        'capital': 'Tirana',
        'breedtegraad': 41.327546,
        'lengtegraad': 19.818698
    },
    'Algeria': {
        'name': 'Algeria',
        'capital': 'Algiers',
        'breedtegraad': 36.752887,
        'lengtegraad': 3.042048
    },
    'American Samoa': {
        'name': 'American Samoa',
        'capital': 'Pago Pago',
        'breedtegraad': -14.275632,
        'lengtegraad': -170.702036
    },
    'Andorra': {
        'name': 'Andorra',
        'capital': 'Andorra la Vella',
        'breedtegraad': 42.506317,
        'lengtegraad': 1.521835
    },
    'Angola': {
        'name': 'Angola',
        'capital': 'Luanda',
        'breedtegraad': -8.839988,
        'lengtegraad': 13.289437
    },
    'Anguilla': {
        'name': 'Anguilla',
        'capital': 'The Valley',
        'breedtegraad': 18.214813,
        'lengtegraad': -63.057441
    },
    'Antarctica': {
        'name': 'Antarctica',
        'capital': 'South Pole',
        'breedtegraad': -90.0,
        'lengtegraad': 0.0
    },
    'Antigua and Barbuda': {
        'name': 'Antigua and Barbuda',
        'capital': "St. John's",
        'breedtegraad': 17.12741,
        'lengtegraad': -61.846772
    },
    'Argentina': {
        'name': 'Argentina',
        'capital': 'Buenos Aires',
        'breedtegraad': -34.603684,
        'lengtegraad': -58.381559
    },
    'Armenia': {
        'name': 'Armenia',
        'capital': 'Yerevan',
        'breedtegraad': 40.179186,
        'lengtegraad': 44.499103
    },
    'Aruba': {
        'name': 'Aruba',
        'capital': 'Oranjestad',
        'breedtegraad': 12.509204,
        'lengtegraad': -70.008631
    },
    'Australia': {
        'name': 'Australia',
        'capital': 'Canberra',
        'breedtegraad': -35.282,
        'lengtegraad': 149.128684
    },
    'Austria': {
        'name': 'Austria',
        'capital': 'Vienna',
        'breedtegraad': 48.208174,
        'lengtegraad': 16.373819
    },
    'Azerbaijan': {
        'name': 'Azerbaijan',
        'capital': 'Baku',
        'breedtegraad': 40.409262,
        'lengtegraad': 49.867092
    },
    'Bahamas': {
        'name': 'Bahamas',
        'capital': 'Nassau',
        'breedtegraad': 25.047984,
        'lengtegraad': -77.355413
    },
    'Bahrain': {
        'name': 'Bahrain',
        'capital': 'Manama',
        'breedtegraad': 26.228516,
        'lengtegraad': 50.58605
    },
    'Bangladesh': {
        'name': 'Bangladesh',
        'capital': 'Dhaka',
        'breedtegraad': 23.810332,
        'lengtegraad': 90.412518
    },
    'Barbados': {
        'name': 'Barbados',
        'capital': 'Bridgetown',
        'breedtegraad': 13.113222,
        'lengtegraad': -59.598809
    },
    'Belarus': {
        'name': 'Belarus',
        'capital': 'Minsk',
        'breedtegraad': 53.90454,
        'lengtegraad': 27.561524
    },
    'Belgium': {
        'name': 'Belgium',
        'capital': 'Brussels',
        'breedtegraad': 50.85034,
        'lengtegraad': 4.35171
    },
    'Belize': {
        'name': 'Belize',
        'capital': 'Belmopan',
        'breedtegraad': 17.251011,
        'lengtegraad': -88.75902
    },
    'Benin': {
        'name': 'Benin',
        'capital': 'Porto-Novo',
        'breedtegraad': 6.496857,
        'lengtegraad': 2.628852
    },
    'Bermuda': {
        'name': 'Bermuda',
        'capital': 'Hamilton',
        'breedtegraad': 32.294816,
        'lengtegraad': -64.781375
    },
    'Bhutan': {
        'name': 'Bhutan',
        'capital': 'Thimphu',
        'breedtegraad': 27.472792,
        'lengtegraad': 89.639286
    },
    'Bolivia': {
        'name': 'Bolivia',
        'capital': 'La Paz',
        'breedtegraad': -16.489689,
        'lengtegraad': -68.119294
    },
    'Bosnia and Herzegovina': {
        'name': 'Bosnia and Herzegovina',
        'capital': 'Sarajevo',
        'breedtegraad': 43.856259,
        'lengtegraad': 18.413076
    },
    'Botswana': {
        'name': 'Botswana',
        'capital': 'Gaborone',
        'breedtegraad': -24.628208,
        'lengtegraad': 25.923147
    },
    'Bouvet Island': {
        'name': 'Bouvet Island',
        'capital': 'Bouvet Island',
        'breedtegraad': -54.43,
        'lengtegraad': 3.38
    },
    'Brazil': {
        'name': 'Brazil',
        'capital': 'Brasília',
        'breedtegraad': -15.794229,
        'lengtegraad': -47.882166
    },
    'British Indian Ocean Territory': {
        'name': 'British Indian Ocean Territory',
        'capital': 'Camp Justice',
        'breedtegraad': 21.3419,
        'lengtegraad': 55.4778
    },
    'British Virgin Islands': {
        'name': 'British Virgin Islands',
        'capital': 'Road Town',
        'breedtegraad': 18.428612,
        'lengtegraad': -64.618466
    },
    'Brunei': {
        'name': 'Brunei',
        'capital': 'Bandar Seri Begawan',
        'breedtegraad': 4.903052,
        'lengtegraad': 114.939821
    },
    'Bulgaria': {
        'name': 'Bulgaria',
        'capital': 'Sofia',
        'breedtegraad': 42.697708,
        'lengtegraad': 23.321868
    },
    'Burkina Faso': {
        'name': 'Burkina Faso',
        'capital': 'Ouagadougou',
        'breedtegraad': 12.371428,
        'lengtegraad': -1.51966
    },
    'Burundi': {
        'name': 'Burundi',
        'capital': 'Bujumbura',
        'breedtegraad': -3.361378,
        'lengtegraad': 29.359878
    },
    'Cambodia': {
        'name': 'Cambodia',
        'capital': 'Phnom Penh',
        'breedtegraad': 11.544873,
        'lengtegraad': 104.892167
    },
    'Cameroon': {
        'name': 'Cameroon',
        'capital': 'Yaoundé',
        'breedtegraad': 3.848033,
        'lengtegraad': 11.502075
    },
    'Canada': {
        'name': 'Canada',
        'capital': 'Ottawa',
        'breedtegraad': 45.42153,
        'lengtegraad': -75.697193
    },
    'Cape Verde': {
        'name': 'Cape Verde',
        'capital': 'Praia',
        'breedtegraad': 14.93305,
        'lengtegraad': -23.513327
    },
    'Cayman Islands': {
        'name': 'Cayman Islands',
        'capital': 'George Town',
        'breedtegraad': 19.286932,
        'lengtegraad': -81.367439
    },
    'Central African Republic': {
        'name': 'Central African Republic',
        'capital': 'Bangui',
        'breedtegraad': 4.394674,
        'lengtegraad': 18.55819
    },
    'Chad': {
        'name': 'Chad',
        'capital': "N'Djamena",
        'breedtegraad': 12.134846,
        'lengtegraad': 15.055742
    },
    'Chile': {
        'name': 'Chile',
        'capital': 'Santiago',
        'breedtegraad': -33.44889,
        'lengtegraad': -70.669265
    },
    'China': {
        'name': 'China',
        'capital': 'Beijing',
        'breedtegraad': 39.904211,
        'lengtegraad': 116.407395
    },
    'Christmas Island': {
        'name': 'Christmas Island',
        'capital': 'Flying Fish Cove',
        'breedtegraad': -10.420686,
        'lengtegraad': 105.679379
    },
    'Cocos (Keeling) Islands': {
        'name': 'Cocos (Keeling) Islands',
        'capital': 'West Island',
        'breedtegraad': -12.188834,
        'lengtegraad': 96.829316
    },
    'Colombia': {
        'name': 'Colombia',
        'capital': 'Bogotá',
        'breedtegraad': 4.710989,
        'lengtegraad': -74.072092
    },
    'Comoros': {
        'name': 'Comoros',
        'capital': 'Moroni',
        'breedtegraad': -11.717216,
        'lengtegraad': 43.247315
    },
    'Congo (DRC)': {
        'name': 'Congo (DRC)',
        'capital': 'Kinshasa',
        'breedtegraad': -4.441931,
        'lengtegraad': 15.266293
    },
    'Congo (Republic)': {
        'name': 'Congo (Republic)',
        'capital': 'Brazzaville',
        'breedtegraad': -4.26336,
        'lengtegraad': 15.242885
    },
    'Cook Islands': {
        'name': 'Cook Islands',
        'capital': 'Avarua',
        'breedtegraad': -21.212901,
        'lengtegraad': -159.782306
    },
    'Costa Rica': {
        'name': 'Costa Rica',
        'capital': 'San José',
        'breedtegraad': 9.928069,
        'lengtegraad': -84.090725
    },
    "Côte d'Ivoire": {
        'name': "Côte d'Ivoire",
        'capital': 'Yamoussoukro',
        'breedtegraad': 6.827623,
        'lengtegraad': -5.289343
    },
    'Croatia': {
        'name': 'Croatia',
        'capital': 'Zagreb ',
        'breedtegraad': 45.815011,
        'lengtegraad': 15.981919
    },
    'Cuba': {
        'name': 'Cuba',
        'capital': 'Havana',
        'breedtegraad': 23.05407,
        'lengtegraad': -82.345189
    },
    'Curaçao': {
        'name': 'Curaçao',
        'capital': 'Willemstad',
        'breedtegraad': 12.122422,
        'lengtegraad': -68.882423
    },
    'Cyprus': {
        'name': 'Cyprus',
        'capital': 'Nicosia',
        'breedtegraad': 35.185566,
        'lengtegraad': 33.382276
    },
    'Czech Republic': {
        'name': 'Czech Republic',
        'capital': 'Prague',
        'breedtegraad': 50.075538,
        'lengtegraad': 14.4378
    },
    'Denmark': {
        'name': 'Denmark',
        'capital': 'Copenhagen',
        'breedtegraad': 55.676097,
        'lengtegraad': 12.568337
    },
    'Djibouti': {
        'name': 'Djibouti',
        'capital': 'Djibouti',
        'breedtegraad': 11.572077,
        'lengtegraad': 43.145647
    },
    'Dominica': {
        'name': 'Dominica',
        'capital': 'Roseau',
        'breedtegraad': 15.309168,
        'lengtegraad': -61.379355
    },
    'Dominican Republic': {
        'name': 'Dominican Republic',
        'capital': 'Santo Domingo',
        'breedtegraad': 18.486058,
        'lengtegraad': -69.931212
    },
    'Ecuador': {
        'name': 'Ecuador',
        'capital': 'Quito',
        'breedtegraad': -0.180653,
        'lengtegraad': -78.467838
    },
    'Egypt': {
        'name': 'Egypt',
        'capital': 'Cairo',
        'breedtegraad': 30.04442,
        'lengtegraad': 31.235712
    },
    'El Salvador': {
        'name': 'El Salvador',
        'capital': 'San Salvador',
        'breedtegraad': 13.69294,
        'lengtegraad': -89.218191
    },
    'Equatorial Guinea': {
        'name': 'Equatorial Guinea',
        'capital': 'Malabo',
        'breedtegraad': 3.750412,
        'lengtegraad': 8.737104
    },
    'Eritrea': {
        'name': 'Eritrea',
        'capital': 'Asmara',
        'breedtegraad': 15.322877,
        'lengtegraad': 38.925052
    },
    'Estonia': {
        'name': 'Estonia',
        'capital': 'Tallinn',
        'breedtegraad': 59.436961,
        'lengtegraad': 24.753575
    },
    'Ethiopia': {
        'name': 'Ethiopia',
        'capital': 'Addis Ababa',
        'breedtegraad': 8.980603,
        'lengtegraad': 38.757761
    },
    'Falkland Islands (Islas Malvinas)': {
        'name': 'Falkland Islands (Islas Malvinas)',
        'capital': 'Stanley',
        'breedtegraad': -51.697713,
        'lengtegraad': -57.851663
    },
    'Faroe Islands': {
        'name': 'Faroe Islands',
        'capital': 'Tórshavn',
        'breedtegraad': 62.007864,
        'lengtegraad': -6.790982
    },
    'Fiji': {
        'name': 'Fiji',
        'capital': 'Suva',
        'breedtegraad': -18.124809,
        'lengtegraad': 178.450079
    },
    'Finland': {
        'name': 'Finland',
        'capital': 'Helsinki',
        'breedtegraad': 60.173324,
        'lengtegraad': 24.941025
    },
    'France': {
        'name': 'France',
        'capital': 'Paris',
        'breedtegraad': 48.856614,
        'lengtegraad': 2.352222
    },
    'French Guiana': {
        'name': 'French Guiana',
        'capital': 'Cayenne',
        'breedtegraad': 4.92242,
        'lengtegraad': -52.313453
    },
    'French Polynesia': {
        'name': 'French Polynesia',
        'capital': 'Papeete',
        'breedtegraad': -17.551625,
        'lengtegraad': -149.558476
    },
    'French Southern Territories': {
        'name': 'French Southern Territories',
        'capital': 'Saint-Pierre ',
        'breedtegraad': -21.3419,
        'lengtegraad': 55.4778
    },
    'Gabon': {
        'name': 'Gabon',
        'capital': 'Libreville',
        'breedtegraad': 0.416198,
        'lengtegraad': 9.467268
    },
    'Gambia': {
        'name': 'Gambia',
        'capital': 'Banjul',
        'breedtegraad': 13.454876,
        'lengtegraad': -16.579032
    },
    'Georgia': {
        'name': 'Georgia',
        'capital': 'Tbilisi',
        'breedtegraad': 41.715138,
        'lengtegraad': 44.827096
    },
    'Germany': {
        'name': 'Germany',
        'capital': 'Berlin',
        'breedtegraad': 52.520007,
        'lengtegraad': 13.404954
    },
    'Ghana': {
        'name': 'Ghana',
        'capital': 'Accra',
        'breedtegraad': 5.603717,
        'lengtegraad': -0.186964
    },
    'Gibraltar': {
        'name': 'Gibraltar',
        'capital': 'Gibraltar',
        'breedtegraad': 36.140773,
        'lengtegraad': -5.353599
    },
    'Greece': {
        'name': 'Greece',
        'capital': 'Athens',
        'breedtegraad': 37.983917,
        'lengtegraad': 23.72936
    },
    'Greenland': {
        'name': 'Greenland',
        'capital': 'Nuuk',
        'breedtegraad': 64.18141,
        'lengtegraad': -51.694138
    },
    'Grenada': {
        'name': 'Grenada',
        'capital': "St. George's",
        'breedtegraad': 12.056098,
        'lengtegraad': -61.7488
    },
    'Guadeloupe': {
        'name': 'Guadeloupe',
        'capital': 'Basse-Terre',
        'breedtegraad': 16.014453,
        'lengtegraad': -61.706411
    },
    'Guam': {
        'name': 'Guam',
        'capital': 'Hagåtña',
        'breedtegraad': 13.470891,
        'lengtegraad': 144.751278
    },
    'Guatemala': {
        'name': 'Guatemala',
        'capital': 'Guatemala City',
        'breedtegraad': 14.634915,
        'lengtegraad': -90.506882
    },
    'Guernsey': {
        'name': 'Guernsey',
        'capital': 'St. Peter Port',
        'breedtegraad': 49.455443,
        'lengtegraad': -2.536871
    },
    'Guinea': {
        'name': 'Guinea',
        'capital': 'Conakry',
        'breedtegraad': 9.641185,
        'lengtegraad': -13.578401
    },
    'Guinea-Bissau': {
        'name': 'Guinea-Bissau',
        'capital': 'Bissau',
        'breedtegraad': 11.881655,
        'lengtegraad': -15.617794
    },
    'Guyana': {
        'name': 'Guyana',
        'capital': 'Georgetown',
        'breedtegraad': 6.801279,
        'lengtegraad': -58.155125
    },
    'Haiti': {
        'name': 'Haiti',
        'capital': 'Port-au-Prince',
        'breedtegraad': 18.594395,
        'lengtegraad': -72.307433
    },
    'Honduras': {
        'name': 'Honduras',
        'capital': 'Tegucigalpa',
        'breedtegraad': 14.072275,
        'lengtegraad': -87.192136
    },
    'Hong Kong': {
        'name': 'Hong Kong',
        'capital': 'Hong Kong',
        'breedtegraad': 22.396428,
        'lengtegraad': 114.109497
    },
    'Hungary': {
        'name': 'Hungary',
        'capital': 'Budapest',
        'breedtegraad': 47.497912,
        'lengtegraad': 19.040235
    },
    'Iceland': {
        'name': 'Iceland',
        'capital': 'Reykjavík',
        'breedtegraad': 64.126521,
        'lengtegraad': -21.817439
    },
    'India': {
        'name': 'India',
        'capital': 'New Delhi',
        'breedtegraad': 28.613939,
        'lengtegraad': 77.209021
    },
    'Indonesia': {
        'name': 'Indonesia',
        'capital': 'Jakarta',
        'breedtegraad': -6.208763,
        'lengtegraad': 106.845599
    },
    'Iran': {
        'name': 'Iran',
        'capital': 'Tehran',
        'breedtegraad': 35.689198,
        'lengtegraad': 51.388974
    },
    'Iraq': {
        'name': 'Iraq',
        'capital': 'Baghdad',
        'breedtegraad': 33.312806,
        'lengtegraad': 44.361488
    },
    'Ireland': {
        'name': 'Ireland',
        'capital': 'Dublin',
        'breedtegraad': 53.349805,
        'lengtegraad': -6.26031
    },
    'Isle of Man': {
        'name': 'Isle of Man',
        'capital': 'Douglas',
        'breedtegraad': 54.152337,
        'lengtegraad': -4.486123
    },
    'Israel': {
        'name': 'Israel',
        'capital': 'Tel Aviv',
        'breedtegraad': 32.0853,
        'lengtegraad': 34.781768
    },
    'Italy': {
        'name': 'Italy',
        'capital': 'Rome',
        'breedtegraad': 41.902784,
        'lengtegraad': 12.496366
    },
    'Jamaica': {
        'name': 'Jamaica',
        'capital': 'Kingston',
        'breedtegraad': 18.042327,
        'lengtegraad': -76.802893
    },
    'Japan': {
        'name': 'Japan',
        'capital': 'Tokyo',
        'breedtegraad': 35.709026,
        'lengtegraad': 139.731992
    },
    'Jersey': {
        'name': 'Jersey',
        'capital': 'St. Helier',
        'breedtegraad': 49.186823,
        'lengtegraad': -2.106568
    },
    'Jordan': {
        'name': 'Jordan',
        'capital': 'Amman',
        'breedtegraad': 31.956578,
        'lengtegraad': 35.945695
    },
    'Kazakhstan': {
        'name': 'Kazakhstan',
        'capital': 'Astana',
        'breedtegraad': 51.160523,
        'lengtegraad': 71.470356
    },
    'Kenya': {
        'name': 'Kenya',
        'capital': 'Nairobi',
        'breedtegraad': -1.292066,
        'lengtegraad': 36.821946
    },
    'Kiribati': {
        'name': 'Kiribati',
        'capital': 'Tarawa Atoll',
        'breedtegraad': 1.451817,
        'lengtegraad': 172.971662
    },
    'Kosovo': {
        'name': 'Kosovo',
        'capital': 'Pristina',
        'breedtegraad': 42.662914,
        'lengtegraad': 21.165503
    },
    'Kuwait': {
        'name': 'Kuwait',
        'capital': 'Kuwait City',
        'breedtegraad': 29.375859,
        'lengtegraad': 47.977405
    },
    'Kyrgyzstan': {
        'name': 'Kyrgyzstan',
        'capital': 'Bishkek',
        'breedtegraad': 42.874621,
        'lengtegraad': 74.569762
    },
    'Laos': {
        'name': 'Laos',
        'capital': 'Vientiane',
        'breedtegraad': 17.975706,
        'lengtegraad': 102.633104
    },
    'Latvia': {
        'name': 'Latvia',
        'capital': 'Riga',
        'breedtegraad': 56.949649,
        'lengtegraad': 24.105186
    },
    'Lebanon': {
        'name': 'Lebanon',
        'capital': 'Beirut',
        'breedtegraad': 33.888629,
        'lengtegraad': 35.495479
    },
    'Lesotho': {
        'name': 'Lesotho',
        'capital': 'Maseru',
        'breedtegraad': -29.363219,
        'lengtegraad': 27.51436
    },
    'Liberia': {
        'name': 'Liberia',
        'capital': 'Monrovia',
        'breedtegraad': 6.290743,
        'lengtegraad': -10.760524
    },
    'Libya': {
        'name': 'Libya',
        'capital': 'Tripoli',
        'breedtegraad': 32.887209,
        'lengtegraad': 13.191338
    },
    'Liechtenstein': {
        'name': 'Liechtenstein',
        'capital': 'Vaduz',
        'breedtegraad': 47.14103,
        'lengtegraad': 9.520928
    },
    'Lithuania': {
        'name': 'Lithuania',
        'capital': 'Vilnius',
        'breedtegraad': 54.687156,
        'lengtegraad': 25.279651
    },
    'Luxembourg': {
        'name': 'Luxembourg',
        'capital': 'Luxembourg',
        'breedtegraad': 49.611621,
        'lengtegraad': 6.131935
    },
    'Macau': {
        'name': 'Macau',
        'capital': 'Macau',
        'breedtegraad': 22.166667,
        'lengtegraad': 113.55
    },
    'Macedonia': {
        'name': 'Macedonia',
        'capital': 'Skopje',
        'breedtegraad': 41.997346,
        'lengtegraad': 21.427996
    },
    'Madagascar': {
        'name': 'Madagascar',
        'capital': 'Antananarivo',
        'breedtegraad': -18.87919,
        'lengtegraad': 47.507905
    },
    'Malawi': {
        'name': 'Malawi',
        'capital': 'Lilongwe',
        'breedtegraad': -13.962612,
        'lengtegraad': 33.774119
    },
    'Malaysia': {
        'name': 'Malaysia',
        'capital': 'Kuala Lumpur',
        'breedtegraad': 3.139003,
        'lengtegraad': 101.686855
    },
    'Maldives': {
        'name': 'Maldives',
        'capital': 'Malé',
        'breedtegraad': 4.175496,
        'lengtegraad': 73.509347
    },
    'Mali': {
        'name': 'Mali',
        'capital': 'Bamako',
        'breedtegraad': 12.639232,
        'lengtegraad': -8.002889
    },
    'Malta': {
        'name': 'Malta',
        'capital': 'Valletta',
        'breedtegraad': 35.898909,
        'lengtegraad': 14.514553
    },
    'Marshall Islands': {
        'name': 'Marshall Islands',
        'capital': 'Majuro',
        'breedtegraad': 7.116421,
        'lengtegraad': 171.185774
    },
    'Martinique': {
        'name': 'Martinique',
        'capital': 'Fort-de-France',
        'breedtegraad': 14.616065,
        'lengtegraad': -61.05878
    },
    'Mauritania': {
        'name': 'Mauritania',
        'capital': 'Nouakchott',
        'breedtegraad': 18.07353,
        'lengtegraad': -15.958237
    },
    'Mauritius': {
        'name': 'Mauritius',
        'capital': 'Port Louis',
        'breedtegraad': -20.166896,
        'lengtegraad': 57.502332
    },
    'Mayotte': {
        'name': 'Mayotte',
        'capital': 'Mamoudzou',
        'breedtegraad': -12.780949,
        'lengtegraad': 45.227872
    },
    'Mexico': {
        'name': 'Mexico',
        'capital': 'Mexico City',
        'breedtegraad': 19.432608,
        'lengtegraad': -99.133208
    },
    'Micronesia': {
        'name': 'Micronesia',
        'capital': 'Palikir',
        'breedtegraad': 6.914712,
        'lengtegraad': 158.161027
    },
    'Moldova': {
        'name': 'Moldova',
        'capital': 'Chisinau',
        'breedtegraad': 47.010453,
        'lengtegraad': 28.86381
    },
    'Monaco': {
        'name': 'Monaco',
        'capital': 'Monaco',
        'breedtegraad': 43.737411,
        'lengtegraad': 7.420816
    },
    'Mongolia': {
        'name': 'Mongolia',
        'capital': 'Ulaanbaatar',
        'breedtegraad': 47.886399,
        'lengtegraad': 106.905744
    },
    'Montenegro': {
        'name': 'Montenegro',
        'capital': 'Podgorica',
        'breedtegraad': 42.43042,
        'lengtegraad': 19.259364
    },
    'Montserrat': {
        'name': 'Montserrat',
        'capital': 'Plymouth',
        'breedtegraad': 16.706523,
        'lengtegraad': -62.215738
    },
    'Morocco': {
        'name': 'Morocco',
        'capital': 'Rabat',
        'breedtegraad': 33.97159,
        'lengtegraad': -6.849813
    },
    'Mozambique': {
        'name': 'Mozambique',
        'capital': 'Maputo',
        'breedtegraad': -25.891968,
        'lengtegraad': 32.605135
    },
    'Myanmar': {
        'name': 'Myanmar',
        'capital': 'Naypyidaw',
        'breedtegraad': 19.763306,
        'lengtegraad': 96.07851
    },
    'Nagorno-Karabakh Republic': {
        'name': 'Nagorno-Karabakh Republic',
        'capital': 'Stepanakert',
        'breedtegraad': 39.826385,
        'lengtegraad': 46.763595
    },
    'Namibia': {
        'name': 'Namibia',
        'capital': 'Windhoek',
        'breedtegraad': -22.560881,
        'lengtegraad': 17.065755
    },
    'Nauru': {
        'name': 'Nauru',
        'capital': 'Yaren',
        'breedtegraad': -0.546686,
        'lengtegraad': 166.921091
    },
    'Nepal': {
        'name': 'Nepal',
        'capital': 'Kathmandu',
        'breedtegraad': 27.717245,
        'lengtegraad': 85.323961
    },
    'Netherlands': {
        'name': 'Netherlands',
        'capital': 'Amsterdam',
        'breedtegraad': 52.370216,
        'lengtegraad': 4.895168
    },
    'Netherlands Antilles': {
        'name': 'Netherlands Antilles',
        'capital': 'Willemstad ',
        'breedtegraad': 12.1091242,
        'lengtegraad': -68.9316546
    },
    'New Caledonia': {
        'name': 'New Caledonia',
        'capital': 'Nouméa',
        'breedtegraad': -22.255823,
        'lengtegraad': 166.450524
    },
    'New Zealand': {
        'name': 'New Zealand',
        'capital': 'Wellington',
        'breedtegraad': -41.28646,
        'lengtegraad': 174.776236
    },
    'Nicaragua': {
        'name': 'Nicaragua',
        'capital': 'Managua',
        'breedtegraad': 12.114993,
        'lengtegraad': -86.236174
    },
    'Niger': {
        'name': 'Niger',
        'capital': 'Niamey',
        'breedtegraad': 13.511596,
        'lengtegraad': 2.125385
    },
    'Nigeria': {
        'name': 'Nigeria',
        'capital': 'Abuja',
        'breedtegraad': 9.076479,
        'lengtegraad': 7.398574
    },
    'Niue': {
        'name': 'Niue',
        'capital': 'Alofi',
        'breedtegraad': -19.055371,
        'lengtegraad': -169.917871
    },
    'Norfolk Island': {
        'name': 'Norfolk Island',
        'capital': 'Kingston',
        'breedtegraad': -29.056394,
        'lengtegraad': 167.959588
    },
    'North Korea': {
        'name': 'North Korea',
        'capital': 'Pyongyang',
        'breedtegraad': 39.039219,
        'lengtegraad': 125.762524
    },
    'Northern Cyprus': {
        'name': 'Northern Cyprus',
        'capital': 'Nicosia',
        'breedtegraad': 35.185566,
        'lengtegraad': 33.382276
    },
    'Northern Mariana Islands': {
        'name': 'Northern Mariana Islands',
        'capital': 'Saipan',
        'breedtegraad': 15.177801,
        'lengtegraad': 145.750967
    },
    'Norway': {
        'name': 'Norway',
        'capital': 'Oslo',
        'breedtegraad': 59.913869,
        'lengtegraad': 10.752245
    },
    'Oman': {
        'name': 'Oman',
        'capital': 'Muscat',
        'breedtegraad': 23.58589,
        'lengtegraad': 58.405923
    },
    'Pakistan': {
        'name': 'Pakistan',
        'capital': 'Islamabad',
        'breedtegraad': 33.729388,
        'lengtegraad': 73.093146
    },
    'Palau': {
        'name': 'Palau',
        'capital': 'Ngerulmud',
        'breedtegraad': 7.500384,
        'lengtegraad': 134.624289
    },
    'Palestine': {
        'name': 'Palestine',
        'capital': 'Ramallah',
        'breedtegraad': 31.9073509,
        'lengtegraad': 35.5354719
    },
    'Panama': {
        'name': 'Panama',
        'capital': 'Panama City',
        'breedtegraad': 9.101179,
        'lengtegraad': -79.402864
    },
    'Papua New Guinea': {
        'name': 'Papua New Guinea',
        'capital': 'Port Moresby',
        'breedtegraad': -9.4438,
        'lengtegraad': 147.180267
    },
    'Paraguay': {
        'name': 'Paraguay',
        'capital': 'Asuncion',
        'breedtegraad': -25.26374,
        'lengtegraad': -57.575926
    },
    'Peru': {
        'name': 'Peru',
        'capital': 'Lima',
        'breedtegraad': -12.046374,
        'lengtegraad': -77.042793
    },
    'Philippines': {
        'name': 'Philippines',
        'capital': 'Manila',
        'breedtegraad': 14.599512,
        'lengtegraad': 120.98422
    },
    'Pitcairn Islands': {
        'name': 'Pitcairn Islands',
        'capital': 'Adamstown',
        'breedtegraad': -25.06629,
        'lengtegraad': -130.100464
    },
    'Poland': {
        'name': 'Poland',
        'capital': 'Warsaw',
        'breedtegraad': 52.229676,
        'lengtegraad': 21.012229
    },
    'Portugal': {
        'name': 'Portugal',
        'capital': 'Lisbon',
        'breedtegraad': 38.722252,
        'lengtegraad': -9.139337
    },
    'Puerto Rico': {
        'name': 'Puerto Rico',
        'capital': 'San Juan',
        'breedtegraad': 18.466334,
        'lengtegraad': -66.105722
    },
    'Qatar': {
        'name': 'Qatar',
        'capital': 'Doha',
        'breedtegraad': 25.285447,
        'lengtegraad': 51.53104
    },
    'Réunion': {
        'name': 'Réunion',
        'capital': 'Saint-Denis',
        'breedtegraad': -20.882057,
        'lengtegraad': 55.450675
    },
    'Romania': {
        'name': 'Romania',
        'capital': 'Bucharest',
        'breedtegraad': 44.426767,
        'lengtegraad': 26.102538
    },
    'Russia': {
        'name': 'Russia',
        'capital': 'Moscow',
        'breedtegraad': 55.755826,
        'lengtegraad': 37.6173
    },
    'Rwanda': {
        'name': 'Rwanda',
        'capital': 'Kigali',
        'breedtegraad': -1.957875,
        'lengtegraad': 30.112735
    },
    'Saint Pierre and Miquelon': {
        'name': 'Saint Pierre and Miquelon',
        'capital': 'St. Pierre',
        'breedtegraad': 46.775846,
        'lengtegraad': -56.180636
    },
    'Saint Vincent and the Grenadines': {
        'name': 'Saint Vincent and the Grenadines',
        'capital': 'Kingstown',
        'breedtegraad': 13.160025,
        'lengtegraad': -61.224816
    },
    'Samoa': {
        'name': 'Samoa',
        'capital': 'Apia',
        'breedtegraad': -13.850696,
        'lengtegraad': -171.751355
    },
    'San Marino': {
        'name': 'San Marino',
        'capital': 'San Marino',
        'breedtegraad': 43.935591,
        'lengtegraad': 12.447281
    },
    'São Tomé and Príncipe': {
        'name': 'São Tomé and Príncipe',
        'capital': 'São Tomé',
        'breedtegraad': 0.330192,
        'lengtegraad': 6.733343
    },
    'Saudi Arabia': {
        'name': 'Saudi Arabia',
        'capital': 'Riyadh',
        'breedtegraad': 24.749403,
        'lengtegraad': 46.902838
    },
    'Senegal': {
        'name': 'Senegal',
        'capital': 'Dakar',
        'breedtegraad': 14.764504,
        'lengtegraad': -17.366029
    },
    'Serbia': {
        'name': 'Serbia',
        'capital': 'Belgrade',
        'breedtegraad': 44.786568,
        'lengtegraad': 20.448922
    },
    'Seychelles': {
        'name': 'Seychelles',
        'capital': 'Victoria',
        'breedtegraad': -4.619143,
        'lengtegraad': 55.451315
    },
    'Sierra Leone': {
        'name': 'Sierra Leone',
        'capital': 'Freetown',
        'breedtegraad': 8.465677,
        'lengtegraad': -13.231722
    },
    'Singapore': {
        'name': 'Singapore',
        'capital': 'Singapore',
        'breedtegraad': 1.280095,
        'lengtegraad': 103.850949
    },
    'Slovakia': {
        'name': 'Slovakia',
        'capital': 'Bratislava',
        'breedtegraad': 48.145892,
        'lengtegraad': 17.107137
    },
    'Slovenia': {
        'name': 'Slovenia',
        'capital': 'Ljubljana',
        'breedtegraad': 46.056947,
        'lengtegraad': 14.505751
    },
    'Solomon Islands': {
        'name': 'Solomon Islands',
        'capital': 'Honiara',
        'breedtegraad': -9.445638,
        'lengtegraad': 159.9729
    },
    'Somalia': {
        'name': 'Somalia',
        'capital': 'Mogadishu',
        'breedtegraad': 2.046934,
        'lengtegraad': 45.318162
    },
    'South Africa': {
        'name': 'South Africa',
        'capital': 'Pretoria',
        'breedtegraad': -25.747868,
        'lengtegraad': 28.229271
    },
    'South Georgia and the South Sandwich Islands': {
        'name': 'South Georgia and the South Sandwich Islands',
        'capital': 'King Edward Point',
        'breedtegraad': -54.28325,
        'lengtegraad': -36.493735
    },
    'South Korea': {
        'name': 'South Korea',
        'capital': 'Seoul',
        'breedtegraad': 37.566535,
        'lengtegraad': 126.977969
    },
    'South Ossetia': {
        'name': 'South Ossetia',
        'capital': 'Tskhinvali',
        'breedtegraad': 42.22146,
        'lengtegraad': 43.964405
    },
    'South Sudan': {
        'name': 'South Sudan',
        'capital': 'Juba',
        'breedtegraad': 4.859363,
        'lengtegraad': 31.57125
    },
    'Spain': {
        'name': 'Spain',
        'capital': 'Madrid',
        'breedtegraad': 40.416775,
        'lengtegraad': -3.70379
    },
    'Sri Lanka': {
        'name': 'Sri Lanka',
        'capital': 'Sri Jayawardenepura Kotte',
        'breedtegraad': 6.89407,
        'lengtegraad': 79.902478
    },
    'St. Barthélemy': {
        'name': 'St. Barthélemy',
        'capital': 'Gustavia',
        'breedtegraad': 17.896435,
        'lengtegraad': -62.852201
    },
    'St. Kitts and Nevis': {
        'name': 'St. Kitts and Nevis',
        'capital': 'Basseterre',
        'breedtegraad': 17.302606,
        'lengtegraad': -62.717692
    },
    'St. Lucia': {
        'name': 'St. Lucia',
        'capital': 'Castries',
        'breedtegraad': 14.010109,
        'lengtegraad': -60.987469
    },
    'St. Martin': {
        'name': 'St. Martin',
        'capital': 'Marigot',
        'breedtegraad': 18.067519,
        'lengtegraad': -63.082466
    },
    'Sudan': {
        'name': 'Sudan',
        'capital': 'Khartoum',
        'breedtegraad': 15.500654,
        'lengtegraad': 32.559899
    },
    'Suriname': {
        'name': 'Suriname',
        'capital': 'Paramaribo',
        'breedtegraad': 5.852036,
        'lengtegraad': -55.203828
    },
    'Svalbard and Jan Mayen': {
        'name': 'Svalbard and Jan Mayen',
        'capital': 'Longyearbyen ',
        'breedtegraad': 78.062,
        'lengtegraad': 22.055
    },
    'Swaziland': {
        'name': 'Swaziland',
        'capital': 'Mbabane',
        'breedtegraad': -26.305448,
        'lengtegraad': 31.136672
    },
    'Sweden': {
        'name': 'Sweden',
        'capital': 'Stockholm',
        'breedtegraad': 59.329323,
        'lengtegraad': 18.068581
    },
    'Switzerland': {
        'name': 'Switzerland',
        'capital': 'Bern',
        'breedtegraad': 46.947974,
        'lengtegraad': 7.447447
    },
    'Syria': {
        'name': 'Syria',
        'capital': 'Damascus',
        'breedtegraad': 33.513807,
        'lengtegraad': 36.276528
    },
    'Taiwan': {
        'name': 'Taiwan',
        'capital': 'Taipei',
        'breedtegraad': 25.032969,
        'lengtegraad': 121.565418
    },
    'Tajikistan': {
        'name': 'Tajikistan',
        'capital': 'Dushanbe',
        'breedtegraad': 38.559772,
        'lengtegraad': 68.787038
    },
    'Tanzania': {
        'name': 'Tanzania',
        'capital': 'Dodoma',
        'breedtegraad': -6.162959,
        'lengtegraad': 35.751607
    },
    'Thailand': {
        'name': 'Thailand',
        'capital': 'Bangkok',
        'breedtegraad': 13.756331,
        'lengtegraad': 100.501765
    },
    'Timor-Leste': {
        'name': 'Timor-Leste',
        'capital': 'Dili',
        'breedtegraad': -8.556856,
        'lengtegraad': 125.560314
    },
    'Togo': {
        'name': 'Togo',
        'capital': 'Lomé',
        'breedtegraad': 6.172497,
        'lengtegraad': 1.231362
    },
    'Tokelau': {
        'name': 'Tokelau',
        'capital': 'Nukunonu',
        'breedtegraad': -9.2005,
        'lengtegraad': -171.848
    },
    'Tonga': {
        'name': 'Tonga',
        'capital': 'Nukuʻalofa',
        'breedtegraad': -21.139342,
        'lengtegraad': -175.204947
    },
    'Transnistria': {
        'name': 'Transnistria',
        'capital': 'Tiraspol',
        'breedtegraad': 46.848185,
        'lengtegraad': 29.596805
    },
    'Trinidad and Tobago': {
        'name': 'Trinidad and Tobago',
        'capital': 'Port of Spain',
        'breedtegraad': 10.654901,
        'lengtegraad': -61.501926
    },
    'Tristan da Cunha': {
        'name': 'Tristan da Cunha',
        'capital': 'Edinburgh of the Seven Seas',
        'breedtegraad': -37.068042,
        'lengtegraad': -12.311315
    },
    'Tunisia': {
        'name': 'Tunisia',
        'capital': 'Tunis',
        'breedtegraad': 36.806495,
        'lengtegraad': 10.181532
    },
    'Turkey': {
        'name': 'Turkey',
        'capital': 'Ankara',
        'breedtegraad': 39.933364,
        'lengtegraad': 32.859742
    },
    'Turkmenistan': {
        'name': 'Turkmenistan',
        'capital': 'Ashgabat',
        'breedtegraad': 37.960077,
        'lengtegraad': 58.326063
    },
    'Turks and Caicos Islands': {
        'name': 'Turks and Caicos Islands',
        'capital': 'Cockburn Town',
        'breedtegraad': 21.467458,
        'lengtegraad': -71.13891
    },
    'Tuvalu': {
        'name': 'Tuvalu',
        'capital': 'Funafuti',
        'breedtegraad': -8.520066,
        'lengtegraad': 179.198128
    },
    'U.S. Virgin Islands': {
        'name': 'U.S. Virgin Islands',
        'capital': 'Charlotte Amalie',
        'breedtegraad': 18.3419,
        'lengtegraad': -64.930701
    },
    'Uganda': {
        'name': 'Uganda',
        'capital': 'Kampala',
        'breedtegraad': 0.347596,
        'lengtegraad': 32.58252
    },
    'Ukraine': {
        'name': 'Ukraine',
        'capital': 'Kyiv',
        'breedtegraad': 50.4501,
        'lengtegraad': 30.5234
    },
    'United Arab Emirates': {
        'name': 'United Arab Emirates',
        'capital': 'Abu Dhabi',
        'breedtegraad': 24.299174,
        'lengtegraad': 54.697277
    },
    'United Kingdom': {
        'name': 'United Kingdom',
        'capital': 'London',
        'breedtegraad': 51.507351,
        'lengtegraad': -0.127758
    },
    'United States': {
        'name': 'United States',
        'capital': 'Washington',
        'breedtegraad': 38.907192,
        'lengtegraad': -77.036871
    },
    'Uruguay': {
        'name': 'Uruguay',
        'capital': 'Montevideo',
        'breedtegraad': -34.901113,
        'lengtegraad': -56.164531
    },
    'Uzbekistan': {
        'name': 'Uzbekistan',
        'capital': 'Tashkent',
        'breedtegraad': 41.299496,
        'lengtegraad': 69.240073
    },
    'Vanuatu': {
        'name': 'Vanuatu',
        'capital': 'Port Vila',
        'breedtegraad': -17.733251,
        'lengtegraad': 168.327325
    },
    'Vatican City': {
        'name': 'Vatican City',
        'capital': 'Vatican City',
        'breedtegraad': 41.902179,
        'lengtegraad': 12.453601
    },
    'Venezuela': {
        'name': 'Venezuela',
        'capital': 'Caracas',
        'breedtegraad': 10.480594,
        'lengtegraad': -66.903606
    },
    'Vietnam': {
        'name': 'Vietnam',
        'capital': 'Hanoi',
        'breedtegraad': 21.027764,
        'lengtegraad': 105.83416
    },
    'Wallis and Futuna': {
        'name': 'Wallis and Futuna',
        'capital': 'Mata-Utu',
        'breedtegraad': -13.282509,
        'lengtegraad': -176.176447
    },
    'Western Sahara': {
        'name': 'Western Sahara',
        'capital': 'El Aaiún',
        'breedtegraad': 27.125287,
        'lengtegraad': -13.1625
    },
    'Yemen': {
        'name': 'Yemen',
        'capital': "Sana'a",
        'breedtegraad': 15.369445,
        'lengtegraad': 44.191007
    },
    'Zambia': {
        'name': 'Zambia',
        'capital': 'Lusaka',
        'breedtegraad': -15.387526,
        'lengtegraad': 28.322817
    },
    'Zimbabwe': {
        'name': 'Zimbabwe',
        'capital': 'Harare',
        'breedtegraad': -17.825166,
        'lengtegraad': 31.03351
    }
}


def convert_bre_leng(breedtegraad, lengtegraad, kaart_breedte, kaart_hoogte):

    false_easting = 180
    straal = kaart_breedte / (2 * pi)
    breedtegraad = radians(breedtegraad)
    lengtegraad = radians(lengtegraad + false_easting)

    x_coord = lengtegraad * straal

    y_afst_van_evenaar = straal * log(tan(pi / 4 + breedtegraad / 2))
    y_coord = kaart_hoogte / 2 - y_afst_van_evenaar

    coordinaten = {'x': x_coord, 'y': y_coord}

    return coordinaten


def get_available_regions():
    return regios.keys()


def haal_regio_coordinaten(regio, kaart_breedte=991, kaart_hoogte=768):
    coordinaten = None

    try:
        lookup = regios[regio]
        coordinaten = convert_bre_leng(
            lookup['breedtegraad'], lookup['lengtegraad'], kaart_breedte, kaart_hoogte)
        return coordinaten
    except KeyError:
        print('Regio niet herkend: ', regio)
