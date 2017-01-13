import random

countries = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua &amp; Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia &amp; Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kuwait","Kyrgyz Republic","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Namibia","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre &amp; Miquelon","Samoa","San Marino","Satellite","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","South Africa","South Korea","Spain","Sri Lanka","St Kitts &amp; Nevis","St Lucia","St Vincent","St. Lucia","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad &amp; Tobago","Tunisia","Turkey","Turkmenistan","Turks &amp; Caicos","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]

committees = [
    {
        "committee" : "Disarmament and International Security (DISEC)",
        "topics" : [
            "Cyber Security", "Militarization of Space", "Terrorist Attacks"
            ]
    },
    {
        "committee" : "Human Rights Council (HRC)",
        "topics" : [
            "Israel-Palestine Conflict", "Syrian Civil War", "Child Soldiers"
        ]
    },
    {
        "committee" : "Security Council (UNSC)",
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
            "Global Food Waste", "Global Allergy Regulations", "Illegal Foods"
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

taken = set()

def getCountry():
    if len(taken) >= len(countries):
        return "There are no more countries."
    elif len(taken) >= len(countries)/2:
        for country in countries:
            if country not in taken:
                return country
    else:
        while True:
            country = countries[random.randint(0, len(countries)-1)]
            if country not in taken:
                return country

def getTopic():
    comNum = random.randint(0, len(committees)-1)
    topicNum = random.randint(0, len(committees[comNum]["topics"])-1)
    committee = committees[comNum]["committee"]
    topic = committees[comNum]["topics"][topicNum]
    return {"committee" : committee, "topic" : topic}

def genCommittee(num_countries = 1):
    result = getTopic()
    taken.clear()
    for _ in range(num_countries):
        taken.add(getCountry())

    result["countries"] = taken
    return result

print(genCommittee())
