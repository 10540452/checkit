wrong_input = """Sorry, Wrong input number.
    Reply 0 for Menu"""

languages = ["English","Hindi","Chinese","French", "Japanese"]
languages_code = ["en","hi","zh","fr","ja"]
s_lang = "en"
lang_changed_text = "Language changed!"


data = [
    """Get information and guidance from WHO regarding the current outbreak of coronavirus disease (COVID-19).

    What would you like to know about coronavirus?
    1. LATEST 🔢  Numbers & cases
    2. PROTECT 👍 Protecting yourself
    3. FAQ❓Your questions answered
    4. MYTHS 📚 Know the facts!
    5. TRAVEL 🗺️ Travel advice
    6. NEWS 📰 News & Press
    7. Covid-19 ChatBot ℹ️
    8. LANGUAGE 🌐 Change language""",

    """Latest numbers 🔢

    Data as reported by national authorities by 
    4:04 PM CET August 4, 2020

    Total (new) cases in last 24 hours

    Pakistan
    278305 confirmed cases (0)
    5951 deaths (0)

    Global
    null confirmed cases (null)
    null deaths (null)

    Novel Coronavirus (COVID-19) Situation dashboard
    This interactive dashboard/map provides the latest 
    global numbers and numbers by country of COVID-19 
    cases on a daily basis.
    https://covid19.who.int/

    For country numbers, find the latest situation reports 
    here: https://www.who.int/emergencies/diseases/
    novel-coronavirus-2019/situation-reports

    📌 Reply 6 for News & Press
    📌 Reply 0 for Menu""",

    """Watch the video: https://youtu.be/8c_UJwLq8PI

    Protect yourself
    🧼 Wash your hands frequently
    👄 Avoid touching your eyes, mouth and nose
    💪 Cover your mouth and nose with your bent elbow 
        or tissue when you cough or sneeze
    🚷 Avoid crowded places
    🏠Stay at home if you feel unwell - even with a 
        slight fever and cough
    🤒 If you have a fever, cough and difficulty breathing, 
        seek medical care early - but call by phone first
    ℹ️ Stay aware of the latest information from WHO

    📌 Reply 0 for MENU""",
    """Reply with the number to get more information on 
    one of these topics:

    General questions on COVID-19
    10. About COVID-19
    11. Symptoms of COVID-19

    Can COVID-19 spread through:
    12. Touch, breathing, droplets
    13. Infected surfaces or packages

    
    14. What can I do?
    15. What if I visited a hotspot?
    16. Treatment options
    17. Should I wear a mask?
    18. What should I not do?
    19. Coping with stress and helping children cope
    20. For tobacco users
    21. Parenting tips
    22. Questions for food consumers
    23. TB and COVID-19
    24. Self care for SRHR
    25. Dexamethasone
    
    📌 Reply 0 for MENU""",

    """WHO Myth-busters
    Think you know the facts? Test you knowledge by replying with the word QUIZ

    There is a lot of false information around. 
    These are the facts.
    😷 The prolonged use of medical masks, when properly worn, 
    DOES NOT cause CO2 intoxication nor oxygen deficiency.
    🍷 Drinking alcohol DOES NOT protect you against COVID-19 and can be dangerous
    🤳 5G mobile networks DO NOT spread COVID-19.
    😳 Being able to hold your breath for 10 seconds or more 
        without coughing or feeling discomfort DOES NOT mean you
         are free from COVID-19 or any other lung disease.
    🧴 Drinking methanol, ethanol or bleach DOES NOT prevent or 
        cure COVID-19 and can be extremely dangerous.
    🐶 There is NO evidence that companion animals/pets such as 
        dogs or cats can transmit the coronavirus.
    💦 Spraying and introducing alcohol, chlorine, bleach or 
        another disinfectant into your body WILL NOT protect you
           against COVID-19 and can be harmful to clothes or 
        mucous membranes (i.e. eyes, mouth). Be aware that both 
        alcohol and chlorine can be useful to disinfect surfaces, 
        but they need to be used under appropriate recommendations.
    💉 Vaccines against pneumonia, such as pneumococcal vaccine and 
        Haemophilus influenzae type b (Hib) vaccine, DO NOT provide 
        protection against the coronavirus.
    💊 Antibiotics DO NOT work against viruses, antibiotics only work 
        against bacteria.
    🧪 To date, there is NO specific medicine recommended to prevent 
        or treat the coronavirus.
    🙂 You can recover from COVID-19. Catching COVID-19 DOES NOT mean 
        you will have it for life.

    ❓ Reply 3 for FAQ
    📌 Reply 0 for MENU""",

    """WHO continues to advise against the application of travel or 
    trade restrictions to countries experiencing COVID-19 outbreaks.
    It is prudent for travellers who are sick to delay or avoid travel
     to affected areas, in particular for elderly travellers and people
      with chronic diseases or underlying health conditions. 
      “Affected areas” are considered those countries, provinces, 
      territories or cities experiencing ongoing transmission of COVID-19,
       in contrast to areas reporting only imported cases.

    General recommendations for all travellers include:
    🧼 Wash your hands frequently
    👄 Avoid touching your eyes, mouth and nose
    💪 Cover your mouth and nose with your bent elbow or tissue when 
        you cough or sneeze
    ↔️ Stay more than 1 meter (3 feet) away from a person who is sick
    🍗 Follow proper food hygiene practices
    😷 Only wear a mask if you are ill with COVID-19 symptoms 
        (especially coughing) or looking after someone who may have COVID-19.

    Travellers returning from affected areas should:
    🌡 Self-monitor for symptoms for 14 days and follow national 
        protocols of receiving countries. Some countries may require 
            returning travellers to enter quarantine.
    🤒 If symptoms occur, such as fever, or cough or difficulty breathing, 
        travellers are advised to contact local health care providers, 
        preferably by phone, and inform them of their symptoms and their travel history.

    For the latest travel advice:
    https://www.who.int/emergencies/diseases/
    novel-coronavirus-2019/travel-advice

    For the latest situation reports for affected areas:
    https://www.who.int/emergencies/diseases/
    novel-coronavirus-2019/situation-reports/

    For advice on proper food hygiene practices:
    https://www.who.int/foodsafety/publications/
    consumer/en/5keys_en.pdf?ua=1&ua=1

    For advice on visiting live animal markets:
    https://www.who.int/health-topics/coronavirus/
    who-recommendations-to-reduce-risk-of-transmission-of
    -emerging-pathogens-from-animals-to-humans-in-live-animal-markets

    Reply 18 for whether to wear a mask
    🔢 Reply 1 for LATEST numbers
    📌 Reply 0 for MENU""",

    """LATEST NEWS & PRESS
    Member States adopt the Global Strategy for TB Research
     and Innovation at 73rd World Health Assembly
    10 Aug 2020 11:45:51 UTC
    Member States have adopted the global strategy for TB 
    research and innovation through an unprecedented  
    written silence procedure of the 73rd session of 
    the World Health Assembly (WHA) last week.
    Read more here: https://www.who.int/news-room/detail/
    10-08-2020-member-states-adopt-the-global-strategy-for-
    tb-research-and-innovation-at-73rd-world-health-assembly
    
    WHO at the virtual High-level Political Forum (HLPF) 2020
    10 Aug 2020 04:41:52 UTC
    The United Nations High-level Political Forum (HLPF), 
    a mechanism that tracks and advances the implementation 
    of the 2030 Agenda for Sustainable Development, was 
    convened virtually due to the COVID-19 pandemic, on 
    7–16 July 2020, on the theme "Accelerated 
    Read more here: https://www.who.int/news-room/detail/
    30-07-2020-who-at-the-virtual-high-level-
    political-forum-(hlpf)-2020
    
    Plane carrying WHO trauma and surgical supplies 
    arrives in Beirut, Lebanon
    07 Aug 2020 14:38:20 UTC
    A plane carrying 20 tonnes of WHO health supplies 
    has landed in Beirut, Lebanon, to support the treatment
     of patients injured by the massive blast that occurred
      in the city on 4 August.Read more here: 
      https://www.who.int/news-room/detail/05-08-2020-plane
      -carrying-who-trauma-and-surgical-supplies-arrives-in
      -beirut-lebanon
    
    WHO Information Notice for Users of Medical Devices 2020/3
    07 Aug 2020 12:03:51 UTC
    Date: 7 August 2020Subject: Substandard/Falsified medical 
    devices and personal protective equipment (PPE) used in the
     context of the COVID-19 pandemicWHO-identifier: 2020/3, 
     version 1 Type of action: Advice to users of medical 
     devices and PPE used for prevention, treatment and care
    for COVID-19.Read more here: https://www.who.int/news-
    room/detail/07-08-2020-who-information-notice-for-users
    -of-medical-devices-2020-3
    
    COVID-19 Emergency Committee highlights need for response
     efforts over long term  01 Aug 2020 14:47:25 UTC
    The Emergency Committee on COVID-19, convened by the WHO
     Director-General under the International Health Regulations
      (2005) (IHR), held its fourth meeting on 31 July.
    Read more here: https://www.who.int/news-room/detail/
    01-08-2020-covid-19-emergency-committee-highlights-
    need-for-response-efforts-over-long-term
    
    Situation reports: Situation reports provide the latest
     updates on the novel coronavirus outbreak. https://www.who.int/
     emergencies/diseases/novel-coronavirus-2019/situation-reports/
    
    Rolling Updates: Rolling updates on coronavirus 
    disease (COVID-19) sourced from across WHO media.
    https://www.who.int/emergencies/diseases/novel-
    coronavirus-2019/events-as-they-happen
    
    News articles: All news releases, statements and
     notes for the media.https://www.who.int/emergencies/
     diseases/novel-coronavirus-2019/media-resources/news
    
    Press briefings: Coronavirus disease (COVID-2019) 
    press briefings including videos, audio and transcripts.
    https://www.who.int/emergencies/diseases/novel-
    coronavirus-2019/media-resources/press-briefings
    
    📌 Reply 0 for MENU""",

    """ChatBot will be integrated Soon :)""",

    """Reply with your preferred language:
    English
    Hindi
    Chinese
    French
    Japanese""",

    """What are coronaviruses, COVID-19 and how are they related to SARS?

    What is a coronavirus?
    Coronaviruses are a large family of viruses which may cause
     illness in animals or humans.  In humans, several coronaviruses
      are known to cause respiratory infections ranging from the
      common cold to more severe diseases such as Middle East 
      Respiratory Syndrome (MERS) and Severe Acute Respiratory 
      Syndrome (SARS). The most recently discovered coronavirus 
      causes coronavirus disease COVID-19.

    What is COVID-19?
    COVID-19 is the infectious disease caused by the most
     recently discovered coronavirus. This new virus and 
     disease were unknown before the outbreak began in Wuhan,
      China, in December 2019. COVID-19 is now a pandemic 
      affecting many countries globally.

    Is COVID-19 the same as SARS?
    No. The virus that causes COVID-19 and the one that 
    caused the outbreak of Severe Acute Respiratory Syndrome 
    (SARS) in 2003 are related to each other genetically, but the diseases they cause are quite different. SARS was more deadly but much less infectious than COVID-19. There have been no outbreaks of SARS anywhere in the world since 2003.

    ❓ Reply 3 for Frequently Asked Questions (FAQ)
    📌 Reply 0 for MENU""",

    """*What are the symptoms of COVID-19?*

    The most common symptoms of COVID-19 are:
    🤒 fever
    😴 tiredness
    💨 dry cough

    Other symptoms that are less common and may affect some patients include aches and pains, nasal congestion, headache, conjunctivitis, sore throat, diarrhea, loss of taste or smell or a rash on skin or discoloration of fingers or toes.
    These symptoms are usually mild and begin gradually. Some people become infected but don’t develop any symptoms and don't feel unwell.
    Most people (about 80%) recover from the disease without needing special treatment. Around 1 out of every 6 people who gets COVID-19 becomes seriously ill and develops difficulty breathing.
    Older people, and those with underlying medical problems like high blood pressure, heart and lung problems, diabetes, or cancer are at higher risk of developing serious illness. However, anyone can catch COVID-19 and become seriously ill.
    People of all ages who experience fever and/or cough associated with difficulty breathing/shortness of breath, chest pain/pressure, or loss of speech or movement should seek medical attention immediately. If possible, it is recommended to call the health care provider or facility first, so the patient can be directed to the right clinic.

    ❓ Reply 3 for Frequently Asked Questions (FAQ)
    📌 Reply 0 for MENU""",

    """How does COVID-19 spread?
    🤧 People can catch COVID-19 from others who have the virus.
    💦 The disease can spread from person to person through small droplets from the nose or mouth which are spread when a person with COVID-19 coughs or exhales.
    🥄 These droplets land on objects and surfaces around the person.
    👈 Other people then catch COVID-19 by touching these objects or surfaces, then touching their eyes, nose or mouth.
    ↔️ People can also catch COVID-19 if they breathe in droplets from a person with COVID-19 who coughs out or exhales droplets. This is why it is important to stay more than 1 meter (3 feet) away from a person who is sick.
    WHO is assessing ongoing research on the ways COVID-19 is spread and will continue to share updated findings.

    Can the virus that causes COVID-19 be transmitted through the air?
    Studies to date suggest that the virus that causes COVID-19 is mainly transmitted through contact with respiratory droplets rather than through the air.

    Can COVID-19 be caught from a person who has no symptoms?
    The main way the disease spreads is through respiratory droplets expelled by someone who is coughing. The risk of catching COVID-19 from someone with no symptoms at all is very low. However, many people with COVID-19 experience only mild symptoms. This is particularly true at the early stages of the disease. It is therefore possible to catch COVID-19 from someone who has, for example, just a mild cough and does not feel ill.

    WHO is assessing ongoing research on the period of transmission of COVID-19 and will continue to share updated findings.

    ❓ Reply 3 for Frequently Asked Questions (FAQ)
    📌 Reply 0 for MENU""",

    """Can I catch COVID-19 from surfaces or packages?

    🥄 How long does the virus survive on surfaces?
    It is not certain how long the virus that causes COVID-19 survives on surfaces, but it seems to behave like other coronaviruses. Studies suggest that coronaviruses (including preliminary information on the COVID-19 virus) may persist on surfaces for a few hours or up to several days. This may vary under different conditions (e.g. type of surface, temperature or humidity of the environment).
    If you think a surface may be infected, clean it with simple disinfectant to kill the virus and protect yourself and others. Clean your hands with an alcohol-based hand rub or wash them with soap and water. Avoid touching your eyes, mouth, or nose.
    
    📦 Is it safe to receive a package from any area where COVID-19 has been reported?
    Yes. The likelihood of an infected person contaminating commercial goods is low and the risk of catching the virus that causes COVID-19 from a package that has been moved, travelled, and exposed to different conditions and temperature is also low.

    ❓ Reply 3 for Frequently Asked Questions (FAQ)
    📌 Reply 0 for MENU""",

    """What can I do to protect myself and prevent the spread of disease?

    Protection measures for everyone:
    
    ℹ️ Stay aware of the latest information on the COVID-19 outbreak, available on the WHO website and through your national and local public health authority. Many countries around the world have seen cases of COVID-19 and several have seen outbreaks. Authorities in China and some other countries have succeeded in slowing or stopping their outbreaks. However, the situation is unpredictable so check regularly for the latest news.
    You can reduce your chances of being infected or spreading COVID-19 by taking some simple precautions:
    
    🧼 Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water.
    Why? Washing your hands with soap and water or using alcohol-based hand rub kills viruses that may be on your hands.
    
    ↔️ Maintain at least 1 metre (3 feet) distance between yourself and anyone who is coughing or sneezing.
    Why?  When someone coughs or sneezes they spray small liquid droplets from their nose or mouth which may contain virus. If you are too close, you can breathe in the droplets, including the COVID-19 virus if the person coughing has the disease.
    
    🚫 Avoid touching eyes, nose and mouth
    Why? Hands touch many surfaces and can pick up viruses. Once contaminated, hands can transfer the virus to your eyes, nose or mouth. From there, the virus can enter your body and can make you sick.

    🤧 Make sure you, and the people around you, follow good respiratory hygiene. This means covering your mouth and nose with your bent elbow or tissue when you cough or sneeze. Then dispose of the used tissue immediately.
    Why? Droplets spread virus. By following good respiratory hygiene you protect the people around you from viruses such as cold, flu and COVID-19.

    🏠 Stay home if you feel unwell. If you have a fever, cough and difficulty breathing, seek medical attention and call in advance. Follow the directions of your local health authority.
    Why? National and local authorities will have the most up to date information on the situation in your area. Calling in advance will allow your health care provider to quickly direct you to the right health facility. This will also protect you and help prevent spread of viruses and other infections.

    🧳 Keep up to date on the latest COVID-19 hotspots (cities or local areas where COVID-19 is spreading widely). If possible, avoid traveling to places  – especially if you are an older person or have diabetes, heart or lung disease.
    Why? You have a higher chance of catching COVID-19 in one of these areas.

    ❓ Reply 3 for Frequently Asked Questions (FAQ)
    📌 Reply 0 for MENU""",

    """What should I do if I have visited an area where COVID-19 is spreading?

    If you have recently visited (past 14 days) areas where COVID-19 is spreading follow the guidance outlined in question 15. (What can I do to protect myself and prevent the spread of disease?) and do the following:

    🏠 Self-isolate by staying at home if you begin to feel unwell, even with mild symptoms such as headache, low grade fever (37.3°C or above) and slight runny nose, until you recover.
    If it is essential for you to have someone bring you supplies or to go out, e.g. to buy food, then wear a mask to avoid infecting other people.

    Why?
    Avoiding contact with others and visits to medical facilities will allow these facilities to operate more effectively and help protect you and others from possible COVID-19 and other viruses.
    🤒 If you develop fever, cough and difficulty breathing, seek medical advice promptly as this may be due to a respiratory infection or other serious condition. Call in advance and tell your provider of any recent travel or contact with travelers.

    Why?
    Calling in advance will allow your health care provider to quickly direct you to the right health facility. This will also help to prevent possible spread of COVID-19 and other viruses.

    Reply 15 for how to protect yourself
    ❓ Reply 3 for Frequently Asked Questions (FAQ)
    📌 Reply 0 for MENU""",

    """What are the treatment options for COVID-19 (including drugs, vaccines, therapies)?

    💊 Are antibiotics effective in preventing or treating COVID-19?
    No. Antibiotics do not work against viruses, they only work on bacterial infections. COVID-19 is caused by a virus, so antibiotics do not work. Antibiotics should not be used as a means of prevention or treatment of COVID-19. They should only be used as directed by a physician to treat a bacterial infection.

    🧪 Are there any medicines or therapies that can prevent or cure COVID-19?
    While some western, traditional or home remedies may provide comfort and alleviate symptoms of mild COVID-19, there are no medicines that have been shown to prevent or cure the disease. WHO does not recommend self-medication with any medicines, including antibiotics, as a prevention or cure for COVID-19.

    💉 Is there a vaccine, drug or treatment for COVID-19?
    Not yet. To date, there is no vaccine and no specific antiviral medicine to prevent or treat COVID-2019. However, those affected should receive care to relieve symptoms. People with serious illness should be hospitalized. Most patients recover thanks to supportive care.
    Possible vaccines and some specific drug treatments are under investigation. They are being tested through clinical trials. WHO is coordinating efforts to develop vaccines and medicines to prevent and treat COVID-19.
    The most effective ways to protect yourself and others against COVID-19 are to frequently clean your hands, cover your cough with the bend of elbow or tissue, and maintain a distance of at least 1 meter (3 feet) from people who are coughing or sneezing.

    Reply 15 for how to protect yourself
    ❓ Reply 3 for Frequently Asked Questions (FAQ)
    📌 Reply 0 for MENU""",

    """Should I wear a mask to protect myself?
    It's important to stay informed and follow the advice given by your national and local public health authorities and your healthcare provider.

    Who should wear a fabric mask?
    If there is widespread community transmission, and especially in settings where a distance of 1-metre cannot be maintained, governments should encourage the general public to wear a fabric mask.

    How to wear a fabric mask:
    www.youtube.com/watch?time_continue=63&v=ciUniZGD4tY&feature=emb_logo

    Q&A on COVID-19 and masks:
    www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/q-a-on-covid-19-and-masks

    Who should wear a medical mask?
    - Health workers
    - Anyone with COVID-19 symptoms
    - People caring for those with COVID-19 symptoms

    At-risk people in areas of widespread transmission where a distance of 1-metre cannot be guaranteed including:
    - People aged 60 or over
    - People with underlying health conditions

    How to wear a medical mask:
    www.youtube.com/watch?v=adB8RW4I3o4&feature=emb_logo

    Q&A on COVID-19 and masks:
    www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/q-a-on-covid-19-and-masks

    ❓ Reply 3 for Frequently Asked Questions (FAQ)
    📌 Reply 0 for the main MENU""",

    """Is there anything I should not do?

    The following measures ARE NOT effective against COVID-19 and can be harmful:

    🚭Smoking
    😷Wearing multiple masks
    💊Taking antibiotics

    In any case, if you have fever, cough and difficulty breathing seek medical care early to reduce the risk of developing a more severe infection and be sure to share your recent travel history with your health care provider.

    Reply 17 for treatment options
    ❓ Reply 3 for Frequently Asked Questions (FAQ)
    📌 Reply 0 for MENU""",

    """Coping with stress during COVID-19

    📞 It is normal to feel sad, stressed, confused, scared or angry during a crisis. Talking to people you trust can help. Contact your friends and family.
    🥦  If you must stay at home, maintain a healthy lifestyle - including proper diet, sleep, exercise and social contacts with loved ones at home and by email and phone with other family and friends.
    🚭 Don’t use smoking, alcohol or other drugs to deal with your emotions. If you feel overwhelmed, talk to a health worker or counsellor. Have a plan, where to go to and how to seek help for physical and mental health needs if required.
    ℹ️ Get the facts. Gather information that will help you accurately determine your risk so that you can take reasonable precautions. Find a credible source you can trust such as WHO website or, a local or state public health agency.
    😭 Limit worry and agitation by lessening the time you and your family spend watching or listening to media coverage that you perceive as upsetting.
    ⭐️ Draw on skills you have used in the past that have helped you to manage previous life’s adversities and use those skills to help you manage your emotions during the challenging time of this outbreak.
    Helping children cope with stress during COVID-19
    🧒 Children may respond to stress in different ways such as being more clingy, anxious, withdrawing, angry or agitated, bedwetting etc. Respond to your child’s reactions in a supportive way, listen to their concerns and give them extra love and attention.
    💖 Children need adults’ love and attention during difficult times. Give them extra time and attention. Remember to listen to your children, speak kindly and reassure them. If possible, make opportunities for the child to play and relax.
    👪 Try and keep children close to their parents and family and avoid separating children and their caregivers to the extent possible. If separation occurs (e.g. hospitalization) ensure regular contact (e.g. via phone) and re-assurance.
    🪁 Keep to regular routines and schedules as much as possible, or help create new ones in a new environment, including school/learning as well as time for safely playing and relaxing.
    ℹ️ Provide facts about what has happened, explain what is going on now and give them clear information about how to reduce their risk of being infected by the disease in words that they can understand depending on their age. This also includes providing information about what could happen in a re-assuring way (e.g. a family member and/or the child may start not feeling well and may have to go to the hospital for some time so doctors can help them feel better).

    ❓ Reply 3 for your questions (FAQ)
    📌 Reply 0 for MENU""",

    """Quit smoking to lower your risk of COVID-19

    COVID-19 is an infectious disease that primarily attacks the lungs. Smoking impairs lung function, making it harder for the body to fight off coronaviruses and other diseases. Smoking can increase your chances of getting COVID-19 because bringing your hands to your mouth can transfer the virus into your body.
    Quit today to reduce these risks and start living a healthier life.

    Quick tips to curb your cravings:
    🚭 Delay: Delay as long as you can before giving in to your urge.
    🧘🏽‍♀ Deep breathing: Take 10 deep breaths to relax from within until the urge passes.
    💦 Drink water: Drinking water is a healthy alternative to sticking a cigarette in your mouth.
    🎶Do something else to distract yourself: Take a shower, read, go for a walk, listen to music!

    Reply 12 for how COVID-19 spreads
    ❓ Reply 3 for Frequently Asked Questions (FAQ)
    📌 Reply 0 for MENU""",

    """What are some parenting tips in the time of COVID-19?
    👨‍👦 Home with the kids? Try taking 20 minutes a day doing something that they choose – play a game or read with them. Quality time will make them feel safe and loved.
    💕Praise is powerful. Try praising your child or teenager for something they have done well.  They may not show their appreciation, but you’ll see them doing that good thing again.
    🗓Routine up! A structured day helps kids feel secure and makes it easier to manage them. Try making a timetable, with schoolwork, games, free time, exercise, and handwashing.
    🧘🏿‍♂Kids at home driving you crazy? Feeling like you are going to scream? Give yourself a 1-minute pause. Breathe in and out five times. Then respond.
    💆🏻‍♂Crowded house? Stressed out? Share your feelings. Take a break. Looking after kids 24-7 during COVID-19 isn’t easy. Remind yourself of what you did well today. Think about the good moments.
    Take care of yourself so you can take care of your children.

    Reply 20 for coping with stress during COVID-19
    ❓ Reply 3 for Frequently Asked Questions (FAQ)
    📌 Reply 0 for MENU""",

    """Questions relating to food consumers

    Can I get COVID-19 from food?
    There is currently no evidence that people can catch COVID-19 from food or food packaging. COVID-19 is a respiratory illness and the transmission route is through person-to-person contact and through direct contact with respiratory droplets generated when an infected person coughs or sneezes.

    Can the virus live on the surface of foods (including fruits and vegetables, frozen foods, pre-packaged foods)?
    Coronaviruses cannot multiply in food – they need a live animal or human host to multiply and survive .

    How to wash fruits and vegetables? Just with water, or something else?
    Washing fruit and vegetables with potable water is sufficient: it is recommended to follow the WHO 5-Keys to Safer Food (bit.ly/2Nn4NuB).

    Can the virus live on the surface of food packaging? How long? Is it necessary to disinfect?
    It is not necessary to disinfect food packaging materials, but hands should be properly washed after handling food packages and before eating.

    How long is it to cook food? To what temperature to kill the virus?
    This virus is not more resistant to heat than the usual viruses and bacteria found in food. As recommended for good hygiene practice, foods should be thoroughly cooked to at least 70°C.

    What precautions should consumers take in grocery stores?
    Consumers should maintain a safe physical distance of at least one metre from all other shoppers and staff while queuing before entering the store and while shopping in the store. If a trolley or basket is used while shopping, sanitize the handle before and after use. Hands should be sanitized before entering the store. Practice good coughing/sneezing etiquette while in the store. Avoid touching mouth, nose or eyes during shopping. Minimise direct hand contact with food by using available tongs and serving utensils. Use contactless payment rather than cash/notes (where feasible).

    Is food/grocery delivery safe?
    Yes, if the provider follows good personal and food hygiene practices. After accepting food/grocery deliveries, hands should be washed with soap and water.

    What is the best household disinfectant for surfaces?
    Regular household cleaning and disinfection products will effectively eliminate the virus from household surfaces.  For cleaning and disinfecting households with suspected or confirmed COVID19 illnesses - surface virucidal disinfectants, such as 0.05% sodium hypochlorite (NaClO) and products based on ethanol (at least 70%), should be used.

    Is it still safe to go to food markets? Animal markets? Wet markets?
    It should be safe provided it is possible to maintain a safe physical distance of at least one metre from all other shoppers and staff, it is possible to wash/sanitize hands, and that Good Manufacturing Practices and Good Hygienic Practices (GMP/GHP) standards are maintained in the market. For more recommendations on how to minimise the risk of transmission of emerging pathogens in wet markets, see the WHO recommendations to reduce risk of transmission of emerging pathogens from animals to humans in live animal markets or animal product markets (bit.ly/2Bycs6M).

    -----
    ❓ Reply 3 for Frequently Asked Questions (FAQ)
    📌 Reply 0 for MENU""",

    """Tuberculosis and COVID-19

    WHO is continuously monitoring and responding to tuberculosis (TB) prevention and care during the COVID-19 pandemic. Health services need to be actively engaged for an effective and rapid response to COVID-19 while ensuring that TB and other essential health services are maintained.

    Are people with tuberculosis likely to be at increased risk of COVID-19 infection, illness and death?
    While experience on COVID-19 infection in tuberculosis (TB) patients remains limited, it is anticipated that people ill with both TB and COVID-19 may have poorer treatment outcomes, especially if TB treatment is interrupted.
    Older age, diabetes and chronic obstructive pulmonary disease (COPD) are linked with more severe COVID-19 and are also risk factors for poor outcomes in TB.
    TB patients should take precautions as advised by health authorities to be protected from COVID-19 and continue their TB treatment as prescribed.
    People ill with COVID-19 and TB show similar symptoms such as cough, fever and difficulty breathing. Both diseases attack primarily the lungs and although both biological agents transmit mainly via close contact, the incubation period from exposure to disease in TB is longer, often with a slow onset.

    For more information on COVID-19 and TB visit bit.ly/2CsQsdL

    -----
    ❓ Reply 3 for Frequently Asked Questions (FAQ)
    📌 Reply 0 for MENU""",

    """Self-care interventions for sexual and reproductive health and rights (SRHR) and COVID-19

    WHO’s definition of self care is the ability of individuals, families and communities to promote health, prevent disease, maintain health, and to cope with illness and disability with or without the support of a health worker.

    What are self-care interventions?
    Self-care interventions recommended by WHO are evidence-based and can include information about a sexual or reproductive health issue as well as ways in which individuals can obtain drugs, devices, diagnostics and/or digital products fully or partially separate from formal health services that can be used with or without the direct supervision of a health worker. For example, self-injectable contraception, HPV self-sampling kits or HIV self-tests.

    Why are self-care interventions important during a pandemic like COVID-19?
    With the major disruptions to the normal functioning of national health systems caused by the need to respond to people who have or are affected by the virus, evidence-based, high-quality self-care interventions can provide an important alternative to the usual health facility- or health worker-based services. Self-care is a valuable part of a well-functioning health system and can be particularly useful when physical distancing measures make it more difficult for people to access their normal health care services and medications.

    What self care actions can I take to protect my sexual and reproductive health?
    In 2019, WHO issued a new guideline that brought together 32 existing or new recommendations on a range of sexual and reproductive health self-care interventions. The guideline has recommendations on pregnancy and newborn care, contraception, abortion, sexually transmitted infections including HIV and HPV, and for sexual health more broadly.

    For more questions about Self-Care visit bit.ly/2BtnRom""",

    """What is dexamethasone and does it work against COVID-19?

    Dexamethasone is a corticosteroid used in a wide range of conditions for its anti-inflammatory and immunosuppressant effects.
    It was tested in hospitalized patients with COVID-19 in the United Kingdom’s national clinical trial RECOVERY and was found to have benefits for critically ill patients.
    According to preliminary findings shared with WHO (and now available as a preprint), for patients on ventilators, the treatment was shown to reduce mortality by about one third, and for patients requiring only oxygen, mortality was cut by about one fifth.
    For more information visit www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/q-a-dexamethasone-and-covid-19"""
]