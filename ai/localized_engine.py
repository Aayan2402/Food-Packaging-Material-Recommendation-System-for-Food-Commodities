"""
PackSense AI - Multilingual Information Engine
Provides fluent, specialized explanations, advice, packaging names and food translations
across all 21 supported global and regional languages.
"""

# Food Name Translations across all 21 languages
FOOD_TRANSLATIONS = {
    "Strawberry": {
        "en": "Strawberry", "hi": "स्ट्रॉबेरी", "mr": "स्ट्रॉबेरी", "gu": "સ્ટ્રોબેરી", "bn": "স্ট্রবেরি",
        "te": "స్ట్రాబెర్రీ", "ta": "ஸ்ட்ராபெர்ரி", "es": "Fresa", "fr": "Fraise", "de": "Erdbeere",
        "zh": "草莓", "ar": "فراولة", "pt": "Morango", "ru": "Клубника", "ja": "イチゴ",
        "it": "Fragola", "tr": "Çilek", "ko": "딸기", "nl": "Aardbei", "vi": "Dâu tây", "id": "Stroberi"
    },
    "Tomato": {
        "en": "Tomato", "hi": "टमाटर", "mr": "टोमॅटो", "gu": "ટામેટા", "bn": "টমেটো",
        "te": "టమోటా", "ta": "தக்காளி", "es": "Tomate", "fr": "Tomate", "de": "Tomate",
        "zh": "番茄", "ar": "طماطم", "pt": "Tomate", "ru": "Помидор", "ja": "トマト",
        "it": "Pomodoro", "tr": "Domates", "ko": "토마토", "nl": "Tomaat", "vi": "Cà chua", "id": "Tomat"
    },
    "Mango": {
        "en": "Mango", "hi": "आम", "mr": "आंबा", "gu": "કેરી", "bn": "আম",
        "te": "మామిడి", "ta": "மாம்பழம்", "es": "Mango", "fr": "Mangue", "de": "Mango",
        "zh": "芒果", "ar": "مانجو", "pt": "Manga", "ru": "Манго", "ja": "マンゴー",
        "it": "Mango", "tr": "Mango", "ko": "망고", "nl": "Mango", "vi": "Xoài", "id": "Mangga"
    },
    "Apple": {
        "en": "Apple", "hi": "सेब", "mr": "सफरचंद", "gu": "સફરજન", "bn": "আপেল",
        "te": "యాపిల్", "ta": "ஆப்பிள்", "es": "Manzana", "fr": "Pomme", "de": "Apfel",
        "zh": "苹果", "ar": "تفاح", "pt": "Maçã", "ru": "Яблоко", "ja": "リンゴ",
        "it": "Mela", "tr": "Elma", "ko": "사과", "nl": "Appel", "vi": "Táo", "id": "Apel"
    },
    "Potato": {
        "en": "Potato", "hi": "आलू", "mr": "बटाटा", "gu": "બટાકા", "bn": "আলু",
        "te": "బంగాళాదుంప", "ta": "உருளைக்கிழங்கு", "es": "Patata", "fr": "Pomme de terre", "de": "Kartoffel",
        "zh": "马铃薯", "ar": "بطاطس", "pt": "Batata", "ru": "Картофель", "ja": "ジャガイモ",
        "it": "Patata", "tr": "Patates", "ko": "감자", "nl": "Aardappel", "vi": "Khoai tây", "id": "Kentang"
    },
    "Paneer": {
        "en": "Paneer", "hi": "पनीर", "mr": "पनीर", "gu": "પનીર", "bn": "পনির",
        "te": "పనీర్", "ta": "பனீர்", "es": "Paneer (Queso fresco)", "fr": "Paneer (Fromage frais)", "de": "Paneer (Frischkäse)",
        "zh": "印度奶酪 (Paneer)", "ar": "بانير (جبن هندي)", "pt": "Paneer (Queijo fresco)", "ru": "Панир (Свежий сыр)", "ja": "パニール (生チーズ)",
        "it": "Paneer (Formaggio fresco)", "tr": "Paneer (Taze Peynir)", "ko": "파니르 (코티지 치즈)", "nl": "Paneer (Verse kaas)", "vi": "Phô mai Paneer", "id": "Paneer (Keju segar)"
    },
    "Meat": {
        "en": "Meat", "hi": "मांस", "mr": "मांस / चिकन", "gu": "માંસ", "bn": "মাংস",
        "te": "మాంసం", "ta": "இறைச்சி", "es": "Carne fresca", "fr": "Viande fraîche", "de": "Frischfleisch",
        "zh": "鲜肉", "ar": "لحم طازج", "pt": "Carne fresca", "ru": "Свежее мясо", "ja": "生肉",
        "it": "Carne fresca", "tr": "Taze Et", "ko": "신선육", "nl": "Vers vlees", "vi": "Thịt tươi", "id": "Daging Segar"
    },
    "Potato Chips": {
        "en": "Potato Chips", "hi": "आलू के चिप्स", "mr": "बटाटा वेफर्स / चिप्स", "gu": "બટાકાની ચિપ્સ", "bn": "আলু চিপস",
        "te": "బంగాళాదుంప చిప్స్", "ta": "உருளைக்கிழங்கு சிப்ஸ்", "es": "Patatas fritas", "fr": "Chips de pomme de terre", "de": "Kartoffelchips",
        "zh": "薯片", "ar": "رقائق البطاطس", "pt": "Batatas fritas", "ru": "Картофельные чипсы", "ja": "ポテトチップス",
        "it": "Patatine fritte", "tr": "Patates Cipsi", "ko": "감자 칩", "nl": "Aardappelchips", "vi": "Khoai tây chiên", "id": "Keripik Kentang"
    },
    "Namkeen": {
        "en": "Namkeen / Fried Snacks", "hi": "नमकीन / स्नैक्स", "mr": "नमकीन / फरसाण", "gu": "નમકીન / ફરસાણ", "bn": "নমকিন / স্ন্যাক্স",
        "te": "మిక్చర్ / చిరుతిళ్ళు", "ta": "கார வகைகள் / சிற்றுண்டி", "es": "Aperitivos fritos", "fr": "Snacks salés", "de": "Knabbergebäck / Snacks",
        "zh": "咸味小吃", "ar": "المقبلات والوجبات الخفيفة", "pt": "Salgadinhos fritos", "ru": "Соленые закуски", "ja": "スナック菓子",
        "it": "Snack salati", "tr": "Tuzlu Atıştırmalıklar", "ko": "스낵 / 튀김 간식", "nl": "Zoute snacks", "vi": "Đồ ăn vặt mặn", "id": "Makanan Ringan Gurih"
    },
    "Other Produce": {
        "en": "Other Fresh Produce", "hi": "अन्य ताजी उपज", "mr": "इतर ताजी शेतमाल उपज", "gu": "અન્ય તાજા શાકભાજી / ફળો", "bn": "অন্যান্য তাজা ফল ও সবজি",
        "te": "ఇతర తాజా పంటలు", "ta": "பிற புதிய விளைபொருட்கள்", "es": "Otros productos frescos", "fr": "Autres produits frais", "de": "Weitere Frischwaren",
        "zh": "其他新鲜农产品", "ar": "منتجات زراعية طازجة أخرى", "pt": "Outros produtos frescos", "ru": "Другие свежие продукты", "ja": "その他の生鮮食品",
        "it": "Altri prodotti freschi", "tr": "Diğer Taze Ürünler", "ko": "기타 신선 농산물", "nl": "Overige verse producten", "vi": "Nông sản tươi khác", "id": "Hasil Bumi Segar Lainnya"
    }
}

def get_food_display_name(food_name, lang="en"):
    """Returns localized display string for a food, e.g. 'स्ट्रॉबेरी (Strawberry)' in non-English."""
    food_clean = food_name.strip() if food_name else "Strawberry"
    trans_map = FOOD_TRANSLATIONS.get(food_clean)
    if not trans_map:
        for k, v in FOOD_TRANSLATIONS.items():
            if k.lower() in food_clean.lower():
                trans_map = v
                break
    if not trans_map:
        return food_clean
    localized = trans_map.get(lang, trans_map.get("en", food_clean))
    if lang != "en" and localized != food_clean:
        return f"{localized} ({food_clean})"
    return localized

# Multilingual Why This Packaging Explanations
WHY_PACKAGING_EXPLANATIONS = {
    "strawberry": {
        "farmer": {
            "en": "Recommended because fresh strawberries have very high natural respiration and lose water rapidly. This breathable punnet allows excess moisture to escape without sweating or condensation, stopping gray mold (Botrytis) from rotting the berries across your {transit_days}-day trip to {destination}.",
            "mr": "शिफारस करण्याचे कारण म्हणजे ताज्या स्ट्रॉबेरीमध्ये नैसर्गिक श्वसन दर खूप जास्त असतो आणि पाणी वेगाने कमी होते. हे हवा खेळती ठेवणारे पनेट पाण्याचा थेंब न साचू देता अतिरिक्त ओलावा बाहेर पडू देते, ज्यामुळे {destination} पर्यंतच्या {transit_days} दिवसांच्या प्रवासात करपा किंवा बुरशी (Botrytis) लागण्यापासून संरक्षण होते.",
            "hi": "सिफारिश इसलिए की गई है क्योंकि ताजी स्ट्रॉबेरी की प्राकृतिक श्वसन दर बहुत अधिक होती है और नमी तेजी से कम होती है। यह सांस लेने योग्य पनेट नमी और पसीने को बाहर निकलने देता है, जिससे {destination} तक की {transit_days} दिनों की यात्रा में स्ट्रॉबेरी को फफूंद (Botrytis) से सड़ने से बचाया जा सकता है।",
            "gu": "ભલામણ કરવામાં આવે છે કારણ કે તાજી સ્ટ્રોબેરીમાં કુદરતી શ્વસન દર ખૂબ વધારે હોય છે અને ભેજ ઝડપથી ગુમાવે છે. આ હવા-પ્રવાહવાળું પનેટ ભેજ જમા થયા વિના વધારાની વરાળ બહાર કાઢે છે, જેથી {destination} સુધીની {transit_days} દિવસની મુસાફરીમાં ફળ સડવાથી બચી જાય છે.",
            "bn": "সুপারিশ করা হয়েছে কারণ তাজা স্ট্রবেরি খুব দ্রুত শ্বাসপ্রশ্বাস গ্রহণ করে এবং জলীয় বাষ্প দ্রুত ত্যাগ করে। এই বায়ুচলাচলযুক্ত প্যানেট আর্দ্রতা জমে থাকা প্রতিরোধ করে, যাতে {destination} অভিমুখে {transit_days} দিনের পরিবহনে বেরি পচে না যায়।",
            "te": "తాజా స్ట్రాబెర్రీలు అధిక శ్వాసక్రియ రేటు కలిగి ఉండి తేమను వేగంగా కోల్పోతాయి కాబట్టి ఇది సిఫార్సు చేయబడింది. ఈ గాలి ప్రసరించే పన్నెట్ అదనపు తేమను బయటకు పంపుతూ {destination} కు {transit_days} రోజుల రవాణాలో బూజు తెగులు పట్టకుండా కాపాడుతుంది.",
            "ta": "புதிய ஸ்ட்ராபெர்ரிகளில் அதிக இயற்கை சுவாச விகிதம் இருப்பதால் மற்றும் நீர் விரைவாக இழக்கப்படுவதால் இது பரிந்துரைக்கப்படுகிறது. இந்த காற்றோட்டமான பன்னெட் ஈரப்பதத்தை வெளியேற்றி, {destination} செல்லும் {transit_days} நாள் பயணத்தில் அழுகாமல் பாதுகாக்கிறது.",
            "es": "Recomendado porque las fresas frescas tienen una tasa de respiración muy alta y pierden humedad rápidamente. Esta tarrina transpirable permite disipar el exceso de humedad evitando condensación y moho (Botrytis) durante el trayecto de {transit_days} días a {destination}.",
            "fr": "Recommandé car les fraises fraîches ont un taux de respiration très élevé. Cette barquette respirante évacue l'excès d'humidité sans condensation, empêchant la moisissure grise (Botrytis) d'altérer les fruits pendant les {transit_days} jours de transport vers {destination}.",
            "de": "Empfohlen, da frische Erdbeeren eine sehr hohe Atmungsrate aufweisen. Diese atmungsaktive Schale lässt überschüssige Feuchtigkeit entweichen und verhindert Kondensat sowie Grauschimmel während des {transit_days}-tägigen Transports nach {destination}.",
            "zh": "推荐此包装，因为新鲜草莓呼吸作用强且极易失水。这种透气小盒使多余湿气排出且不结露，防止在前往{destination}的{transit_days}天运输途中滋生灰霉病腐烂。",
            "ar": "يوصى بهذه العبوة لأن الفراولة الطازجة تتنفس بمعدل مرتفع للغاية وتفقد الرطوبة بسرعة. تتيح هذه العبوة ذات التهوية خروج الرطوبة الزائدة دون تكاثف، مما يمنع تعفن الثمار أثناء رحلة {transit_days} أيام إلى {destination}.",
            "pt": "Recomendado porque os morangos frescos possuem altíssima taxa respiratória. Esta bandeja respirável dissipa a umidade excessiva sem condensação, protegendo contra mofo cinzento durante os {transit_days} dias de viagem até {destination}.",
            "ru": "Рекомендовано, так как свежая клубника обладает высокой интенсивностью дыхания. Этот дышащий контейнер выводит избыточную влагу без конденсата, предотвращая развитие серой гнили при {transit_days}-дневной перевозке в {destination}.",
            "ja": "イチゴは呼吸量が非常に多く水分蒸散が激しいため本包装を推奨します。防曇マイクロ通気容器が結露を防ぎ、{destination}までの{transit_days}日間の輸送中の灰色かび病の発生を防ぎます。",
            "it": "Consigliato perché le fragole fresche hanno un'elevata frequenza respiratoria. Questo cestino traspirante disperde l'umidità in eccesso senza condensa, prevenendo la muffa grigia durante i {transit_days} giorni di transito verso {destination}.",
            "tr": "Çileğin yüksek solunum hızı ve su kaybı nedeniyle önerilmiştir. Bu nefes alabilir kap, buğulanma yapmadan fazla nemi tahliye ederek {destination} kentine yapılan {transit_days} günlük sevkiyatta çürümeyi önler.",
            "ko": "신선한 딸기는 호흡률이 매우 높아 수분이 급격히 소실되므로 이 포장을 권장합니다. 통기성 펀넷이 결로 없이 수분을 배출하여 {destination}까지 {transit_days}일간의 운송 중 잿빛곰팡이병을 방지합니다.",
            "nl": "Aanbevolen omdat verse aardbeien een hoge ademhalingssnelheid hebben. Dit ademende bakje voert overtollig vocht af zonder condensatie, waardoor vruchtrot tijdens het transport van {transit_days} dagen naar {destination} wordt voorkomen.",
            "vi": "Được khuyến nghị vì dâu tây tươi có cường độ hô hấp cao và mất nước nhanh. Hộp thoáng khí này giúp thoát ẩm thừa mà không đọng sương, ngăn ngừa nấm mốc thối rữa trong {transit_days} ngày vận chuyển đến {destination}.",
            "id": "Direkomendasikan karena stroberi segar memiliki laju respirasi tinggi. Wadah berventilasi ini membuang kelembapan berlebih tanpa kondensasi, mencegah jamur busuk selama {transit_days} hari perjalanan ke {destination}."
        },
        "industry": {
            "en": "Calibrated to strawberry respiratory quotient (RQ ~ 1.0) and high transpiration coefficient. The micro-perforations prevent anaerobic fermentation (O₂ < 2%) and ethanol off-flavor formation, while anti-fog coating maintains high optical clarity without water droplet pooling that fosters Botrytis cinerea.",
            "mr": "स्ट्रॉबेरीच्या श्वसन गुणोत्तर (RQ ~ 1.0) आणि उच्च बाष्पोत्सर्जन गुणांकानुसार कॅलिब्रेट केलेले. मायक्रो-परफोरेशन्स ॲनेरोबिक किण्वन (O₂ < 2%) आणि इथेनॉलचा दुर्गंध तयार होण्यास प्रतिबंध करतात, तर अँटी-फॉग कोटिंग बोट्रीटिस सिनेरिया बुरशीला उत्तेजन देणाऱ्या पाण्याचे थेंब साचू न देता उच्च पारदर्शकता टिकवून ठेवते.",
            "hi": "स्ट्रॉबेरी के श्वसन गुणांक (RQ ~ 1.0) और उच्च वाष्पोत्सर्जन दर के अनुसार कैलिब्रेट किया गया। माइक्रो-छिद्र अवायवीय किण्वन (O₂ < 2%) और इथेनॉल की दुर्गंध को रोकते हैं, जबकि एंटी-फॉग कोटिंग पानी की बूंदें जमा होने से रोककर दृश्य स्पष्टता बनाए रखती है।",
            "gu": "સ્ટ્રોબેરીના શ્વસન ગુણાંક (RQ ~ 1.0) અનુસાર માઇક્રો-છિદ્રો ઍનેરોબિક આથો અટકાવે છે, જ્યારે એન્ટિ-ફોગ કોટિંગ પાણીના ટીપાં જમા થવા દેતું નથી.",
            "bn": "স্ট্রবেরির শ্বসন অনুপাত (RQ ~ 1.0) অনুসারে ক্যালিব্রেট করা হয়েছে। মাইক্রো-ছিদ্র অ্যানেরোবিক গাঁজন রোধ করে এবং অ্যান্টি-ফগ প্রলেপ জলবিন্দু জমা হতে দেয় না।",
            "te": "స్ట్రాబెర్రీ శ్వాసకోశ గుణకం (RQ ~ 1.0) కు అనుగుణంగా మైక్రో-రంధ్రాలు ఆక్సిజన్ సమతుల్యతను కాపాడతాయి మరియు యాంటీ-ఫాగ్ కోటింగ్ నీటి తుంపరలు చేరకుండా స్పష్టతను ఇస్తుంది.",
            "ta": "ஸ்ட்ராபெர்ரி சுவாச விகிதத்திற்கு ஏற்ப துல்லியமாக வடிவமைக்கப்பட்டுள்ளது. நுண் துளைகள் காற்றில்லா நொதித்தலைத் தடுக்கின்றன மற்றும் பனி படரா பூச்சு நீர்த்துளிகள் சேர்வதை தவிர்க்கிறது.",
            "es": "Calibrado al cociente respiratorio de la fresa (RQ ~ 1.0). Las microperforaciones previenen fermentación anaeróbica (O₂ < 2%) y la formación de etanol, mientras el recubrimiento antivaho evita gotas de condensación.",
            "fr": "Calibré sur le quotient respiratoire de la fraise (QR ~ 1,0). Les micro-perforations empêchent la fermentation anaérobie et le revêtement antibuée élimine le perlage des gouttelettes d'eau.",
            "de": "Kalibriert auf den respiratorischen Quotienten der Erdbeere. Die Mikroperforation verhindert anaerobe Gärung, während die Antibeschlag-Beschichtung klare Sicht ohne Tropfenbildung sichert.",
            "zh": "根据草莓呼吸商(RQ~1.0)精准校准。微孔膜防止无氧呼吸发酵，防雾涂层防止水滴凝结并抑制灰霉菌繁殖。",
            "ar": "معاير وفق المعامل التنفسي للفراولة. تمنع الثقوب الدقيقة التخمر اللاهوائي، بينما يمنع طلاء مقاومة الضباب تجمع قطرات الماء على السطح الداخلي.",
            "pt": "Calibrado de acordo com o quociente respiratório do morango. As microperfurações evitam fermentação anaeróbia e o revestimento antiembaçante impede o acúmulo de gotas d'água.",
            "ru": "Откалибровано под дыхательный коэффициент клубники. Микроперфорация предотвращает анаэробное брожение, а антифоговое покрытие препятствует скоплению капель конденсата.",
            "ja": "イチゴの呼吸商(RQ~1.0)に合わせて設計。微細孔が無酸素発酵を防ぎ、防曇コーティングにより水滴付着と灰色かび病の発生を抑えます。",
            "it": "Calibrato sul quoziente respiratorio della fragola. Le micro-perforazioni prevengono la fermentazione anaerobica e il rivestimento antiappannante impedisce la condensa.",
            "tr": "Çileğin solunum katsayısına göre kalibre edilmiştir. Mikro delikler anaerobik fermantasyonu önlerken, buğu önleyici kaplama su damlacığı birikimini engeller.",
            "ko": "딸기의 호흡 지수에 맞춰 보정되었습니다. 미세 타공이 무산소 발효를 방지하고 방담 코팅이 물방울 맺힘을 차단하여 신선도를 유지합니다.",
            "nl": "Afgestemd op de respiratie van aardbeien. De microperforaties voorkomen anaerobe gisting en de anti-condenslaag voorkomt druppelvorming.",
            "vi": "Được hiệu chuẩn theo hệ số hô hấp của dâu tây. Lớp vi lỗ ngăn ngừa lên men kỵ khí và lớp phủ chống đọng sương duy trì độ trong suốt tối ưu.",
            "id": "Dikalibrasi sesuai koefisien respirasi stroberi. Lubang mikro mencegah fermentasi anaerob dan lapisan anti-embun menjaga kejernihan tanpa genangan tetes air."
        }
    },
    "chips": {
        "farmer": {
            "en": "Recommended because fried snacks contain high amounts of cooking oil that turn smelly and rancid when exposed to air and light. The metallic silver layer completely blocks sunlight and oxygen, while keeping out highway humidity so snacks stay crispy for {total_storage_days} days.",
            "mr": "शिफारस करण्याचे कारण म्हणजे तळलेल्या खाद्यपदार्थांमध्ये तेलाचे प्रमाण जास्त असते, जे हवा आणि प्रकाशाच्या संपर्कात आल्यास खवट व दुर्गंधीयुक्त होते. चंदेरी धातूचा थर सूर्यप्रकाश आणि ऑक्सिजन पूर्णपणे अडवतो आणि आर्द्रता आत येऊ न देता {total_storage_days} दिवस कुरकुरीत ठेवतो.",
            "hi": "सिफारिश इसलिए की गई है क्योंकि तले हुए नमकीन और चिप्स में तेल होता है जो हवा और रोशनी के संपर्क में आने पर खराब हो जाता है। सिल्वर मेटैलिक परत धूप और ऑक्सीजन को रोकती है तथा {total_storage_days} दिनों तक कुरकुरापन बनाए रखती है।",
            "gu": "તળેલા નાસ્તામાં રહેલું તેલ હવા અને સૂર્યપ્રકાશથી ખરાબ ન થાય તે માટે આ સિલ્વર મેટાલિક પાઉચ ઓક્સિજન અને ભેજને અટકાવીને {total_storage_days} દિવસ સુધી ક્રિસ્પી રાખે છે.",
            "bn": "ভাজা নাস্তায় তেল থাকে যা বাতাস ও আলোর সংস্পর্শে নষ্ট হয়ে যায়। এই রুপোলি স্তরের থলি সূর্যালোক ও অক্সিজেন সম্পূর্ণ প্রতিরোধ করে {total_storage_days} দিন মচমচে রাখে।",
            "te": "నూనెలో వేయించిన చిరుతిళ్ళు గాలి, కాంతి తగిలితే వాసన వస్తాయి. ఈ సిల్వర్ మెటాలిక్ పౌచ్ సూర్యకాంతి మరియు ఆక్సిజన్\u200cను అడ్డుకుని {total_storage_days} రోజుల పాటు స్నాక్స్ కరకరలాడేలా ఉంచుతుంది.",
            "ta": "வறுத்த தின்பண்டங்களில் உள்ள எண்ணெய் காற்று மற்றும் வெளிச்சத்தால் கெட்டுப்போகாமல் இருக்க, இந்த வெள்ளி உலோகப் பை ஒளியைத் தடுத்து {total_storage_days} நாட்கள் மொறுமொறுப்பாக வைக்கிறது.",
            "es": "Recomendado porque los aperitivos fritos contienen aceites que se enrancian con el aire y la luz. La capa metalizada bloquea oxígeno y luz solar, conservando el crujiente durante {total_storage_days} días.",
            "fr": "Recommandé car les snacks frits contiennent de l'huile sujette au rancissement. La couche métallisée bloque l'oxygène et la lumière, maintenant les chips croustillantes pendant {total_storage_days} jours.",
            "de": "Empfohlen, da gebratene Snacks Öle enthalten, die bei Luft- und Lichteinwirkung ranzig werden. Die metallisierte Schicht schützt vor Sauerstoff und Feuchtigkeit für {total_storage_days} Tage Knusprigkeit.",
            "zh": "推荐此包装，因为油炸食品油脂易氧化酸败。镀铝金属层100%隔绝阳光与氧气，防潮阻气，确保小吃在{total_storage_days}天内保持香脆。",
            "ar": "يوصى بهذه العبوة لأن الوجبات المقلية تتأكسد بوجود الضوء والهواء. تحجب الطبقة المعدنية الفضية الضوء والأكسجين تماماً، مما يحافظ على القرمشة لمدة {total_storage_days} يوماً.",
            "pt": "Recomendado pois salgadinhos fritos contêm óleos que oxidam ao contato com luz e oxigênio. A laminação metalizada bloqueia a luz e umidade por {total_storage_days} dias.",
            "ru": "Рекомендовано, так как масло в чипсах быстро окисляется на свету и воздухе. Металлизированный слой полностью блокирует УФ-лучи и кислород на {total_storage_days} дней.",
            "ja": "油分を含むスナック菓子の酸化・酸敗を防ぐため本包装を推奨。アルミ蒸着層が光と酸素を完全遮断し、{total_storage_days}日間パリッとした食感を保ちます。",
            "it": "Consigliato perché gli snack fritti contengono oli che irrancidiscono alla luce. Lo strato metallizzato blocca luce e ossigeno, mantenendoli croccanti per {total_storage_days} giorni.",
            "tr": "Kızartılmış ürünlerdeki yağların ışık ve hava ile acılaşmasını önlemek için önerilmiştir. Metalize bariyer tabakası nemi ve oksijeni engelleyerek {total_storage_days} gün çıtırlık sağlar.",
            "ko": "튀김 스낵의 유지 산패를 방지하기 위해 추천합니다. 알루미늄 증착층이 햇빛과 산소를 완벽히 차단하여 {total_storage_days}일 동안 바삭함을 유지합니다.",
            "nl": "Aanbevolen omdat gefrituurde snacks snel oxideren door licht en lucht. De gemetalliseerde zilverlaag blokkeert zuurstof en vocht voor {total_storage_days} dagen knapperigheid.",
            "vi": "Khuyến nghị vì đồ ăn chiên chứa dầu dễ bị ôi thiu khi gặp ánh sáng và không khí. Lớp tráng nhôm chặn hoàn toàn tia UV và oxy, giữ độ giòn suốt {total_storage_days} ngày.",
            "id": "Direkomendasikan karena makanan ringan goreng mengandung minyak yang rentan tengik. Lapisan metalik memblokir sinar matahari dan oksigen agar tetap renyah selama {total_storage_days} hari."
        },
        "industry": {
            "en": "Snack matrix contains ~35% unsaturated free lipid fraction prone to free radical auto-oxidation. Nitrogen flush (>99% N₂) suppresses headspace oxygen below 0.5%, preventing peroxide value surge across the {origin} to {destination} corridor.",
            "mr": "तळलेल्या स्नॅक्समध्ये ~३५% असंतृप्त तेल असते, जे हवेमुळे ऑक्सिडाईज होते. नायट्रोजन फ्लशिंग ऑक्सिजन ०.५% पेक्षा कमी ठेवते, ज्यामुळे {origin} ते {destination} दरम्यान पेरोक्साइड मूल्य वाढत नाही.",
            "hi": "स्नैक में लगभग 35% असंतृप्त वसा होती है। नाइट्रोजन फ्लश हेडस्पेस ऑक्सीजन को 0.5% से नीचे रखकर पेरोक्साइड वृद्धि और दुर्गंध को पूरी तरह रोकता है।",
            "gu": "નાસ્તામાં રહેલ તેલના ઓક્સિડેશનને રોકવા માટે નાઇટ્રોજન ફ્લશ ઓક્સિજનને 0.5% થી નીચે રાખે છે.",
            "bn": "স্ন্যাক্সে থাকা তেলের জারণ রোধে নাইট্রোজেন ফ্লাশ অক্সিজেন ০.৫%-এর নিচে রাখে এবং গন্ধ হওয়া প্রতিরোধ করে।",
            "te": "ఆహారంలోని నూనెలు ఆక్సీకరణం చెందకుండా నైట్రోజన్ ఫ్లషింగ్ ఆక్సిజన్ పరిమాణాన్ని 0.5% కంటే తక్కువగా ఉంచుతుంది.",
            "ta": "எண்ணெய் ஆக்சிஜனேற்றத்தைத் தடுக்க நைட்ரஜன் வாயு நிரப்பப்பட்டு ஆக்சிஜன் அளவு 0.5% க்கும் குறைவாக பராமரிக்கப்படுகிறது.",
            "es": "La matriz del snack contiene ~35% de lípidos propensos a autooxidación. El barrido con nitrógeno (>99% N₂) mantiene el oxígeno bajo 0.5% previniendo rancidez.",
            "fr": "La matrice contient ~35% de lipides insaturés. L'injection d'azote maintient l'oxygène sous 0,5%, stoppant net la dégradation par auto-oxydation.",
            "de": "Snack enthält ~35% ungesättigte Fettsäuren. Die Stickstoffspülung senkt den Restsauerstoff auf unter 0,5% und stoppt die Peroxidbildung.",
            "zh": "含油率约35%易发生自由基自动氧化。高纯度充氮(>99% N₂)将顶隙氧降至0.5%以下，杜绝过氧化值升高产生哈败味。",
            "ar": "يحتوي المنتج على زيوت غير مشبعة معرضة للأكسدة. يقلل ضخ النيتروجين نسبة الأكسجين لأقل من 0.5% لمنع التزنخ تماماً.",
            "pt": "Contém ~35% de lipídios propensos à auto-oxidação. A lavagem com nitrogênio mantém o oxigênio residual abaixo de 0,5%, evitando a rancidez.",
            "ru": "Содержит до 35% жиров, склонных к прогорканию. Защитная газовая среда с азотом снижает уровень кислорода ниже 0,5%, предотвращая окисление.",
            "ja": "スナック中の油脂酸化を防ぐため窒素充填を実施。包装内酸素濃度を0.5%未満に抑制し過酸化物価の上昇を遮断します。",
            "it": "Contiene circa il 35% di lipidi suscettibili all'ossidazione. Il lavaggio con azoto riduce l'ossigeno residuo sotto lo 0,5% evitando l'irrancidimento.",
            "tr": "Yağ oksidasyonunu önlemek için azot dolumu uygulanır. Oksijen oranı %0.5 altına indirilerek peroksit artışı engellenir.",
            "ko": "지방 자동 산화를 방지하기 위해 질소 충전을 적용합니다. 잔존 산소 농도를 0.5% 이하로 낮춰 산패취 발생을 원천 차단합니다.",
            "nl": "Voorkomt ranzigheid door stikstofspoeling die de zuurstofconcentratie onder de 0,5% houdt tijdens de gehele distributie.",
            "vi": "Chứa khoảng 35% chất béo dễ bị oxy hóa. Bơm khí nitơ giữ lượng oxy dưới 0,5% giúp triệt tiêu quá trình ôi dầu.",
            "id": "Mengandung lemak yang rentan oksidasi. Pengisian nitrogen menekan kadar oksigen di bawah 0,5% untuk mencegah ketengikan."
        }
    },
    "paneer": {
        "farmer": {
            "en": "Recommended because fresh paneer is wet and rich in protein and moisture, making it spoil quickly if touched by air. Vacuum sealing removes all air pockets, stopping mold and sour bacteria from growing so it stays fresh for {total_storage_days} days under refrigeration.",
            "mr": "शिफारस करण्याचे कारण म्हणजे ताज्या पनीरमध्ये पाणी आणि प्रथिनांचे प्रमाण जास्त असल्याने हवेच्या संपर्कात ते लवकर खराब होते. व्हॅक्यूम सीलिंग सर्व हवा काढून टाकते, ज्यामुळे बुरशी आणि आंबट बॅक्टेरियांची वाढ थांबते व शीतकरणामध्ये {total_storage_days} दिवस ताजे राहते.",
            "hi": "सिफारिश इसलिए की गई है क्योंकि ताजे पनीर में नमी और प्रोटीन अधिक होता है, जिससे यह हवा के संपर्क में आने पर जल्दी खट्टा हो जाता है। वैक्यूम सीलिंग हवा निकाल देती है और {total_storage_days} दिनों तक ताजी रखती है।",
            "gu": "તાજા પનીરમાં પ્રોટીન અને ભેજ વધારે હોવાથી હવા લાગવાથી બગડી જાય છે. વેક્યુમ સીલિંગ બધી હવા દૂર કરીને બેક્ટેરિયા અટકાવે છે અને {total_storage_days} દિવસ સારું રાખે છે.",
            "bn": "তাজা পনিরে আর্দ্রতা ও প্রোটিন বেশি থাকায় বাতাসের সংস্পর্শে দ্রুত নষ্ট হয়। ভ্যাকুয়াম সিলিং বাতাস দূর করে ব্যাকটেরিয়ার বৃদ্ধি আটকায় এবং {total_storage_days} দিন তাজা রাখে।",
            "te": "తాజా పనీర్\u200cలో తేమ మరియు ప్రోటీన్లు అధికంగా ఉండటం వల్ల గాలి తగిలితే త్వరగా పాడవుతుంది. వాక్యూమ్ సీలింగ్ గాలిని తొలగించి బ్యాక్టీరియా పెరగకుండా {total_storage_days} రోజులు తాజాగా ఉంచుతుంది.",
            "ta": "புதிய பனீரில் ஈரப்பதம் அதிகம் இருப்பதால் காற்றில் கெட்டுவிடும். வெற்றிட சீலிங் (Vacuum seal) காற்றை அகற்றி பாக்டீரியா வளர்ச்சியைத் தடுத்து {total_storage_days} நாட்கள் புத்துணர்ச்சியுடன் வைக்கிறது.",
            "es": "Recomendado porque el queso fresco tiene alta humedad y proteínas, degradándose rápidamente al aire. El envasado al vacío elimina el aire y frena las bacterias durante {total_storage_days} días en frío.",
            "fr": "Recommandé car le fromage frais est riche en eau et protéines. La mise sous vide élimine l'air, stoppant la prolifération bactérienne pendant {total_storage_days} jours au frais.",
            "de": "Empfohlen, da Frischkäse viel Feuchtigkeit und Protein enthält. Die Vakuumversiegelung entzieht Sauerstoff und hemmt das Bakterienwachstum für {total_storage_days} Tage.",
            "zh": "推荐此包装，因为新鲜鲜酪(Paneer)水分和蛋白质含量极高，极易滋生酸败菌。高阻隔真空贴体彻底抽除氧气，冷藏保鲜{total_storage_days}天。",
            "ar": "يوصى بالجبن الطازج لأنه غني بالبروتين والرطوبة ويتلف بسرعة عند تعرضه للهواء. يسحب التغليف المفرغ الهواء بالكامل لمنع البكتيريا والحفاظ عليه لمدة {total_storage_days} يوماً.",
            "pt": "Recomendado pois o queijo fresco possui alta umidade e proteínas. A selagem a vácuo remove o ar, inibindo bactérias e preservando por {total_storage_days} dias sob refrigeração.",
            "ru": "Рекомендовано из-за высокой влажности и белка в свежем сыре. Вакуумная герметизация удаляет воздух, подавляя рост бактерий на {total_storage_days} дней.",
            "ja": "高水分・高タンパクな生チーズの腐敗を防ぐため真空包装を推奨。脱気密封により好気性細菌の増殖を抑え、冷蔵下で{total_storage_days}日間鮮度を保持します。",
            "it": "Consigliato poiché il formaggio fresco è ricco di umidità e proteine. Il sottovuoto elimina l'aria, bloccando la proliferazione batterica per {total_storage_days} giorni in frigo.",
            "tr": "Yüksek nem ve protein içeren taze peynirin bozulmasını önlemek için önerilmiştir. Vakumlu ambalaj havayı tamamen tahliye ederek {total_storage_days} gün tazelik sağlar.",
            "ko": "수분과 단백질이 풍부한 신선 치즈의 부패를 방지하기 위해 진공 밀봉을 권장합니다. 잔여 공기를 제거하여 냉장 보관 시 {total_storage_days}일간 신선도를 유지합니다.",
            "nl": "Aanbevolen omdat verse kaas veel vocht en eiwit bevat. Vacuümverpakking verwijdert alle lucht en remt bacteriegroei gedurende {total_storage_days} dagen.",
            "vi": "Khuyến nghị vì phô mai tươi chứa nhiều nước và đạm, dễ chua hỏng khi gặp không khí. Hút chân không loại bỏ hoàn toàn khí, giữ tươi {total_storage_days} ngày trong tủ mát.",
            "id": "Direkomendasikan karena keju segar berkadar air dan protein tinggi. Kemasan vakum mengeluarkan seluruh udara untuk mencegah bakteri asam selama {total_storage_days} hari."
        },
        "industry": {
            "en": "Fresh dairy matrix exhibits high water activity (aw > 0.98) and near-neutral pH (~6.1). EVOH multi-layer core prevents oxygen ingress, while hermetic seal integrity suppresses psychrotrophic bacterial growth under chilled logistics.",
            "mr": "ताज्या दुग्धजन्य पदार्थांमध्ये उच्च पाण्याची क्रियाशीलता (aw > 0.98) असते. EVOH मल्टी-लेयर कोर ऑक्सिजनचा शिरकाव रोखतो, ज्यामुळे शीत साखळीत सायक्रोट्रॉफिक बॅक्टेरियाची वाढ पूर्णपणे थांबते.",
            "hi": "ताजा पनीर उच्च जल गतिविधि (aw > 0.98) दर्शाता है। EVOH बहुस्तरीय संरचना ऑक्सीजन प्रवेश को रोकती है और कोल्ड-चेन में बैक्टीरिया के विकास को पूरी तरह नियंत्रित करती है।",
            "gu": "પનીરમાં ઊંચી ભેજ પ્રવૃત્તિ હોવાથી EVOH મલ્ટી-લેયર ઓક્સિજન અટકાવીને ગુણવત્તા જાળવે છે.",
            "bn": "তাজা দুগ্ধজাত দ্রব্যের উচ্চ জলীয় কার্যকলাপ থাকে। EVOH বহুস্তরীয় কাঠামো অক্সিজেন প্রবেশ রোধ করে ব্যাকটেরিয়ার বিস্তার আটকায়।",
            "te": "డైరీ ఉత్పత్తులలో అధిక తేమ వలన బ్యాక్టీరియా పెరగకుండా EVOH మల్టీ-లేయర్ ప్యాకింగ్ ఆక్సిజన్\u200cను సమర్థవంతంగా అడ్డుకుంటుంది.",
            "ta": "பால் பொருட்களின் அதிக ஈரப்பதம் காரணமாக, EVOH பல அடுக்கு பேக்கேஜிங் ஆக்சிஜன் நுழைவதைத் தடுத்து தரத்தை பாதுகாக்கிறது.",
            "es": "La matriz láctea presenta alta actividad de agua (aw > 0.98). La estructura multicapa con EVOH previene la penetración de oxígeno y frena patógenos psicrótrofos.",
            "fr": "Activité de l'eau élevée (aw > 0,98). La barrière multicouche EVOH empêche la pénétration d'oxygène et inhibe la flore psychrotrophe.",
            "de": "Hohe Wasseraktivität (aw > 0,98). Die EVOH-Mehrschichtfolie verhindert Sauerstoffeintritt und stoppt psychrotrophe Keime zuverlässig.",
            "zh": "乳制品水活度极高(aw>0.98)。EVOH高阻隔共挤膜阻隔氧气渗透，杜绝嗜冷菌滋生。",
            "ar": "تتميز منتجات الألبان بنشاط مائي مرتفع. تمنع طبقات EVOH نفاذ الأكسجين وتثبط نمو البكتيريا في درجات التبريد.",
            "pt": "Apresenta alta atividade de água (aw > 0,98). A barreira EVOH multicamadas impede a entrada de oxigênio sob cadeia do frio.",
            "ru": "Высокая активность воды (aw > 0,98). Многослойный барьер с EVOH блокирует кислород, останавливая рост психротрофных бактерий.",
            "ja": "水分活性(aw>0.98)が高い乳製品に対し、EVOH多層バリアフィルムが酸素透過を遮断し低温細菌の繁殖を抑制します。",
            "it": "Elevata attività dell'acqua (aw > 0,98). La struttura barriera multistrato in EVOH blocca l'ossigeno prevenendo la contaminazione.",
            "tr": "Yüksek su aktivitesine sahip süt ürünlerinde EVOH çok katmanlı yapı oksijen girişini keserek bakteri üremesini durdurur.",
            "ko": "높은 수분 활성도(aw > 0.98)에 대응하여 EVOH 다층 배리어 필름이 산소 유입을 차단하고 저온 세균 증식을 억제합니다.",
            "nl": "Hoge wateractiviteit (aw > 0,98). De EVOH meerlaagse folie blokkeert zuurstofinfiltratie tijdens gekoelde logistiek.",
            "vi": "Hoạt độ nước cao (aw > 0,98). Cấu trúc màng đa lớp EVOH ngăn oxy thẩm thấu, ức chế vi khuẩn phát triển trong chuỗi lạnh.",
            "id": "Aktivitas air tinggi (aw > 0,98). Lapisan multi-layer EVOH menghalangi oksigen dan menekan pertumbuhan bakteri selama rantai dingin."
        }
    },
    "mango": {
        "farmer": {
            "en": "Recommended because mangoes release natural ripening gas (ethylene) and can overheat if packed in airtight plastic. This ventilated eco-pack lets ripening gases vent out smoothly while protecting fruits from transit vibrations across the {transit_days}-day route to {destination}.",
            "mr": "शिफारस करण्याचे कारण म्हणजे आंबे पिकताना नैसर्गिक वायू (इथिलीन) सोडतात आणि हवाबंद प्लॅस्टिकमध्ये पॅक केल्यास ते आतून गरम होऊन खराब होतात. हे वायुवीजनयुक्त इको-पॅक पिकवणारे वायू बाहेर पडू देते आणि {destination} कडे जाणाऱ्या {transit_days} दिवसांच्या प्रवासात धक्क्यांपासून फळांचे रक्षण करते.",
            "hi": "सिफारिश इसलिए की गई है क्योंकि आम पकने के दौरान प्राकृतिक गैस (एथिलीन) छोड़ते हैं। यह हवादार इको-पैक गैस को बाहर निकलने देता है और {destination} के {transit_days} दिनों के सफर में आमों को दबने से बचाता है।",
            "gu": "કેરી પાકતી વખતે કુદરતી ઇથિલીન ગેસ છોડે છે. આ વેન્ટિલેટેડ ઇકો-પેક ગેસને સરળતાથી બહાર નીકળવા દે છે અને {destination} સુધીની મુસાફરીમાં ફળને સુરક્ષિત રાખે છે.",
            "bn": "আম পাকার সময় প্রাকৃতিকভাবে ইথিলিন গ্যাস নির্গত হয়। এই বায়ুচলাচলযুক্ত পরিবেশবান্ধব প্যাক গ্যাস নির্গমনে সাহায্য করে এবং পরিবহনের ঝাঁকুনি থেকে রক্ষা করে।",
            "te": "మామిడి పండ్లు పక్వానికి వచ్చేటప్పుడు ఇథిలీన్ వాయువును విడుదల చేస్తాయి. ఈ వెంటిలేటెడ్ ప్యాక్ వాయువులు బయటకు పోయేలా చేసి ప్రయాణంలో దెబ్బతినకుండా కాపాడుతుంది.",
            "ta": "மாம்பழங்கள் பழுக்கும் போது எத்திலீன் வாயுவை வெளியிடுகின்றன. இந்த காற்றோட்ட சூழல் நட்பு பேக் வாயுவை வெளியேற்றி பயண அதிர்வுகளிலிருந்து பழங்களைப் பாதுகாக்கிறது.",
            "es": "Recomendado porque los mangos emiten etileno y pueden sobrecalentarse en plástico hermético. Este envase ventilado disipa gases y protege contra impactos hacia {destination}.",
            "fr": "Recommandé car les mangues libèrent de l'éthylène naturel. Cet emballage ventilé évacue les gaz de maturation et protège des chocs jusqu'à {destination}.",
            "de": "Empfohlen, da Mangos Reifegas (Ethylen) abgeben. Diese belüftete Öko-Verpackung lässt Reifegase entweichen und schützt vor Transportschäden.",
            "zh": "推荐此包装，因为芒果后熟释放乙烯气体。微通风环保包装使乙烯顺畅释放，防止闷热变质并缓冲前往{destination}的运输震动。",
            "ar": "يوصى بهذه العبوة لأن المانجو تطلق غاز الإيثيلين أثناء النضج. تتيح هذه العبوة المهواة تنفيس الغازات وحماية الثمار من صدمات النقل إلى {destination}.",
            "pt": "Recomendado pois as mangas liberam etileno ao amadurecer. Esta embalagem ventilada dissipa os gases e amortece vibrações durante o frete.",
            "ru": "Рекомендовано, так как манго выделяет этилен при созревании. Вентилируемая эко-упаковка отводит газы и смягчает удары в пути до {destination}.",
            "ja": "マンゴーの追熟エチレンガスと呼吸熱の蓄積を防ぐため微細通気孔付き包装を推奨。{destination}への輸送衝撃を吸収します。",
            "it": "Consigliato perché i manghi rilasciano etilene. Questo imballaggio ventilato disperde i gas di maturazione e protegge dagli urti verso {destination}.",
            "tr": "Mangolar olgunlaşırken etilen gazı salgılar. Bu havalandırmalı ambalaj gazı tahliye ederek meyveleri {destination} yolculuğundaki darbelerden korur.",
            "ko": "망고는 숙성 중 에틸렌 가스를 방출합니다. 통기성 친환경 패키지가 가스를 원활히 배출하고 {destination}까지의 운송 진동으로부터 과일을 보호합니다.",
            "nl": "Aanbevolen omdat mango's ethyleengas afgeven. Deze geventileerde eco-verpakking voert rijpingsgassen af en beschermt tegen schokken naar {destination}.",
            "vi": "Khuyến nghị vì xoài thải khí ethylene khi chín. Bao bì thông gió sinh học giúp thoát khí ethylene và chống va đập trên đường đến {destination}.",
            "id": "Direkomendasikan karena mangga melepas gas etilen saat matang. Kemasan berventilasi ini membuang gas dan melindungi dari getaran menuju {destination}."
        },
        "industry": {
            "en": "Climacteric fruit with peak ethylene surge upon physiological ripening. Controlled breathability retards chlorophyll degradation and softening enzymes without causing anaerobic fermentation.",
            "mr": "शारीरिक पक्वतेच्या वेळी इथिलीनचे प्रमाण वाढणारे हे फळ आहे. नियंत्रित श्वासोच्छवास क्लोरोफिलचा ऱ्हास आणि फळ मऊ पडणे थांबवतो आणि किण्वन होऊ देत नाही.",
            "hi": "क्लाइमेक्टेरिक फल होने के कारण एथिलीन तेजी से बढ़ता है। नियंत्रित गैस विनिमय फल को अत्यधिक मुलायम होने से रोकता है।",
            "gu": "ફળના કુદરતી પાકવાના દરને નિયંત્રિત કરવા માટે યોગ્ય ગેસ પારગમ્યતા જાળવી રાખવામાં આવે છે.",
            "bn": "নিয়ন্ত্রিত শ্বসন হার ফলের অতিরিক্ত নরম হওয়া ও পচন প্রতিরোধ করে এবং সতেজতা বজায় রাখে।",
            "te": "ఇథిలీన్ స్థాయిలను సమతుల్యం చేస్తూ కాయ మెత్తబడకుండా ఈ నియంత్రిత ప్యాకింగ్ ఉపయోగపడుతుంది.",
            "ta": "கட்டுப்படுத்தப்பட்ட வாயு ஊடுருவல் மாம்பழம் விரைவில் மென்மையாவதைத் தடுத்து புத்துணர்ச்சியை நீடிக்கிறது.",
            "es": "Fruta climatérica con pico de etileno. La permeabilidad calibrada retrasa enzimas de ablandamiento sin inducir fermentación.",
            "fr": "Fruit climatérique à pic d'éthylène. La perméabilité contrôlée retarde le ramollissement sans provoquer de fermentation.",
            "de": "Klimakterische Frucht mit Ethylenanstieg. Kontrollierte Gasdurchlässigkeit verzögert die Fruchterweichung.",
            "zh": "跃变型果实具有乙烯高峰。调控型透气膜延缓叶绿素分解与果肉软化，保持细胞饱满度。",
            "ar": "فاكهة مناخية تطلق كميات من الإيثيلين. تسمح النفاذية المتحكم فيها بتأخير ليونة الثمار دون تخمر.",
            "pt": "Fruta climatérica com pico de etileno. A permeabilidade calibrada retarda o amolecimento sem fermentar.",
            "ru": "Климактерический фрукт с пиком этилена. Контролируемый газообмен замедляет размягчение тканей плода.",
            "ja": "クライマクテリック型果実のエチレン急増に対応。適正な通気性で軟化酵素の活性を抑え鮮度を保ちます。",
            "it": "Frutto climaterico con picco di etilene. La permeabilità controllata ritarda l'ammorbidimento dei tessuti.",
            "tr": "Klimakterik meyvelerde etilen çıkışını dengeleyen kontrollü geçirgenlik, meyvenin yumuşamasını geciktirir.",
            "ko": "호흡 급등형 과일의 에틸렌 피크에 대응하여 적정 통기성 필름이 과육 연화를 지연시킵니다.",
            "nl": "Klimakterisch fruit met ethyleenpiek. Gecontroleerde gasdoorlaatbaarheid vertraagt vruchtoverzachting.",
            "vi": "Trái cây có đỉnh hô hấp ethylene. Độ thẩm thấu khí được kiểm soát làm chậm quá trình mềm quả.",
            "id": "Buah klimakterik dengan lonjakan etilen. Permeabilitas terukur memperlambat pelunakan buah."
        }
    },
    "produce": {
        "farmer": {
            "en": "Recommended because {food_name} requires balanced airflow to stay firm and fresh without sweating or drying out. This packaging protects produce from highway humidity and vibrations across the {origin} to {destination} route for {total_storage_days} days.",
            "mr": "शिफारस करण्याचे कारण म्हणजे {food_name} ला पाण्याचा घाम न येता किंवा सुकण्यापासून वाचवण्यासाठी संतुलित हवेची गरज असते. हे पॅकेजिंग {origin} ते {destination} दरम्यानच्या प्रवासात आर्द्रता आणि धक्क्यांपासून {total_storage_days} दिवस संरक्षण करते.",
            "hi": "सिफारिश इसलिए की गई है क्योंकि {food_name} को नमी और सड़न से बचाने के लिए संतुलित हवा की आवश्यकता होती है। यह पैकेजिंग {origin} से {destination} के मार्ग में {total_storage_days} दिनों तक सुरक्षा प्रदान करती है।",
            "gu": "{food_name} માટે યોગ્ય હવાની અવરજવર જરૂરી છે જેથી તે સુકાઈ ન જાય. આ પેકેજિંગ {origin} થી {destination} ના રસ્તે {total_storage_days} દિવસ સુધી તાજગી જાળવે છે.",
            "bn": "{food_name} সতেজ ও শক্ত রাখতে সুষম বায়ুপ্রবাহ প্রয়োজন। এই প্যাকেজিং {origin} থেকে {destination} পর্যন্ত {total_storage_days} দিন মান বজায় রাখে।",
            "te": "{food_name} తాజాగా మరియు గట్టిగా ఉండటానికి సమతుల్య గాలి ప్రసరణ అవసరం. ఈ ప్యాకేజింగ్ {origin} నుండి {destination} వరకు {total_storage_days} రోజులు కాపాడుతుంది.",
            "ta": "{food_name} உலராமல் புத்துணர்ச்சியுடன் இருக்க சீரான காற்று தேவை. இந்த பேக்கேஜிங் {origin} முதல் {destination} வரை {total_storage_days} நாட்கள் பாதுகாக்கிறது.",
            "es": "Recomendado porque {food_name} requiere flujo de aire equilibrado para mantenerse firme sin sudar. Protege contra humedad y vibraciones de {origin} a {destination} durante {total_storage_days} días.",
            "fr": "Recommandé car {food_name} nécessite une aération équilibrée pour rester ferme sans flétrir. Protège sur l'itinéraire de {origin} à {destination} pendant {total_storage_days} jours.",
            "de": "Empfohlen, da {food_name} eine ausgewogene Luftzirkulation benötigt, um knackig zu bleiben. Schützt vor Feuchtigkeit auf der Strecke {origin} nach {destination} für {total_storage_days} Tage.",
            "zh": "推荐此包装，因为{food_name}需要平衡的气体流通以保持脆嫩紧实。在{origin}至{destination}的运输中防潮抗震，保鲜{total_storage_days}天。",
            "ar": "يوصى بهذه العبوة لأن {food_name} يتطلب تهوية متوازنة للبقاء طازجاً دون فقدان رطوبته. تحمي من الرطوبة والاهتزازات بين {origin} و {destination} لمدة {total_storage_days} يوماً.",
            "pt": "Recomendado porque {food_name} necessita de aeração balanceada para manter-se firme sem desidratar na rota de {origin} a {destination} por {total_storage_days} dias.",
            "ru": "Рекомендовано, так как {food_name} требует сбалансированной циркуляции воздуха. Защищает от влажности и вибраций по маршруту из {origin} в {destination} на {total_storage_days} дней.",
            "ja": "{food_name}の蒸散と乾燥を防ぎつつ鮮度を保つ微細通気フィルムを推奨。{origin}から{destination}への{total_storage_days}日間の品質を維持します。",
            "it": "Consigliato perché {food_name} richiede circolazione d'aria per rimanere sodo senza appassire. Protegge durante il tragitto da {origin} a {destination} per {total_storage_days} giorni.",
            "tr": "{food_name} ürününün terlemeden taze ve diri kalması için dengeli hava akışı sağlar. {origin} ile {destination} arasında {total_storage_days} gün boyunca korur.",
            "ko": "{food_name}의 아삭함과 수분을 유지하기 위해 균형 잡힌 통기성을 제공합니다. {origin}에서 {destination}까지 {total_storage_days}일간 안전하게 보호합니다.",
            "nl": "Aanbevolen omdat {food_name} gebalanceerde luchtstroom vereist om stevig te blijven zonder uitdroging tijdens de route van {origin} naar {destination} voor {total_storage_days} dagen.",
            "vi": "Khuyến nghị vì {food_name} cần lưu thông không khí cân bằng để giữ độ giòn tươi mà không bị teo héo trên tuyến đường từ {origin} đến {destination} suốt {total_storage_days} ngày.",
            "id": "Direkomendasikan karena {food_name} butuh sirkulasi udara seimbang agar tetap segar tanpa layu di rute {origin} ke {destination} selama {total_storage_days} hari."
        },
        "industry": {
            "en": "Calibrated against commodity decay kinetics and respiration rate. Matches target transmission limits to maintain cellular turgor and prevent microbial proliferation across the logistics corridor.",
            "mr": "वस्तूच्या विघटनाचे गतिशास्त्र आणि श्वसन दरानुसार कॅलिब्रेट केलेले. पेशींचा टवटवीतपणा टिकवण्यासाठी आणि लॉजिस्टिक्स कॉरिडॉरमध्ये सूक्ष्मजीवांची वाढ रोखण्यासाठी लक्ष्यित मर्यादा पूर्ण करते.",
            "hi": "उत्पाद की श्वसन दर और क्षय दर के अनुसार कैलिब्रेट किया गया। यह कोशिकाओं के तनाव को बनाए रखता है और रोगाणुओं के विकास को रोकता है।",
            "gu": "ઉત્પાદનની કુદરતી ગુણવત્તા જાળવવા માટે માઇક્રોબાયલ વૃદ્ધિ અટકાવવા માટે માપાંકિત.",
            "bn": "দ্রব্যের প্রাকৃতিক বৈশিষ্ট্যের সাথে সামঞ্জস্য রেখে জীবাণুর বিস্তার রোধে এবং সতেজতা রক্ষায় তৈরি।",
            "te": "సరుకు నాణ్యతను కాపాడటానికి సూక్ష్మజీవుల పెరుగుదలను నిరోధించేలా సమతుల్య ప్రమాణాలతో రూపొందించబడింది.",
            "ta": "உணவுப் பொருளின் தன்மைகளுக்கு ஏற்ப நுண்ணுயிர் வளர்ச்சியைத் தடுத்து புத்துணர்ச்சியை உறுதி செய்கிறது.",
            "es": "Calibrado según la cinética de degradación celular. Satisface las tasas de permeabilidad para conservar turgencia celular y prevenir proliferación microbiana.",
            "fr": "Calibré sur la cinétique de respiration. Respecte les taux de perméabilité cibles pour maintenir la turgescence cellulaire sans développement microbien.",
            "de": "Kalibriert auf die Verfallskinetik des Produkts. Erhält den Zellinnendruck und verhindert Keimbildung im Transportverlauf.",
            "zh": "针对农产品呼吸与衰变动力学校准。精确匹配透气透湿限度，保持植物细胞膨压并抑制微生物滋生。",
            "ar": "معاير وفق حركية التلف ومعدل التنفس. يطابق حدود النفاذية المستهدفة للحفاظ على حيوية الخلايا ومنع التكاثر البكتيري.",
            "pt": "Calibrado contra a cinética de deterioração. Mantém o turgor celular e inibe a proliferação microbiana ao longo do trajeto.",
            "ru": "Откалибровано с учетом кинетики порчи продукта. Обеспечивает тургор клеток и препятствует размножению микроорганизмов.",
            "ja": "青果物の呼吸・蒸散動態に基づき設計。適正なガスバリア性により細胞のハリを維持し菌の繁殖を防ぎます。",
            "it": "Calibrato sulla cinetica di degradazione. Mantiene il turgore cellulare e impedisce la proliferazione microbica.",
            "tr": "Ürünün bozulma kinetiğine göre kalibre edilmiştir. Hücresel canlılığı korur ve mikrobiyal çoğalmayı önler.",
            "ko": "농산물 호흡 속도에 맞춰 보정되었습니다. 세포 팽압을 유지하고 미생물 증식을 효과적으로 억제합니다.",
            "nl": "Afgestemd op het respiratieproces van het product. Behoudt celspanning en voorkomt bacteriegroei tijdens distributie.",
            "vi": "Được hiệu chuẩn theo động học phân hủy của nông sản. Giữ độ căng mọng của tế bào và ức chế vi sinh vật phát triển.",
            "id": "Dikalibrasi sesuai kinetika pembusukan produk. Menjaga turgor sel dan mencegah perkembangbiakan mikroba di jalur logistik."
        }
    }
}

# Multilingual Farmer Practical Transportation Advice
FARMER_PRACTICAL_ADVICE = {
    "strawberry": {
        "en": [
            "Store harvested fruit in a cool, shaded shed; never leave crates under direct afternoon sun.",
            "Stack crates maximum 4 layers high to prevent crushing delicate bottom punnets.",
            "Maintain transit temperature between 2°C – 6°C using insulated vehicle covering.",
            "Keep punnets dry and protected from road water spray during monsoon highway transit."
        ],
        "mr": [
            "कापणी केलेले फळ थंड आणि सावलीच्या शेडमध्ये ठेवा; दुपारच्या कडक उन्हात क्रेट्स ठेवू नका.",
            "खालच्या नाजूक पनेट्सचे नुकसान होऊ नये म्हणून क्रेट्स जास्तीत जास्त ४ थरांमध्येच ठेवा.",
            "इन्सुलेटेड किंवा वातानुकूलित वाहनाचा वापर करून तापमान २°C ते ६°C दरम्यान ठेवा.",
            "पावसाळ्यात महामार्गावरील प्रवासात पाण्याचे शिंतोडे उडणार नाहीत याची काळजी घ्या आणि पनेट्स कोरडे ठेवा."
        ],
        "hi": [
            "तोड़े गए फलों को ठंडी और छायादार जगह पर रखें; कभी भी दोपहर की तेज धूप में क्रेट न छोड़ें।",
            "नीचे के नाजुक डिब्बों को दबने से बचाने के लिए क्रेटों को अधिकतम 4 परतों तक ही रखें।",
            "इंसुलेटेड वाहन का उपयोग करके पारगमन तापमान 2°C - 6°C के बीच बनाए रखें।",
            "परिवहन के दौरान फलों को बारिश या पानी के छींटों से पूरी तरह सूखा और सुरक्षित रखें।"
        ],
        "gu": [
            "ઉતારેલા ફળોને છાંયડાવાળી ઠંડી જગ્યાએ રાખો; બપોરના તડકામાં ક્રેટ્સ ન મૂકો.",
            "નીચેના પેકિંગને દબાણ ન થાય તે માટે ક્રેટ્સ મહત્તમ 4 સ્તરો સુધી જ ગોઠવો.",
            "વાહનમાં તાપમાન 2°C - 6°C ની વચ્ચે જાળવી રાખવાનો પ્રયાસ કરો.",
            "મુસાફરી દરમિયાન પાણીના છંટકાવથી બચાવીને પેક સંપૂર્ણ સૂકા રાખો."
        ]
    },
    "default": {
        "en": [
            "Sort and remove any damaged or bruised produce before packing into units.",
            "Stack crates squarely on pallets with space for cross air ventilation.",
            "Keep produce out of hot noon sunshine during vehicle transit stops.",
            "Store in dry, shaded warehouse below 15°C upon destination arrival."
        ],
        "mr": [
            "पॅकिंग करण्यापूर्वी खराब झालेला किंवा जखम झालेला शेतमाल निवडून बाजूला काढा.",
            "हवा खेळती राहण्यासाठी पुरेशी जागा ठेवून क्रेट्स व्यवस्थित थरांमध्ये रचा.",
            "प्रवासात वाहन थांबल्यावर शेतमाल दुपारच्या कडक उन्हात उघडा ठेवू नका.",
            "मुक्कामावर पोहोचल्यावर शेतमाल १५°C पेक्षा कमी तापमान असलेल्या कोरड्या सावलीत साठवा."
        ],
        "hi": [
            "पैकिंग करने से पहले किसी भी क्षतिग्रस्त या दाग लगे उत्पाद को छांट कर अलग कर लें।",
            "हवा के संचलन के लिए जगह छोड़ते हुए क्रेटों को पैलेट पर व्यवस्थित रखें।",
            "वाहन रुकने के दौरान उपज को दोपहर की तेज धूप के संपर्क में न आने दें।",
            "गंतव्य पर पहुंचने पर 15°C से कम तापमान वाले सूखे गोदाम में भंडारण करें।"
        ],
        "gu": [
            "પેક કરતાં પહેલાં ક્ષતિગ્રસ્ત કે દબાયેલા માલને અલગ કરી લો.",
            "હવાની અવરજવર જળવાઈ રહે તે રીતે ક્રેટ્સ સરખી રીતે ગોઠવો.",
            "વાહન રોકાય ત્યારે માલ સીધા બપોરના તડકામાં ન રહે તેનું ધ્યાન રાખો.",
            "ગંતવ્ય પર પહોંચ્યા પછી માલને ઠંડી અને સૂકી જગ્યાએ સંગ્રહિત કરો."
        ]
    }
}

def get_localized_why_packaging(category, food_name, transit_days, destination, origin, total_storage_days, lang="en", mode="farmer"):
    """Fetches formatted, localized reason for the recommended packaging."""
    cat = category.lower() if category else "produce"
    if cat not in WHY_PACKAGING_EXPLANATIONS:
        if "strawberr" in cat or "berry" in cat: cat = "strawberry"
        elif "chip" in cat or "namkeen" in cat: cat = "chips"
        elif "paneer" in cat or "dairy" in cat: cat = "paneer"
        elif "mango" in cat: cat = "mango"
        else: cat = "produce"
    
    cat_dict = WHY_PACKAGING_EXPLANATIONS.get(cat, WHY_PACKAGING_EXPLANATIONS["produce"])
    mode_dict = cat_dict.get(mode, cat_dict["farmer"])
    
    template = mode_dict.get(lang, mode_dict.get("en", ""))
    if not template:
        template = mode_dict.get("en", "")
        
    try:
        return template.format(
            food_name=get_food_display_name(food_name, lang),
            transit_days=transit_days or 4,
            destination=destination or "Destination",
            origin=origin or "Origin",
            total_storage_days=total_storage_days or 7
        )
    except Exception:
        return template

def get_localized_advice_list(category, food_name, lang="en"):
    """Fetches list of localized transportation advice points."""
    cat = category.lower() if category else "produce"
    if "strawberr" in cat or "berry" in cat: key = "strawberry"
    else: key = "default"
    
    advice_map = FARMER_PRACTICAL_ADVICE.get(key, FARMER_PRACTICAL_ADVICE["default"])
    if lang in advice_map:
        return advice_map[lang]
    # Fallback to English
    return advice_map.get("en", advice_map["en"])

# Multilingual Farmer Packaging Names across all 21 languages
FARMER_PACKAGING_NAMES = {
    "strawberry": {
        "en": "Eco Breathable Punnet with Anti-Fog Moisture Buffer",
        "mr": "अँटी-फॉग आर्द्रता बफरसह पर्यावरणपूरक श्वास घेण्यायोग्य पनेट",
        "hi": "एंटी-फॉग नमी बफर के साथ पर्यावरण-अनुकूल सांस लेने योग्य पनेट",
        "gu": "એન્ટિ-ફોગ ભેજ બફર સાથે ઇકો-ફ્રેન્ડલી શ્વાસ લેવા યોગ્ય પનેટ",
        "bn": "অ্যান্টি-ফগ আর্দ্রতা বাফার সহ পরিবেশবান্ধব বায়ুচলাচলযুক্ত প্যানেট",
        "te": "యాంటీ-ఫాగ్ తేమ బఫర్ తో కూడిన పర్యావరణ అనుకూల బ్రీతబుల్ పన్నెట్",
        "ta": "பனி படரா ஈரப்பத தாங்கலுடன் கூடிய சூழல் நட்பு காற்றோட்ட பன்னெட்",
        "es": "Tarrina transpirable ecológica con barrera antivaho",
        "fr": "Barquette respirante écologique avec tampon d'humidité antibuée",
        "de": "Ökologische atmungsaktive Schale mit Antibeschlag-Feuchtigkeitspuffer",
        "zh": "防雾控湿环保微透气小盒",
        "ar": "عبوة كرتونية قابلة للتحلل مع عازل رطوبة مقاوم للضباب",
        "pt": "Bandeja respirável ecológica com barreira antiembaçante",
        "ru": "Экологичный дышащий лоток с антифоговым барьером",
        "ja": "防曇調湿機能付きエコ通気パンネット",
        "it": "Cestino traspirante ecologico con tampone antiappannante",
        "tr": "Buğu önleyici nem tamponlu çevre dostu nefes alabilir kap",
        "ko": "방담 수분 완충재가 포함된 친환경 통기성 펀넷",
        "nl": "Milieuvriendelijk ademend bakje met anti-condens vochtbuffer",
        "vi": "Hộp đục lỗ thoáng khí sinh học chống đọng sương",
        "id": "Wadah berventilasi ramah lingkungan dengan penyangga anti-embun"
    },
    "chips": {
        "en": "Silver High-Barrier Airtight Foil Pouch (Nitrogen Flushed)",
        "mr": "सिल्व्हर हाय-बॅरियर हवाबंद फॉइल पाउच (नायट्रोजन फ्लश)",
        "hi": "सिल्वर हाई-बैरियर एयरटाइट फॉयल पाउच (नाइट्रोजन फ्लश)",
        "gu": "સિલ્વર હાઇ-બેરિયર હવાચુસ્ત ફોઇલ પાઉચ (નાઇટ્રોજન ફ્લશ્ડ)",
        "bn": "সিলভার হাই-ব্যারিয়ার বায়ুরোধী ফয়েল পাউচ (নাইট্রোজেন ফ্লাশড)",
        "te": "సిల్వర్ హై-బారియర్ ఎయిర్ టైట్ ఫాయిల్ పౌచ్ (నైట్రోజన్ ఫ్లష్డ్)",
        "ta": "வெள்ளி உயர்-தடுப்பு காற்றுப்புகா ஃபாயில் பை (நைட்ரஜன் நிரப்பப்பட்டது)",
        "es": "Bolsa de aluminio de alta barrera hermética (con nitrógeno)",
        "fr": "Sachet métallisé haute barrière hermétique (injecté d'azote)",
        "de": "Silberner Hochbarriere-Folienbeutel luftdicht (Stickstoffbegast)",
        "zh": "高阻隔镀铝充氮密封立袋",
        "ar": "كيس قصدير فضي محكم الغلق عالي العزل (مضغوط بالنيتروجين)",
        "pt": "Sachet metalizado de alta barreira hermético (com nitrogênio)",
        "ru": "Металлизированный пакет с высоким барьером (в среде азота)",
        "ja": "高バリア性アルミ蒸着気密パウチ（窒素置換包装）",
        "it": "Busta in alluminio ad alta barriera ermetica (con azoto)",
        "tr": "Yüksek bariyerli hava geçirmez gümüş folyo poşet (Azot dolumlu)",
        "ko": "고차단성 알루미늄 증착 기밀 파우치 (질소 충전)",
        "nl": "Zilveren hoogbarrière luchtdichte foliezak (met stikstof)",
        "vi": "Túi màng nhôm cản khí cao cấp hút chân không bơm nitơ",
        "id": "Kantong foil perak kedap udara berpenghalang tinggi (isi nitrogen)"
    },
    "paneer": {
        "en": "Vacuum-Sealed Heavy-Duty Dairy Pouch",
        "mr": "व्हॅक्यूम-सीलबंद हेवी-ड्युटी डेअरी पाउच",
        "hi": "वैक्यूम-सीलबंद हेवी-ड्यूटी डेयरी पाउच",
        "gu": "વેક્યુમ-સીલ્ડ હેવી-ડ્યુટી ડેરી પાઉચ",
        "bn": "ভ্যাকুয়াম-সিলযুক্ত মজবুত দুগ্ধজাত পাউচ",
        "te": "వాక్యూమ్-సీల్డ్ హెవీ-డ్యూటీ డైరీ పౌచ్",
        "ta": "வெற்றிட சீலிடப்பட்ட உறுதியான பால்பொருள் பை",
        "es": "Bolsa láctea de alta resistencia envasada al vacío",
        "fr": "Sachet pour produits laitiers renforcé sous vide",
        "de": "Vakuumversiegelter robuster Molkereibeutel",
        "zh": "高强度真空密封乳品锁鲜袋",
        "ar": "كيس مفرغ من الهواء شديد التحمل لمنتجات الألبان",
        "pt": "Embalagem a vácuo de alta resistência para laticínios",
        "ru": "Высокопрочный вакуумный пакет для молочной продукции",
        "ja": "高耐久性真空密封デイリーパウチ",
        "it": "Busta per latticini ad alta resistenza sottovuoto",
        "tr": "Vakumla kapatılmış dayanıklı süt ürünleri poşeti",
        "ko": "고강도 진공 밀봉 유제품 파우치",
        "nl": "Vacuümverpakte sterke zuivelzak",
        "vi": "Túi hút chân không chuyên dụng chịu lực cho sản phẩm từ sữa",
        "id": "Kantong vakum tugas berat untuk produk susu"
    },
    "meat": {
        "en": "Cold-Seal High-Barrier Meat Tray with Liquid Absorbent Pad",
        "mr": "द्रव शोषक पॅडसह कोल्ड-सील हाय-बॅरियर मांस ट्रे",
        "hi": "तरल शोषक पैड के साथ कोल्ड-सील हाई-बैरियर मीट ट्रे",
        "gu": "પ્રવાહી શોષક પેડ સાથે કોલ્ડ-સીલ હાઇ-બેરિયર મીટ ટ્રે",
        "bn": "তরল শোষক প্যাড সহ কোল্ড-সিল হাই-ব্যারিয়ার মাংসের ট্রে",
        "te": "ద్రవ శోషక ప్యాడ్ తో కూడిన కోల్డ్-సీల్ హై-బారియర్ మీట్ ట్రే",
        "ta": "திரவ உறிஞ்சும் பஞ்சுடன் கூடிய உயர்-தடுப்பு இறைச்சி தட்டு",
        "es": "Bandeja para carne de alta barrera con almohadilla absorbente",
        "fr": "Barquette à viande haute barrière avec buvard absorbant",
        "de": "Hochbarriere-Fleischschale mit Flüssigkeitssauger",
        "zh": "带吸血吸湿垫的高阻隔鲜肉托盘",
        "ar": "صينية لحوم عالية العزل مع وسادة ماصة للسوائل",
        "pt": "Bandeja de alta barreira para carne com almofada absorvente",
        "ru": "Лоток для мяса с высоким барьером и влаговпитывающей салфеткой",
        "ja": "ドリップ吸収パッド付き高バリア生肉用トレイ",
        "it": "Vassoio per carne ad alta barriera con tampone assorbente",
        "tr": "Sıvı emici pedli yüksek bariyerli et tepsisi",
        "ko": "흡수 패드가 포함된 고차단성 신선육 트레이",
        "nl": "Hoogbarrière vleesschaal met vochtabsorberend kussen",
        "vi": "Khay thịt rào cản cao cấp có đệm hút dịch",
        "id": "Baki daging berpenghalang tinggi dengan bantalan penyerap cairan"
    },
    "mango": {
        "en": "Ventilated Bio-Composite Produce Box with Ethylene Ventilation",
        "mr": "इथिलीन वायुवीजनयुक्त इको-कंपोझिट शेतमाल बॉक्स",
        "hi": "एथिलीन वेंटिलेशन के साथ हवादार बायो-कंपोजिट बॉक्स",
        "gu": "ઇથિલીન વેન્ટિલેશન સાથે હવાવાળો બાયો-કમ્પોઝિટ બોક્સ",
        "bn": "ইথিলিন ভেন্টিলেশন সহ বায়ুচলাচলযুক্ত পরিবেশবান্ধব বক্স",
        "te": "ఇథిలీన్ వెంటిలేషన్ తో కూడిన బయో-కంపోజిట్ బాక్స్",
        "ta": "எத்திலீன் காற்றோட்டத்துடன் கூடிய சூழல் நட்பு விளைபொருள் பெட்டி",
        "es": "Caja bio-compuesta ventilada con disipación de etileno",
        "fr": "Caisse bio-composite ventilée avec aération pour l'éthylène",
        "de": "Belüftete Bio-Komposit-Obstkiste mit Ethylenabführung",
        "zh": "乙烯调控型生物基微通风果蔬箱",
        "ar": "صندوق منتجات حيوية مهواة مع تصريف غاز الإيثيلين",
        "pt": "Caixa bio-composta ventilada com exaustão de etileno",
        "ru": "Вентилируемый биокомпозитный короб с отводом этилена",
        "ja": "エチレンガス通気機能付きバイオ複合素材青果ボックス",
        "it": "Scatola bio-composita ventilata con sfiato per etilene",
        "tr": "Etilen havalandırmalı biyo-kompozit ürün kutusu",
        "ko": "에틸렌 배출 환기형 친환경 바이오 복합 농산물 상자",
        "nl": "Geventileerde biocomposiet groentekist met ethyleenafvoer",
        "vi": "Thùng nông sản composite sinh học có van thông khí ethylene",
        "id": "Kotak hasil bumi bio-komposit berventilasi dengan pembuangan etilen"
    },
    "produce": {
        "en": "Micro-Vented Eco-Friendly Moisture-Balanced Bag",
        "mr": "सूक्ष्म-वायुवीजनयुक्त पर्यावरणपूरक आर्द्रता-संतुलित बॅग",
        "hi": "माइक्रो-वेंटेड पर्यावरण-अनुकूल नमी-संतुलित बैग",
        "gu": "માઇક્રો-વેન્ટવાળી ઇકો-ફ્રેન્ડલી ભેજ-સંતુલિત બેગ",
        "bn": "মাইক্রো-ভেন্টিলেটেড পরিবেশবান্ধব আর্দ্রতা-ভারসাম্য ব্যাগ",
        "te": "మైక్రో-వెంటిలేటెడ్ పర్యావరణ అనుకూల తేమ-సమతుల్య బ్యాగ్",
        "ta": "நுண்-காற்றோட்ட சூழல் நட்பு ஈரப்பத சமநிலை பை",
        "es": "Bolsa ecológica microperforada con equilibrio de humedad",
        "fr": "Sachet écologique micro-perforé à régulation d'humidité",
        "de": "Mikrogelochter umweltfreundlicher Feuchtigkeitsausgleichsbeutel",
        "zh": "微孔环保湿气平衡保鲜袋",
        "ar": "كيس صديق للبيئة دقيق التهوية لموازنة الرطوبة",
        "pt": "Saco ecológico microperfurado com equilíbrio de umidade",
        "ru": "Микроперфорированный эко-пакет с контролем влажности",
        "ja": "微細孔付きエコ調湿鮮度保持袋",
        "it": "Sacchetto ecologico microforato a umidità bilanciata",
        "tr": "Mikro delikli çevre dostu nem dengeli torba",
        "ko": "미세 타공 친환경 수분 균형 보존백",
        "nl": "Micro-geventileerde milieuvriendelijke vochtregulerende zak",
        "vi": "Túi vi đục lỗ sinh học cân bằng độ ẩm thân thiện môi trường",
        "id": "Kantong ramah lingkungan berlubang mikro penyeimbang kelembapan"
    }
}

def get_localized_packaging_name(category, default_name="Eco Breathable Punnet", lang="en"):
    """Fetches localized packaging title for Farmer/SME view."""
    cat = category.lower() if category else "produce"
    if "strawberr" in cat or "berry" in cat: key = "strawberry"
    elif "chip" in cat or "namkeen" in cat: key = "chips"
    elif "paneer" in cat or "dairy" in cat: key = "paneer"
    elif "meat" in cat: key = "meat"
    elif "mango" in cat: key = "mango"
    else: key = "produce"
    
    trans_map = FARMER_PACKAGING_NAMES.get(key, FARMER_PACKAGING_NAMES["produce"])
    return trans_map.get(lang, trans_map.get("en", default_name))

