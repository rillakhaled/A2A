from faker import Faker
from faker.providers import BaseProvider
import pandas as pd
import random
from io import StringIO
import json

amount = 100
# create faker object and set locality to India (English)
faker = Faker('en_IN')

# create pandas DataFrame to store faker profiles
df = pd.DataFrame()

# sets the initial profile data provided by faker
for i in range(amount):
    df = df.append(faker.profile(), ignore_index = True)

# delete unnecessary columns
del df['blood_group']
del df['ssn']
del df['sex']
del df['job']
# adding custom columns
# use this same format for adding as many columns as desired

# create a list of possible entry values to new column (ex: religion)

languages = ['Telugu', 'Malayalam', 'Kannada', 'Hindi', 'Marathi', 'Bengali', 'Gujarati', 'Angika', 'Arunachali', 'Assamese', 'Awadhi', 'Bhojpuri', 'Brij', 'Bihari', 'Badaga', 'Chatisgarhi', 'Dogri', 'English', 'French', 'Garhwali', 'Garo', 'Haryanvi', 'Himachali/Pahari', 'Kanauji', 'Kashmiri', 'Khandesi', 'Khasi', 'Konkani', 'Koshali', 'Kumaoni', 'Kutchi', 'Lepcha', 'Ladacki', 'Magahi', 'Maithili', 'Manipuri', 'Marwari', 'Miji', 'Mizo', 'Monpa', 'Nicobarese', 'Nepali', 'Oriya', 'Punjabi', 'Rajasthani', 'Sanskrit', 'Santhali', 'Sindhi', 'Sourashtra', 'Tripuri', 'Tulu', 'Urdu']
community = ['Aka', 'Arabic', 'Arunachali', 'Assamese', 'Awadhi', 'Baluchi', 'Bengali', 'Bhojpuri', 'Bhutia', 'Brahui', 'Brij', 'Burmese', 'Chhattisgarhi', 'Chinese', 'Coorgi', 'Dogri', 'English', 'French', 'Garhwali', 'Garo', 'Gujarati', 'Haryanavi', 'Himachali/Pahari', 'Hindi', 'Hindko', 'Kakbarak', 'Kanauji', 'Kannada', 'Kashmiri', 'Khandesi', 'Khasi', 'Konkani', 'Koshali', 'Kumaoni', 'Kutchi', 'Ladakhi', 'Lepcha', 'Magahi', 'Maithili', 'Malay', 'Malayalam', 'Manipuri', 'Marathi', 'Marwari', 'Miji', 'Mizo', 'Monpa', 'Nepali', 'Odia', 'Pashto', 'Persian', 'Punjabi', 'Rajasthani', 'Russian', 'Sanskrit', 'Santhali', 'Seraiki', 'Sindhi', 'Sinhala', 'Sourashtra', 'Spanish', 'Swedish', 'Tagalog', 'Tamil', 'Telugu', 'Tulu', 'Urdu', 'Other']
marital_status = ['Never married', 'widowed', 'divorced', 'awaiting divorce', 'Annulled']
annual_income = ['Under $25,000', '$25,001 - $40,000', '$40,001 - $60,000', '$60,001 - $80,000', '$80,001 - $100,000', '$100,001 - $150,000', '$150,001 - $200,000', '$200,001 and Above']
eye_color = ['Brown', 'Blue', 'Hazel', 'Amber', 'Gray', 'Green']
hair_color = ['Black', 'Brown', 'Blonde', 'Gray', 'colorful']
gender = ['Male' , 'Female' , 'Non-binary' , 'Trans' , 'Prefer not to say']
body_type = ['Rather not say', 'Slim', 'Athletic', 'Average', 'Fit', 'Jacked', 'A little extra', 'Curvy', 'Overweight']
dietary_habits = ['Veg', 'Non-veg', 'Occasionally non-veg', 'Eggetarian', 'Jain', 'Vegan']
sports = ['tennis', 'Table tennis', 'Badminton', 'Soccer', 'Hockey', 'Handball', 'Volleyball', 'Basketball', 'Swimming Sailing', 'Rowing', 'Surfing', 'Cycling', 'Horseback riding', 'Skiing', 'Jogging', 'Hiking', 'Rock climbing', 'Bowling', 'Yoga/Pilates', 'Fitness']
passions = ['Yoga', 'Language exchange', 'DIY', 'Coffee', 'Karaoke', 'Reading', 'Foodie', 'Cat Lover', 'Comedy', 'Gamer', 'Shopping', 'Cycling', 'Hiking', 'Dog Lover', 'Disney', 'Working out']

#education
education = { 'engineering/design' : ['B.E/B.Tech', 'B.Pharma', 'M.E/M.Tech', 'M.Pharma', 'M.S. (Engineering)', 'B.Arch', 'M.Arch', 'B.Des', 'M.Des']
            , 'computers': ['MCA/PGDCA', 'BCA', 'B.IT']
            , 'finance/commerce': ['B.Com' , 'CA' , 'CS' , 'ICWA' , 'M.Com' , 'CFA']
            , 'management': ['MBA/PGDM', 'BBA', 'BHM']
            , 'medicine': ['MBBS', 'M.D.', 'BAMS', 'BHMS', 'BDS', 'M.S. (Medicine)', 'MVSc.', 'BVSc.', 'MDS', 'BPT', 'MPT', 'DM', 'MCh']
            , 'law': ['BL/LLB', 'ML/LLM']
            , 'arts/science': ['B.A', 'B.Sc', 'M.A', 'M.Sc', 'B.Ed', 'M.Ed', 'MSW', 'BFA', 'MFA', 'BJMC', 'MJMC']
            , 'doctorate': ['Ph. D', 'M.Phil']
            , 'non-Graduate': ['Diploma', 'High School', 'Trade School', 'Other']
            }

#employment
employed_in = {
                'private sector' : ['Actor/Model', 'Advertising Professional', 'Film/ Entertainment Professional', 'Media Professional', 'Agriculture Professional',  'Farming', 'Architect', 'Chartered Accountant', 'Education Professional', 'Educational Institution Owner', 'Animator', 'Developer', 'Product Designer', 'Fashion Designer', 'Interior Designer', 'Hotels/ Hospitality Professional', 'Lawyer & Legal Professional', 'Paramedic', 'Pharmacist', 'Physiotherapist', 'Psychologist', 'Veterinary Doctor', 'Dentist', 'Doctor', 'Surgeon',  'Artist', 'Beautician', 'Broker', 'Business Owner/ Entrepreneur', 'Fitness Professional',  'Singer',  'Sportsperson', 'Travel Professional', 'Writer', 'Others'],
                'government/public sector' : [ 'Media Professional', 'Agriculture Professional',  'Architect', 'Chartered Accountant', 'Education Professional',  'Librarian', 'Professor/Lecturer', 'Research Assistant',  'Research Professional', 'Science Professional', 'Scientist', 'Teacher', 'Hotels/ Hospitality Professional', 'Lawyer & Legal Professional', 'Medical/ Healthcare Professional', 'Nurse', 'Paramedic', 'Pharmacist', 'Physiotherapist', 'Psychologist', 'Veterinary Doctor', 'Dentist', 'Doctor', 'Surgeon',  'Social Services/NGO/ Volunteer',  'Sportsperson', 'Others'],
                'defense' : [ 'Education Professional', 'Librarian', 'Professor/Lecturer', 'Lawyer & Legal Professional', 'Medical/ Healthcare Professional', 'Nurse', 'Paramedic', 'Pharmacist', 'Physiotherapist', 'Psychologist', 'Veterinary Doctor', 'Dentist', 'Doctor', 'Surgeon', 'Others'],
                'Civil Services' : [ 'Chartered Accountant', 'Education Professional', 'Educational Institution Owner', 'Librarian', 'Professor/Lecturer', 'Research Assistant',  'Research Professional','Teacher', 'Lawyer & Legal Professional', 'Medical/ Healthcare Professional', 'Nurse', 'Paramedic', 'Pharmacist', 'Physiotherapist', 'Psychologist', 'Dentist', 'Doctor', 'Surgeon', 'Social Services/NGO/ Volunteer', 'Writer', 'Others'],
                'business/ Self Employed' : ['Actor/Model', 'Corporate Management Professional', 'Animator', 'Developer', 'Product Designer', 'Fashion Designer', 'Interior Designer', 'Hotels/ Hospitality Professional', 'C*O /Chairman/ President/ Director', 'VP/ AVP/ GM/ DGM',  'Artist', 'Beautician', 'Broker', 'Business Owner/ Entrepreneur', 'Fitness Professional',  'Singer', 'Sportsperson', 'Travel Professional', 'Writer', 'Others'],
                'not Working' : ['not working']
}

#religion/caste

religion_caste = { "muslim/others" : ["Ansari","Arain","Awan","Bohra","Dekkani","Dudekula","Hanafi","Jat","Khoja","Lebbai","Malik","Mapila","Maraicar","Memon","Mughal","Others","Pathan","Qureshi","Rajput","Rowther","Shafi","Sheikh","Siddiqui","Syed","UnSpecified","Don't wish to specify"],
                    "hindu" : ["Ad Dharmi","Adi Andhra","Adi Dravida","Agarwal","Agnikula Kshatriya","Agri","Ahir Shimpi","Ahom","Ambalavasi","Arekatica","Arora","Arunthathiyar","Arya Vysya","Ayyaraka","Bagdi","Baidya","Baishnab","Baishya","Bajantri","Balija","Banayat ORIYA","Banik","Baniya","Baniya - Bania","Baniya - Kumuti","Banjara","Barai","Bari","Baria","Barujibi","Besta","Bhandari","Bhatia","Bhatraju","Bhavasar Kshatriya","Bhoi","Bhovi","Bhoyar","Billava","Bishnoi\/Vishnoi","Bondili","Boyar","Brahmbatt","Brahmin - Anavil","Brahmin - Audichya","Brahmin - Barendra","Brahmin - Bhatt","Brahmin - Bhumihar","Brahmin - Daivadnya","Brahmin - Danua","Brahmin - Deshastha","Brahmin - Dhiman","Brahmin - Dravida","Brahmin - GARHWALI","Brahmin - Gaur","Brahmin - Goswami\/Gosavi","Brahmin - Gujar Gaur","Brahmin - Gurukkal","Brahmin - Halua","Brahmin - Havyaka","Brahmin - Hoysala","Brahmin - Iyengar","Brahmin - Iyer","Brahmin - Jangid","Brahmin - Jhadua","Brahmin - Jyotish","Brahmin - Kanyakubj","Brahmin - Karhade","Brahmin - Khandelwal","Brahmin - Kokanastha","Brahmin - Kota","Brahmin - Kulin","Brahmin - Kumaoni","Brahmin - Madhwa","Brahmin ? Maithil","Brahmin - Modh","Brahmin - Mohyal","Brahmin - Nagar","Brahmin - Namboodiri","Brahmin - Narmadiya ","Brahmin - Niyogi","Brahmin - Others","Brahmin - Paliwal","Brahmin - Panda","Brahmin - Pandit","Brahmin - Pareek","Brahmin - Pushkarna","Brahmin - Rarhi","Brahmin - Rigvedi","Brahmin - Rudraj","Brahmin - Sakaldwipi","Brahmin - Sanadya","Brahmin - Sanketi","Brahmin - Saraswat","Brahmin - Saryuparin","Brahmin - Shivhalli","Brahmin - Shrimali","Brahmin - Sikhwal","Brahmin - Smartha","Brahmin - Sri Vaishnava","Brahmin - Stanika","Brahmin - Tyagi","Brahmin - Vaidiki","Brahmin - Vaikhanasa","Brahmin - Velanadu","Brahmin - Vyas","Brajastha Maithil","Bunt (Shetty)","Chalawadi and Holeya","Chambhar","Chandravanshi Kahar","Chasa","Chattada Sri Vaishnava ","Chaudary","Chaurasia","Chennadasar","Chettiar","Chhetri","Chippolu (Mera)","CKP","Coorgi","Devadiga","Devandra Kula Vellalar","Devang Koshthi","Devanga","Devar\/Thevar\/Mukkulathor","Devrukhe Brahmin","Dhangar","Dheevara","Dhiman","Dhoba","Dhobi","Dhor \/ Kakkayya","Dommala","Dumal","Dusadh (Paswan)","Ediga","Ezhava","Ezhuthachan","Gabit","Ganda","Gandla","Ganiga","Garhwali","Gatti","Gavara","Gawali","Ghisadi","Ghumar","Goala","Goan","Gomantak","Gondhali","Goud","Gounder","Gowda","Gramani","Gudia","Gujjar","Gupta","Guptan","Gurav","Gurjar","Halba Koshti","Helava","Hugar (Jeer)","Intercaste","Irani","Jaalari","Jaiswal","Jandra","Jangam","Jangra - Brahmin","Jat","Jatav","Jetty\/Malla","Jijhotia Brahmin","Jogi (Nath)","Kachara","Kadava Patel","Kahar","Kaibarta","Kalal","Kalanji","Kalar","Kalinga","Kalinga Vysya","Kalita","Kalwar","Kamboj","Kamma","Kansari","Kapu","Karana","Karmakar","Karuneegar","Kasar","Kashyap","Katiya","Kavuthiyya\/Ezhavathy","Kayastha","Khandayat","Khandelwal","Kharwa","Kharwar","Khatri","Kirar","Kokanastha Maratha","Koli","Koli Mahadev","Koli Patel","Kongu Vellala Gounder","Korama","Kori","Kosthi","Krishnavaka","Kshatriya","Kudumbi","Kulal","Kulalar","Kulita","Kumawat","Kumbhakar","Kumbhar","Kumhar","Kummari","Kunbi","Kuravan","Kurmi\/Kurmi Kshatriya","Kuruba","Kuruhina Shetty","Kurumbar","Kushwaha (Koiri)","Lambadi","Leva patel","Leva patil","Lingayath","Lodhi Rajput","Lohana","Lohar","Loniya","Lubana","Madiga","Mahajan","Mahar","Mahendra","Maheshwari","Mahishya","Majabi","Mala","Mali","Mallah","Malviya Brahmin","Mangalorean","Mapila","Maratha","Maruthuvar","Matang","Mathur","Maurya \/ Shakya","Meena","Meenavar","Mehra","Meru Darji","Mochi","Modak","Mogaveera","Mudaliyar","Mudiraj","Munnuru Kapu","Muthuraja","Naagavamsam","Nadar","Nagaralu","Nai","Naicker","Naidu","Naik","Nair","Namasudra \/ Namassej","Nambiar","Napit","Nayaka","Neeli","Nhavi","Oswal","Otari","Padmasali","Pal","Panchal","Pandaram","Panicker","Parkava Kulam","Parsi","Partraj","Pasi","Patel","Pathare Prabhu","Patnaick\/Sistakaranam","Patra","Perika","Pillai","Poosala","Porwal","Prajapati","Raigar","Rajaka","Rajastani","Rajbhar","Rajbonshi","Rajpurohit","Rajput","Ramanandi","Ramdasia","Ramgariah","Ramoshi","Ravidasia","Rawat","Reddy","Relli","Ror","Sadgope","Sagara (Uppara)","Saha","Sahu","Saini","Saliya","Sathwara","Savji","SC","Senai Thalaivar","Senguntha Mudaliyar","Settibalija","Shimpi\/Namdev","Sindhi-Amil","Sindhi-Baibhand","Sindhi-Bhanusali","Sindhi-Bhatia","Sindhi-Chhapru","Sindhi-Dadu","Sindhi-Hyderabadi","Sindhi-Larai","Sindhi-Larkana","Sindhi-Lohana","Sindhi-Rohiri","Sindhi-Sahiti","Sindhi-Sakkhar","Sindhi-Sehwani","Sindhi-Shikarpuri","Sindhi-Thatai","SKP","Sonar","Soni","Sozhiya Vellalar","Srisayana","ST","ENGLISH","Sunari","Sundhi","Surya Balija","Suthar","Swakula Sali","Tamboli","Tanti","Tantubai","Telaga","Teli","Thakkar","Thakore","Thakur","Thigala","Thiyya","Tili","Togata","Tonk Kshatriya","Turupu Kapu","Urali Gounder","Urs","Vada Balija","Vaddera","Vaish","Vaishnav","Vaishnava","Vaishya","Vaishya Vani","Valluvan","Valmiki","Vania","Vanika Vyshya","Vaniya","Vanjara","Vanjari","Vankar","Vannar","Vannia Kula Kshatriyar","Variar","Varshney","Veera Saivam","Velaan","Velama","Vellalar","Veluthedathu Nair","Vettuva Gounder","Vilakkithala Nair","Vishwakarma","Viswabrahmin","Vokkaliga","Vysya","Yadav","Yellapu","Brahmin - Embrandiri","Others","Don't wish to specify","Badaga","Adi kannada"],
                    "muslim - shia" : ["Ansari","Arain","Awan","Bohra","Dekkani","Dudekula","Hanafi","Jat","Khoja","Lebbai","Malik","Mapila","Maraicar","Memon","Mughal","Others","Pathan","Qureshi","Rajput","Rowther","Shafi","Sheikh","Siddiqui","Syed","UnSpecified","Don't wish to specify"],
                    'musilm - sunni' : ["Ansari","Arain","Awan","Bohra","Dekkani","Dudekula","Hanafi","Jat","Khoja","Lebbai","Malik","Mapila","Maraicar","Memon","Mughal","Others","Pathan","Qureshi","Rajput","Rowther","Shafi","Sheikh","Siddiqui","Syed","UnSpecified","Don't wish to specify"],
                    'christian - catholic' : ["UnSpecified","Born Again","Bretheren","Church of South India","Evangelist","Jacobite","Knanaya","Knanaya Catholic","Knanaya Jacobite","Latin Catholic","Malankara","Marthoma","Others","Pentecost","Roman Catholic","Seventh-day Adventist","Syrian Catholic","Syrian Jacobite","Syrian Orthodox","Syro Malabar","Don't wish to specify"],
                    'christian - orthodox' : ["UnSpecified","Born Again","Bretheren","Church of South India","Evangelist","Jacobite","Knanaya","Knanaya Catholic","Knanaya Jacobite","Latin Catholic","Malankara","Marthoma","Others","Pentecost","Roman Catholic","Seventh-day Adventist","Syrian Catholic","Syrian Jacobite","Syrian Orthodox","Syro Malabar","Don't wish to specify"],
                    'christian - protestant' : ["UnSpecified","Born Again","Bretheren","Church of South India","Evangelist","Jacobite","Knanaya","Knanaya Catholic","Knanaya Jacobite","Latin Catholic","Malankara","Marthoma","Others","Pentecost","Roman Catholic","Seventh-day Adventist","Syrian Catholic","Syrian Jacobite","Syrian Orthodox","Syro Malabar","Don't wish to specify"],
                    'christian - others' : ["UnSpecified","Born Again","Bretheren","Church of South India","Evangelist","Jacobite","Knanaya","Knanaya Catholic","Knanaya Jacobite","Latin Catholic","Malankara","Marthoma","Others","Pentecost","Roman Catholic","Seventh-day Adventist","Syrian Catholic","Syrian Jacobite","Syrian Orthodox","Syro Malabar","Don't wish to specify"],
                    'sikh' : ["UnSpecified","Ahluwalia","Arora","Bhatia","Bhatra","Ghumar","Intercaste","Jat","Kamboj","Khatri","Kshatriya","Lubana","Majabi","Nai","Others","Rajput","Ramdasia","Ramgharia","Ravidasia","Saini","Tonk Kshatriya","Don't wish to specify"],
                    'jain - digambar' : ["UnSpecified","Agarwal","Bania","Intercaste","Jaiswal","KVO","Khandelwal","Kutchi","Oswal","Others","Porwal","Vaishya","Don't wish to specify"],
                    'jain - shwetambar' : ["UnSpecified","Agarwal","Bania","Intercaste","Jaiswal","KVO","Khandelwal","Kutchi","Oswal","Others","Porwal","Vaishya","Don't wish to specify"],
                    'jain - others' : ["UnSpecified","Agarwal","Bania","Intercaste","Jaiswal","KVO","Khandelwal","Kutchi","Oswal","Others","Porwal","Vaishya","Don't wish to specify"],
                    'parsi' : ["Others","Intercaste","Irani","Parsi","Don't wish to specify"],
                    'buddhist' : ["others" , "Do not wish to specify"],
                    'jewish' : ["others" , "Do not wish to specify"],
                    'inter - religion' : ["Ad Dharmi","Adi Andhra","Adi Dravida","Agarwal","Agnikula Kshatriya","Agri","Ahir Shimpi","Ahom","Ambalavasi","Arekatica","Arora","Arunthathiyar","Arya Vysya","Ayyaraka","Bagdi","Baidya","Baishnab","Baishya","Bajantri","Balija","Banayat ORIYA","Banik","Baniya","Baniya - Bania","Baniya - Kumuti","Banjara","Barai","Bari","Baria","Barujibi","Besta","Bhandari","Bhatia","Bhatraju","Bhavasar Kshatriya","Bhoi","Bhovi","Bhoyar","Billava","Bishnoi\/Vishnoi","Bondili","Boyar","Brahmbatt","Brahmin - Anavil","Brahmin - Audichya","Brahmin - Barendra","Brahmin - Bhatt","Brahmin - Bhumihar","Brahmin - Daivadnya","Brahmin - Danua","Brahmin - Deshastha","Brahmin - Dhiman","Brahmin - Dravida","Brahmin - GARHWALI","Brahmin - Gaur","Brahmin - Goswami\/Gosavi","Brahmin - Gujar Gaur","Brahmin - Gurukkal","Brahmin - Halua","Brahmin - Havyaka","Brahmin - Hoysala","Brahmin - Iyengar","Brahmin - Iyer","Brahmin - Jangid","Brahmin - Jhadua","Brahmin - Jyotish","Brahmin - Kanyakubj","Brahmin - Karhade","Brahmin - Khandelwal","Brahmin - Kokanastha","Brahmin - Kota","Brahmin - Kulin","Brahmin - Kumaoni","Brahmin - Madhwa","Brahmin ? Maithil","Brahmin - Modh","Brahmin - Mohyal","Brahmin - Nagar","Brahmin - Namboodiri","Brahmin - Narmadiya","Brahmin - Narmadiya ","Brahmin - Niyogi","Brahmin - Others","Brahmin - Paliwal","Brahmin - Panda","Brahmin - Pandit","Brahmin - Pareek","Brahmin - Pushkarna","Brahmin - Rarhi","Brahmin - Rigvedi","Brahmin - Rudraj","Brahmin - Sakaldwipi","Brahmin - Sanadya","Brahmin - Sanketi","Brahmin - Saraswat","Brahmin - Saryuparin","Brahmin - Shivhalli","Brahmin - Shrimali","Brahmin - Sikhwal","Brahmin - Smartha","Brahmin - Sri Vaishnava","Brahmin - Stanika","Brahmin - Tyagi","Brahmin - Vaidiki","Brahmin - Vaikhanasa","Brahmin - Velanadu","Brahmin - Vyas","Brajastha Maithil","Bunt (Shetty)","Chalawadi and Holeya","Chambhar","Chandravanshi Kahar","Chasa","Chattada Sri Vaishnava","Chattada Sri Vaishnava ","Chaudary","Chaurasia","Chennadasar","Chettiar","Chhetri","Chippolu (Mera)","CKP","Coorgi","Devadiga","Devandra Kula Vellalar","Devang Koshthi","Devanga","Devar\/Thevar\/Mukkulathor","Devrukhe Brahmin","Dhangar","Dheevara","Dhiman","Dhoba","Dhobi","Dhor \/ Kakkayya","Dommala","Dumal","Dusadh (Paswan)","Ediga","Ezhava","Ezhuthachan","Gabit","Ganda","Gandla","Ganiga","Garhwali","Gatti","Gavara","Gawali","Ghisadi","Ghumar","Goala","Goan","Gomantak","Gondhali","Goud","Gounder","Gowda","Gramani","Gudia","Gujjar","Gupta","Guptan","Gurav","Gurjar","Halba Koshti","Helava","Hugar (Jeer)","Intercaste","Irani","Jaalari","Jaiswal","Jandra","Jangam","Jangra - Brahmin","Jat","Jatav","Jetty\/Malla","Jijhotia Brahmin","Jogi (Nath)","Kachara","Kadava Patel","Kahar","Kaibarta","Kalal","Kalanji","Kalar","Kalinga","Kalinga Vysya","Kalita","Kalwar","Kamboj","Kamma","Kansari","Kapu","Karana","Karmakar","Karuneegar","Kasar","Kashyap","Katiya","Kavuthiyya\/Ezhavathy","Kayastha","Khandayat","Khandelwal","Kharwa","Kharwar","Khatri","Kirar","Kokanastha Maratha","Koli","Koli Mahadev","Koli Patel","Kongu Vellala Gounder","Korama","Kori","Kosthi","Krishnavaka","Kshatriya","Kudumbi","Kulal","Kulalar","Kulita","Kumawat","Kumbhakar","Kumbhar","Kumhar","Kummari","Kunbi","Kuravan","Kurmi\/Kurmi Kshatriya","Kuruba","Kuruhina Shetty","Kurumbar","Kushwaha (Koiri)","Lambadi","Leva patel","Leva patil","Lingayath","Lodhi Rajput","Lohana","Lohar","Loniya","Lubana","Madiga","Mahajan","Mahar","Mahendra","Maheshwari","Mahishya","Majabi","Mala","Mali","Mallah","Malviya Brahmin","Mangalorean","Mapila","Maratha","Maruthuvar","Matang","Mathur","Maurya \/ Shakya","Meena","Meenavar","Mehra","Meru Darji","Mochi","Modak","Mogaveera","Mudaliyar","Mudiraj","Munnuru Kapu","Muthuraja","Naagavamsam","Nadar","Nagaralu","Nai","Naicker","Naidu","Naik","Nair","Namasudra \/ Namassej","Nambiar","Napit","Nayaka","Neeli","Nhavi","Oswal","Otari","Padmasali","Pal","Panchal","Pandaram","Panicker","Parkava Kulam","Parsi","Partraj","Pasi","Patel","Pathare Prabhu","Patnaick\/Sistakaranam","Patra","Perika","Pillai","Poosala","Porwal","Prajapati","Raigar","Rajaka","Rajastani","Rajbhar","Rajbonshi","Rajpurohit","Rajput","Ramanandi","Ramdasia","Ramgariah","Ramoshi","Ravidasia","Rawat","Reddy","Relli","Ror","Sadgope","Sagara (Uppara)","Saha","Sahu","Saini","Saliya","Sathwara","Savji","SC","Senai Thalaivar","Senguntha Mudaliyar","Settibalija","Shimpi\/Namdev","Sindhi-Amil","Sindhi-Baibhand","Sindhi-Bhanusali","Sindhi-Bhatia","Sindhi-Chhapru","Sindhi-Dadu","Sindhi-Hyderabadi","Sindhi-Larai","Sindhi-Larkana","Sindhi-Lohana","Sindhi-Rohiri","Sindhi-Sahiti","Sindhi-Sakkhar","Sindhi-Sehwani","Sindhi-Shikarpuri","Sindhi-Thatai","SKP","Sonar","Soni","Sozhiya Vellalar","Srisayana","ST","ENGLISH","Sunari","Sundhi","Surya Balija","Suthar","Swakula Sali","Tamboli","Tanti","Tantubai","Telaga","Teli","Thakkar","Thakore","Thakur","Thigala","Thiyya","Tili","Togata","Tonk Kshatriya","Turupu Kapu","Urali Gounder","Urs","Vada Balija","Vaddera","Vaish","Vaishnav","Vaishnava","Vaishya","Vaishya Vani","Valluvan","Valmiki","Vania","Vanika Vyshya","Vaniya","Vanjara","Vanjari","Vankar","Vannar","Vannia Kula Kshatriyar","Variar","Varshney","Veera Saivam","Velaan","Velama","Vellalar","Veluthedathu Nair","Vettuva Gounder","Vilakkithala Nair","Vishwakarma","Viswabrahmin","Vokkaliga","Vysya","Yadav","Yellapu","Brahmin - Embrandiri","Ansari","Arain","Awan","Bohra","Dekkani","Dudekula","Hanafi","Jat","Khoja","Lebbai","Malik","Mapila","Maraicar","Memon","Mughal","Others","Pathan","Qureshi","Rajput","Rowther","Shafi","Sheikh","Siddiqui","Syed","UnSpecified","Born Again","Bretheren","Church of South India","Evangelist","Jacobite","Knanaya","Knanaya Catholic","Knanaya Jacobite","Latin Catholic","Malankara","Marthoma","Others","Pentecost","Roman Catholic","Seventh-day Adventist","Syrian Catholic","Syrian Jacobite","Syrian Orthodox","Syro Malabar","Ahluwalia","Arora","Bhatia","Bhatra","Ghumar","Jat","Kamboj","Khatri","Kshatriya","Lubana","Majabi","Nai","Others","Rajput","Ramdasia","Ramgharia","Ravidasia","Saini","Tonk Kshatriya","Agarwal","Bania","Jaiswal","KVO","Khandelwal","Kutchi","Oswal","Others","Porwal","Vaishya","Irani","Parsi","Don't wish to specify","Badaga","Adi kannada"],
                    'no religious belief' : ["others" , "Do not wish to specify"]
}

#kundali
kundali = { 'Ashwini': ['Mesham', 'Mesha (Aries)'],
            'Bharani': ['Mesham', 'Mesha(Aries)'],
            'Krittika': ['Mesham', 'Mesha(Aries)', 'Rishabam / Vrushaba(Taurus)'],
            'Rohini': ['Rishabam', 'Vrushaba(Taurus)'],
            'Mrigasira': ['Rishabam', 'Vrushaba (Taurus)', 'Mithunam', 'Midhunam (Gemini)'],
            'Ardra': ['Mithunam', 'Midhunam (Gemini)'],
            'Punarvasu': ['Mithunam', 'Midhunam(Gemini)', 'Katagam', 'Karkataka(Cancer)'],
            'Pusya Aslesa': ['Katagam', 'Karkataka (Cancer)'],
            'Magha': ['Simmham', 'Simha (Leo)'],
            'Purva Phalguni': ['Simmham', 'Simha (Leo)'],
            'Uttara Phalguni': ['Simmham', 'Simha (Leo)', 'Kanni', 'Kanya (Virgo)'],
            'Hasta': ['Kanni', 'Kanya (Virgo)'],
            'Chitha': ['Kanni', 'Kanya (Virgo)', 'Thulam', 'Thula (Libra)'],
            'Swati': ['Thulam', 'Thula (Libra)'],
            'Vishakha': ['Thulam', 'Thula (Libra)', 'Viruchigam', 'Vruchika (Scorpio)'],
            'Anuradha': ['Viruchigam', 'Vruchika (Scorpio)'],
            'Jyestha': ['Viruchigam', 'Vruchika (Scorpio)'],
            'Mula': ['Dhanusu', 'Dhanu (Sagittarius)'],
            'Purva Ashadha': ['Dhanusu',' Dhanu (Sagittarius)'],
            'Uttara Ashadha': ['Dhanusu', 'Dhanu (Sagittarius)', 'Makaram', 'Makara (Capricon)'],
            'Shravana': ['Makaram', 'Makara (Capricon)'],
            'Dhanistha': ['Makaram', 'Makara(Capricon)', 'Kumbham', 'Kumbha(Aquarius)'],
            'Shatabhishak': ['Kumbham', 'Kumbha (Aquarius)'],
            'Purva Bhadrapada': ['Kumbham', 'Kumbha(Aquarius)', 'Meenam', 'Meena(Pisces)'],
            'Uttara Bhadrapada': ['Meenam', 'Meena (Pisces)'],
            'Revathi': ['Meenam', 'Meena (Pisces)']

}

#e-Harmony
living_interests = ['Large city', ' Suburb ', 'Small quiet town', 'Rural area', 'Doesn’t matter', 'I love travelling!']
purpose_of_relationship = ['Life is easier with a partner', 'Emotional security', 'Having a partner I can trust','Frequent intimacy', 'Not being alone', 'Security']
ideal_partner = ['looks good with me', 'share my interests', 'Be adorable to me']
partner_criteria = ['Career', 'Financial security', 'Health and fitness', 'Warm-heartedness', 'Appearance']
relationship_criteria = ['Giving each other a lot of space', 'Considering each other in what you want', 'Not examining everything in depth', 'Making life easier and peaceful for one another', 'Accepting our imperfections', 'Always trying new things', 'Sticking to a routine']
going_to_wedding_crisis = ['Are we going to look good together?', 'Have we brought the right gift?','Will there be too many people I don\'t know?', 'I notice that I really don\'t like dressing up']
being_single_reasons = ['high expectations of my future partner', 'wasn’t ready before now', 'too shy to meet people', 'haven’t had the time to date', 'Just don’t socialize much']
book_sharing = ['Yes, I’d like to share my interests with my partner' , 'It doesn’t matter to me']
sleeping_arrangements = ['Share one bedroom', 'Each of us would have our own bedroom', 'but we could spend the night together in either room']
love_sickness_reaction = ['no longer enjoy my food','eat more', 'neither']
cheating = ['Cheating is never ok!', 'It\'s important to try to be faithful', 'Being true to your heart is much more important than physical fidelity', 'Flings occasionally happen in relationships', 'To demand absolute fidelity is possessive thinking']
ideal_wedding = [ 'Ceremony or event, at church or venue!', 'Courthouse would suffice' , 'Whatever my partner decides', 'Haven’t thought about it!']
family_and_friends_opinion_about_you = [ 'Always up for anything fun', 'Always optimistic', 'Thinks a lot - and seriously - about life' , 'Always happy and in a good mood', 'Is a bit of a daydreamer', 'Deals with problems in an objective and thoughtful manner', 'Always finds a good solution for herself, even in unpleasant situations', 'Calm and level-headed', 'Actively participates in everything']
what_your_partner_likes_about_you = ['Cheerful', 'Humorous', 'Uncomplicated', 'Natural', 'Honest', 'Serious', 'Adaptable', 'Empathetic', 'Affectionate', 'Spirited', 'Reserved', 'Frugal', 'Domestic', 'Nature-loving', 'Optimistic', 'Sporty', 'Capable', 'reliable', 'Fond of children', 'Self-disciplined', 'attractive', 'warm-hearted', 'educated', 'ethical', 'well-mannered', 'thoughtful', 'independent', 'tolerant', 'spontaneous', 'self-assured', 'imaginative', 'career-driven', 'calm', 'understanding']
your_values_family_frriends = ['My family\'s approval of my choice of partner', 'My friends being pleased about my choice of partner', 'I don’t care about others opinions', 'My partner\'s family liking me']
alcohol = ['Yes, at mealtimes or to relax' , 'Socially' , 'Never']
smoke = [ 'Yes', 'Socially' , 'No']
hobbies = ['Reading', 'Watching television', 'Relaxing', 'Going out', 'Watching movies', 'Playing board games', 'Surfing the internet', 'Volunteering', 'Hanging out with friends', 'Spending time with my family', 'Going to the theater / cinema', 'ballet  or opera', 'Listening to music', 'Sports', 'Dancing', 'Photography', 'Film/Video', 'Art', 'Playing instruments', 'Cooking', 'Crafts', 'Pottery', 'Carpentry/DIY', 'Collecting', 'None']
free_times = ['At my house or visiting friends', 'Outside in nature', 'Socializing']
cooking = ['I\'m always cooking and trying new recipes', 'I like to cook occasionally', 'I only cook if I have to', 'I only cook on special occasions', 'I only eat out']
workout_routine = ['Daily', 'A few times a week', 'Several times a month', 'Not very often']
favorite_musical_genre = ['Musicals', 'Opera', 'Orchestral Music', 'Chamber Music', 'Folk Music', 'Easy listening', 'Spiritual', 'World music', 'Jazz, Rock', 'Metal/Hard Rock', 'Reggae, Rap', 'Dance', 'House', 'Blues', 'Hip Hop', 'Pop']
play_instruments = ['Yes', 'No']
favorite_vacations = ['Beach vacation', 'Sports', 'Activity holiday', 'educational tour', 'Meditation', 'Cruises', 'Resorts', 'Staycations', 'City trips', 'Vacations for pure relaxation', 'In the mountains Camping', 'Adventure vacation', 'Hiking', 'Spa vacation', 'Group travel']
vacation_planning = ['As little as possible', 'I prefer to pack and go', 'Plan far in advance and schedule everything', 'I arrange the destination and dates but I leave the rest to the moment']
planning_strategy = ['Very systematic', 'let things work themselves out', 'I have to be in the right mood to plan things']
enjoy_long_walks = ['Yes', 'No']
temperature = ['Comfortably warm (72 degrees)', 'A bit cooler (Maximum of 68 degrees)']
home_or_gathering = ['Home', 'Large gathering']
windows_open = ['Always', 'Whenever possible', 'Never', 'I don\'t mind if the window is open or closed']
morning_or_night = ['Morning person', 'ight owl', 'It depends on the day']
easily_excited = ['Not really', 'Yes, often']
favorite_part_of_song = ['Lyrics', 'Rhythm', 'Melody']
favorite_instrument = ['Saxophone', 'Violin', 'Piano']
clothing_color = ['Restrained and muted', 'Bold and extravagant']
clothing_style = ['Casually', 'Sporty', 'Practically', 'Elegantly', 'Fashionably', 'Appropriate to the occasion', 'Uniquely and unconventionally']
alone_time_tv_music = ['Yes', 'No']
people_use_cellphone = ['Not really', 'I''ve gotten used to it', 'It does bother me, but it\'s so common', 'I just have to deal with it', 'I can\'t stand it!', 'I use the time to check my phone too']
immediate_reaction = ['I let them know right away that they upset me', 'I try to remain calm and find out what happened', 'I think: Why does this always happen to me?', 'I smile and pretend nothing\'s wrong']
being_hurt_reaction = ['I tell myself they didn\'t mean it', 'I know I’ll find a way to deal with it', 'I hold a grudge for a while', 'I want to retaliate right away']
reaction_in_contradiction = ['I get annoyed about their know-it-all attitude', 'but don\'t say anything', 'It doesn\'t matter', 'being right isn\'t important to me', 'I try to argue my point', 'I have to find a way to convince them that I\'m right']
sustainability_beliefs = ['With all of our advanced technology we really should come up with something that can help', 'We must learn how to take better care of the planet', 'I\'d prefer to ignore what\'s happening it\'s too horrible']
appearance_satisfaction = ['Yes, On the whole', 'Yes, It depends', 'I\'m sometimes unhappy about it']
people_being_inherently_good = ['Absolutely I want to', 'Sometimes it\'s hard to believe', 'It just depends on the situation']
sexuality_importance = ['Very important', 'Important', 'Not particularly important', 'Not important']
marriage_as_institution = ['If two people really love each other they should get married', 'Anyone wanting to start a family should get married', 'Marriage as an institution is completely unnecessary']
organization_importance = ['Yes, definitely', 'Not really', 'The right place can mean something different for every single person']
expensive_restaurants = ['I highly value good cuisine', 'Does not matter to me', 'I\'d rather eat at casual places food isn\'t worth that much', 'All that\'s important to me is eating healthy']
regular_meal_times = ['Eat regularly and at set times', 'No, I eat whenever I’m hungry']
sexy_ads = ['Sometimes tasteless', 'I think it\'s kind of fun', 'I\'m not impressed']
what_bothers_you_when_you_date = ['When their dad is really overbearing', 'When their mom is overprotective of them', 'If their old friends have too much influence over their behavior', 'If they are frequently in a bad mood', 'My partner\'s friends that are weird/unstable']
values = ['True friendship', 'Love', 'Peace and happiness', 'A successful career', 'Respect from everyone I know', 'Stable social setting', 'Personal development and growth', 'A comfortable home with the person I love']
mantra = ['Work hard' , 'Play hard Love your neighbor as you love yourself', 'Live and let live']

#height
for i in range(amount):
    df.at[i, 'height'] = random.randrange(140,200)


# loop to assign a random entry to each row of the original df
def newColumn (column,columnName):
    for i in range(amount):
     # do this for each new column to add
         df.at[i, columnName ] = random.choice(column)

def newColumnByDictionary(parent_dict,columnName):
    keys = list(parent_dict.keys())
    for i in range(amount):
        select_key = random.choice(keys)
        select_value = random.choice(parent_dict[select_key])
        df.at[i, columnName ] = select_key + '-' + select_value



newColumn(languages, 'languages')
newColumn(community, 'community')
newColumn(marital_status, 'marital status')
newColumn(annual_income, 'annual income')
newColumn(eye_color, 'eye color')
newColumn(hair_color, 'hair color')
newColumn(gender, 'gender')
newColumn(body_type, 'body type')
newColumn(dietary_habits, 'dietaty habits')
newColumn(sports, 'sports')
newColumn(passions, 'passions')
newColumnByDictionary(education, 'education')
newColumnByDictionary(employed_in, 'employment')
newColumnByDictionary(religion_caste,'religion/caste')
newColumnByDictionary(kundali, 'kundali: Star - Raasi')


for i in range(amount):
    numbers_of_possible_answers = random.randrange(0,6)
    random_answers = random.sample(what_your_partner_likes_about_you,numbers_of_possible_answers)
    json_str_random_answers = json.dumps(random_answers)
    #json_list_random_answers = json.loads(json_str_random_answers)
    df.at[i, 'what your partner likes about you?'] = json_str_random_answers

# reorders the columns alphabetically
# note: case-senstive (if column name is capitalized, it will be placed before all columns that start with lower-case)
df = df.reindex(sorted(df.columns), axis=1)

#e-Harmony
newColumn(living_interests, 'living ineterests')
newColumn(purpose_of_relationship, 'purpose of relationship')
newColumn(ideal_partner, 'ideal partner')
newColumn(partner_criteria, 'partner criteria')
newColumn(relationship_criteria, 'relationship criteria')
newColumn(going_to_wedding_crisis, 'When going to a friend\'s wedding. As you get ready for the party, which thoughts are you most likely to be thinking?')
newColumn(being_single_reasons, 'Why do you think you\'re single?')
newColumn(book_sharing, 'If you find a book or article particularly interesting, do you want your partner to read it as well? ')
newColumn(sleeping_arrangements, 'Suppose you lived in a two-bedroom apartment with your partner, what would the sleeping arrangement be?')
newColumn(love_sickness_reaction, 'How do you react to lovesickness?')
newColumn(cheating, 'What do you think about cheating in a relationship? ')
newColumn(ideal_wedding, 'Which statement best represents your ideal wedding? ')
newColumn(family_and_friends_opinion_about_you, 'Which of the following do your friends and family think about you? ')
newColumn(your_values_family_frriends, 'Imagine your family and friends: Which of the following reactions about your choice of partner would you value the most?')
newColumn(alcohol, 'Do you drink alcohol?')
newColumn(smoke, 'Do you smoke?')
newColumn(hobbies, 'What do you like to do in your free time?')
newColumn(free_times, 'Where do you like to spend your free time? ')
newColumn(cooking, 'How much do you like to cook?')
newColumn(workout_routine, 'How often do you work out/play sports?')
newColumn(favorite_musical_genre, 'What type of music do you like to listen to?')
newColumn(play_instruments, 'Do you play an instrument?')
newColumn(favorite_part_of_song, 'If you like a song, what is the usual reason?')
newColumn(favorite_instrument, 'Which instrument sound do you like the most? ')
newColumn(favorite_vacations, 'What kinds of vacations do you like to take?')
newColumn(vacation_planning, 'How do you plan your vacations?')
newColumn(planning_strategy, 'What\'s your approach to planning things?')
newColumn(enjoy_long_walks, 'Do you enjoy taking long walks?')
newColumn(temperature, 'What is the ideal temperature for your house?')
newColumn(home_or_gathering, 'Do you feel more at ease at home than when you\'re out in a large gathering?')
newColumn(windows_open, 'Do you sleep with the window open?')
newColumn(morning_or_night, 'Are you a morning person or a night person?')
newColumn(easily_excited, 'Are you easily excited about things? ')
newColumn(clothing_color, 'Regardless of current trends, is the style and color of your clothing mostly..')
newColumn(clothing_style, 'How do you prefer to dress?')
newColumn(alone_time_tv_music, 'Do you normally turn on music or the television when you\'re home alone?')
newColumn(people_use_cellphone, 'Does it bother you when people use their cell phone around you?')
newColumn(immediate_reaction, 'What is your immediate reaction if a person you\'re close to does something that upsets you? ')
newColumn(being_hurt_reaction, 'Sometimes people hurt you. How do you react? ')
newColumn(reaction_in_contradiction, 'If someone contradicts you when you know that you are right, how do you usually react?')
newColumn(sustainability_beliefs, 'What do you think about climate change, conservation, renewable energy, etc?')
newColumn(appearance_satisfaction, 'Do you like your physical appearance? ')
newColumn(people_being_inherently_good, 'Do you believe that people are inherently good?')
newColumn(sexuality_importance, 'How important is sexuality to you?')
newColumn(marriage_as_institution, 'What do you think about marriage as an institution?')
newColumn(organization_importance, 'Is it important that your belongings are always organized properly?')
newColumn(expensive_restaurants, 'What do you think about going out to expensive restaurants?')
newColumn(regular_meal_times, 'Are regular mealtimes important to you?')
newColumn(sexy_ads, 'Does sex sell? What do you think of ads that use sex to promote their products?')
newColumn(what_bothers_you_when_you_date, 'When you first start dating someone, what bothers you the most about those who are close to them?')
newColumn(values, 'What values are the most important to you?')
newColumn(mantra, 'What mantra do you live your life by?')


# export the df to csv file
df.to_csv('user-profiles-test.csv')