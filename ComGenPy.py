import random

countries = ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegowina", "Botswana", "Bouvet Island", "Brazil", "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo", "Congo, the Democratic Republic of the", "Cook Islands", "Costa Rica", "Cote d'Ivoire", "Croatia (Hrvatska)", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji", "Finland", "France", "France Metropolitan", "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard and Mc Donald Islands", "Holy See (Vatican City State)", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran (Islamic Republic of)", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, Democratic People's Republic of", "Korea, Republic of", "Kuwait", "Kyrgyzstan", "Lao, People's Democratic Republic", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libyan Arab Jamahiriya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia, The Former Yugoslav Republic of", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia, Federated States of", "Moldova, Republic of", "Monaco", "Mongolia", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Slovakia (Slovak Republic)", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia and the South Sandwich Islands", "Spain", "Sri Lanka", "St. Helena", "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbard and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan, Province of China", "Tajikistan", "Tanzania, United Republic of", "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "United States Minor Outlying Islands", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Virgin Islands (British)", "Virgin Islands (U.S.)", "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Yugoslavia", "Zambia", "Zimbabwe"]
committees = [
    {
        "committee" : "Disarmament and International Security (DISEC)",
        "topics" : [
            "Cyber Security", "Militarization of Space", "Terrorist Attacks"
            ]
    },
    {
        "committee" : "Human Rights Council {HRC}",
        "topics" : [
            "Israel-Palestine Conflict", "Syrian Civil War", "Child Soldiers"
        ]
    },
    {
        "committee" : "Security Council {UNSC}",
        "topics" : [
            "ISIS", "Territorial Aggression", "Nuclear Proliferation"
        ]
    },
    {
        "committee" : "United Nations Economic and Social Council (ECOSOC)",
        "topics" : [
            "Internet Censorship", "Tariffs", "Water Pollution"
        ]
    },
    {
        "committee": "United Nations Women",
        "topics": [
            "Violence Against Women", "Gender Equality", "Job Discrimination"
        ]
    },
    {
        "committee": "United Nations Environment Programme (UNEP)",
        "topics": [
            "Sinking Islands", "Melting Glaciers", "Destruction of Rainforests"
        ]
    },
    {
        "committee": "World Health Organization (WHO)",
        "topics": [
            "Access to Medicine", "Epidemics", "Mandatory Dentistry Laws"
        ]
    },
    {
        "committee": "Food and Agricultural Organization (FAO)",
        "topics": [
            "Global Food Waste", "Global Allergy Warnings", "Illegal Foods"
        ]
    },
    {
        "committee": "United Nations Children's Fund (UNICEF)",
        "topics": [
            "Access to Education", "Child Labor", "Orphan Laws"
        ]
    },
    {
        "committee": "Office of the United Nations High Commissioner on Refugees (UNHCR)",
        "topics": [
            "Climate Change-Related Disasters", "Trapped Populations", "Right to Migration"
        ]
    },
    {
        "committee": "Legal Committee",
        "topics": [
            "Drone Laws", "Legal Rebellion", "Endangered Species Laws"
        ]
    },
    {
        "committee": "United Nations Development Programme (UNDP)",
        "topics": [
            "Orphan Rights", "Decaying Infrastructure", "Chronic Rural Poverty"
        ]
    },
    {
        "committee": "United Nations Economic, Social, and Cultural Organization (UNESCO)",
        "topics": [
            "Educating Migrants", "Equality of Education", "Religious Tension"
        ]
    },
    {
        "committee": "Committee on Crime Prevention and Criminial Justice (CCPCJ)",
        "topics": [
            'Capital Punishment', 'Cyber Crime', 'Human Trafficking'
        ]
    }


]

takenCountries = []

def getCountry():
    if len(takenCountries) >= len(countries):
        return "There are no more countries."
    elif len(takenCountries) >= len(countries)/2:
        for country in countries:
            if country not in takenCountries:
                return country
    else:
        while True:
            country = countries[random.randint(0, len(countries)-1)]
            if country not in takenCountries:
                return country

def getTopic():
    comNum = random.randint(0, len(committees)-1)
    topicNum = random.randint(0, len(committees[comNum]["topics"])-1)
    committee = committees[comNum]["committee"]
    topic = committees[comNum]["topics"][topicNum]
    return {"committee" : committee, "topic" : topic}

def genCommittee(num_countries = 10):
    result = getTopic()
    takenCountries = []
    for _ in range(num_countries):
        takenCountries.append(getCountry())

    result["countries"] = takenCountries
    return result

print(genCommittee())
