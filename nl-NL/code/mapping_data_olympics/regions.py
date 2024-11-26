#!/bin/python3
from math import radians, pi, log, tan

regios = {
    'Abkhazia': {
        'naam': 'Abkhazia',
        'capital': 'Sukhumi',
        'breedtegraad': 43.001525,
        'lengtegraad': 41.023415
    },
    'Afghanistan': {
        'naam': 'Afghanistan',
        'capital': 'Kabul',
        'breedtegraad': 34.575503,
        'lengtegraad': 69.240073
    },
    'Aland Islands': {
        'naam': 'Aland Islands',
        'capital': 'Mariehamn',
        'breedtegraad': 60.1,
        'lengtegraad': 19.933333
    },
    'Albania': {
        'naam': 'Albania',
        'capital': 'Tirana',
        'breedtegraad': 41.327546,
        'lengtegraad': 19.818698
    },
    'Algeria': {
        'naam': 'Algeria',
        'capital': 'Algiers',
        'breedtegraad': 36.752887,
        'lengtegraad': 3.042048
    },
    'American Samoa': {
        'naam': 'American Samoa',
        'capital': 'Pago Pago',
        'breedtegraad': -14.275632,
        'lengtegraad': -170.702036
    },
    'Andorra': {
        'naam': 'Andorra',
        'capital': 'Andorra la Vella',
        'breedtegraad': 42.506317,
        'lengtegraad': 1.521835
    },
    'Angola': {
        'naam': 'Angola',
        'capital': 'Luanda',
        'breedtegraad': -8.839988,
        'lengtegraad': 13.289437
    },
    'Anguilla': {
        'naam': 'Anguilla',
        'capital': 'The Valley',
        'breedtegraad': 18.214813,
        'lengtegraad': -63.057441
    },
    'Antarctica': {
        'naam': 'Antarctica',
        'capital': 'South Pole',
        'breedtegraad': -90.0,
        'lengtegraad': 0.0
    },
    'Antigua and Barbuda': {
        'naam': 'Antigua and Barbuda',
        'capital': "St. John's",
        'breedtegraad': 17.12741,
        'lengtegraad': -61.846772
    },
    'Argentina': {
        'naam': 'Argentina',
        'capital': 'Buenos Aires',
        'breedtegraad': -34.603684,
        'lengtegraad': -58.381559
    },
    'Armenia': {
        'naam': 'Armenia',
        'capital': 'Yerevan',
        'breedtegraad': 40.179186,
        'lengtegraad': 44.499103
    },
    'Aruba': {
        'naam': 'Aruba',
        'capital': 'Oranjestad',
        'breedtegraad': 12.509204,
        'lengtegraad': -70.008631
    },
    'Australia': {
        'naam': 'Australia',
        'capital': 'Canberra',
        'breedtegraad': -35.282,
        'lengtegraad': 149.128684
    },
    'Austria': {
        'naam': 'Austria',
        'capital': 'Vienna',
        'breedtegraad': 48.208174,
        'lengtegraad': 16.373819
    },
    'Azerbaijan': {
        'naam': 'Azerbaijan',
        'capital': 'Baku',
        'breedtegraad': 40.409262,
        'lengtegraad': 49.867092
    },
    'Bahamas': {
        'naam': 'Bahamas',
        'capital': 'Nassau',
        'breedtegraad': 25.047984,
        'lengtegraad': -77.355413
    },
    'Bahrain': {
        'naam': 'Bahrain',
        'capital': 'Manama',
        'breedtegraad': 26.228516,
        'lengtegraad': 50.58605
    },
    'Bangladesh': {
        'naam': 'Bangladesh',
        'capital': 'Dhaka',
        'breedtegraad': 23.810332,
        'lengtegraad': 90.412518
    },
    'Barbados': {
        'naam': 'Barbados',
        'capital': 'Bridgetown',
        'breedtegraad': 13.113222,
        'lengtegraad': -59.598809
    },
    'Belarus': {
        'naam': 'Belarus',
        'capital': 'Minsk',
        'breedtegraad': 53.90454,
        'lengtegraad': 27.561524
    },
    'Belgium': {
        'naam': 'Belgium',
        'capital': 'Brussels',
        'breedtegraad': 50.85034,
        'lengtegraad': 4.35171
    },
    'Belize': {
        'naam': 'Belize',
        'capital': 'Belmopan',
        'breedtegraad': 17.251011,
        'lengtegraad': -88.75902
    },
    'Benin': {
        'naam': 'Benin',
        'capital': 'Porto-Novo',
        'breedtegraad': 6.496857,
        'lengtegraad': 2.628852
    },
    'Bermuda': {
        'naam': 'Bermuda',
        'capital': 'Hamilton',
        'breedtegraad': 32.294816,
        'lengtegraad': -64.781375
    },
    'Bhutan': {
        'naam': 'Bhutan',
        'capital': 'Thimphu',
        'breedtegraad': 27.472792,
        'lengtegraad': 89.639286
    },
    'Bolivia': {
        'naam': 'Bolivia',
        'capital': 'La Paz',
        'breedtegraad': -16.489689,
        'lengtegraad': -68.119294
    },
    'Bosnia and Herzegovina': {
        'naam': 'Bosnia and Herzegovina',
        'capital': 'Sarajevo',
        'breedtegraad': 43.856259,
        'lengtegraad': 18.413076
    },
    'Botswana': {
        'naam': 'Botswana',
        'capital': 'Gaborone',
        'breedtegraad': -24.628208,
        'lengtegraad': 25.923147
    },
    'Bouvet Island': {
        'naam': 'Bouvet Island',
        'capital': 'Bouvet Island',
        'breedtegraad': -54.43,
        'lengtegraad': 3.38
    },
    'Brazil': {
        'naam': 'Brazil',
        'capital': 'Brasília',
        'breedtegraad': -15.794229,
        'lengtegraad': -47.882166
    },
    'British Indian Ocean Territory': {
        'naam': 'British Indian Ocean Territory',
        'capital': 'Camp Justice',
        'breedtegraad': 21.3419,
        'lengtegraad': 55.4778
    },
    'British Virgin Islands': {
        'naam': 'British Virgin Islands',
        'capital': 'Road Town',
        'breedtegraad': 18.428612,
        'lengtegraad': -64.618466
    },
    'Brunei': {
        'naam': 'Brunei',
        'capital': 'Bandar Seri Begawan',
        'breedtegraad': 4.903052,
        'lengtegraad': 114.939821
    },
    'Bulgaria': {
        'naam': 'Bulgaria',
        'capital': 'Sofia',
        'breedtegraad': 42.697708,
        'lengtegraad': 23.321868
    },
    'Burkina Faso': {
        'naam': 'Burkina Faso',
        'capital': 'Ouagadougou',
        'breedtegraad': 12.371428,
        'lengtegraad': -1.51966
    },
    'Burundi': {
        'naam': 'Burundi',
        'capital': 'Bujumbura',
        'breedtegraad': -3.361378,
        'lengtegraad': 29.359878
    },
    'Cambodia': {
        'naam': 'Cambodia',
        'capital': 'Phnom Penh',
        'breedtegraad': 11.544873,
        'lengtegraad': 104.892167
    },
    'Cameroon': {
        'naam': 'Cameroon',
        'capital': 'Yaoundé',
        'breedtegraad': 3.848033,
        'lengtegraad': 11.502075
    },
    'Canada': {
        'naam': 'Canada',
        'capital': 'Ottawa',
        'breedtegraad': 45.42153,
        'lengtegraad': -75.697193
    },
    'Cape Verde': {
        'naam': 'Cape Verde',
        'capital': 'Praia',
        'breedtegraad': 14.93305,
        'lengtegraad': -23.513327
    },
    'Cayman Islands': {
        'naam': 'Cayman Islands',
        'capital': 'George Town',
        'breedtegraad': 19.286932,
        'lengtegraad': -81.367439
    },
    'Central African Republic': {
        'naam': 'Central African Republic',
        'capital': 'Bangui',
        'breedtegraad': 4.394674,
        'lengtegraad': 18.55819
    },
    'Chad': {
        'naam': 'Chad',
        'capital': "N'Djamena",
        'breedtegraad': 12.134846,
        'lengtegraad': 15.055742
    },
    'Chile': {
        'naam': 'Chile',
        'capital': 'Santiago',
        'breedtegraad': -33.44889,
        'lengtegraad': -70.669265
    },
    'China': {
        'naam': 'China',
        'capital': 'Beijing',
        'breedtegraad': 39.904211,
        'lengtegraad': 116.407395
    },
    'Christmas Island': {
        'naam': 'Christmas Island',
        'capital': 'Flying Fish Cove',
        'breedtegraad': -10.420686,
        'lengtegraad': 105.679379
    },
    'Cocos (Keeling) Islands': {
        'naam': 'Cocos (Keeling) Islands',
        'capital': 'West Island',
        'breedtegraad': -12.188834,
        'lengtegraad': 96.829316
    },
    'Colombia': {
        'naam': 'Colombia',
        'capital': 'Bogotá',
        'breedtegraad': 4.710989,
        'lengtegraad': -74.072092
    },
    'Comoros': {
        'naam': 'Comoros',
        'capital': 'Moroni',
        'breedtegraad': -11.717216,
        'lengtegraad': 43.247315
    },
    'Congo (DRC)': {
        'naam': 'Congo (DRC)',
        'capital': 'Kinshasa',
        'breedtegraad': -4.441931,
        'lengtegraad': 15.266293
    },
    'Congo (Republic)': {
        'naam': 'Congo (Republic)',
        'capital': 'Brazzaville',
        'breedtegraad': -4.26336,
        'lengtegraad': 15.242885
    },
    'Cook Islands': {
        'naam': 'Cook Islands',
        'capital': 'Avarua',
        'breedtegraad': -21.212901,
        'lengtegraad': -159.782306
    },
    'Costa Rica': {
        'naam': 'Costa Rica',
        'capital': 'San José',
        'breedtegraad': 9.928069,
        'lengtegraad': -84.090725
    },
    "Côte d'Ivoire": {
        'naam': "Côte d'Ivoire",
        'capital': 'Yamoussoukro',
        'breedtegraad': 6.827623,
        'lengtegraad': -5.289343
    },
    'Croatia': {
        'naam': 'Croatia',
        'capital': 'Zagreb ',
        'breedtegraad': 45.815011,
        'lengtegraad': 15.981919
    },
    'Cuba': {
        'naam': 'Cuba',
        'capital': 'Havana',
        'breedtegraad': 23.05407,
        'lengtegraad': -82.345189
    },
    'Curaçao': {
        'naam': 'Curaçao',
        'capital': 'Willemstad',
        'breedtegraad': 12.122422,
        'lengtegraad': -68.882423
    },
    'Cyprus': {
        'naam': 'Cyprus',
        'capital': 'Nicosia',
        'breedtegraad': 35.185566,
        'lengtegraad': 33.382276
    },
    'Czech Republic': {
        'naam': 'Czech Republic',
        'capital': 'Prague',
        'breedtegraad': 50.075538,
        'lengtegraad': 14.4378
    },
    'Denmark': {
        'naam': 'Denmark',
        'capital': 'Copenhagen',
        'breedtegraad': 55.676097,
        'lengtegraad': 12.568337
    },
    'Djibouti': {
        'naam': 'Djibouti',
        'capital': 'Djibouti',
        'breedtegraad': 11.572077,
        'lengtegraad': 43.145647
    },
    'Dominica': {
        'naam': 'Dominica',
        'capital': 'Roseau',
        'breedtegraad': 15.309168,
        'lengtegraad': -61.379355
    },
    'Dominican Republic': {
        'naam': 'Dominican Republic',
        'capital': 'Santo Domingo',
        'breedtegraad': 18.486058,
        'lengtegraad': -69.931212
    },
    'Ecuador': {
        'naam': 'Ecuador',
        'capital': 'Quito',
        'breedtegraad': -0.180653,
        'lengtegraad': -78.467838
    },
    'Egypt': {
        'naam': 'Egypt',
        'capital': 'Cairo',
        'breedtegraad': 30.04442,
        'lengtegraad': 31.235712
    },
    'El Salvador': {
        'naam': 'El Salvador',
        'capital': 'San Salvador',
        'breedtegraad': 13.69294,
        'lengtegraad': -89.218191
    },
    'Equatorial Guinea': {
        'naam': 'Equatorial Guinea',
        'capital': 'Malabo',
        'breedtegraad': 3.750412,
        'lengtegraad': 8.737104
    },
    'Eritrea': {
        'naam': 'Eritrea',
        'capital': 'Asmara',
        'breedtegraad': 15.322877,
        'lengtegraad': 38.925052
    },
    'Estonia': {
        'naam': 'Estonia',
        'capital': 'Tallinn',
        'breedtegraad': 59.436961,
        'lengtegraad': 24.753575
    },
    'Ethiopia': {
        'naam': 'Ethiopia',
        'capital': 'Addis Ababa',
        'breedtegraad': 8.980603,
        'lengtegraad': 38.757761
    },
    'Falkland Islands (Islas Malvinas)': {
        'naam': 'Falkland Islands (Islas Malvinas)',
        'capital': 'Stanley',
        'breedtegraad': -51.697713,
        'lengtegraad': -57.851663
    },
    'Faroe Islands': {
        'naam': 'Faroe Islands',
        'capital': 'Tórshavn',
        'breedtegraad': 62.007864,
        'lengtegraad': -6.790982
    },
    'Fiji': {
        'naam': 'Fiji',
        'capital': 'Suva',
        'breedtegraad': -18.124809,
        'lengtegraad': 178.450079
    },
    'Finland': {
        'naam': 'Finland',
        'capital': 'Helsinki',
        'breedtegraad': 60.173324,
        'lengtegraad': 24.941025
    },
    'France': {
        'naam': 'France',
        'capital': 'Paris',
        'breedtegraad': 48.856614,
        'lengtegraad': 2.352222
    },
    'French Guiana': {
        'naam': 'French Guiana',
        'capital': 'Cayenne',
        'breedtegraad': 4.92242,
        'lengtegraad': -52.313453
    },
    'French Polynesia': {
        'naam': 'French Polynesia',
        'capital': 'Papeete',
        'breedtegraad': -17.551625,
        'lengtegraad': -149.558476
    },
    'French Southern Territories': {
        'naam': 'French Southern Territories',
        'capital': 'Saint-Pierre ',
        'breedtegraad': -21.3419,
        'lengtegraad': 55.4778
    },
    'Gabon': {
        'naam': 'Gabon',
        'capital': 'Libreville',
        'breedtegraad': 0.416198,
        'lengtegraad': 9.467268
    },
    'Gambia': {
        'naam': 'Gambia',
        'capital': 'Banjul',
        'breedtegraad': 13.454876,
        'lengtegraad': -16.579032
    },
    'Georgia': {
        'naam': 'Georgia',
        'capital': 'Tbilisi',
        'breedtegraad': 41.715138,
        'lengtegraad': 44.827096
    },
    'Germany': {
        'naam': 'Germany',
        'capital': 'Berlin',
        'breedtegraad': 52.520007,
        'lengtegraad': 13.404954
    },
    'Ghana': {
        'naam': 'Ghana',
        'capital': 'Accra',
        'breedtegraad': 5.603717,
        'lengtegraad': -0.186964
    },
    'Gibraltar': {
        'naam': 'Gibraltar',
        'capital': 'Gibraltar',
        'breedtegraad': 36.140773,
        'lengtegraad': -5.353599
    },
    'Greece': {
        'naam': 'Greece',
        'capital': 'Athens',
        'breedtegraad': 37.983917,
        'lengtegraad': 23.72936
    },
    'Greenland': {
        'naam': 'Greenland',
        'capital': 'Nuuk',
        'breedtegraad': 64.18141,
        'lengtegraad': -51.694138
    },
    'Grenada': {
        'naam': 'Grenada',
        'capital': "St. George's",
        'breedtegraad': 12.056098,
        'lengtegraad': -61.7488
    },
    'Guadeloupe': {
        'naam': 'Guadeloupe',
        'capital': 'Basse-Terre',
        'breedtegraad': 16.014453,
        'lengtegraad': -61.706411
    },
    'Guam': {
        'naam': 'Guam',
        'capital': 'Hagåtña',
        'breedtegraad': 13.470891,
        'lengtegraad': 144.751278
    },
    'Guatemala': {
        'naam': 'Guatemala',
        'capital': 'Guatemala City',
        'breedtegraad': 14.634915,
        'lengtegraad': -90.506882
    },
    'Guernsey': {
        'naam': 'Guernsey',
        'capital': 'St. Peter Port',
        'breedtegraad': 49.455443,
        'lengtegraad': -2.536871
    },
    'Guinea': {
        'naam': 'Guinea',
        'capital': 'Conakry',
        'breedtegraad': 9.641185,
        'lengtegraad': -13.578401
    },
    'Guinea-Bissau': {
        'naam': 'Guinea-Bissau',
        'capital': 'Bissau',
        'breedtegraad': 11.881655,
        'lengtegraad': -15.617794
    },
    'Guyana': {
        'naam': 'Guyana',
        'capital': 'Georgetown',
        'breedtegraad': 6.801279,
        'lengtegraad': -58.155125
    },
    'Haiti': {
        'naam': 'Haiti',
        'capital': 'Port-au-Prince',
        'breedtegraad': 18.594395,
        'lengtegraad': -72.307433
    },
    'Honduras': {
        'naam': 'Honduras',
        'capital': 'Tegucigalpa',
        'breedtegraad': 14.072275,
        'lengtegraad': -87.192136
    },
    'Hong Kong': {
        'naam': 'Hong Kong',
        'capital': 'Hong Kong',
        'breedtegraad': 22.396428,
        'lengtegraad': 114.109497
    },
    'Hungary': {
        'naam': 'Hungary',
        'capital': 'Budapest',
        'breedtegraad': 47.497912,
        'lengtegraad': 19.040235
    },
    'Iceland': {
        'naam': 'Iceland',
        'capital': 'Reykjavík',
        'breedtegraad': 64.126521,
        'lengtegraad': -21.817439
    },
    'India': {
        'naam': 'India',
        'capital': 'New Delhi',
        'breedtegraad': 28.613939,
        'lengtegraad': 77.209021
    },
    'Indonesia': {
        'naam': 'Indonesia',
        'capital': 'Jakarta',
        'breedtegraad': -6.208763,
        'lengtegraad': 106.845599
    },
    'Iran': {
        'naam': 'Iran',
        'capital': 'Tehran',
        'breedtegraad': 35.689198,
        'lengtegraad': 51.388974
    },
    'Iraq': {
        'naam': 'Iraq',
        'capital': 'Baghdad',
        'breedtegraad': 33.312806,
        'lengtegraad': 44.361488
    },
    'Ireland': {
        'naam': 'Ireland',
        'capital': 'Dublin',
        'breedtegraad': 53.349805,
        'lengtegraad': -6.26031
    },
    'Isle of Man': {
        'naam': 'Isle of Man',
        'capital': 'Douglas',
        'breedtegraad': 54.152337,
        'lengtegraad': -4.486123
    },
    'Israel': {
        'naam': 'Israel',
        'capital': 'Tel Aviv',
        'breedtegraad': 32.0853,
        'lengtegraad': 34.781768
    },
    'Italy': {
        'naam': 'Italy',
        'capital': 'Rome',
        'breedtegraad': 41.902784,
        'lengtegraad': 12.496366
    },
    'Jamaica': {
        'naam': 'Jamaica',
        'capital': 'Kingston',
        'breedtegraad': 18.042327,
        'lengtegraad': -76.802893
    },
    'Japan': {
        'naam': 'Japan',
        'capital': 'Tokyo',
        'breedtegraad': 35.709026,
        'lengtegraad': 139.731992
    },
    'Jersey': {
        'naam': 'Jersey',
        'capital': 'St. Helier',
        'breedtegraad': 49.186823,
        'lengtegraad': -2.106568
    },
    'Jordan': {
        'naam': 'Jordan',
        'capital': 'Amman',
        'breedtegraad': 31.956578,
        'lengtegraad': 35.945695
    },
    'Kazakhstan': {
        'naam': 'Kazakhstan',
        'capital': 'Astana',
        'breedtegraad': 51.160523,
        'lengtegraad': 71.470356
    },
    'Kenya': {
        'naam': 'Kenya',
        'capital': 'Nairobi',
        'breedtegraad': -1.292066,
        'lengtegraad': 36.821946
    },
    'Kiribati': {
        'naam': 'Kiribati',
        'capital': 'Tarawa Atoll',
        'breedtegraad': 1.451817,
        'lengtegraad': 172.971662
    },
    'Kosovo': {
        'naam': 'Kosovo',
        'capital': 'Pristina',
        'breedtegraad': 42.662914,
        'lengtegraad': 21.165503
    },
    'Kuwait': {
        'naam': 'Kuwait',
        'capital': 'Kuwait City',
        'breedtegraad': 29.375859,
        'lengtegraad': 47.977405
    },
    'Kyrgyzstan': {
        'naam': 'Kyrgyzstan',
        'capital': 'Bishkek',
        'breedtegraad': 42.874621,
        'lengtegraad': 74.569762
    },
    'Laos': {
        'naam': 'Laos',
        'capital': 'Vientiane',
        'breedtegraad': 17.975706,
        'lengtegraad': 102.633104
    },
    'Latvia': {
        'naam': 'Latvia',
        'capital': 'Riga',
        'breedtegraad': 56.949649,
        'lengtegraad': 24.105186
    },
    'Lebanon': {
        'naam': 'Lebanon',
        'capital': 'Beirut',
        'breedtegraad': 33.888629,
        'lengtegraad': 35.495479
    },
    'Lesotho': {
        'naam': 'Lesotho',
        'capital': 'Maseru',
        'breedtegraad': -29.363219,
        'lengtegraad': 27.51436
    },
    'Liberia': {
        'naam': 'Liberia',
        'capital': 'Monrovia',
        'breedtegraad': 6.290743,
        'lengtegraad': -10.760524
    },
    'Libya': {
        'naam': 'Libya',
        'capital': 'Tripoli',
        'breedtegraad': 32.887209,
        'lengtegraad': 13.191338
    },
    'Liechtenstein': {
        'naam': 'Liechtenstein',
        'capital': 'Vaduz',
        'breedtegraad': 47.14103,
        'lengtegraad': 9.520928
    },
    'Lithuania': {
        'naam': 'Lithuania',
        'capital': 'Vilnius',
        'breedtegraad': 54.687156,
        'lengtegraad': 25.279651
    },
    'Luxembourg': {
        'naam': 'Luxembourg',
        'capital': 'Luxembourg',
        'breedtegraad': 49.611621,
        'lengtegraad': 6.131935
    },
    'Macau': {
        'naam': 'Macau',
        'capital': 'Macau',
        'breedtegraad': 22.166667,
        'lengtegraad': 113.55
    },
    'Macedonia': {
        'naam': 'Macedonia',
        'capital': 'Skopje',
        'breedtegraad': 41.997346,
        'lengtegraad': 21.427996
    },
    'Madagascar': {
        'naam': 'Madagascar',
        'capital': 'Antananarivo',
        'breedtegraad': -18.87919,
        'lengtegraad': 47.507905
    },
    'Malawi': {
        'naam': 'Malawi',
        'capital': 'Lilongwe',
        'breedtegraad': -13.962612,
        'lengtegraad': 33.774119
    },
    'Malaysia': {
        'naam': 'Malaysia',
        'capital': 'Kuala Lumpur',
        'breedtegraad': 3.139003,
        'lengtegraad': 101.686855
    },
    'Maldives': {
        'naam': 'Maldives',
        'capital': 'Malé',
        'breedtegraad': 4.175496,
        'lengtegraad': 73.509347
    },
    'Mali': {
        'naam': 'Mali',
        'capital': 'Bamako',
        'breedtegraad': 12.639232,
        'lengtegraad': -8.002889
    },
    'Malta': {
        'naam': 'Malta',
        'capital': 'Valletta',
        'breedtegraad': 35.898909,
        'lengtegraad': 14.514553
    },
    'Marshall Islands': {
        'naam': 'Marshall Islands',
        'capital': 'Majuro',
        'breedtegraad': 7.116421,
        'lengtegraad': 171.185774
    },
    'Martinique': {
        'naam': 'Martinique',
        'capital': 'Fort-de-France',
        'breedtegraad': 14.616065,
        'lengtegraad': -61.05878
    },
    'Mauritania': {
        'naam': 'Mauritania',
        'capital': 'Nouakchott',
        'breedtegraad': 18.07353,
        'lengtegraad': -15.958237
    },
    'Mauritius': {
        'naam': 'Mauritius',
        'capital': 'Port Louis',
        'breedtegraad': -20.166896,
        'lengtegraad': 57.502332
    },
    'Mayotte': {
        'naam': 'Mayotte',
        'capital': 'Mamoudzou',
        'breedtegraad': -12.780949,
        'lengtegraad': 45.227872
    },
    'Mexico': {
        'naam': 'Mexico',
        'capital': 'Mexico City',
        'breedtegraad': 19.432608,
        'lengtegraad': -99.133208
    },
    'Micronesia': {
        'naam': 'Micronesia',
        'capital': 'Palikir',
        'breedtegraad': 6.914712,
        'lengtegraad': 158.161027
    },
    'Moldova': {
        'naam': 'Moldova',
        'capital': 'Chisinau',
        'breedtegraad': 47.010453,
        'lengtegraad': 28.86381
    },
    'Monaco': {
        'naam': 'Monaco',
        'capital': 'Monaco',
        'breedtegraad': 43.737411,
        'lengtegraad': 7.420816
    },
    'Mongolia': {
        'naam': 'Mongolia',
        'capital': 'Ulaanbaatar',
        'breedtegraad': 47.886399,
        'lengtegraad': 106.905744
    },
    'Montenegro': {
        'naam': 'Montenegro',
        'capital': 'Podgorica',
        'breedtegraad': 42.43042,
        'lengtegraad': 19.259364
    },
    'Montserrat': {
        'naam': 'Montserrat',
        'capital': 'Plymouth',
        'breedtegraad': 16.706523,
        'lengtegraad': -62.215738
    },
    'Morocco': {
        'naam': 'Morocco',
        'capital': 'Rabat',
        'breedtegraad': 33.97159,
        'lengtegraad': -6.849813
    },
    'Mozambique': {
        'naam': 'Mozambique',
        'capital': 'Maputo',
        'breedtegraad': -25.891968,
        'lengtegraad': 32.605135
    },
    'Myanmar': {
        'naam': 'Myanmar',
        'capital': 'Naypyidaw',
        'breedtegraad': 19.763306,
        'lengtegraad': 96.07851
    },
    'Nagorno-Karabakh Republic': {
        'naam': 'Nagorno-Karabakh Republic',
        'capital': 'Stepanakert',
        'breedtegraad': 39.826385,
        'lengtegraad': 46.763595
    },
    'Namibia': {
        'naam': 'Namibia',
        'capital': 'Windhoek',
        'breedtegraad': -22.560881,
        'lengtegraad': 17.065755
    },
    'Nauru': {
        'naam': 'Nauru',
        'capital': 'Yaren',
        'breedtegraad': -0.546686,
        'lengtegraad': 166.921091
    },
    'Nepal': {
        'naam': 'Nepal',
        'capital': 'Kathmandu',
        'breedtegraad': 27.717245,
        'lengtegraad': 85.323961
    },
    'Netherlands': {
        'naam': 'Netherlands',
        'capital': 'Amsterdam',
        'breedtegraad': 52.370216,
        'lengtegraad': 4.895168
    },
    'Netherlands Antilles': {
        'naam': 'Netherlands Antilles',
        'capital': 'Willemstad ',
        'breedtegraad': 12.1091242,
        'lengtegraad': -68.9316546
    },
    'New Caledonia': {
        'naam': 'New Caledonia',
        'capital': 'Nouméa',
        'breedtegraad': -22.255823,
        'lengtegraad': 166.450524
    },
    'New Zealand': {
        'naam': 'New Zealand',
        'capital': 'Wellington',
        'breedtegraad': -41.28646,
        'lengtegraad': 174.776236
    },
    'Nicaragua': {
        'naam': 'Nicaragua',
        'capital': 'Managua',
        'breedtegraad': 12.114993,
        'lengtegraad': -86.236174
    },
    'Niger': {
        'naam': 'Niger',
        'capital': 'Niamey',
        'breedtegraad': 13.511596,
        'lengtegraad': 2.125385
    },
    'Nigeria': {
        'naam': 'Nigeria',
        'capital': 'Abuja',
        'breedtegraad': 9.076479,
        'lengtegraad': 7.398574
    },
    'Niue': {
        'naam': 'Niue',
        'capital': 'Alofi',
        'breedtegraad': -19.055371,
        'lengtegraad': -169.917871
    },
    'Norfolk Island': {
        'naam': 'Norfolk Island',
        'capital': 'Kingston',
        'breedtegraad': -29.056394,
        'lengtegraad': 167.959588
    },
    'North Korea': {
        'naam': 'North Korea',
        'capital': 'Pyongyang',
        'breedtegraad': 39.039219,
        'lengtegraad': 125.762524
    },
    'Northern Cyprus': {
        'naam': 'Northern Cyprus',
        'capital': 'Nicosia',
        'breedtegraad': 35.185566,
        'lengtegraad': 33.382276
    },
    'Northern Mariana Islands': {
        'naam': 'Northern Mariana Islands',
        'capital': 'Saipan',
        'breedtegraad': 15.177801,
        'lengtegraad': 145.750967
    },
    'Norway': {
        'naam': 'Norway',
        'capital': 'Oslo',
        'breedtegraad': 59.913869,
        'lengtegraad': 10.752245
    },
    'Oman': {
        'naam': 'Oman',
        'capital': 'Muscat',
        'breedtegraad': 23.58589,
        'lengtegraad': 58.405923
    },
    'Pakistan': {
        'naam': 'Pakistan',
        'capital': 'Islamabad',
        'breedtegraad': 33.729388,
        'lengtegraad': 73.093146
    },
    'Palau': {
        'naam': 'Palau',
        'capital': 'Ngerulmud',
        'breedtegraad': 7.500384,
        'lengtegraad': 134.624289
    },
    'Palestine': {
        'naam': 'Palestine',
        'capital': 'Ramallah',
        'breedtegraad': 31.9073509,
        'lengtegraad': 35.5354719
    },
    'Panama': {
        'naam': 'Panama',
        'capital': 'Panama City',
        'breedtegraad': 9.101179,
        'lengtegraad': -79.402864
    },
    'Papua New Guinea': {
        'naam': 'Papua New Guinea',
        'capital': 'Port Moresby',
        'breedtegraad': -9.4438,
        'lengtegraad': 147.180267
    },
    'Paraguay': {
        'naam': 'Paraguay',
        'capital': 'Asuncion',
        'breedtegraad': -25.26374,
        'lengtegraad': -57.575926
    },
    'Peru': {
        'naam': 'Peru',
        'capital': 'Lima',
        'breedtegraad': -12.046374,
        'lengtegraad': -77.042793
    },
    'Philippines': {
        'naam': 'Philippines',
        'capital': 'Manila',
        'breedtegraad': 14.599512,
        'lengtegraad': 120.98422
    },
    'Pitcairn Islands': {
        'naam': 'Pitcairn Islands',
        'capital': 'Adamstown',
        'breedtegraad': -25.06629,
        'lengtegraad': -130.100464
    },
    'Poland': {
        'naam': 'Poland',
        'capital': 'Warsaw',
        'breedtegraad': 52.229676,
        'lengtegraad': 21.012229
    },
    'Portugal': {
        'naam': 'Portugal',
        'capital': 'Lisbon',
        'breedtegraad': 38.722252,
        'lengtegraad': -9.139337
    },
    'Puerto Rico': {
        'naam': 'Puerto Rico',
        'capital': 'San Juan',
        'breedtegraad': 18.466334,
        'lengtegraad': -66.105722
    },
    'Qatar': {
        'naam': 'Qatar',
        'capital': 'Doha',
        'breedtegraad': 25.285447,
        'lengtegraad': 51.53104
    },
    'Réunion': {
        'naam': 'Réunion',
        'capital': 'Saint-Denis',
        'breedtegraad': -20.882057,
        'lengtegraad': 55.450675
    },
    'Romania': {
        'naam': 'Romania',
        'capital': 'Bucharest',
        'breedtegraad': 44.426767,
        'lengtegraad': 26.102538
    },
    'Russia': {
        'naam': 'Russia',
        'capital': 'Moscow',
        'breedtegraad': 55.755826,
        'lengtegraad': 37.6173
    },
    'Rwanda': {
        'naam': 'Rwanda',
        'capital': 'Kigali',
        'breedtegraad': -1.957875,
        'lengtegraad': 30.112735
    },
    'Saint Pierre and Miquelon': {
        'naam': 'Saint Pierre and Miquelon',
        'capital': 'St. Pierre',
        'breedtegraad': 46.775846,
        'lengtegraad': -56.180636
    },
    'Saint Vincent and the Grenadines': {
        'naam': 'Saint Vincent and the Grenadines',
        'capital': 'Kingstown',
        'breedtegraad': 13.160025,
        'lengtegraad': -61.224816
    },
    'Samoa': {
        'naam': 'Samoa',
        'capital': 'Apia',
        'breedtegraad': -13.850696,
        'lengtegraad': -171.751355
    },
    'San Marino': {
        'naam': 'San Marino',
        'capital': 'San Marino',
        'breedtegraad': 43.935591,
        'lengtegraad': 12.447281
    },
    'São Tomé and Príncipe': {
        'naam': 'São Tomé and Príncipe',
        'capital': 'São Tomé',
        'breedtegraad': 0.330192,
        'lengtegraad': 6.733343
    },
    'Saudi Arabia': {
        'naam': 'Saudi Arabia',
        'capital': 'Riyadh',
        'breedtegraad': 24.749403,
        'lengtegraad': 46.902838
    },
    'Senegal': {
        'naam': 'Senegal',
        'capital': 'Dakar',
        'breedtegraad': 14.764504,
        'lengtegraad': -17.366029
    },
    'Serbia': {
        'naam': 'Serbia',
        'capital': 'Belgrade',
        'breedtegraad': 44.786568,
        'lengtegraad': 20.448922
    },
    'Seychelles': {
        'naam': 'Seychelles',
        'capital': 'Victoria',
        'breedtegraad': -4.619143,
        'lengtegraad': 55.451315
    },
    'Sierra Leone': {
        'naam': 'Sierra Leone',
        'capital': 'Freetown',
        'breedtegraad': 8.465677,
        'lengtegraad': -13.231722
    },
    'Singapore': {
        'naam': 'Singapore',
        'capital': 'Singapore',
        'breedtegraad': 1.280095,
        'lengtegraad': 103.850949
    },
    'Slovakia': {
        'naam': 'Slovakia',
        'capital': 'Bratislava',
        'breedtegraad': 48.145892,
        'lengtegraad': 17.107137
    },
    'Slovenia': {
        'naam': 'Slovenia',
        'capital': 'Ljubljana',
        'breedtegraad': 46.056947,
        'lengtegraad': 14.505751
    },
    'Solomon Islands': {
        'naam': 'Solomon Islands',
        'capital': 'Honiara',
        'breedtegraad': -9.445638,
        'lengtegraad': 159.9729
    },
    'Somalia': {
        'naam': 'Somalia',
        'capital': 'Mogadishu',
        'breedtegraad': 2.046934,
        'lengtegraad': 45.318162
    },
    'South Africa': {
        'naam': 'South Africa',
        'capital': 'Pretoria',
        'breedtegraad': -25.747868,
        'lengtegraad': 28.229271
    },
    'South Georgia and the South Sandwich Islands': {
        'naam': 'South Georgia and the South Sandwich Islands',
        'capital': 'King Edward Point',
        'breedtegraad': -54.28325,
        'lengtegraad': -36.493735
    },
    'South Korea': {
        'naam': 'South Korea',
        'capital': 'Seoul',
        'breedtegraad': 37.566535,
        'lengtegraad': 126.977969
    },
    'South Ossetia': {
        'naam': 'South Ossetia',
        'capital': 'Tskhinvali',
        'breedtegraad': 42.22146,
        'lengtegraad': 43.964405
    },
    'South Sudan': {
        'naam': 'South Sudan',
        'capital': 'Juba',
        'breedtegraad': 4.859363,
        'lengtegraad': 31.57125
    },
    'Spain': {
        'naam': 'Spain',
        'capital': 'Madrid',
        'breedtegraad': 40.416775,
        'lengtegraad': -3.70379
    },
    'Sri Lanka': {
        'naam': 'Sri Lanka',
        'capital': 'Sri Jayawardenepura Kotte',
        'breedtegraad': 6.89407,
        'lengtegraad': 79.902478
    },
    'St. Barthélemy': {
        'naam': 'St. Barthélemy',
        'capital': 'Gustavia',
        'breedtegraad': 17.896435,
        'lengtegraad': -62.852201
    },
    'St. Kitts and Nevis': {
        'naam': 'St. Kitts and Nevis',
        'capital': 'Basseterre',
        'breedtegraad': 17.302606,
        'lengtegraad': -62.717692
    },
    'St. Lucia': {
        'naam': 'St. Lucia',
        'capital': 'Castries',
        'breedtegraad': 14.010109,
        'lengtegraad': -60.987469
    },
    'St. Martin': {
        'naam': 'St. Martin',
        'capital': 'Marigot',
        'breedtegraad': 18.067519,
        'lengtegraad': -63.082466
    },
    'Sudan': {
        'naam': 'Sudan',
        'capital': 'Khartoum',
        'breedtegraad': 15.500654,
        'lengtegraad': 32.559899
    },
    'Suriname': {
        'naam': 'Suriname',
        'capital': 'Paramaribo',
        'breedtegraad': 5.852036,
        'lengtegraad': -55.203828
    },
    'Svalbard and Jan Mayen': {
        'naam': 'Svalbard and Jan Mayen',
        'capital': 'Longyearbyen ',
        'breedtegraad': 78.062,
        'lengtegraad': 22.055
    },
    'Swaziland': {
        'naam': 'Swaziland',
        'capital': 'Mbabane',
        'breedtegraad': -26.305448,
        'lengtegraad': 31.136672
    },
    'Sweden': {
        'naam': 'Sweden',
        'capital': 'Stockholm',
        'breedtegraad': 59.329323,
        'lengtegraad': 18.068581
    },
    'Switzerland': {
        'naam': 'Switzerland',
        'capital': 'Bern',
        'breedtegraad': 46.947974,
        'lengtegraad': 7.447447
    },
    'Syria': {
        'naam': 'Syria',
        'capital': 'Damascus',
        'breedtegraad': 33.513807,
        'lengtegraad': 36.276528
    },
    'Taiwan': {
        'naam': 'Taiwan',
        'capital': 'Taipei',
        'breedtegraad': 25.032969,
        'lengtegraad': 121.565418
    },
    'Tajikistan': {
        'naam': 'Tajikistan',
        'capital': 'Dushanbe',
        'breedtegraad': 38.559772,
        'lengtegraad': 68.787038
    },
    'Tanzania': {
        'naam': 'Tanzania',
        'capital': 'Dodoma',
        'breedtegraad': -6.162959,
        'lengtegraad': 35.751607
    },
    'Thailand': {
        'naam': 'Thailand',
        'capital': 'Bangkok',
        'breedtegraad': 13.756331,
        'lengtegraad': 100.501765
    },
    'Timor-Leste': {
        'naam': 'Timor-Leste',
        'capital': 'Dili',
        'breedtegraad': -8.556856,
        'lengtegraad': 125.560314
    },
    'Togo': {
        'naam': 'Togo',
        'capital': 'Lomé',
        'breedtegraad': 6.172497,
        'lengtegraad': 1.231362
    },
    'Tokelau': {
        'naam': 'Tokelau',
        'capital': 'Nukunonu',
        'breedtegraad': -9.2005,
        'lengtegraad': -171.848
    },
    'Tonga': {
        'naam': 'Tonga',
        'capital': 'Nukuʻalofa',
        'breedtegraad': -21.139342,
        'lengtegraad': -175.204947
    },
    'Transnistria': {
        'naam': 'Transnistria',
        'capital': 'Tiraspol',
        'breedtegraad': 46.848185,
        'lengtegraad': 29.596805
    },
    'Trinidad and Tobago': {
        'naam': 'Trinidad and Tobago',
        'capital': 'Port of Spain',
        'breedtegraad': 10.654901,
        'lengtegraad': -61.501926
    },
    'Tristan da Cunha': {
        'naam': 'Tristan da Cunha',
        'capital': 'Edinburgh of the Seven Seas',
        'breedtegraad': -37.068042,
        'lengtegraad': -12.311315
    },
    'Tunisia': {
        'naam': 'Tunisia',
        'capital': 'Tunis',
        'breedtegraad': 36.806495,
        'lengtegraad': 10.181532
    },
    'Turkey': {
        'naam': 'Turkey',
        'capital': 'Ankara',
        'breedtegraad': 39.933364,
        'lengtegraad': 32.859742
    },
    'Turkmenistan': {
        'naam': 'Turkmenistan',
        'capital': 'Ashgabat',
        'breedtegraad': 37.960077,
        'lengtegraad': 58.326063
    },
    'Turks and Caicos Islands': {
        'naam': 'Turks and Caicos Islands',
        'capital': 'Cockburn Town',
        'breedtegraad': 21.467458,
        'lengtegraad': -71.13891
    },
    'Tuvalu': {
        'naam': 'Tuvalu',
        'capital': 'Funafuti',
        'breedtegraad': -8.520066,
        'lengtegraad': 179.198128
    },
    'U.S. Virgin Islands': {
        'naam': 'U.S. Virgin Islands',
        'capital': 'Charlotte Amalie',
        'breedtegraad': 18.3419,
        'lengtegraad': -64.930701
    },
    'Uganda': {
        'naam': 'Uganda',
        'capital': 'Kampala',
        'breedtegraad': 0.347596,
        'lengtegraad': 32.58252
    },
    'Ukraine': {
        'naam': 'Ukraine',
        'capital': 'Kyiv',
        'breedtegraad': 50.4501,
        'lengtegraad': 30.5234
    },
    'United Arab Emirates': {
        'naam': 'United Arab Emirates',
        'capital': 'Abu Dhabi',
        'breedtegraad': 24.299174,
        'lengtegraad': 54.697277
    },
    'United Kingdom': {
        'naam': 'United Kingdom',
        'capital': 'London',
        'breedtegraad': 51.507351,
        'lengtegraad': -0.127758
    },
    'United States': {
        'naam': 'United States',
        'capital': 'Washington',
        'breedtegraad': 38.907192,
        'lengtegraad': -77.036871
    },
    'Uruguay': {
        'naam': 'Uruguay',
        'capital': 'Montevideo',
        'breedtegraad': -34.901113,
        'lengtegraad': -56.164531
    },
    'Uzbekistan': {
        'naam': 'Uzbekistan',
        'capital': 'Tashkent',
        'breedtegraad': 41.299496,
        'lengtegraad': 69.240073
    },
    'Vanuatu': {
        'naam': 'Vanuatu',
        'capital': 'Port Vila',
        'breedtegraad': -17.733251,
        'lengtegraad': 168.327325
    },
    'Vatican City': {
        'naam': 'Vatican City',
        'capital': 'Vatican City',
        'breedtegraad': 41.902179,
        'lengtegraad': 12.453601
    },
    'Venezuela': {
        'naam': 'Venezuela',
        'capital': 'Caracas',
        'breedtegraad': 10.480594,
        'lengtegraad': -66.903606
    },
    'Vietnam': {
        'naam': 'Vietnam',
        'capital': 'Hanoi',
        'breedtegraad': 21.027764,
        'lengtegraad': 105.83416
    },
    'Wallis and Futuna': {
        'naam': 'Wallis and Futuna',
        'capital': 'Mata-Utu',
        'breedtegraad': -13.282509,
        'lengtegraad': -176.176447
    },
    'Western Sahara': {
        'naam': 'Western Sahara',
        'capital': 'El Aaiún',
        'breedtegraad': 27.125287,
        'lengtegraad': -13.1625
    },
    'Yemen': {
        'naam': 'Yemen',
        'capital': "Sana'a",
        'breedtegraad': 15.369445,
        'lengtegraad': 44.191007
    },
    'Zambia': {
        'naam': 'Zambia',
        'capital': 'Lusaka',
        'breedtegraad': -15.387526,
        'lengtegraad': 28.322817
    },
    'Zimbabwe': {
        'naam': 'Zimbabwe',
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
