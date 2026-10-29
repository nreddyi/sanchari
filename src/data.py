from images import add

# ---------------------------------------------------------------- images
A = "2026/08/"
S = "2026/09/"
# Telangana
add("tel", "Sacred Telangana", "temple", A + "Telangana-Tourism-636x426.jpg")
add("tel-ramappa", "Ramappa Temple", "temple", A + "telangana-ramappa-temple-636x426.webp")
add("tel-yadadri", "Yadadri", "temple", A + "telangana-yedagiri-gutta-636x426.webp")
add("tel-pillars", "Thousand Pillar Temple", "temple", A + "telangana-1000-pillars-636x426.webp")
add("tel-fort", "Warangal Fort", "temple", A + "telangana-warangal-fort-636x426.webp")
add("tel-birla", "Birla Mandir", "temple", A + "telangana-birla-mandir-636x426.webp")
add("tel-swarna", "Swarnagiri", "temple", A + "telangana-swarna-giri-636x426.webp")
# Tamil Nadu
add("tn", "Tamil Nadu Temples", "temple", A + "Tamilnadu-636x426.webp")
add("tn-adiyogi", "Adiyogi", "temple", A + "tamilnadu-adi-yogi-636x426.webp")
add("tn-palani", "Palani Murugan", "temple", A + "tamilnadu-palani-dhandayuthapani-swamy-temple-636x426.webp")
add("tn-rockfort", "Rockfort Temple", "temple", A + "tamilnadu-rockfort-temple-636x426.webp")
add("tn-brihad", "Brihadeeswarar Temple", "temple", A + "tamilnadu-brihadeeswarar-temple-636x426.webp")
add("tn-nataraja", "Nataraja Temple", "temple", A + "tamilnadu-nataraja-temple-chidambaram-636x426.webp")
add("tn-arunachala", "Arunachaleswarar", "temple", A + "tamilnadu-arunachaleswarar-temple-636x426.webp")
# Kerala
add("kl", "Sacred Kerala", "temple", A + "Kerala-636x426.jpg")
add("kl-adiyogi", "Adiyogi & Dhyanalinga", "temple", A + "kerala-adiyogi-shiva-statue-dhyanalinga-636x426.webp")
add("kl-vadakkunnathan", "Vadakkunnathan", "temple", A + "kerala-sree-vadakkunnathan-temple-thrissur-636x426.webp")
add("kl-guruvayur", "Guruvayur Temple", "temple", A + "kerala-guruvayur-temple-636x426.webp")
add("kl-kodungallur", "Kodungallur Bhagavathy", "temple", A + "kerala-kodungallur-bhagavathy-temple-636x426.webp")
add("kl-vaikom", "Vaikom Mahadeva", "temple", A + "kerala-vaikom-mahadeva-temple-636x426.webp")
add("kl-ambalappuzha", "Ambalappuzha", "temple", A + "kerala-ambalappuzha-sree-krishna-swamy-temple-636x426.webp")
# Andhra
add("ap", "Sacred Andhra Pradesh", "temple", A + "durgamma-temple-636x426.webp")
add("ap-durga", "Kanaka Durga Temple", "temple", A + "andhra-pradesh-durgamma-temple-636x426.webp")
add("ap-amararama", "Amararama", "temple", A + "andhra-pradesh-amararama-temple-636x426.webp")
add("ap-bhadrachalam", "Bhadrachalam", "temple", A + "andhra-pradesh-bhadrachalam-sri-rama-temple-636x426.webp")
add("ap-dwarka", "Dwarka Tirumala", "temple", A + "andhra-pradesh-dwarka-tirumala-636x426.webp")
add("ap-draksharama", "Draksharama", "temple", A + "andhra-pradeshdraksharama-bhimeswara-swamy-temple-636x426.webp")
# Karnataka
add("ka", "Sacred Karnataka", "wellness", A + "bangalore-palace-636x426.webp")
add("ka-chamundi", "Chamundeshwari", "temple", A + "karnataka-chamundeshwari-temple-636x426.webp")
add("ka-hoysala", "Hoysaleswara Temple", "temple", A + "karanataka-hoysaleswara-temple-636x426.webp")
add("ka-belur", "Chennakeshava Temple", "temple", A + "karanataka-chennakeshava-temple-636x426.webp")
add("ka-kukke", "Kukke Subramanya", "temple", A + "karnataka-kukke-subramanya-temple-636x426.webp")
add("ka-dharma", "Dharmasthala", "temple", A + "karanataka-dharmasthala-temple-636x426.webp")
# Everest
add("ev", "Everest Base Camp", "mountain", S + "mt-everest-1-636x426.webp")
for i in range(2, 7):
    add(f"ev-{i}", "Khumbu Region", "mountain", S + f"mt-everest-{i}-636x426.webp")
# Kilimanjaro
add("ki", "Kilimanjaro", "mountain", S + "kilimanjaro--636x426.webp")
for i in range(1, 6):
    add(f"ki-{i}", "Marangu Route", "mountain", S + f"kilimanjaro-{i}-636x426.webp")
# Elbrus
add("el", "Mount Elbrus", "mountain", S + "mount-elbrus-1-636x426.webp")
for n in ["1-1", "2", "3", "4", "5"]:
    add(f"el-{n}", "Caucasus", "mountain", S + f"mount-elbrus-{n}-636x426.webp")
# Site
add("hero-home", "", "temple", 'https://commons.wikimedia.org/wiki/Special:FilePath/Gopurams_of_the_Madurai_Meenakshi_Temple%2C_Madurai%2C_Tamil_Nadu%2C_India_%282016%29.jpg?width=1600', 1600, 900)
# Slide 1 Temple Tours -> gopuram of Meenakshi Temple, Madurai
add("hero-s1", "", "temple", 'https://commons.wikimedia.org/wiki/Special:FilePath/Meenakshi_Temple%2C_Gopuram%2C_Madurai%2C_India.jpg?width=2000', 1600, 900)
# Slide 2 Adventure Tours -> Ama Dablam on the Everest Base Camp trail
add("hero-s2", "", "mountain", 'https://commons.wikimedia.org/wiki/Special:FilePath/Himalayas%2C_Ama_Dablam%2C_Nepal.jpg?width=2000', 1600, 900)
add("hero-s3", "", "wellness", A + "sider-2.webp", 1600, 900)
add("hero-north", "", "mountain", 'https://commons.wikimedia.org/wiki/Special:FilePath/Kedarnath_Temple_with_Snow_Covered_Mountains_in_Background.jpg?width=1600', 1600, 900)
add("hero-temple", "", "temple", 'https://commons.wikimedia.org/wiki/Special:FilePath/Brihadisvara_Temple%2C_Thanjavur%2C_Tamil_Nadu%2C_India.jpg?width=1600', 1600, 900)
add("hero-adventure", "", "mountain", 'https://commons.wikimedia.org/wiki/Special:FilePath/Himalayas%2C_Ama_Dablam%2C_Nepal.jpg?width=1600', 1600, 900)
add("hero-wellness", "", "wellness", 'https://commons.wikimedia.org/wiki/Special:FilePath/Kerala_backwaters%2C_Vembanad_Lake%2C_Houseboats%2C_India.jpg?width=1600', 1600, 900)
add("hero-about", "", "city", 'https://commons.wikimedia.org/wiki/Special:FilePath/Hampi%2C_India%2C_Aerial_view_of_Virupaksha_Temple%2C_Panorama_of_Hampi.jpg?width=1600', 1600, 900)
add("hero-blog", "", "wellness", 'https://commons.wikimedia.org/wiki/Special:FilePath/Misty_tea_plantation_munnar.jpg?width=1600', 1600, 900)
add("hero-contact", "", "city", 'https://commons.wikimedia.org/wiki/Special:FilePath/Charminar%2C_Hyderabad%2C_Telangana%2C_India.jpg?width=1600', 1600, 900)
add("cat-temple", "", "temple", A + "temple-tours.webp")
add("cat-adventure", "", "mountain", A + "adventure-trip.webp")
add("cat-wellness", "", "wellness", A + "yoga.webp")
add("about-main", "Experience Bharat", "temple", A + "About-Page-683x1024.webp", 600, 800)
add("custom", "", "wellness", 'https://commons.wikimedia.org/wiki/Special:FilePath/View_of_tea_plantations_in_Munnar.jpg?width=1600')
for i, n in enumerate(["Dil Raju", "Pranay Nistala", "Vygha Reddy", "Ganesh Reddy", "Karthik"], 1):
    add(f"team{i}", "", "person", S + f"team{i}.webp", 600, 700)
add("anmish", "", "mountain", 'https://commons.wikimedia.org/wiki/Special:FilePath/Uhuru_Peak_Mt._Kilimanjaro_1.JPG?width=1600', 600, 700)
add("blog-1", "Temple Etiquette", "temple", 'https://commons.wikimedia.org/wiki/Special:FilePath/Golden_Lily_Pond_and_South_Gopuram_at_Meenakshi_Amman_Temple_%2C_Madurai.jpg?width=1600')
add("blog-2", "High Altitude", "mountain", 'https://commons.wikimedia.org/wiki/Special:FilePath/Sagarmatha_National_Park-Lobuche_to_Gorak_Shep_2013-05-05_12-37-25.jpg?width=1600')
add("blog-3", "Senior Travel", "wellness", 'https://commons.wikimedia.org/wiki/Special:FilePath/Srirangam_Temple_Gopuram.jpg?width=1600')

# ---------------------------------------------------------------- shared text
TEMPLE_KNOW = [
    ("Dress code", "Traditional or modest clothing is recommended at all temples. Footwear is removed before entering."),
    ("What to carry", "A valid photo ID, comfortable walking shoes, a water bottle and any regular medication."),
    ("Physical activity", "Some shrines involve steps or hill climbs. Tell us about mobility needs and we’ll plan accordingly."),
    ("Best time to visit", "October to March offers pleasant weather. Festival dates may affect crowds and darshan times."),
]
ADV_KNOW = [
    ("Fitness", "Good cardiovascular fitness is essential. Start a training plan of walking, stair climbs and cardio at least 8–12 weeks before departure."),
    ("Gear", "A detailed gear list is shared on booking. Personal trekking and mountaineering gear can be rented on request."),
    ("Altitude", "The itinerary includes acclimatisation days. Guides monitor every trekker and the plan may change for safety."),
    ("Documents", "A valid passport, visa where required, and medical and evacuation insurance details are needed before travel."),
]
TEMPLE_FAQ = lambda start: [
    ("Where does the tour start and end?", start),
    ("Can the itinerary be customised?", "Yes. We can add or skip temples, change hotel categories, or extend your stay. Share your preferences when you enquire."),
    ("Is this tour suitable for senior citizens?", "Yes. Travel is by private vehicle and the pace is comfortable. Tell us about any mobility needs in advance."),
    ("Are special darshan tickets included?", "No, special darshan tickets are not included, but our team can help you book them where available."),
]
ADV_FAQ = lambda start: [
    ("Where does the expedition start and end?", start),
    ("Do I need prior trekking experience?", "Prior multi-day trekking experience is recommended. Our team will talk you through fitness preparation before you book."),
    ("What happens if the weather turns?", "Buffer and reserve days are built in. Final decisions on summit attempts are made by the expedition leaders for everyone’s safety."),
    ("Who leads the expedition?", "Adventure journeys are run with Anmish Adventures, led by mountaineer Anmish Varma, with experienced local guides and support staff."),
]
TEMPLE_INCL = ["Travel as per itinerary", "Private air-conditioned transport", "Breakfast, lunch & dinner",
               "Hotel accommodation", "Dedicated tour manager"]
TEMPLE_EXCL = ["Departure taxes", "Monument & temple entry fees", "Special darshan tickets", "Personal expenses & tips"]

# ---------------------------------------------------------------- tours
TOURS = []

TOURS.append(dict(
    slug="tour-sacred-telangana", cat="temple", region="Telangana", rkey="telangana",
    title="Sacred Telangana: 5 Days Through Its Most Blessed Temples", short="Sacred Telangana",
    days=5, nights=4, route="Hyderabad → Ramappa", price=7500, featured=True,
    card=["The state’s most revered temples in one circuit", "UNESCO-listed Ramappa Temple", "Stays, transport & guide included"],
    stats=[("temple", "8", "Sacred temples"), ("map", "600+ km", "Covered by road"), ("pin", "7", "Cities visited"),
           ("car", "Private", "Transport"), ("meal", "All meals", "Included")],
    overview=["From Charminar’s storied streets in Hyderabad to Ramappa’s UNESCO-listed masterwork, this five-day circuit brings together Telangana’s most revered shrines — hilltop temples, riverside sanctuaries and Kakatiya-era stone masterpieces.",
              "You’ll travel in a private vehicle with a tour manager, with darshan times planned around temple schedules and all meals taken care of. It’s a well-paced journey for families, senior travellers and first-time pilgrims alike."],
    highlights=[("Yadadri", "Lakshmi Narasimha cave shrine, rebuilt in white stone and gold"),
                ("Basar", "Gnana Saraswati Temple on the banks of the Godavari"),
                ("Kondagattu", "Forest hilltop shrine of Swayambhu Anjaneya Swamy"),
                ("Ramappa", "13th-century UNESCO World Heritage temple")],
    stops=["Hyderabad", "Swarnagiri", "Yadadri", "Nizamabad", "Basar", "Kondagattu", "Karimnagar", "Warangal", "Ramappa"],
    itinerary=[
        ("Arrival in Hyderabad", "Heritage & local exploration · Overnight: Hyderabad",
         "Arrive by 3:00 PM, meet your vehicle and tour manager, and check in. The afternoon is spent exploring the city’s landmarks.",
         [("Afternoon", "Charminar & Laad Bazaar", "The 1591 CE monument and the bangle bazaar around it."),
          ("Evening", "Hussain Sagar", "The heart-shaped lake (1563 CE) with a monolithic Buddha at its centre."),
          ("Evening", "Birla Mandir", "White marble Vaishnava temple on a 280-ft granite hill."),
          ("Night", "Dinner & overnight stay", "Hyderabad.")], False),
        ("Hyderabad → Swarnagiri → Yadadri → Nizamabad", "Two hilltop shrines · Overnight: Nizamabad", "",
         [("08:00 – 10:00", "Drive to Swarnagiri", "The “Golden Mountain” hilltop shrine with views over the Deccan plains."),
          ("10:00 – 13:00", "Swarnagiri darshan", "Around three hours at the temple."),
          ("13:00 – 14:00", "Lunch", "Near Swarnagiri."),
          ("14:30 – 17:30", "Yadadri Lakshmi Narasimha Swamy Temple", "Cave shrine atop a granite hill, recently rebuilt in white stone and gold."),
          ("17:30 – 21:30", "Drive to Nizamabad", "Dinner and overnight stay.")], False),
        ("Nizamabad → Basar → Kondagattu → Karimnagar", "Saraswati & Hanuman shrines · Overnight: Karimnagar", "",
         [("09:00 – 10:00", "Drive to Basar", "A scenic route along the Godavari."),
          ("10:00 – 12:00", "Gnana Saraswati Temple", "South India’s best-known Saraswati temple, famed for Vidyarambham ceremonies."),
          ("12:00 – 13:00", "Lunch", "In Basar."),
          ("13:00 – 16:30", "Kondagattu Anjaneya Swamy Temple", "Forest hilltop shrine to the self-manifested Hanuman, Jagtial district."),
          ("18:30 – 21:00", "Drive to Karimnagar", "Dinner and overnight stay.")], False),
        ("Karimnagar → Warangal", "Kakatiya heritage · Overnight: Warangal", "",
         [("Morning", "Drive to Warangal", "Former capital of the Kakatiya dynasty."),
          ("Late morning", "Thousand Pillar Temple", "Star-shaped 12th-century temple with intricately carved pillars."),
          ("Afternoon", "Warangal Fort", "Stone gateways (Kakatiya Kala Thoranam) and fort ruins."),
          ("Evening", "Bhadrakali Temple", "Hilltop temple overlooking Bhadrakali Lake. Dinner and overnight stay.")], True),
        ("Warangal → Ramappa → Hyderabad", "UNESCO World Heritage · Tour ends", "",
         [("Morning", "Ramappa Temple, Palampet", "UNESCO-listed 13th-century Kakatiya temple, renowned for its sculpture."),
          ("Afternoon", "Lunch & return drive", "Head back towards Hyderabad."),
          ("Evening", "Drop-off in Hyderabad", "Tour concludes.")], True),
    ],
    incl=["Travel as per itinerary", "Private air-conditioned transport", "Breakfast, lunch & dinner",
          "Hotel accommodation (4 nights)", "Dedicated tour manager"],
    excl=TEMPLE_EXCL,
    images=["tel", "tel-ramappa", "tel-yadadri", "tel-pillars", "tel-fort", "tel-birla", "tel-swarna"],
    know=TEMPLE_KNOW, faq=TEMPLE_FAQ("The tour starts and ends in Hyderabad. Please plan to arrive by 3:00 PM on Day 1."),
))

TOURS.append(dict(
    slug="tour-tamil-nadu-temple-journey", cat="temple", region="Tamil Nadu", rkey="tamilnadu",
    title="Tamil Nadu Temple Journey: 7 Days Through Its Living Temples", short="Tamil Nadu Temple Journey",
    days=7, nights=6, route="Velliangiri → Mahabalipuram", price=10500, featured=True,
    card=["Living Dravidian temples still in daily worship", "Adiyogi, Srirangam & Thanjavur", "Stays, transport & guide included"],
    stats=[("temple", "12", "Sacred temples"), ("map", "800+ km", "Covered by road"), ("pin", "8", "Cities visited"),
           ("car", "Private", "Transport"), ("meal", "All meals", "Included")],
    overview=["Your sacred journey at a glance: from Adiyogi at the foot of the Velliangiri hills, through twelve of Tamil Nadu’s great temples, to the shore temples of Mahabalipuram and the temple town of Kanchipuram.",
              "Tamil Nadu’s temples are living places of worship, with rituals that have continued for more than a thousand years. Each day is planned around darshan times, with comfortable stays, all meals and a private vehicle throughout."],
    highlights=[("Adiyogi", "The 112-ft Shiva face and Dhyanalinga at the Isha Yoga Center"),
                ("Srirangam", "Sri Ranganathaswamy, one of the largest functioning temple complexes in the world"),
                ("Thanjavur", "Brihadeeswarar, the great Chola temple and UNESCO World Heritage site"),
                ("Mahabalipuram", "Pallava-era Shore Temple and rock-cut monuments")],
    stops=["Coimbatore", "Palani", "Trichy", "Srirangam", "Thanjavur", "Chidambaram", "Tiruvannamalai", "Kanchipuram", "Mahabalipuram"],
    itinerary=[
        ("Hyderabad → Coimbatore | Isha Yoga Center", "Adiyogi & Dhyanalinga · Overnight: Coimbatore", "",
         [("10:10 – 11:35", "Flight to Coimbatore", "Hyderabad to Coimbatore."),
          ("11:35 – 13:00", "Airport transfer & check-in", ""),
          ("13:00 – 14:00", "Lunch", "A traditional Kongu-style meal."),
          ("14:00 – 16:30", "Rest & freshen up", ""),
          ("17:00 – 20:00", "Adiyogi & Dhyanalinga", "Around three hours at the Isha Yoga Center."),
          ("21:00", "Dinner & overnight stay", "Coimbatore.")], False),
        ("Coimbatore → Palani Murugan → Trichy", "Hill temple & Rockfort · Overnight: Trichy", "",
         [("06:30 – 08:00", "Breakfast", ""),
          ("08:00 – 10:30", "Drive to Palani", ""),
          ("10:30 – 13:30", "Palani Dhandayuthapani Swamy Temple", "Reach the hilltop by ropeway or 690 steps."),
          ("13:30 – 14:30", "Lunch", "In Palani."),
          ("14:30 – 18:00", "Drive to Tiruchirappalli", "Via Dindigul."),
          ("19:00 – 21:00", "Rockfort Temple (optional)", "Evening visit to the hilltop temple. Dinner and overnight stay.")], False),
        ("Trichy → Srirangam → Thanjavur", "Two of South India’s grandest temples · Overnight: Thanjavur", "",
         [("06:30 – 09:00", "Breakfast & check-out", ""),
          ("09:30 – 12:30", "Sri Ranganathaswamy Temple, Srirangam", "Around three hours at the temple."),
          ("12:30 – 13:30", "Lunch", ""),
          ("13:30 – 15:00", "Drive to Thanjavur", ""),
          ("15:00 – 18:00", "Brihadeeswarar Temple", "The great Chola temple."),
          ("18:00 – 21:30", "Explore Thanjavur", "Royal Palace, Saraswati Mahal Library and bazaars. Dinner and overnight stay.")], False),
        ("Thanjavur → Kumbakonam → Chidambaram", "Chola country · Overnight: Chidambaram", "",
         [("Morning", "Airavatesvara Temple, Darasuram", "UNESCO-listed Chola temple near Kumbakonam."),
          ("Afternoon", "Drive to Chidambaram", "Lunch en route."),
          ("Evening", "Thillai Nataraja Temple", "Evening rituals at the temple of the cosmic dancer. Overnight stay.")], True),
        ("Chidambaram → Tiruvannamalai", "Arunachala · Overnight: Tiruvannamalai", "",
         [("Morning", "Drive to Tiruvannamalai", ""),
          ("Afternoon", "Arunachaleswarar Temple", "One of the Pancha Bhoota Sthalams, at the foot of Arunachala hill."),
          ("Evening", "Girivalam path (optional)", "Walk part of the sacred path around the hill. Dinner and overnight stay.")], True),
        ("Tiruvannamalai → Kanchipuram → Mahabalipuram", "City of a thousand temples · Overnight: Mahabalipuram", "",
         [("Morning", "Drive to Kanchipuram", ""),
          ("Late morning", "Kamakshi Amman & Ekambareswarar", "Two of Kanchipuram’s principal temples."),
          ("Afternoon", "Kailasanathar Temple", "Pallava sandstone temple. Then continue to Mahabalipuram."),
          ("Evening", "Check-in", "Dinner and overnight stay by the coast.")], True),
        ("Mahabalipuram → Chennai", "Shore Temple · Tour ends", "",
         [("Morning", "Shore Temple & Pancha Rathas", "Pallava-era monuments on the Bay of Bengal."),
          ("Afternoon", "Drive to Chennai", "Drop-off at Chennai airport for your onward journey.")], True),
    ],
    incl=TEMPLE_INCL, excl=TEMPLE_EXCL,
    images=["tn", "tn-adiyogi", "tn-palani", "tn-brihad", "tn-rockfort", "tn-nataraja", "tn-arunachala"],
    know=TEMPLE_KNOW, faq=TEMPLE_FAQ("The tour starts with a morning flight from Hyderabad to Coimbatore and ends in Chennai."),
))

TOURS.append(dict(
    slug="tour-sacred-kerala", cat="temple", region="Kerala", rkey="kerala",
    title="Sacred Kerala: A 7-Day Spiritual Sojourn Through Temples", short="Sacred Kerala Sojourn",
    days=7, nights=6, route="Coimbatore → Thiruvananthapuram", price=11500, featured=True,
    card=["Kerala’s traditional temple architecture", "One night on a backwater houseboat", "Stays, transport & guide included"],
    stats=[("temple", "12", "Sacred temples"), ("map", "2", "States"), ("pin", "7", "Cities visited"),
           ("boat", "1 night", "Houseboat"), ("meal", "All meals", "Included")],
    overview=["A slower, reflective journey through Kerala’s temple traditions — from Adiyogi in Coimbatore across the Palakkad Gap to Thrissur, Guruvayur and the backwaters, ending at Thiruvananthapuram.",
              "Kerala’s temples have a distinct architecture of sloping roofs, wooden carvings and lamp-lit courtyards. Along the way you’ll spend a night on a houseboat, with all meals, stays and private transport arranged."],
    highlights=[("Guruvayur", "One of the most important Sri Krishna temples in India"),
                ("Vadakkunnathan", "Thrissur’s great Shiva temple at the heart of the city"),
                ("Backwaters", "A night aboard a traditional Kerala houseboat"),
                ("Thiruvananthapuram", "Sree Padmanabhaswamy Temple")],
    stops=["Coimbatore", "Thrissur", "Guruvayur", "Kodungallur", "Chottanikkara", "Kochi", "Vaikom", "Alappuzha", "Thiruvananthapuram"],
    itinerary=[
        ("Coimbatore | Adiyogi → Night drive to Thrissur", "Isha Yoga Center · Overnight: Thrissur",
         "Arrive in Coimbatore in the afternoon, check in and freshen up.",
         [("15:30 – 16:00", "Drive to Isha Yoga Center", ""),
          ("16:00 – 19:00", "Adiyogi & Dhyanalinga", "Around three hours."),
          ("19:00 – 20:00", "Dinner", "In Coimbatore."),
          ("20:00 – 23:00", "Night drive to Thrissur", "Through the Palakkad Gap. Overnight stay.")], False),
        ("Thrissur → Vadakkunnathan → Guruvayur", "Shiva & Krishna · Overnight: Guruvayur", "",
         [("09:00 – 12:00", "Sree Vadakkunnathan Temple", "Around three hours in Thrissur."),
          ("12:00 – 13:00", "Lunch", ""),
          ("13:00 – 14:00", "Drive to Guruvayur", ""),
          ("16:00 – 19:00", "Guruvayur Temple", "Evening darshan. Dinner and overnight stay.")], False),
        ("Guruvayur → Kodungallur → Chottanikkara → Kochi", "Bhagavathy temples · Overnight: Kochi", "",
         [("10:00 – 13:00", "Kodungallur Bhagavathy Temple", ""),
          ("13:00 – 14:00", "Lunch", ""),
          ("16:00 – 19:00", "Chottanikkara Bhagavathy Temple", ""),
          ("19:30", "Drive to Kochi", "Dinner and overnight stay.")], False),
        ("Kochi → Vaikom → Alappuzha houseboat", "Backwaters · Overnight: Houseboat", "",
         [("Morning", "Vaikom Mahadeva Temple", "Historic Shiva temple on the shores of Vembanad Lake."),
          ("Afternoon", "Board your houseboat", "Cruise the backwaters with lunch on board."),
          ("Evening", "Sunset on the backwaters", "Dinner and overnight stay on the houseboat.")], True),
        ("Alappuzha → Ambalappuzha → Thiruvananthapuram", "Krishna temple & capital city · Overnight: Thiruvananthapuram", "",
         [("Morning", "Disembark & Ambalappuzha Sree Krishna Temple", "Famous for its palpayasam offering."),
          ("Afternoon", "Drive to Thiruvananthapuram", "Lunch en route."),
          ("Evening", "Check-in", "Dinner and overnight stay.")], True),
        ("Thiruvananthapuram", "Sree Padmanabhaswamy · Overnight: Thiruvananthapuram", "",
         [("Morning", "Sree Padmanabhaswamy Temple", "Strict traditional dress code applies."),
          ("Afternoon", "Attukal Bhagavathy Temple", ""),
          ("Evening", "At leisure", "Dinner and overnight stay.")], True),
        ("Departure", "Tour ends", "",
         [("Morning", "Check-out", "Drop-off at Thiruvananthapuram airport for your onward journey.")], True),
    ],
    incl=TEMPLE_INCL + ["One night on a houseboat"], excl=TEMPLE_EXCL,
    images=["kl", "kl-guruvayur", "kl-vadakkunnathan", "kl-kodungallur", "kl-vaikom", "kl-ambalappuzha", "kl-adiyogi"],
    know=TEMPLE_KNOW, faq=TEMPLE_FAQ("The tour starts in Coimbatore in the afternoon of Day 1 and ends in Thiruvananthapuram."),
))

TOURS.append(dict(
    slug="tour-sacred-andhra-pradesh", cat="temple", region="Andhra Pradesh", rkey="andhra",
    title="Sacred Andhra Pradesh: 6 Days Across AP Temples", short="Sacred Andhra Pradesh",
    days=6, nights=5, route="Vijayawada → Vizag", price=7500, featured=True,
    card=["Kanaka Durga Temple, Vijayawada", "Godavari temples to Simhachalam", "Stays, transport & guide included"],
    stats=[("temple", "11", "Sacred temples"), ("map", "700+ km", "Covered by road"), ("pin", "7", "Cities visited"),
           ("car", "Private", "Transport"), ("meal", "All meals", "Included")],
    overview=["Eleven darshans across Andhra Pradesh, from Kanaka Durga on Indrakeeladri hill in Vijayawada to Simhachalam in Visakhapatnam — following the Krishna and Godavari through some of the state’s most important pilgrimage centres.",
              "The route includes Pancharama shrines, Bhadrachalam’s Sri Rama temple and the coastal temples of the north. A private vehicle, a tour manager, stays and all meals are included."],
    highlights=[("Kanaka Durga", "Hilltop shrine overlooking the Krishna in Vijayawada"),
                ("Bhadrachalam", "Sri Sita Ramachandra Swamy Temple on the Godavari"),
                ("Pancharamas", "Amararama and Draksharama, ancient Shiva shrines"),
                ("Simhachalam", "Varaha Lakshmi Narasimha Temple near Vizag")],
    stops=["Vijayawada", "Amararama", "Bhadrachalam", "Dwarka Tirumala", "Draksharama", "Kakinada", "Annavaram", "Visakhapatnam"],
    itinerary=[
        ("Arrival in Vijayawada | Kanaka Durga Darshan", "Overnight: Vijayawada",
         "Arrive at Vijayawada Airport, meet your vehicle and tour manager, and check in.",
         [("15:00 – 16:00", "Drive to Sri Kanaka Durga Temple", ""),
          ("16:00 – 19:30", "Kanaka Durga darshan", "Around three and a half hours."),
          ("19:30 – 20:30", "Dinner & overnight stay", "Vijayawada.")], False),
        ("Vijayawada → Amararama → Bhadrachalam", "Pancharama & Sri Rama · Overnight: Bhadrachalam", "",
         [("08:00 – 09:30", "Drive to Amararama", ""),
          ("09:30 – 11:30", "Amararama Temple", "One of the five Pancharama Shiva shrines."),
          ("11:30 – 12:30", "Lunch", ""),
          ("12:30 – 17:30", "Drive to Bhadrachalam", ""),
          ("17:30 – 20:30", "Bhadrachalam Sri Rama Temple", "Dinner and overnight stay.")], False),
        ("Bhadrachalam → Dwarka Tirumala → Draksharama → Kakinada", "Overnight: Kakinada", "",
         [("07:00 – 10:30", "Drive to Dwarka Tirumala", ""),
          ("10:30 – 13:30", "Dwarka Tirumala Temple", "Known as “Chinna Tirupati”."),
          ("13:30 – 14:30", "Lunch", ""),
          ("17:30 – 20:00", "Draksharama Bhimeswara Swamy Temple", "Another of the Pancharama shrines."),
          ("21:00 – 22:00", "Dinner & overnight stay", "Kakinada.")], False),
        ("Kakinada → Annavaram → Visakhapatnam", "Hilltop shrine · Overnight: Visakhapatnam", "",
         [("Morning", "Annavaram Satyanarayana Swamy Temple", "Hilltop temple on Ratnagiri hill."),
          ("Afternoon", "Drive to Visakhapatnam", "Lunch en route."),
          ("Evening", "RK Beach", "Evening by the sea. Dinner and overnight stay.")], True),
        ("Visakhapatnam | Simhachalam", "Overnight: Visakhapatnam", "",
         [("Morning", "Simhachalam Varaha Lakshmi Narasimha Temple", "Hilltop temple with Kalinga-style architecture."),
          ("Afternoon", "Kailasagiri", "Hilltop park with views over the city and coast."),
          ("Evening", "At leisure", "Dinner and overnight stay.")], True),
        ("Departure from Visakhapatnam", "Tour ends", "",
         [("Morning", "Check-out", "Drop-off at Visakhapatnam airport or railway station.")], True),
    ],
    incl=TEMPLE_INCL, excl=TEMPLE_EXCL,
    images=["ap", "ap-durga", "ap-bhadrachalam", "ap-amararama", "ap-dwarka", "ap-draksharama"],
    know=TEMPLE_KNOW, faq=TEMPLE_FAQ("The tour starts at Vijayawada Airport on Day 1 and ends in Visakhapatnam."),
))

TOURS.append(dict(
    slug="tour-sacred-karnataka", cat="wellness", region="Karnataka", rkey="karnataka",
    title="Sacred Karnataka: 6 Days From Mysuru to the Konkan Coast", short="Sacred Karnataka",
    days=6, nights=5, route="Mysuru → Goa", price=9500, featured=True,
    card=["Hoysala temples of Belur & Halebeedu", "Western Ghats and the Konkan coast", "Stays, transport & guide included"],
    stats=[("temple", "9", "Sacred temples"), ("map", "800+ km", "Covered by road"), ("wave", "3", "Sacred beaches"),
           ("star", "2", "UNESCO sites"), ("meal", "All meals", "Included")],
    overview=["A restorative journey across Karnataka — from Chamundi Hill in Mysuru to the carved Hoysala temples of Belur and Halebeedu, through the forests of the Western Ghats, and down to the quiet sacred beaches of the Konkan coast.",
              "Unhurried days, comfortable stays and time by the sea at Murudeshwar and Gokarna make this a gentle mix of pilgrimage and renewal. A private vehicle and all meals are included."],
    highlights=[("Mysuru", "Chamundeshwari Temple on Chamundi Hill"),
                ("Belur & Halebeedu", "Hoysala temples, part of a UNESCO World Heritage site"),
                ("Western Ghats", "Kukke Subramanya and Dharmasthala in the forested hills"),
                ("Konkan coast", "Murudeshwar and Gokarna’s sacred beaches")],
    stops=["Bengaluru", "Mysuru", "Halebeedu", "Belur", "Hassan", "Kukke Subramanya", "Dharmasthala", "Udupi", "Murudeshwar", "Gokarna", "Goa"],
    itinerary=[
        ("Bengaluru → Mysuru | Chamundeshwari", "Overnight: Mysuru",
         "Arrive at Kempegowda International Airport, Bengaluru, and meet your driver.",
         [("12:30 – 16:00", "Drive to Mysuru", "Via Ramanagara and Mandya."),
          ("16:30 – 18:30", "Chamundeshwari Temple", "On Chamundi Hill, including evening arati."),
          ("19:00", "Dinner & overnight stay", "Mysuru.")], False),
        ("Mysuru → Halebeedu → Belur → Hassan", "Hoysala masterpieces · Overnight: Hassan", "",
         [("08:00 – 12:00", "Drive to Halebeedu", ""),
          ("12:00 – 13:00", "Lunch", ""),
          ("13:00 – 16:00", "Hoysaleswara Temple, Halebeedu", "Twin-shrined Hoysala temple."),
          ("16:45 – 19:30", "Chennakeshava Temple, Belur", ""),
          ("20:30 – 21:30", "Drive to Hassan", "Dinner and overnight stay.")], False),
        ("Hassan → Kukke Subramanya → Dharmasthala", "Western Ghats · Overnight: Dharmasthala", "",
         [("08:00 – 10:30", "Drive through the Western Ghats", ""),
          ("10:30 – 13:30", "Kukke Subramanya Temple", ""),
          ("13:30 – 14:30", "Lunch", ""),
          ("16:30 – 19:30", "Dharmasthala Manjunatha Temple", "Dinner and overnight stay.")], False),
        ("Dharmasthala → Udupi → Murudeshwar", "To the coast · Overnight: Murudeshwar", "",
         [("Morning", "Udupi Sri Krishna Temple", ""),
          ("Afternoon", "Drive along the coast to Murudeshwar", "Lunch en route."),
          ("Evening", "Murudeshwar Temple & beach", "The towering Shiva statue at sunset. Dinner and overnight stay.")], True),
        ("Murudeshwar → Gokarna", "Sacred beaches · Overnight: Gokarna", "",
         [("Morning", "Drive to Gokarna", ""),
          ("Late morning", "Mahabaleshwar Temple", ""),
          ("Afternoon", "Om Beach & Kudle Beach", "Time to unwind by the sea."),
          ("Evening", "At leisure", "Dinner and overnight stay.")], True),
        ("Gokarna → Goa", "Tour ends", "",
         [("Morning", "Drive to Goa", "Drop-off at Goa airport for your onward journey.")], True),
    ],
    incl=TEMPLE_INCL, excl=TEMPLE_EXCL,
    images=["ka", "ka-chamundi", "ka-hoysala", "ka-belur", "ka-kukke", "ka-dharma"],
    know=TEMPLE_KNOW, faq=TEMPLE_FAQ("The tour starts at Bengaluru airport on Day 1 and ends in Goa."),
))

TOURS.append(dict(
    slug="tour-everest-base-camp", cat="adventure", region="Nepal", rkey="nepal",
    title="Everest Base Camp & Kala Patthar Trek", short="Everest Base Camp Trek",
    days=15, nights=14, route="Kathmandu → Everest Base Camp", price=217500, featured=True, badge="Anmish Adventures",
    card=["Everest Base Camp (5,486 m) & Kala Patthar", "Tengboche Monastery", "Flights, guides & meals on trek"],
    stats=[("peak", "5,545 m", "Highest point"), ("cal", "15", "Days"), ("pin", "Nepal", "Khumbu region"),
           ("user", "Guided", "Expert team"), ("shield", "Insured", "Medical & evacuation")],
    overview=["A classic trek through the Khumbu to Everest Base Camp and the summit of Kala Patthar — passing through rhododendron forests, Sherpa villages and high glacial terrain, with views of Everest, Lhotse, Nuptse and Ama Dablam.",
              "The itinerary includes two acclimatisation days, a visit to Tengboche Monastery and a sunrise climb of Kala Patthar. Experienced guides, porters, meals on the trek and high-altitude insurance are included. The itinerary is indicative and may change with weather and trail conditions."],
    highlights=[("Everest Base Camp", "Stand at 5,486 m beside the Khumbu Icefall"),
                ("Kala Patthar", "Sunrise over Everest from 5,545 m"),
                ("Tengboche", "Prayer ceremony at the Khumbu’s great monastery"),
                ("Namche Bazaar", "The Sherpa capital and acclimatisation hub")],
    stops=["Kathmandu", "Lukla", "Phakding", "Namche", "Deboche", "Dingboche", "Lobuche", "Gorakshep", "EBC", "Kala Patthar"],
    itinerary=[
        ("Arrival in Kathmandu", "Briefing · Drive to Ramechhap", "",
         [("Day", "Airport pick-up & check-in", "Trek briefing and equipment check."),
          ("Evening", "Drive to Ramechhap", "For the early flight to Lukla.")], False),
        ("Fly to Lukla (2,800 m) → Trek to Phakding (2,610 m)", "3–4 hours trekking", "",
         [("Morning", "Flight to Lukla", "From Ramechhap (Manthali) airport."),
          ("Afternoon", "Trek to Phakding", "A gentle first walk along the Dudh Kosi.")], False),
        ("Phakding → Namche Bazaar (3,450 m)", "5–6 hours trekking", "",
         [("Day", "Trek along the Dudh Kosi", "Cross two suspension bridges, then a steep two-hour climb to Namche.")], False),
        ("Acclimatisation day in Namche Bazaar", "3,450 m", "",
         [("Morning", "Hike to Everest View point", "First views of Everest."),
          ("Afternoon", "Explore Namche", "Rest and local sightseeing.")], False),
        ("Namche → Deboche (3,820 m)", "4–5 hours trekking", "",
         [("Day", "Trek to Tengboche", "Visit the monastery and attend a prayer ceremony, then continue to Deboche.")], False),
        ("Deboche → Dingboche (4,260 m)", "4–5 hours trekking", "",
         [("Day", "Into the Imja Valley", "Past chortens and mani walls.")], False),
        ("Acclimatisation day in Dingboche", "4,260 m", "",
         [("Day", "Hike up Nagarjuna Hill", "Panoramic mountain views, then rest.")], False),
        ("Dingboche → Lobuche (4,930 m)", "4–5 hours trekking", "",
         [("Day", "Via Pheriche and Dugla", "Trek beside the Khumbu Glacier.")], False),
        ("Lobuche → Everest Base Camp (5,486 m) → Gorakshep (5,140 m)", "7–8 hours trekking", "",
         [("Morning", "Trek to Gorakshep", "Lunch at Gorakshep."),
          ("Afternoon", "Everest Base Camp", "Photos at base camp beside the Khumbu Icefall, then return to Gorakshep.")], False),
        ("Kala Patthar (5,545 m) sunrise → Pheriche", "Summit day", "",
         [("Pre-dawn", "Climb Kala Patthar", "Sunrise over Everest."),
          ("Day", "Return & descend", "Back to Gorakshep for breakfast, then descend to Pheriche.")], False),
        ("Pheriche → Namche Bazaar", "Descent", "",
         [("Day", "Trek back to Namche", "Time for souvenir shopping.")], False),
        ("Namche → Lukla", "Final day of trekking", "",
         [("Evening", "Farewell dinner", "With the guides and porters.")], False),
        ("Fly to Kathmandu", "Weather dependent", "",
         [("Day", "Flight to Kathmandu or Ramechhap", "Celebration dinner in Kathmandu.")], False),
        ("Kathmandu", "Buffer day", "",
         [("Day", "Weather backup or leisure", "Half-day sightseeing if the buffer is not needed.")], False),
        ("Departure", "Trek ends", "",
         [("Day", "Transfer to Kathmandu airport", "")], False),
    ],
    incl=["Round-trip flights Hyderabad – Kathmandu", "Airport transfers in Kathmandu", "3 nights in 3-star hotels in Kathmandu (B&B)",
          "Transfer to Ramechhap & domestic flights to Lukla", "One porter per two trekkers", "English-speaking guides (3 per 10 trekkers)",
          "All meals on the trek, boiled water & hot drinks", "First aid, emergency oxygen & communication devices",
          "Staff wages & insurance", "High-altitude, medical & evacuation insurance", "EBC trek certificate"],
    excl=["Personal clothing & trekking equipment", "Personal expenses (laundry, phone, internet, drinks)",
          "Costs from weather changes or unforeseen events", "Tips for guides & porters", "Nepal visa fees for non-Indian passport holders"],
    images=["ev", "ev-2", "ev-3", "ev-4", "ev-5", "ev-6"],
    know=ADV_KNOW, faq=ADV_FAQ("The trek starts and ends in Kathmandu, with flights from Hyderabad included."),
))

TOURS.append(dict(
    slug="tour-kilimanjaro-expedition", cat="adventure", region="Tanzania", rkey="tanzania",
    title="Kilimanjaro Expedition via the Marangu Route", short="Kilimanjaro Expedition",
    days=9, nights=8, route="Moshi → Uhuru Peak", price=119699, featured=True, badge="Anmish Adventures",
    card=["Uhuru Peak (5,895 m), Africa’s highest point", "Hut stays on the Marangu route", "Park fees, crew & meals included"],
    stats=[("peak", "5,895 m", "Uhuru Peak"), ("cal", "9", "Days"), ("pin", "Tanzania", "Kilimanjaro NP"),
           ("user", "Guided", "Expert crew"), ("shield", "Insured", "Trip insurance")],
    overview=["Climb Africa’s highest mountain by the Marangu route — through tropical rainforest and alpine moorland to the volcanic scree of Kibo, reaching Gillman’s Point and Uhuru Peak at 5,895 m for sunrise on the crater rim.",
              "The route uses mountain huts, with an acclimatisation day at Horombo and a buffer day for weather. Park fees, camping equipment, oxygen, meals on the mountain and crew are included."],
    highlights=[("Uhuru Peak", "The summit of Kilimanjaro at 5,895 m"),
                ("Gillman’s Point", "Sunrise on the crater rim at 5,685 m"),
                ("Rainforest to moorland", "Five climate zones in a single climb"),
                ("Zebra Rocks", "Acclimatisation walk with views of Mawenzi")],
    stops=["Moshi", "Marangu Gate", "Mandara Hut", "Horombo Hut", "Kibo Hut", "Uhuru Peak"],
    itinerary=[
        ("Arrival at Kilimanjaro International Airport", "Overnight: Moshi", "",
         [("Day", "Airport reception", "Transfer to the hotel in Moshi.")], False),
        ("Marangu Gate → Mandara Hut (2,700 m)", "5–6 hours walking", "",
         [("Day", "Through tropical rainforest", "Full board on the mountain.")], False),
        ("Mandara Hut → Horombo Hut (3,720 m)", "4–5 hours walking", "",
         [("Day", "Forest to moorland", "Views of Kibo and Mawenzi in clear weather.")], False),
        ("Acclimatisation day at Horombo", "3,720 m", "",
         [("Day", "Walk towards Mawenzi Hut", "Passing Zebra Rocks, then return to Horombo.")], False),
        ("Horombo Hut → Kibo Hut (4,700 m)", "6–7 hours walking", "",
         [("Day", "Across the saddle", "Gradual climb between Mawenzi and Kibo. There is no running water at Kibo Hut.")], False),
        ("Summit day: Uhuru Peak (5,895 m) → Horombo Hut", "The big day", "",
         [("Before midnight", "Summit push", "Over volcanic scree to Gillman’s Point (5,685 m)."),
          ("Sunrise", "Crater rim & Uhuru Peak", "The highest point in Africa."),
          ("Afternoon", "Descend to Horombo", "")], False),
        ("Horombo Hut → Marangu Gate", "5–6 hours walking", "",
         [("Day", "Descent via Mandara Hut", "Summit certificates presented, then transfer to the hotel.")], False),
        ("Buffer day", "Reserve", "",
         [("Day", "Reserve for weather", "Held back in case of harsh weather or other delays.")], False),
        ("Departure", "Expedition ends", "",
         [("Morning", "Transfer to the airport", "After breakfast.")], False),
    ],
    incl=["Airport transfers (arrival & departure)", "Hotel–gate transfers for clients & crew", "2 nights hotel with breakfast",
          "Park & camping fees", "Camping equipment", "Portable toilets & oxygen cylinders", "3 meals a day on the mountain",
          "Crew salaries", "Trip insurance"],
    excl=["Flights", "Personal clothing & equipment", "Expenses not in the itinerary", "Costs from unexpected weather changes"],
    images=["ki", "ki-1", "ki-2", "ki-3", "ki-4", "ki-5"],
    know=ADV_KNOW, faq=ADV_FAQ("The expedition starts and ends at Kilimanjaro International Airport, Tanzania. Flights are not included."),
))

TOURS.append(dict(
    slug="tour-mount-elbrus-expedition", cat="adventure", region="Russia", rkey="russia",
    title="Mount Elbrus Expedition: Summit of Europe", short="Mount Elbrus Expedition",
    days=8, nights=7, route="Mineralnye Vody → Elbrus Summit", price=129599, featured=True, badge="Anmish Adventures",
    card=["Elbrus summit (5,642 m), Europe’s highest", "Acclimatisation to Pastukhov Rocks", "Permits, cable car & meals included"],
    stats=[("peak", "5,642 m", "Summit"), ("cal", "8", "Days"), ("pin", "Caucasus", "Russia"),
           ("user", "Guided", "Expert team"), ("cert", "Certified", "Completion certificate")],
    overview=["An expedition to the summit of Mount Elbrus in the Caucasus — the highest peak in Europe at 5,642 m. The climb is based at the Gara-Bashi high camp, with acclimatisation hikes to Mount Cheget and Pastukhov Rocks before a night summit push.",
              "A reserve day is built in for weather. Accommodation, meals, permits, the cable car and a professional support team are included."],
    highlights=[("Elbrus summit", "Europe’s highest point at 5,642 m"),
                ("Gara-Bashi", "High camp at around 3,800 m"),
                ("Pastukhov Rocks", "Acclimatisation climb to 4,800 m"),
                ("Mount Cheget", "Views across the Baksan Valley")],
    stops=["Mineralnye Vody", "Terskol", "Mount Cheget", "Gara-Bashi", "Pastukhov Rocks", "Summit"],
    itinerary=[
        ("Arrival at Mineralnye Vody → Terskol/Cheget (2,100 m)", "180 km · 3–4 hours by road", "",
         [("Day", "Meet the team at MRV airport", "Transfer to Terskol/Cheget."),
          ("Evening", "Expedition briefing", "Followed by dinner.")], False),
        ("Acclimatisation hike to Mount Cheget", "Up to 3,100 m", "",
         [("Morning", "Gear check & rentals", ""),
          ("Day", "Hike towards Mount Cheget", "Weather permitting.")], False),
        ("Terskol/Cheget → Gara-Bashi (3,800 m)", "Cable car · 1–2 hours", "",
         [("Day", "Move to high camp", "Settle in and acclimatise.")], False),
        ("Acclimatisation hike to Pastukhov Rocks (4,800 m)", "6 km · 5–6 hours round trip", "",
         [("Day", "Climb and return", "Rest and hydrate at Gara-Bashi.")], False),
        ("Rest day & summit preparation", "Gara-Bashi", "",
         [("Day", "Summit briefing", "Final equipment checks."),
          ("Night", "Summit push begins", "Around 22:00–23:00 on foot, or 01:00–02:00 by snowcat, depending on conditions.")], False),
        ("Summit day: Mount Elbrus (5,642 m)", "16 km · 12–16 hours", "",
         [("Night", "Gara-Bashi → Pastukhov Rocks", "4 km, 3–4 hours on foot or about 1 hour by snowcat."),
          ("Morning", "Pastukhov Rocks → Summit", "4 km, about 3–4 hours."),
          ("Afternoon", "Descend to Gara-Bashi", "")], False),
        ("Reserve day & descent to Terskol/Cheget", "Contingency", "",
         [("Day", "Summit attempt if needed", "Otherwise descend to Terskol/Cheget and celebrate.")], False),
        ("Terskol/Cheget → Mineralnye Vody Airport", "Expedition ends", "",
         [("Morning", "Road transfer to MRV airport", "After breakfast.")], False),
    ],
    incl=["Accommodation as per itinerary", "Meals from Day 1 dinner to Day 8 breakfast", "Professional support team & first aid",
          "Permits, entry, park & camping fees", "Cable car to Gara-Bashi and back", "Airport–hotel transfers",
          "Mandatory expedition insurance", "Completion certificate from Anmish Adventures"],
    excl=["Flights to and from Mineralnye Vody", "Personal gear (rental on request)", "Breakfast & lunch on arrival day",
          "Porter for personal luggage", "Personal travel insurance & expenses", "Visa fees",
          "Emergency evacuation & hospitalisation", "Costs from changes beyond our control"],
    images=["el", "el-1-1", "el-2", "el-3", "el-4", "el-5"],
    know=ADV_KNOW, faq=ADV_FAQ("The expedition starts and ends at Mineralnye Vody (MRV) airport. Flights are not included."),
))


# ================================================================ ALL-INDIA TEMPLE TOURS (added Oct 2026)
# Every day of these itineraries is a DRAFT (flag = True) and prices are indicative -
# confirm routes, timings and prices with operations before publishing.
ZONES = {"north": "North India", "south": "South India", "west": "West India", "east": "East India", "central": "Central India"}

def temple_know(best, extra=None):
    k = [x for x in TEMPLE_KNOW if x[0] != "Best time to visit"]
    if extra: k[2] = extra
    return k + [("Best time to visit", best)]


from urllib.parse import quote as _q
def _fp(name, w=1200):
    return "https://commons.wikimedia.org/wiki/Special:FilePath/" + _q(name) + f"?width={w}"
# Wikimedia Commons photos for the all-India temple tours (hotlinked; credited on photo-credits.html)
COMMONS_NEW = {
    "uk": ("Kedarnath_Temple_with_Snow_Covered_Mountains_in_Background.jpg", "Kedarnath Temple, Uttarakhand"),
    "uk-kedarnath": ("Majestic_and_Serene_Kedarnath_temple.jpg", "Kedarnath Temple"),
    "uk-badrinath": ("Badrinath_Temple_,_Uttarakhand.jpg", "Badrinath Temple, Uttarakhand"),
    "uk-gangotri": ("Gangotri_temple.jpg", "Gangotri Temple"),
    "uk-yamunotri": ("Yamunotri_temple_and_ashram.jpg", "Yamunotri Temple"),
    "uk-haridwar": ("Aarti_at_Har-ki-Pauri,_Haridwar.jpg", "Aarti at Har Ki Pauri, Haridwar"),
    "up": ("Dashashwamedha_ghat_on_the_Ganga,_Varanasi.jpg", "Dashashwamedh Ghat, Varanasi"),
    "up-kashi": ("Kashi_Vishwanath_temple.jpg", "Kashi Vishwanath Temple, Varanasi"),
    "up-ghats": ("Morning_Aarti_of_the_Ganges,_ghats_of_Varanasi.jpg", "Morning aarti on the ghats of Varanasi"),
    "up-sangam": ("Boat_Pilgrims_Triveni_Sangam_Allahabad_Jan24_A7C_08513.jpg", "Pilgrims at the Triveni Sangam, Prayagraj"),
    "up-ayodhya": ("Shri_Ram_Janambhoomi_Mandir,_Ayodhya_Dham.jpg", "Shri Ram Janmabhoomi Mandir, Ayodhya"),
    "up-sarnath": ("Dhamekh_Stupa_at_Sarnath,_Varanasi,_India.jpg", "Dhamek Stupa, Sarnath"),
    "pb": ("Golden_Temple_(Harmandir_Sahib),_Amritsar.jpg", "Golden Temple (Harmandir Sahib), Amritsar"),
    "pb-golden": ("Harmandir_Sahib,_Amritsar,_India.jpg", "Harmandir Sahib, Amritsar"),
    "pb-wagah": ("Wagah_-_attari_border_ceremony.jpg", "Attari–Wagah border ceremony"),
    "pb-vaishno": ("Mata_Vaishno_Devi_Bhawan,_Jammu._India.jpg", "Mata Vaishno Devi Bhawan"),
    "pb-katra": ("Trikuta_Mountains.jpg", "Trikuta Mountains, Katra"),
    "gj": ("Dwarkadhish_Temple,_Dwarka,_Gujarat.JPG", "Dwarkadhish Temple, Dwarka"),
    "gj-dwarka": ("Dwarakadhish_Temple_Of_Lord_Krishna,_At_Dwarka,_Gujarat..JPG", "Dwarkadhish Temple of Lord Krishna"),
    "gj-somnath": ("Somnath_Temple_Patan_Gujarat.jpg", "Somnath Temple, Gujarat"),
    "gj-nageshwar": ("Shri_Nageshwar_Jyotirling_temple,_Dwarka,_Gujarat.jpg", "Nageshwar Jyotirlinga, Dwarka"),
    "gj-betdwarka": ("Dwarka_temple_Gomati_ghat.jpg", "Gomti Ghat, Dwarka"),
    "od": ("Konark_Sun_Temple_-_North_Side_View.jpg", "Konark Sun Temple, Odisha"),
    "od-konark": ("Sun_Temple_Main_Structure,_Konark,_Orissa.jpg", "Sun Temple, Konark"),
    "od-puri": ("Jagannath_Temple,_Puri,_Odisha.jpg", "Jagannath Temple, Puri"),
    "od-lingaraj": ("Lingaraj_temple_Bhubaneswar.jpg", "Lingaraj Temple, Bhubaneswar"),
    "od-chandrabhaga": ("Chandrabhaga_Beach_in_Odisha_21.jpg", "Chandrabhaga Beach, Konark"),
    "mp": ("Omkareshwar_Mandhata_island.jpg", "Mandhata island, Omkareshwar"),
    "mp-mahakal": ("Mahakaleshwar_Temple,_Ujjain.jpg", "Mahakaleshwar Temple, Ujjain"),
    "mp-omkareshwar": ("Temple_view_omkareshwar.jpg", "Omkareshwar Temple"),
    "mp-maheshwar": ("Maheshwar_Fort-Ahilya_Ghat.jpg", "Ahilya Fort and ghat, Maheshwar"),
    "mp-ramghat": ("Ram_Ghat,_Ujjain_01.jpg", "Ram Ghat, Ujjain"),
}
CREDITS_NEW = []
# images
for key, label, kind in [
        ("uk", "Char Dham Yatra", "mountain"), ("uk-kedarnath", "Kedarnath", "mountain"), ("uk-badrinath", "Badrinath", "temple"),
        ("uk-gangotri", "Gangotri", "mountain"), ("uk-yamunotri", "Yamunotri", "mountain"), ("uk-haridwar", "Har Ki Pauri, Haridwar", "temple"),
        ("up", "Kashi, Prayagraj & Ayodhya", "temple"), ("up-kashi", "Kashi Vishwanath", "temple"), ("up-ghats", "Ganga Aarti, Varanasi", "temple"),
        ("up-sangam", "Triveni Sangam", "wellness"), ("up-ayodhya", "Ram Mandir, Ayodhya", "temple"), ("up-sarnath", "Sarnath", "temple"),
        ("pb", "Golden Temple & Vaishno Devi", "temple"), ("pb-golden", "Golden Temple, Amritsar", "temple"), ("pb-wagah", "Attari–Wagah Border", "city"),
        ("pb-vaishno", "Vaishno Devi", "mountain"), ("pb-katra", "Katra", "mountain"),
        ("gj", "Dwarka & Somnath", "temple"), ("gj-dwarka", "Dwarkadhish Temple", "temple"), ("gj-somnath", "Somnath Temple", "temple"),
        ("gj-nageshwar", "Nageshwar Jyotirlinga", "temple"), ("gj-betdwarka", "Gomti Ghat, Dwarka", "temple"),
        ("od", "Puri, Konark & Bhubaneswar", "temple"), ("od-konark", "Konark Sun Temple", "temple"), ("od-puri", "Jagannath Temple, Puri", "temple"),
        ("od-lingaraj", "Lingaraj Temple", "temple"), ("od-chandrabhaga", "Chandrabhaga Beach", "wellness"),
        ("mp", "Ujjain & Omkareshwar", "temple"), ("mp-mahakal", "Mahakaleshwar, Ujjain", "temple"), ("mp-omkareshwar", "Omkareshwar", "temple"),
        ("mp-maheshwar", "Maheshwar Ghats", "city"), ("mp-ramghat", "Ram Ghat, Ujjain", "temple")]:
    f = COMMONS_NEW.get(key)
    add(key, label, kind, _fp(f[0]) if f else None)
    if f: CREDITS_NEW.append((f[1], "https://commons.wikimedia.org/wiki/File:" + f[0]))

D = True  # draft itinerary day

TOURS.append(dict(
    slug="tour-char-dham-yatra", cat="temple", region="Uttarakhand", rkey="uttarakhand", zone="north",
    title="Char Dham Yatra: 12 Days to Yamunotri, Gangotri, Kedarnath & Badrinath", short="Char Dham Yatra",
    days=12, nights=11, route="Haridwar → Rishikesh", price=38500, featured=True, badge="Seasonal",
    card=["All four Himalayan dhams in one journey", "Treks to Yamunotri & Kedarnath, with pony and helicopter options", "Stays, transport & guide included"],
    stats=[("temple", "4", "Himalayan dhams"), ("peak", "3,583 m", "Kedarnath"), ("map", "2", "Treks on the route"),
           ("car", "Private", "Transport"), ("meal", "All meals", "Included")],
    overview=["The Char Dham Yatra is one of Hinduism’s most revered pilgrimages: four shrines high in the Garhwal Himalaya, at the sources of the Yamuna and the Ganga, the Jyotirlinga of Kedarnath and the abode of Lord Vishnu at Badrinath.",
              "This twelve-day journey starts and ends on the Ganga at Haridwar and Rishikesh, with a private vehicle, a tour manager, all meals and stays near each dham. The route is long and mountainous, so we pace it with early starts, rest stops and time to acclimatise."],
    highlights=[("Yamunotri", "Source of the Yamuna, reached by a trek from Janki Chatti"),
                ("Gangotri", "Temple of Goddess Ganga on the Bhagirathi river"),
                ("Kedarnath", "Jyotirlinga temple set below snow peaks at 3,583 m"),
                ("Badrinath", "Shrine of Lord Badri Vishal on the Alaknanda")],
    stops=["Haridwar", "Barkot", "Yamunotri", "Uttarkashi", "Gangotri", "Guptkashi", "Kedarnath", "Badrinath", "Devprayag", "Rishikesh"],
    itinerary=[
        ("Arrival in Haridwar", "Ganga Aarti · Overnight: Haridwar", "Arrive in Haridwar by afternoon and check in.",
         [("Evening", "Ganga Aarti at Har Ki Pauri", "The evening aarti on the ghats of the Ganga."),
          ("Night", "Yatra briefing & dinner", "Your tour manager walks you through the route ahead.")], D),
        ("Haridwar → Barkot", "Into the mountains · Overnight: Barkot", "",
         [("Morning", "Drive to Barkot", "Via Dehradun and Mussoorie, with views of the Yamuna valley."),
          ("Evening", "Check-in & rest", "Dinner and overnight stay.")], D),
        ("Barkot → Yamunotri → Barkot", "First dham · Overnight: Barkot", "",
         [("Early morning", "Drive to Janki Chatti", "Start point for the Yamunotri trek."),
          ("Morning", "Trek to Yamunotri", "About 6 km each way; ponies and palkis are available."),
          ("Midday", "Yamunotri Temple & Surya Kund", "Darshan and the hot spring where rice is cooked as prasad."),
          ("Evening", "Return to Barkot", "Dinner and overnight stay.")], D),
        ("Barkot → Uttarkashi", "Valley drive · Overnight: Uttarkashi", "",
         [("Morning", "Drive to Uttarkashi", "Along the Bhagirathi valley."),
          ("Evening", "Kashi Vishwanath Temple, Uttarkashi", "Evening darshan. Dinner and overnight stay.")], D),
        ("Uttarkashi → Gangotri → Uttarkashi", "Second dham · Overnight: Uttarkashi", "",
         [("Morning", "Drive to Gangotri", "Through Harsil’s apple orchards and deodar forests."),
          ("Midday", "Gangotri Temple", "Darshan and a holy dip in the Bhagirathi."),
          ("Evening", "Return to Uttarkashi", "Dinner and overnight stay.")], D),
        ("Uttarkashi → Guptkashi", "Long mountain drive · Overnight: Guptkashi", "",
         [("Day", "Drive to Guptkashi", "Via Tehri, along the Mandakini valley."),
          ("Evening", "Ardhanareeshwar Temple (optional)", "Dinner and overnight stay.")], D),
        ("Guptkashi → Gaurikund → Kedarnath", "Third dham · Overnight: Kedarnath", "",
         [("Early morning", "Drive to Sonprayag & shuttle to Gaurikund", ""),
          ("Day", "Trek to Kedarnath", "About 16 km; ponies, palkis and helicopter services are available."),
          ("Evening", "Evening aarti at Kedarnath", "Dinner and overnight stay near the temple.")], D),
        ("Kedarnath → Guptkashi", "Morning darshan · Overnight: Guptkashi", "",
         [("Early morning", "Kedarnath darshan", "Followed by a visit to the Adi Shankaracharya Samadhi."),
          ("Day", "Trek down to Gaurikund", "Then drive back to Guptkashi. Dinner and overnight stay.")], D),
        ("Guptkashi → Badrinath", "Fourth dham · Overnight: Badrinath", "",
         [("Day", "Drive to Badrinath", "Via Rudraprayag and Joshimath."),
          ("Evening", "Badrinath Temple darshan", "After a dip in Tapt Kund. Dinner and overnight stay.")], D),
        ("Badrinath → Mana → Rudraprayag", "Mana village · Overnight: Rudraprayag", "",
         [("Morning", "Mana village", "Vyas Gufa, Ganesh Gufa and Bhim Pul near the Saraswati river."),
          ("Afternoon", "Drive to Rudraprayag", "At the confluence of the Alaknanda and Mandakini. Dinner and overnight stay.")], D),
        ("Rudraprayag → Devprayag → Rishikesh", "Birth of the Ganga · Overnight: Rishikesh", "",
         [("Morning", "Devprayag", "Where the Alaknanda and Bhagirathi meet to form the Ganga."),
          ("Evening", "Ganga Aarti at Triveni Ghat, Rishikesh", "Dinner and overnight stay.")], D),
        ("Rishikesh → Haridwar", "Tour ends", "",
         [("Morning", "Rishikesh at leisure", "Then drop-off at Haridwar railway station or Dehradun airport.")], D),
    ],
    incl=["Travel as per itinerary", "Private vehicle suited to hill roads", "Breakfast, lunch & dinner", "Hotel & guesthouse accommodation (11 nights)",
          "Dedicated tour manager", "Yatra registration support"],
    excl=["Flights or trains to Haridwar", "Ponies, palkis & helicopter tickets", "Special puja & darshan tickets", "Personal expenses & tips"],
    images=["uk", "uk-kedarnath", "uk-badrinath", "uk-gangotri", "uk-yamunotri", "uk-haridwar"],
    know=temple_know("The temples open around late April or May and close around October–November; exact dates are announced each year. Avoid the peak monsoon weeks of July and August.",
                     ("Fitness & altitude", "The route reaches 3,583 m at Kedarnath and includes two long treks. A basic fitness routine and a doctor’s check-up are advised; ponies, palkis and helicopters can be arranged.")),
    faq=[("Where does the tour start and end?", "The tour starts in Haridwar and ends with a drop-off at Haridwar or Dehradun airport."),
         ("Is the yatra suitable for senior citizens?", "Yes, with planning. Ponies, palkis and helicopter services can replace the treks. Tell us about any health conditions so we can advise."),
         ("Is registration required?", "Yes, the Uttarakhand government requires yatra registration for every pilgrim. Our team helps you complete it."),
         ("Can I do only Do Dham (Kedarnath & Badrinath)?", "Yes. We can plan a shorter Do Dham itinerary of around 6–7 days.")],
))

TOURS.append(dict(
    slug="tour-kashi-prayagraj-ayodhya", cat="temple", region="Uttar Pradesh", rkey="uttarpradesh", zone="north",
    title="Kashi, Prayagraj & Ayodhya: 6 Days on the Sacred Ganga Trail", short="Kashi, Prayagraj & Ayodhya",
    days=6, nights=5, route="Varanasi → Ayodhya", price=16500, featured=True,
    card=["Kashi Vishwanath & the Ganga Aarti", "Triveni Sangam and Ayodhya’s Ram Mandir", "Stays, transport & guide included"],
    stats=[("temple", "10", "Sacred sites"), ("boat", "2", "Boat rides"), ("pin", "3", "Holy cities"),
           ("car", "Private", "Transport"), ("meal", "All meals", "Included")],
    overview=["Three of India’s holiest cities in one unhurried journey: Varanasi on the Ganga, Prayagraj where three rivers meet, and Ayodhya, birthplace of Lord Rama.",
              "Watch the evening Ganga Aarti, take a sunrise boat past the ghats, bathe at the Triveni Sangam and offer prayers at the Ram Mandir. A private vehicle, a tour manager, comfortable stays and all meals are included."],
    highlights=[("Kashi Vishwanath", "The Jyotirlinga temple and its riverfront corridor in Varanasi"),
                ("Ganga Aarti", "Evening aarti at Dashashwamedh Ghat"),
                ("Triveni Sangam", "Confluence of the Ganga, Yamuna and the mythical Saraswati"),
                ("Ayodhya", "Shri Ram Janmabhoomi Mandir and Hanuman Garhi")],
    stops=["Varanasi", "Sarnath", "Prayagraj", "Ayodhya"],
    itinerary=[
        ("Arrival in Varanasi", "Ganga Aarti · Overnight: Varanasi", "Arrive in Varanasi and check in.",
         [("Evening", "Ganga Aarti at Dashashwamedh Ghat", "Watch from the ghats or from a boat on the river."),
          ("Night", "Dinner & overnight stay", "Varanasi.")], D),
        ("Varanasi: ghats & temples", "Kashi Vishwanath · Overnight: Varanasi", "",
         [("Sunrise", "Boat ride along the ghats", "From Assi to Manikarnika as the city wakes."),
          ("Morning", "Kashi Vishwanath Temple", "Darshan at the Jyotirlinga, then Annapurna Devi and Kaal Bhairav."),
          ("Afternoon", "Sarnath", "Where the Buddha gave his first sermon — Dhamek Stupa and the museum."),
          ("Evening", "Sankat Mochan Hanuman Temple", "Dinner and overnight stay.")], D),
        ("Varanasi → Prayagraj", "Triveni Sangam · Overnight: Prayagraj", "",
         [("Morning", "Drive to Prayagraj", "About three hours."),
          ("Afternoon", "Boat to the Triveni Sangam", "A holy dip at the meeting point of three rivers."),
          ("Evening", "Bade Hanuman Temple & Alopi Devi", "Dinner and overnight stay.")], D),
        ("Prayagraj → Ayodhya", "Saryu Aarti · Overnight: Ayodhya", "",
         [("Morning", "Drive to Ayodhya", "About four hours, with a lunch stop."),
          ("Evening", "Saryu Aarti at Ram ki Paidi", "Dinner and overnight stay.")], D),
        ("Ayodhya", "Ram Mandir · Overnight: Ayodhya", "",
         [("Morning", "Shri Ram Janmabhoomi Mandir", "Phones and bags are deposited at the lockers before entry."),
          ("Late morning", "Hanuman Garhi", "Hilltop Hanuman temple reached by steps."),
          ("Afternoon", "Kanak Bhawan & Dashrath Mahal", "Dinner and overnight stay.")], D),
        ("Departure", "Tour ends", "",
         [("Morning", "Drop-off", "At Ayodhya airport or Lucknow for your onward journey.")], D),
    ],
    incl=TEMPLE_INCL + ["Boat rides in Varanasi and Prayagraj"], excl=TEMPLE_EXCL,
    images=["up", "up-ghats", "up-kashi", "up-sangam", "up-ayodhya", "up-sarnath"],
    know=temple_know("October to March is the most comfortable time. Summers are very hot, and the Magh Mela (January–February) brings large crowds to Prayagraj."),
    faq=TEMPLE_FAQ("The tour starts in Varanasi and ends with a drop-off at Ayodhya airport or Lucknow."),
))

TOURS.append(dict(
    slug="tour-golden-temple-vaishno-devi", cat="temple", region="Punjab & J&K", rkey="punjab-jk", zone="north",
    title="Golden Temple & Vaishno Devi: 5 Days of Faith in the North", short="Golden Temple & Vaishno Devi",
    days=5, nights=4, route="Amritsar → Jammu", price=14500,
    card=["Harmandir Sahib and the Palki Sahib ceremony", "Mata Vaishno Devi yatra from Katra", "Stays, transport & guide included"],
    stats=[("temple", "5", "Sacred sites"), ("map", "~12 km", "Trek to Bhawan"), ("pin", "3", "Cities visited"),
           ("car", "Private", "Transport"), ("meal", "All meals", "Included")],
    overview=["Two of North India’s most visited shrines in one journey: the Golden Temple in Amritsar, where the langar serves free meals to everyone who comes, and the cave shrine of Mata Vaishno Devi in the Trikuta hills.",
              "Spend two days in Amritsar, including the Beating Retreat ceremony at the Attari–Wagah border, then travel to Katra for the yatra — on foot, by pony or by helicopter where available."],
    highlights=[("Golden Temple", "Harmandir Sahib, its sarovar and the night Palki Sahib ceremony"),
                ("Attari–Wagah", "The Beating Retreat ceremony at the border"),
                ("Vaishno Devi", "Cave shrine of the Mother Goddess above Katra"),
                ("Bhairon Baba", "Hilltop temple reached by ropeway after darshan")],
    stops=["Amritsar", "Attari–Wagah", "Katra", "Vaishno Devi", "Jammu"],
    itinerary=[
        ("Arrival in Amritsar", "Golden Temple · Overnight: Amritsar", "Arrive in Amritsar and check in.",
         [("Evening", "Golden Temple (Harmandir Sahib)", "The temple lit up over the sarovar."),
          ("Night", "Palki Sahib ceremony", "The nightly procession carrying the Guru Granth Sahib.")], D),
        ("Amritsar", "Heritage & the border · Overnight: Amritsar", "",
         [("Morning", "Jallianwala Bagh & Partition Museum", ""),
          ("Late morning", "Durgiana Temple", "Lakshmi Narayan temple built in the style of the Golden Temple."),
          ("Afternoon", "Attari–Wagah Beating Retreat", "The daily flag-lowering ceremony at the border."),
          ("Evening", "Langar at the Golden Temple (optional)", "Dinner and overnight stay.")], D),
        ("Amritsar → Katra", "Into the Trikuta hills · Overnight: Katra", "",
         [("Morning", "Drive to Katra", "About six hours."),
          ("Evening", "Yatra registration & rest", "Collect your RFID yatra card. Dinner and overnight stay.")], D),
        ("Katra → Vaishno Devi → Katra", "Mata’s darshan · Overnight: Katra", "",
         [("Early morning", "Trek to Bhawan", "About 12 km from Banganga; ponies, palkis, battery cars and a Katra–Sanjichhat helicopter are available."),
          ("Midday", "Mata Vaishno Devi darshan", "In the holy cave."),
          ("Afternoon", "Bhairon Baba Temple", "By ropeway from Bhawan, then return to Katra.")], D),
        ("Katra → Jammu", "Tour ends", "",
         [("Morning", "Drive to Jammu", "Drop-off at Jammu airport or railway station.")], D),
    ],
    incl=TEMPLE_INCL, excl=TEMPLE_EXCL[:-2] + ["Ponies, palkis, helicopter & ropeway tickets", "Personal expenses & tips"],
    images=["pb", "pb-golden", "pb-vaishno", "pb-wagah", "pb-katra"],
    know=temple_know("The yatra runs all year. March to June and September to November have the most comfortable weather; winters are cold at Bhawan.",
                     ("Physical activity", "The Vaishno Devi trek is about 12 km each way on a paved path. Ponies, palkis, battery cars and helicopters can be arranged, subject to availability.")),
    faq=TEMPLE_FAQ("The tour starts in Amritsar and ends with a drop-off at Jammu airport or railway station."),
))

TOURS.append(dict(
    slug="tour-jyotirlinga-ujjain-omkareshwar", cat="temple", region="Madhya Pradesh", rkey="madhyapradesh", zone="central",
    title="Jyotirlinga Trail: 4 Days in Ujjain, Omkareshwar & Maheshwar", short="Ujjain & Omkareshwar Jyotirlinga",
    days=4, nights=3, route="Indore → Indore", price=9500,
    card=["Two Jyotirlingas: Mahakaleshwar & Omkareshwar", "Mahakal Lok and the Narmada ghats", "Stays, transport & guide included"],
    stats=[("temple", "8", "Sacred temples"), ("map", "2", "Jyotirlingas"), ("pin", "4", "Cities visited"),
           ("car", "Private", "Transport"), ("meal", "All meals", "Included")],
    overview=["A short, rewarding circuit in Madhya Pradesh that covers two of the twelve Jyotirlingas — Mahakaleshwar in Ujjain and Omkareshwar on an island in the Narmada — along with the ghats of Maheshwar.",
              "Ideal for a long weekend, with a private vehicle from Indore, a tour manager, comfortable stays and all meals included. We can help you apply for the early-morning Bhasma Aarti at Mahakaleshwar."],
    highlights=[("Mahakaleshwar", "Jyotirlinga of Ujjain and the Mahakal Lok corridor"),
                ("Omkareshwar", "Jyotirlinga on Mandhata island in the Narmada"),
                ("Ekatma Dham", "The 108-ft Statue of Oneness of Adi Shankaracharya"),
                ("Maheshwar", "Ahilya Fort and the Narmada ghats")],
    stops=["Indore", "Ujjain", "Omkareshwar", "Maheshwar"],
    itinerary=[
        ("Indore → Ujjain", "Mahakal · Overnight: Ujjain", "Pick-up in Indore and drive to Ujjain (about 1.5 hours).",
         [("Afternoon", "Mahakal Lok", "The temple corridor with murals and sculptures from Shiva’s stories."),
          ("Evening", "Mahakaleshwar darshan & Ram Ghat aarti", "On the Shipra river. Dinner and overnight stay.")], D),
        ("Ujjain → Omkareshwar", "Temples of Ujjain · Overnight: Omkareshwar", "",
         [("Early morning", "Bhasma Aarti (if booked)", "Requires advance online booking and is subject to availability."),
          ("Morning", "Kal Bhairav, Harsiddhi & Sandipani Ashram", ""),
          ("Afternoon", "Drive to Omkareshwar", "About three hours. Dinner and overnight stay.")], D),
        ("Omkareshwar → Maheshwar → Indore", "Narmada · Overnight: Indore", "",
         [("Morning", "Omkareshwar & Mamleshwar darshan", "Cross to Mandhata island by bridge or boat."),
          ("Late morning", "Ekatma Dham", "Statue of Oneness of Adi Shankaracharya."),
          ("Afternoon", "Maheshwar", "Ahilya Fort, the ghats and Maheshwari weavers."),
          ("Evening", "Drive to Indore", "Sarafa night food market (optional). Overnight stay.")], D),
        ("Indore", "Tour ends", "",
         [("Morning", "Khajrana Ganesh Temple & Rajwada", "Then drop-off at Indore airport or railway station.")], D),
    ],
    incl=TEMPLE_INCL, excl=TEMPLE_EXCL,
    images=["mp", "mp-mahakal", "mp-omkareshwar", "mp-maheshwar", "mp-ramghat"],
    know=temple_know("October to March is the most comfortable time. Shravan (July–August) and Mahashivratri bring very large crowds."),
    faq=TEMPLE_FAQ("The tour starts and ends in Indore."),
))

TOURS.append(dict(
    slug="tour-dwarka-somnath", cat="temple", region="Gujarat", rkey="gujarat", zone="west",
    title="Dwarka & Somnath: 6 Days Through Gujarat’s Sacred Coast", short="Dwarka & Somnath",
    days=6, nights=5, route="Ahmedabad → Ahmedabad", price=18500,
    card=["Dwarkadhish, Nageshwar & Bet Dwarka", "Somnath, the first Jyotirlinga", "Stays, transport & guide included"],
    stats=[("temple", "9", "Sacred temples"), ("map", "2", "Jyotirlingas"), ("pin", "5", "Cities visited"),
           ("car", "Private", "Transport"), ("meal", "All meals", "Included")],
    overview=["Follow Gujarat’s Saurashtra coast to the kingdom of Lord Krishna at Dwarka and the shore temple of Somnath, the first of the twelve Jyotirlingas.",
              "Along the way visit Nageshwar Jyotirlinga, cross the Sudarshan Setu to Bet Dwarka and stop at Porbandar, birthplace of Mahatma Gandhi. A private vehicle, a tour manager, comfortable stays and all meals are included."],
    highlights=[("Dwarkadhish", "Jagat Mandir of Lord Krishna above the Gomti Ghat"),
                ("Nageshwar", "One of the twelve Jyotirlingas, near Dwarka"),
                ("Bet Dwarka", "Island shrine reached by the Sudarshan Setu bridge"),
                ("Somnath", "The first Jyotirlinga, on the Arabian Sea")],
    stops=["Ahmedabad", "Dwarka", "Nageshwar", "Bet Dwarka", "Porbandar", "Somnath"],
    itinerary=[
        ("Arrival in Ahmedabad", "City of Gandhi · Overnight: Ahmedabad", "Arrive in Ahmedabad and check in.",
         [("Afternoon", "Sabarmati Ashram", "Gandhi’s home on the Sabarmati river."),
          ("Evening", "Akshardham, Gandhinagar", "Dinner and overnight stay.")], D),
        ("Ahmedabad → Dwarka", "Saurashtra drive · Overnight: Dwarka", "",
         [("Day", "Drive to Dwarka", "A full-day drive with stops for meals."),
          ("Evening", "Dwarkadhish Temple aarti", "Dinner and overnight stay.")], D),
        ("Dwarka: Nageshwar & Bet Dwarka", "Krishna’s kingdom · Overnight: Dwarka", "",
         [("Morning", "Dwarkadhish darshan & Gomti Ghat", ""),
          ("Late morning", "Nageshwar Jyotirlinga", ""),
          ("Afternoon", "Bet Dwarka via the Sudarshan Setu", "Then Gopi Talav and Rukmini Devi Temple."),
          ("Evening", "At leisure", "Dinner and overnight stay.")], D),
        ("Dwarka → Porbandar → Somnath", "Coastal road · Overnight: Somnath", "",
         [("Morning", "Drive to Porbandar", "Kirti Mandir, Gandhi’s birthplace, and Sudama Temple."),
          ("Afternoon", "Continue to Somnath", "Along the coast."),
          ("Evening", "Somnath aarti & light-and-sound show", "Dinner and overnight stay.")], D),
        ("Somnath → Ahmedabad", "First Jyotirlinga · Overnight: Ahmedabad", "",
         [("Morning", "Somnath darshan, Bhalka Tirth & Triveni Sangam", ""),
          ("Afternoon", "Drive to Ahmedabad", "Dinner and overnight stay.")], D),
        ("Departure", "Tour ends", "",
         [("Morning", "Drop-off", "At Ahmedabad airport or railway station.")], D),
    ],
    incl=TEMPLE_INCL, excl=TEMPLE_EXCL,
    images=["gj", "gj-dwarka", "gj-somnath", "gj-nageshwar", "gj-betdwarka"],
    know=temple_know("October to March is the most comfortable time. Janmashtami at Dwarka and Mahashivratri at Somnath are special but crowded."),
    faq=TEMPLE_FAQ("The tour starts and ends in Ahmedabad."),
))

TOURS.append(dict(
    slug="tour-puri-konark-bhubaneswar", cat="temple", region="Odisha", rkey="odisha", zone="east",
    title="Puri, Konark & Bhubaneswar: 4 Days in Odisha’s Golden Triangle", short="Puri, Konark & Bhubaneswar",
    days=4, nights=3, route="Bhubaneswar → Bhubaneswar", price=12500,
    card=["Jagannath Temple, Puri", "UNESCO-listed Konark Sun Temple", "Stays, transport & guide included"],
    stats=[("temple", "7", "Sacred sites"), ("star", "1", "UNESCO site"), ("pin", "3", "Cities visited"),
           ("car", "Private", "Transport"), ("meal", "All meals", "Included")],
    overview=["Odisha’s golden triangle brings together the temple city of Bhubaneswar, the Jagannath Temple at Puri and the great stone chariot of the Konark Sun Temple.",
              "Explore Kalinga-style temple architecture, the rock-cut caves of Udayagiri and a village of pattachitra painters, with time by the sea at Puri. A private vehicle, a tour manager, stays and all meals are included."],
    highlights=[("Jagannath Temple", "One of the Char Dham shrines, home of Lord Jagannath"),
                ("Konark", "13th-century Sun Temple, a UNESCO World Heritage site"),
                ("Lingaraj", "Bhubaneswar’s great 11th-century Shiva temple"),
                ("Raghurajpur", "Heritage village of pattachitra painters")],
    stops=["Bhubaneswar", "Dhauli", "Puri", "Raghurajpur", "Konark"],
    itinerary=[
        ("Arrival in Bhubaneswar", "Temple city · Overnight: Bhubaneswar", "Arrive in Bhubaneswar and check in.",
         [("Afternoon", "Lingaraj Temple", "Non-Hindu visitors can view the temple from the platform outside."),
          ("Evening", "Mukteswar & Rajarani temples", "Dinner and overnight stay.")], D),
        ("Bhubaneswar → Puri", "Caves & the coast · Overnight: Puri", "",
         [("Morning", "Udayagiri & Khandagiri caves", "Rock-cut Jain caves from the 2nd century BCE."),
          ("Late morning", "Dhauli Shanti Stupa", "On the site of the Kalinga war."),
          ("Afternoon", "Drive to Puri", "About 1.5 hours."),
          ("Evening", "Puri beach & Swargadwar", "Dinner and overnight stay.")], D),
        ("Puri & Konark", "Jagannath & the Sun Temple · Overnight: Puri", "",
         [("Early morning", "Jagannath Temple darshan", "Phones, cameras and leather items are not allowed inside."),
          ("Late morning", "Raghurajpur artisan village", "Pattachitra paintings and palm-leaf engraving."),
          ("Afternoon", "Konark Sun Temple", "The temple built as the chariot of the Sun God."),
          ("Evening", "Chandrabhaga beach", "Then back to Puri. Dinner and overnight stay.")], D),
        ("Puri → Bhubaneswar", "Tour ends", "",
         [("Morning", "Drive to Bhubaneswar", "Drop-off at the airport or railway station.")], D),
    ],
    incl=TEMPLE_INCL, excl=TEMPLE_EXCL,
    images=["od", "od-konark", "od-puri", "od-lingaraj", "od-chandrabhaga"],
    know=temple_know("October to March is the most comfortable time. The Rath Yatra in Puri (June or July) is spectacular but very crowded.",
                     ("Temple entry", "Entry into the Jagannath and Lingaraj temples is restricted to Hindus. Other travellers can view Lingaraj from a platform outside and visit Konark and the other sites.")),
    faq=TEMPLE_FAQ("The tour starts and ends in Bhubaneswar."),
))

# zones for existing South India temple tours, and order temple tours north → south
for t in TOURS:
    if t["cat"] == "temple": t.setdefault("zone", "south")
_zorder = ["north", "central", "west", "east", "south"]
_temple = sorted([t for t in TOURS if t["cat"] == "temple"], key=lambda t: _zorder.index(t["zone"]))
TOURS[:] = _temple + [t for t in TOURS if t["cat"] != "temple"]

CATS = {
    "temple": dict(file="temple-tours.html", name="Temple Tours", nav="Temple", hero="hero-temple", tile="cat-temple",
                   eyebrow="See More. Feel Divine.", h1="Journeys to India’s <em>sacred temples</em>, thoughtfully planned.",
                   lead="Fully guided pilgrimages across India — from the Himalayan dhams to the temples of the south — with comfortable stays, private transport and well-planned darshan schedules.",
                   sec_h="Curated spiritual journeys across India",
                   sec_p="North, South, East, West and Central India — each itinerary blends temple visits with the history and living traditions behind them.",
                   blurb="Curated pilgrimages to India’s great temples, with comfortable stays and every darshan planned."),
    "adventure": dict(file="adventure-tours.html", name="Adventure Tours", nav="Adventure", hero="hero-adventure", tile="cat-adventure",
                      eyebrow="See More. Feel the Thrill.", h1="Expeditions to the <em>world’s great summits</em>, safely led.",
                      lead="High-altitude treks and expeditions run with Anmish Adventures — expert leadership, acclimatisation built in, and full support from base to summit.",
                      sec_h="Journeys made for every adventurer",
                      sec_p="From Everest Base Camp to the summits of Africa and Europe, each expedition is planned around safety and acclimatisation.",
                      blurb="Treks and expeditions led by experienced mountaineers, with safety at the centre of every plan."),
    "wellness": dict(file="wellness-tours.html", name="Wellness Tours", nav="Wellness", hero="hero-wellness", tile="cat-wellness",
                     eyebrow="See More. Feel Better.", h1="Journeys made for <em>your well-being</em>.",
                     lead="Unhurried journeys that bring together sacred places, nature and quiet time by the sea — designed to leave you restored.",
                     sec_h="Restorative journeys",
                     sec_p="Gentle itineraries with time to slow down, reflect and reconnect.",
                     blurb="Unhurried journeys combining sacred places, nature and time to rest and reset."),
}

POSTS = [
    dict(slug="blog-temple-tour-dress-code-packing", img="blog-1", cat="Temple Tours", date="October 2, 2026", read="4 min read",
         title="What to Wear and Carry on a South Indian Temple Tour",
         excerpt="Dress codes, footwear, documents and the small things that make long darshan days easier.",
         body=[("p", "South India’s temples are living places of worship, and each has its own customs. A little preparation means you spend less time worrying about the rules and more time taking in the experience."),
               ("h2", "Dress modestly and traditionally"),
               ("p", "Most temples expect shoulders and knees to be covered. Some, such as Sree Padmanabhaswamy in Thiruvananthapuram and Guruvayur, have stricter rules: men wear a dhoti or mundu and no shirt, and women wear a saree, half-saree or salwar. If you’re unsure, carry a simple dhoti or a stole — they’re easy to pack and can be bought near most temples."),
               ("h2", "Plan for bare feet"),
               ("p", "Footwear is removed before entering, often at a counter outside the temple. Wear slip-on shoes, and carry a pair of socks for hot stone floors in the afternoon."),
               ("h2", "Keep a small day bag"),
               ("ul", ["A valid photo ID — some temples and special darshan queues ask for one", "A refillable water bottle", "Any regular medication", "A small towel or handkerchief", "Some cash for offerings and prasadam"]),
               ("h2", "Phones and cameras"),
               ("p", "Photography is usually not permitted inside the sanctum and, at some temples, anywhere inside the complex. Many have mobile phone counters at the entrance. Your tour manager will let you know before each visit."),
               ("p", "Have questions about a specific temple? Get in touch and we’ll share what to expect.")]),
    dict(slug="blog-first-time-high-altitude-trek", img="blog-2", cat="Adventure", date="September 24, 2026", read="5 min read",
         title="Preparing for Your First High-Altitude Trek",
         excerpt="How to train, what acclimatisation means, and the signs to watch for on the trail.",
         body=[("p", "A trek to Everest Base Camp or a climb of Kilimanjaro is achievable for most fit, determined people — but the altitude is a different kind of challenge. Here’s how to prepare."),
               ("h2", "Start training early"),
               ("p", "Begin at least 8–12 weeks before departure. Build up to long walks with a loaded day pack, stair climbs and regular cardio. Train on consecutive days so your body learns to recover overnight."),
               ("h2", "Understand acclimatisation"),
               ("p", "As you gain altitude there is less oxygen in each breath. Our itineraries include rest and acclimatisation days — such as Namche Bazaar and Dingboche on the Everest trek — when you hike higher and return to sleep lower. These days matter; they are not optional."),
               ("h2", "Know the warning signs"),
               ("ul", ["A headache that doesn’t ease with rest and water", "Nausea or loss of appetite", "Unusual breathlessness at rest", "Dizziness or confusion"]),
               ("p", "Tell your guide straight away if you notice any of these. Descending is the most effective treatment, and the expedition team is trained to decide when it’s needed."),
               ("h2", "Pack for every season"),
               ("p", "You’ll pass through warm valleys and freezing nights in the same trip. Layer clothing, carry a good down jacket and sleeping bag, and break in your boots before you go. A full gear list is shared when you book.")]),
    dict(slug="blog-pilgrimage-with-senior-parents", img="blog-3", cat="Temple Tours", date="September 12, 2026", read="4 min read",
         title="Planning a Pilgrimage With Senior Parents",
         excerpt="Pacing, comfort and support that make a temple journey easier for older travellers.",
         body=[("p", "A pilgrimage with parents or grandparents can be one of the most meaningful journeys a family makes. With a little planning, it can be comfortable too."),
               ("h2", "Choose the right pace"),
               ("p", "Look for itineraries with no more than two major darshans a day and time to rest in the afternoon. Long drives are easier when they’re broken up with meal stops."),
               ("h2", "Ask about steps and hill climbs"),
               ("p", "Some shrines, such as Palani and Kondagattu, involve steps or hill climbs. Many have ropeways, lifts or doli services. Let us know about mobility needs in advance so we can plan access and keep a wheelchair ready where possible."),
               ("h2", "Keep medicines and documents handy"),
               ("ul", ["Carry medicines in a day bag, not checked luggage", "Keep copies of prescriptions", "Carry photo ID for each traveller", "Note emergency contacts for the trip"]),
               ("h2", "Lean on on-ground support"),
               ("p", "Our companion model provides on-ground assistance for senior and differently-abled travellers — from transfers to temple queues — so the whole family can focus on the journey.")]),
]

CREDITS = [('Gopurams of Meenakshi Temple, Madurai', 'https://commons.wikimedia.org/wiki/File:Gopurams_of_the_Madurai_Meenakshi_Temple,_Madurai,_Tamil_Nadu,_India_(2016).jpg'), ('Ama Dablam, Nepal', 'https://commons.wikimedia.org/wiki/File:Himalayas,_Ama_Dablam,_Nepal.jpg'), ('Houseboats on Vembanad Lake, Kerala', 'https://commons.wikimedia.org/wiki/File:Kerala_backwaters,_Vembanad_Lake,_Houseboats,_India.jpg'), ('Virupaksha Temple, Hampi', 'https://commons.wikimedia.org/wiki/File:Hampi,_India,_Aerial_view_of_Virupaksha_Temple,_Panorama_of_Hampi.jpg'), ('Tea plantation, Munnar', 'https://commons.wikimedia.org/wiki/File:Misty_tea_plantation_munnar.jpg'), ('Charminar, Hyderabad', 'https://commons.wikimedia.org/wiki/File:Charminar,_Hyderabad,_Telangana,_India.jpg'), ('Tea plantations, Munnar', 'https://commons.wikimedia.org/wiki/File:View_of_tea_plantations_in_Munnar.jpg'), ('Uhuru Peak, Kilimanjaro', 'https://commons.wikimedia.org/wiki/File:Uhuru_Peak_Mt._Kilimanjaro_1.JPG'), ('Golden Lily Pond, Meenakshi Temple', 'https://commons.wikimedia.org/wiki/File:Golden_Lily_Pond_and_South_Gopuram_at_Meenakshi_Amman_Temple_,_Madurai.jpg'), ('Trail from Lobuche to Gorak Shep', 'https://commons.wikimedia.org/wiki/File:Sagarmatha_National_Park-Lobuche_to_Gorak_Shep_2013-05-05_12-37-25.jpg'), ('Srirangam Temple gopuram', 'https://commons.wikimedia.org/wiki/File:Srirangam_Temple_Gopuram.jpg')]
CREDITS = CREDITS + CREDITS_NEW
CREDITS = CREDITS + [('Video: Ganga Aarti at Rishikesh (Sukh1810, CC BY-SA 4.0)', 'https://commons.wikimedia.org/wiki/File:Ganga_Aarti_at_Rishikesh.webm')]
CREDITS = CREDITS + [
    ("Meenakshi Temple gopuram, Madurai (home slider)", "https://commons.wikimedia.org/wiki/File:Meenakshi_Temple,_Gopuram,_Madurai,_India.jpg"),
]

# Travel style per temple tour (mix of private and group departures) - confirm with operations
TEMPLE_STYLES = {
    "tour-char-dham-yatra": ["group"],
    "tour-kashi-prayagraj-ayodhya": ["individual", "group"],
    "tour-golden-temple-vaishno-devi": ["individual"],
    "tour-jyotirlinga-ujjain-omkareshwar": ["individual"],
    "tour-dwarka-somnath": ["group"],
    "tour-puri-konark-bhubaneswar": ["individual"],
    "tour-sacred-telangana": ["group"],
    "tour-tamil-nadu-temple-journey": ["individual", "group"],
    "tour-sacred-kerala": ["individual"],
    "tour-sacred-andhra-pradesh": ["group"],
}
for _t in TOURS:
    if _t["slug"] in TEMPLE_STYLES: _t["styles"] = TEMPLE_STYLES[_t["slug"]]

# Square destination photos from the live site (Discover India carousel)
add("d-karnataka", "Karnataka", "temple", "2022/07/karnataka-636x636.webp", 636, 636)
add("d-kerala", "Kerala", "wellness", "2022/07/kerala-636x636.webp", 636, 636)
add("d-tamilnadu", "Tamil Nadu", "temple", "2022/07/Tamilnadu-636x636.jpg", 636, 636)
add("d-telangana", "Telangana", "temple", "2022/07/telangana1.webp", 636, 636)
add("d-andhra", "Andhra Pradesh", "temple", "2022/07/andhra-pradesh-636x636.webp", 636, 636)
DEST_IMG = {"karnataka": "d-karnataka", "kerala": "d-kerala", "tamilnadu": "d-tamilnadu", "telangana": "d-telangana", "andhra": "d-andhra"}


# ================================================================ CMS: tours come from content/tours/*.json
# The dashboard (Pages CMS) edits those JSON files; they replace the TOURS defined above.
import json as _json, os as _os, glob as _glob, re as _re
import images as _IM
_CDIR = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "content", "tours")
_real2key = {}
for _k in list(_IM.REG):
    _u = _IM._real_url(_k)
    if _u: _real2key.setdefault(_u, _k)

def _img_key(slug, n, item, cat):
    url = (item.get("image") or "").strip()
    if not url: return None
    if url in _real2key: return _real2key[url]
    m = _re.match(r"^assets/img/([\w-]+)\.svg$", url)
    if m and m.group(1) in _IM.REG: return m.group(1)
    key = f"u-{slug}-{n}"
    kind = item.get("kind") or {"adventure": "mountain", "wellness": "wellness"}.get(cat, "temple")
    _IM.add(key, item.get("caption") or "", kind if kind in _IM.KINDS else "temple", url.lstrip("/"))
    return key

def _tour_from_json(d, fname):
    slug = (d.get("slug") or _os.path.splitext(_os.path.basename(fname))[0]).strip()
    slug = "tour-" + _re.sub(r"[^a-z0-9-]+", "-", slug.lower()).strip("-")
    cat = d.get("category") or "temple"
    imgs = [k for k in (_img_key(slug, i, g, cat) for i, g in enumerate(d.get("gallery") or [], 1)) if k]
    if not imgs:
        _IM.add(f"u-{slug}-0", d.get("short_name") or d.get("title") or "", {"adventure": "mountain", "wellness": "wellness"}.get(cat, "temple"))
        imgs = [f"u-{slug}-0"]
    t = dict(
        slug=slug, cat=cat, region=d.get("region") or "", rkey=d.get("region_key") or _re.sub(r"[^a-z0-9]+", "", (d.get("region") or "x").lower()),
        title=d.get("title") or "", short=d.get("short_name") or d.get("title") or "",
        days=int(d.get("days") or 1), nights=int(d.get("nights") or 0), route=d.get("route") or "", price=int(d.get("price") or 0),
        card=list(d.get("card_points") or []),
        stats=[(s.get("icon") or "star", str(s.get("value") or ""), s.get("label") or "") for s in d.get("stats") or []],
        overview=[p for p in (d.get("overview") or []) if p],
        highlights=[(h.get("title") or "", h.get("text") or "") for h in d.get("highlights") or []],
        stops=list(d.get("stops") or []),
        itinerary=[(it.get("title") or "", it.get("subtitle") or "", it.get("intro") or "",
                    [(a.get("time") or "", a.get("title") or "", a.get("text") or "") for a in it.get("activities") or []], bool(it.get("draft")))
                   for it in d.get("itinerary") or []],
        incl=list(d.get("inclusions") or []), excl=list(d.get("exclusions") or []),
        images=imgs,
        know=[(k.get("title") or "", k.get("text") or "") for k in d.get("good_to_know") or []],
        faq=[(q.get("question") or "", q.get("answer") or "") for q in d.get("faqs") or []],
    )
    if cat == "temple": t["zone"] = d.get("zone") or "south"
    if d.get("travel_styles"): t["styles"] = list(d["travel_styles"])
    if d.get("featured"): t["featured"] = True
    if d.get("badge"): t["badge"] = d["badge"]
    t["_order"] = d.get("order") if isinstance(d.get("order"), (int, float)) else 999
    return t

if not _os.environ.get("SANCHARI_NO_JSON") and _glob.glob(_os.path.join(_CDIR, "*.json")):
    _loaded = []
    for _f in sorted(_glob.glob(_os.path.join(_CDIR, "*.json"))):
        with open(_f, encoding="utf-8") as _fh:
            _d = _json.load(_fh)
        if _d.get("hidden"): continue
        _loaded.append(_tour_from_json(_d, _f))
    _loaded.sort(key=lambda t: (t["_order"], t["title"]))
    _temple = sorted([t for t in _loaded if t["cat"] == "temple"], key=lambda t: (_zorder.index(t["zone"]) if t["zone"] in _zorder else 9, t["_order"]))
    TOURS[:] = _temple + [t for t in _loaded if t["cat"] != "temple"]
