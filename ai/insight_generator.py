"""
PackSense AI - Multilingual Insight & Comparison Table Generator
Generates localized dynamic smart insights and comparison matrices
across all 21 supported global and country languages.
"""

from ai.translations import get_translation

FOOD_NAME_KEYS = {
    "Strawberry": "food_strawberry",
    "Alphonso Mango": "food_mango",
    "Mango": "food_mango",
    "Apple": "food_apple",
    "Tomato": "food_tomato",
    "Potato": "food_potato",
    "Potato Chips": "food_potato_chips",
    "Namkeen": "food_namkeen",
    "Paneer": "food_paneer",
    "Fresh Meat": "food_meat",
    "Meat": "food_meat",
}

COMPARISON_ROWS_META = [
    {
        "id": "param_material",
        "labels": {
            "en": ("Primary Material", "Single-layer unsealed Polyethylene / Flimsy Bag", "High barrier & mechanical integrity"),
            "hi": ("प्राथमिक सामग्री", "एकल-परत बिना सील पॉलीथीन / कमजोर थैली", "उच्च अवरोध और यांत्रिक अखंडता"),
            "mr": ("प्राथमिक साहित्य", "एकल-थर विनासील पॉलिथिन / कमकुवत पिशवी", "उच्च अडथळा आणि यांत्रिक मजबुती"),
            "es": ("Material Primario", "Polietileno monocapa no sellado / Bolsa simple", "Alta barrera e integridad mecánica"),
            "fr": ("Matériau Principal", "Polyéthylène monocouche non scellé / Sachet simple", "Haute barrière et intégrité mécanique"),
            "de": ("Hauptmaterial", "Einlagiges unversiegeltes Polyethylen / Einfacher Beutel", "Hohe Barriere und mechanische Stabilität"),
            "zh": ("主要材料", "单层未封口聚乙烯 / 普通薄袋", "高阻隔性与机械强度"),
            "ar": ("المادة الأساسية", "بولي إيثيلين أحادي الطبقة غير محكم / كيس رقيق", "حاجز عالي ومقاومة ميكانيكية فائقة"),
            "pt": ("Material Principal", "Polietileno monocamada não selado / Saco simples", "Alta barreira e integridade mecânica"),
            "ru": ("Основной материал", "Однослойный незапечатанный полиэтилен / тонкий пакет", "Высокий барьер и механическая прочность"),
            "ja": ("主要素材", "単層未密封ポリエチレン / 簡易包装袋", "高バリア性と機械的保護性"),
            "it": ("Materiale Principale", "Polietilene monostrato non sigillato / Busta semplice", "Alta barriera e integrità meccanica"),
            "tr": ("Birincil Malzeme", "Tek katmanlı mühürsüz polietilen / Dayanıksız torba", "Yüksek bariyer ve mekanik dayanıklılık"),
            "ko": ("주요 포장재", "단층 비밀봉 폴리에틸렌 / 얇은 비닐백", "우수한 차단성 및 기계적 내구성"),
            "nl": ("Belangrijkste Materiaal", "Enkellaags ongezeald polyethyleen / Eenvoudige zak", "Hoge barrière en mechanische integriteit"),
            "vi": ("Vật liệu chính", "Túi Polyethylene đơn lớp chưa ép kín", "Khả năng cản khí và độ bền cơ học cao"),
            "id": ("Material Utama", "Polietilena satu lapis tanpa segel / Kantong tipis", "Integritas mekanik dan penghalang tinggi"),
            "bn": ("প্রধান উপাদান", "একক-স্তর আনসিলড পলিথিন / পাতলা ব্যাগ", "উচ্চ বাধা ও চমৎকার কাঠামোগত শক্তি"),
            "te": ("ప్రధాన పదార్థం", "సింగిల్ లేయర్ సీల్ చేయని పాలిథిన్ బ్యాగ్", "అధిక బారియర్ మరియు నాణ్యమైన పటిష్టత"),
            "ta": ("முதன்மை பொருள்", "ஒற்றை அடுக்கு சீல் செய்யப்படாத பாலித்தீன் பை", "உயர் தடுப்பு மற்றும் இயந்திர உறுதித்தன்மை"),
            "gu": ("મુખ્ય સામગ્રી", "એકલ-સ્તર અનસીલ્ડ પોલીથીન / સામાન્ય થેલી", "ઉચ્ચ અવરોધ અને યાંત્રિક મજબૂતાઈ"),
        }
    },
    {
        "id": "param_gauge",
        "labels": {
            "en": ("Film Thickness (Gauge)", "65 – 80 micron (Non-optimized)", "Down-gauged by {reduc}% plastic reduction"),
            "hi": ("फिल्म की मोटाई (गेज)", "65 – 80 माइक्रोन (गैर-अनुकूलित)", "{reduc}% प्लास्टिक की कमी (डाउन-गेज)"),
            "mr": ("फिल्म जाडी (गेज)", "65 – 80 मायक्रॉन (अनुकूलित नसलेली)", "{reduc}% प्लास्टिक बचत (डाउन-गेज)"),
            "es": ("Espesor del Film (Calibre)", "65 – 80 micrones (No optimizado)", "Reducción de calibre de {reduc}% de plástico"),
            "fr": ("Épaisseur du Film (Jauge)", "65 – 80 microns (Non optimisé)", "Réduction d'épaisseur : {reduc}% de plastique en moins"),
            "de": ("Foliendicke (Stärke)", "65 – 80 Mikrometer (Nicht optimiert)", "Dickenreduktion: {reduc}% weniger Plastik"),
            "zh": ("薄膜厚度（规格）", "65 – 80 微米（未优化）", "薄膜降厚：减少 {reduc}% 塑料用量"),
            "ar": ("سماكة الفيلم", "65 - 80 ميكرون (غير محسن)", "تقليل السماكة بنسبة {reduc}% من البلاستيك"),
            "pt": ("Espessura do Filme", "65 – 80 micrômetros (Não otimizado)", "Redução de espessura de {reduc}% de plástico"),
            "ru": ("Толщина пленки", "65 – 80 микрон (не оптимизировано)", "Уменьшение толщины: -{reduc}% пластика"),
            "ja": ("フィルム厚（ゲージ）", "65 – 80 ミクロン（未最適化）", "薄膜化によりプラスチック使用量 {reduc}% 削減"),
            "it": ("Spessore del Film", "65 – 80 micron (Non ottimizzato)", "Riduzione spessore: -{reduc}% di plastica"),
            "tr": ("Film Kalınlığı", "65 – 80 mikron (Optimize edilmemiş)", "İncelterek %{reduc} plastik tasarrufu"),
            "ko": ("필름 두께", "65 – 80 마이크론 (최적화 전)", "두께 축소로 플라스틱 {reduc}% 절감"),
            "nl": ("Foliedikte", "65 – 80 micron (Niet geoptimaliseerd)", "Diktevermindering: {reduc}% minder plastic"),
            "vi": ("Độ dày màng", "65 – 80 micron (Chưa tối ưu)", "Giảm độ dày: tiết kiệm {reduc}% nhựa"),
            "id": ("Ketebalan Film", "65 – 80 mikron (Tidak optimal)", "Pengurangan ketebalan hemat {reduc}% plastik"),
            "bn": ("ফিল্মের বেধ", "৬৫ – ৮০ মাইক্রন (অনিয়ন্ত্রিত)", "বেধ হ্রাস করে {reduc}% প্লাস্টিক সাশ্রয়"),
            "te": ("ఫిల్మ్ మందం (గేజ్)", "65 – 80 మైక్రాన్లు (ఆప్టిమైజ్ చేయని)", "{reduc}% ప్లాస్టిక్ తగ్గింపు"),
            "ta": ("ஃபிலிம் தடிமன்", "65 – 80 மைக்ரான் (உகப்பாக்கப்படாதது)", "தடிமன் குறைப்பால் {reduc}% பிளாஸ்டிக் சேமிப்பு"),
            "gu": ("ફિલ્મ જાડાઈ (ગેજ)", "65 – 80 માઇક્રોન (બિન-ઓપ્ટિમાઇઝ)", "જાડાઈ ઘટાડીને {reduc}% પ્લાસ્ટિક બચત"),
        }
    },
    {
        "id": "param_otr",
        "labels": {
            "en": ("Oxygen Transmission Rate (OTR)", "3,500 – 6,000 cc/m²/day (Uncalibrated)", "Calibrated to prevent oxidation/suffocation"),
            "hi": ("ऑक्सीजन संचरण दर (OTR)", "3,500 – 6,000 cc/m²/दिन (अनियंत्रित)", "ऑक्सीकरण व घुटन रोकने हेतु कैलिब्रेटेड"),
            "mr": ("ऑक्सिजन ट्रान्समिशन रेट (OTR)", "3,500 – 6,000 cc/m²/दिवस (अनियंत्रित)", "ऑक्सिडेशन व कुजणे रोखण्यासाठी अचूक"),
            "es": ("Tasa de Transmisión de Oxígeno (OTR)", "3.500 – 6.000 cc/m²/día", "Calibrado contra oxidación y asfixia"),
            "fr": ("Perméabilité à l'Oxygène (OTR)", "3 500 – 6 000 cc/m²/jour", "Calibré pour éviter oxydation et étouffement"),
            "de": ("Sauerstoffdurchlässigkeit (OTR)", "3.500 – 6.000 cc/m²/Tag", "Exakt kalibriert gegen Oxidation"),
            "zh": ("氧气透过率 (OTR)", "3,500 – 6,000 cc/m²/天", "精准校准，防止氧化变质或窒息"),
            "ar": ("معدل نقل الأكسجين (OTR)", "3,500 - 6,000 سم³/م²/يوم", "معاير بدقة لمنع الأكسدة أو الاختناق"),
            "pt": ("Taxa de Transmissão de Oxigênio", "3.500 – 6.000 cc/m²/dia", "Calibrado para evitar oxidação"),
            "ru": ("Кислородопроницаемость (OTR)", "3500 – 6000 см³/м²/сутки", "Откалибровано против окисления"),
            "ja": ("酸素透過率 (OTR)", "3,500 – 6,000 cc/m²/日", "酸化や呼吸不全を防ぐ正確な調整"),
            "it": ("Tasso Trasmissione Ossigeno (OTR)", "3.500 – 6.000 cc/m²/giorno", "Calibrato contro ossidazione e deperimento"),
            "tr": ("Oksijen Geçirgenlik Oranı (OTR)", "3.500 – 6.000 cc/m²/gün", "Oksitlenmeyi önlemek için kalibre edildi"),
            "ko": ("산소 투과율 (OTR)", "3,500 – 6,000 cc/m²/일", "산화 및 질식을 방지하도록 정밀 조율"),
            "nl": ("Zuurstoftransmissie (OTR)", "3.500 – 6.000 cc/m²/dag", "Gekalibreerd tegen oxidatie en verstikking"),
            "vi": ("Tốc độ truyền oxy (OTR)", "3.500 – 6.000 cc/m²/ngày", "Được hiệu chuẩn chống oxy hóa hiệu quả"),
            "id": ("Laju Transmisi Oksigen (OTR)", "3.500 – 6.000 cc/m²/hari", "Dikalibrasi untuk mencegah oksidasi"),
            "bn": ("অক্সিজেন সঞ্চালন হার (OTR)", "৩,৫০০ – ৬,০০০ cc/m²/দিন", "অক্সিডেশন ও দমবন্ধ অবস্থা রোধে সমন্বিত"),
            "te": ("ఆక్సిజన్ ట్రాన్స్‌మిషన్ రేట్ (OTR)", "3,500 – 6,000 cc/m²/రోజు", "ఆక్సీకరణను నిరోధించడానికి నిర్ధారించబడింది"),
            "ta": ("ஆக்ஸிஜன் பரிமாற்ற வீதம் (OTR)", "3,500 – 6,000 cc/m²/நாள்", "ஆக்சிஜனேற்றத்தைத் தடுக்க உகந்தது"),
            "gu": ("ઓક્સિજન ટ્રાન્સમિશન રેટ (OTR)", "3,500 – 6,000 cc/m²/દિવસ", "ઓક્સિડેશન અટકાવવા યોગ્ય કેલિબ્રેટ કરેલ"),
        }
    },
    {
        "id": "param_wvtr",
        "labels": {
            "en": ("Water Vapor Transmission (WVTR)", "25 – 45 g/m²/day (Excessive loss/sweat)", "Tightly sealed against ambient moisture"),
            "hi": ("जल वाष्प संचरण दर (WVTR)", "25 – 45 g/m²/दिन (अत्यधिक नमी नुकसान)", "परिवेशी नमी से पूर्ण सुरक्षा"),
            "mr": ("वॉटर व्हेपर ट्रान्समिशन (WVTR)", "25 – 45 g/m²/दिवस (जास्त ओलावा गळती)", "हवेतील आर्द्रतेपासून संपूर्ण संरक्षण"),
            "es": ("Transmisión de Vapor de Agua (WVTR)", "25 – 45 g/m²/día", "Barrera hermética contra humedad ambiental"),
            "fr": ("Perméabilité à la Vapeur d'Eau (WVTR)", "25 – 45 g/m²/jour", "Barrière étanche à l'humidité ambiante"),
            "de": ("Wasserdampfdurchlässigkeit (WVTR)", "25 – 45 g/m²/Tag", "Hervorragender Schutz vor Feuchtigkeit"),
            "zh": ("水蒸气透过率 (WVTR)", "25 – 45 g/m²/天", "严密阻隔外界湿气，防止失水受潮"),
            "ar": ("نقل بخار الماء (WVTR)", "25 - 45 جم/م²/يوم", "حاجز محكم ضد رطوبة الجو المحيط"),
            "pt": ("Transmissão de Vapor de Água (WVTR)", "25 – 45 g/m²/dia", "Proteção estanque contra umidade"),
            "ru": ("Влагопроницаемость (WVTR)", "25 – 45 г/м²/сутки", "Надежный барьер против влажности"),
            "ja": ("水蒸気透過率 (WVTR)", "25 – 45 g/m²/日", "外気湿気から密閉保護し鮮度維持"),
            "it": ("Trasmissione Vapore Acqueo (WVTR)", "25 – 45 g/m²/giorno", "Sigillato contro l'umidità ambientale"),
            "tr": ("Su Buharı Geçirgenliği (WVTR)", "25 – 45 g/m²/gün", "Dış neme karşı yüksek sızdırmazlık"),
            "ko": ("수증기 투과율 (WVTR)", "25 – 45 g/m²/일", "외부 습기를 차단하여 부패 방지"),
            "nl": ("Waterdampdoorlaatbaarheid (WVTR)", "25 – 45 g/m²/dag", "Strakke bescherming tegen luchtvochtigheid"),
            "vi": ("Tốc độ truyền hơi nước (WVTR)", "25 – 45 g/m²/ngày", "Bảo vệ kín chống ẩm môi trường"),
            "id": ("Transmisi Uap Air (WVTR)", "25 – 45 g/m²/hari", "Penghalang rapat terhadap kelembapan udara"),
            "bn": ("জলীয় বাষ্প সঞ্চালন হার (WVTR)", "২৫ – ৪৫ g/m²/দিন", "পরিবেশের আর্দ্রতা থেকে সুরক্ষিত"),
            "te": ("నీటి ఆవిరి ప్రసార రేటు (WVTR)", "25 – 45 g/m²/రోజు", "తేమ నుంచి పూర్తి రక్షణ"),
            "ta": ("நீராவி பரிமாற்ற வீதம் (WVTR)", "25 – 45 g/m²/நாள்", "சுற்றுப்புற ஈரப்பதத்திலிருந்து பாதுகாப்பு"),
            "gu": ("વોટર વેપર ટ્રાન્સમિશન (WVTR)", "25 – 45 g/m²/દિવસ", "વાતાવરણના ભેજ સામે ઉત્તમ સુરક્ષા"),
        }
    },
    {
        "id": "param_shelflife",
        "labels": {
            "en": ("Shelf Life at Destination", "{orig} Days", "+{pct}% freshness longevity"),
            "hi": ("गंतव्य पर शेल्फ लाइफ", "{orig} दिन", "+{pct}% ताजगी और शेल्फ लाइफ विस्तार"),
            "mr": ("गंतव्यस्थानी टिकवण क्षमता (Shelf Life)", "{orig} दिवस", "+{pct}% जास्त टिकवण क्षमता"),
            "es": ("Vida Útil en Destino", "{orig} Días", "+{pct}% mayor frescura y duración"),
            "fr": ("Durée de Conservation", "{orig} Jours", "+{pct}% de longévité et fraîcheur"),
            "de": ("Haltbarkeit am Zielort", "{orig} Tage", "+{pct}% längere Frische"),
            "zh": ("到达目的地保质期", "{orig} 天", "+{pct}% 新鲜保质期延长"),
            "ar": ("فترة الصلاحية في الوجهة", "{orig} أيام", "+{pct}% زيادة في نضارة المنتج"),
            "pt": ("Vida Útil no Destino", "{orig} Dias", "+{pct}% extensão de frescor"),
            "ru": ("Срок годности в пункте назначения", "{orig} дн.", "+{pct}% сохранение свежести"),
            "ja": ("目的地での賞味期限", "{orig} 日間", "+{pct}% 鮮度保持期間の延長"),
            "it": ("Durata a Destinazione", "{orig} Giorni", "+{pct}% estensione della freschezza"),
            "tr": ("Varış Noktasında Raf Ömrü", "{orig} Gün", "+%{pct} daha uzun tazelik"),
            "ko": ("도착지 유통기한", "{orig} 일", "+{pct}% 신선도 보존 연장"),
            "nl": ("Houdbaarheid op Bestemming", "{orig} Dagen", "+{pct}% langere versheid"),
            "vi": ("Hạn sử dụng tại điểm đến", "{orig} Ngày", "Tăng thêm +{pct}% độ tươi ngon"),
            "id": ("Masa Simpan di Tujuan", "{orig} Hari", "+{pct}% kesegaran lebih lama"),
            "bn": ("গন্তব্যে সংরক্ষণ মেয়াদ", "{orig} দিন", "+{pct}% সতেজতা ও স্থায়িত্ব বৃদ্ধি"),
            "te": ("గమ్యస్థానంలో నిల్వకాలం", "{orig} రోజులు", "+{pct}% ఎక్కువ తాజాదనం"),
            "ta": ("சேருமிடத்தில் அடுக்கு ஆயுள்", "{orig} நாட்கள்", "+{pct}% கூடுதல் புத்துணர்ச்சி"),
            "gu": ("ગંતવ્ય સ્થળે શેલ્ફ-લાઇફ", "{orig} દિવસ", "+{pct}% વધુ સમય તાજગી"),
        }
    }
]


def generate_localized_smart_insight(food_name, origin, destination, season, clim_stress, avg_rh, humidity_mult, optimized_gauge, plastic_reduc, shelf_extension_pct, spoilage_mechanism, lang="en"):
    """Generates natural language dynamic insight for all 21 languages."""
    if not lang or lang not in ["en", "hi", "mr", "es", "fr", "de", "zh", "ar", "pt", "ru", "ja", "it", "tr", "ko", "nl", "vi", "id", "bn", "te", "ta", "gu"]:
        lang = "en"
    
    gauge_num = optimized_gauge.split(' ')[0] if ' ' in optimized_gauge else optimized_gauge
    food_trans = get_translation(FOOD_NAME_KEYS.get(food_name, "food_other"), lang)

    # 1. Marathi
    if lang == "mr":
        if clim_stress >= 75:
            climate_note = f"{origin} ते {destination} दरम्यानच्या वाहतूक मार्गावर तीव्र हवामान ताण ({avg_rh}% सापेक्ष आर्द्रता, {season}) असल्याने, महामार्गावरील वाहतुकीदरम्यान मालाचे नुकसान टाळण्यासाठी ओलावा अडथळा {int((1.0 - humidity_mult)*100)}% ने अधिक मजबूत करण्यात आला आहे."
        else:
            climate_note = f"{origin} ते {destination} दरम्यानचा वाहतूक मार्ग सामान्य असल्याने, बॅरियर सुरक्षेशिवाय प्लास्टिकची जाडी लक्षणीयरीत्या कमी करता आली आहे."
        return (
            f"पॅकसेन्स एआयने {food_trans} साठी त्याच्या मुख्य विघटन प्रक्रियेवर आधारित ही शिफारस तयार केली आहे. "
            f"{climate_note} "
            f"फिल्मची जाडी {gauge_num} मायक्रॉनपर्यंत ऑप्टिमाइझ करून, तुमचे पॅकेजिंग प्लास्टिकचा वापर {plastic_reduc}% कमी करते आणि उत्पादनाची टिकवण क्षमता {shelf_extension_pct}% वाढवते."
        )

    # 2. Hindi
    if lang == "hi":
        if clim_stress >= 75:
            climate_note = f"क्योंकि {origin} से {destination} के बीच लॉजिस्टिक्स मार्ग अत्यधिक जलवायु तनाव ({avg_rh}% सापेक्ष आर्द्रता, {season}) का सामना करता है, इसलिए हाईवे ट्रांजिट के दौरान खराबी रोकने के लिए नमी अवरोध को {int((1.0 - humidity_mult)*100)}% सख्त किया गया है।"
        else:
            climate_note = f"{origin} से {destination} का ट्रांजिट मार्ग सामान्य परिवेश बनाए रखता है, जिससे बिना बैरियर जोखिम के सामग्री की मोटाई में भारी कमी संभव हुई है।"
        return (
            f"पाकसेंस एआई ने {food_trans} के प्राथमिक अपघटन तंत्र के आधार पर यह सिफारिश तैयार की है। "
            f"{climate_note} "
            f"फिल्म की मोटाई को {gauge_num} माइक्रोन तक अनुकूलित करके, आपकी पैकेजिंग प्लास्टिक खपत को {plastic_reduc}% कम करती है और शेल्फ लाइफ में {shelf_extension_pct}% का विस्तार करती है।"
        )

    # 3. Gujarati
    if lang == "gu":
        if clim_stress >= 75:
            climate_note = f"{origin} થી {destination} વચ્ચેના પરિવહન માર્ગ પર તીવ્ર વાતાવરણીય તાણ ({avg_rh}% સાપેક્ષ ભેજ, {season}) હોવાથી, હાઇવે પરિવહન દરમિયાન બગાડ અટકાવવા ભેજ અવરોધને {int((1.0 - humidity_mult)*100)}% વધુ મજબૂત બનાવવામાં આવ્યો છે."
        else:
            climate_note = f"{origin} થી {destination} વચ્ચેનો પરિવહન માર્ગ અનુકૂળ હોવાથી, બેરિયર જોખમ વિના પ્લાસ્ટિકની જાડાઈ નોંધપાત્ર રીતે ઘટાડી શકાઈ છે."
        return (
            f"પેકસેન્સ એઆઈએ {food_trans} માટે તેની પ્રાથમિક બગાડ પ્રક્રિયા પર આધારિત આ ભલામણ તૈયાર કરી છે. "
            f"{climate_note} "
            f"ફિલ્મની જાડાઈ {gauge_num} માઇક્રોન સુધી ઓપ્ટિમાઇઝ કરીને, તમારું પેકેજિંગ પ્લાસ્ટિક વપરાશ {plastic_reduc}% ઘટાડે છે અને ટકાઉપણું {shelf_extension_pct}% વધારે છે."
        )

    # 4. Bengali
    if lang == "bn":
        if clim_stress >= 75:
            climate_note = f"যেহেতু {origin} থেকে {destination} ট্রানজিট রুটে তীব্র আর্দ্রতা ও জলবায়ু চাপ ({avg_rh}% আর্দ্রতা, {season}) বিদ্যমান, তাই ট্রানজিট চলাকালীন পচন রোধ করতে আর্দ্রতা বাধা {int((1.0 - humidity_mult)*100)}% জোরদার করা হয়েছে।"
        else:
            climate_note = f"{origin} থেকে {destination} ট্রানজিট রুট তুলনামূলকভাবে স্থিতিশীল পরিবেশ বজায় রাখে, যা উপাদানের বেধ কার্যকরভাবে কমাতে সাহায্য করে।"
        return (
            f"প্যাকসেন্স এআই {food_trans}-এর প্রাথমিক পচন বৈশিষ্ট্যের ওপর ভিত্তি করে এই সুপারিশ তৈরি করেছে। "
            f"{climate_note} "
            f"ফিল্মের বেধ {gauge_num} মাইক্রনে অপ্টিমাইজ করে, প্যাকেজিং প্লাস্টিকের ব্যবহার {plastic_reduc}% হ্রাস করে এবং শেল্ফ লাইফ {shelf_extension_pct}% বৃদ্ধি করে।"
        )

    # 5. Telugu
    if lang == "te":
        if clim_stress >= 75:
            climate_note = f"{origin} నుండి {destination} వరకు రవాణా మార్గంలో తీవ్రమైన వాతావరణ ఒత్తిడి ({avg_rh}% తేమ, {season}) ఉన్నందున, రవాణా సమయంలో నష్టాన్ని నివారించడానికి తేమ అవరోధం {int((1.0 - humidity_mult)*100)}% పెంచబడింది."
        else:
            climate_note = f"{origin} నుండి {destination} మార్గంలో సాధారణ వాతావరణం ఉన్నందున ప్లాస్టిక్ మందాన్ని గణనీయంగా తగ్గించడం సాధ్యమైంది."
        return (
            f"ప్యాక్‌సెన్స్ ఏఐ {food_trans} ఆహార క్షీణత ఆధారంగా ఈ ఖచ్చితమైన సిఫార్సును రూపొందించింది. "
            f"{climate_note} "
            f"ఫిల్మ్ మందాన్ని {gauge_num} మైక్రాన్లకు ఆప్టిమైజ్ చేయడం ద్వారా, ప్లాస్టిక్ వినియోగాన్ని {plastic_reduc}% తగ్గిస్తూ, నిల్వకాలాన్ని {shelf_extension_pct}% పెంచుతుంది."
        )

    # 6. Tamil
    if lang == "ta":
        if clim_stress >= 75:
            climate_note = f"{origin} முதல் {destination} வரையிலான போக்குவரத்து பாதையில் கடுமையான காலநிலை அழுத்தம் ({avg_rh}% ஈரப்பதம், {season}) நிலவுவதால், கெட்டுப்போவதைத் தடுக்க ஈரப்பதத் தடுப்பு {int((1.0 - humidity_mult)*100)}% வலுப்படுத்தப்பட்டுள்ளது."
        else:
            climate_note = f"{origin} முதல் {destination} போக்குவரத்து பாதை மிதமான சூழலைக் கொண்டிருப்பதால் ஃபிலிம் தடிமனை எளிதாகக் குறைக்க முடிகிறது."
        return (
            f"பேக்சென்ஸ் ஏஐ {food_trans} உணவின் கெட்டுப்போகும் தன்மைக்கு ஏற்ப இந்த உகந்த பரிந்துரையை வடிவமைத்துள்ளது. "
            f"{climate_note} "
            f"ஃபிலிம் தடிமனை {gauge_num} மைக்ரான்களாக உகப்பாக்குவதன் மூலம், பிளாஸ்டிக் பயன்பாட்டை {plastic_reduc}% குறைத்து, ஆயுளை {shelf_extension_pct}% நீட்டிக்கிறது."
        )

    # 7. Spanish
    if lang == "es":
        if clim_stress >= 75:
            climate_note = f"Dado que el corredor logístico de {origin} a {destination} experimenta un severo estrés climático ({avg_rh}% HR, {season}), la barrera contra la humedad se ajustó dinámicamente un {int((1.0 - humidity_mult)*100)}% para evitar el deterioro durante el tránsito."
        else:
            climate_note = f"La ruta de tránsito de {origin} a {destination} mantiene perfiles ambientales moderados, lo que permite una reducción significativa del calibre sin riesgo de fallo de barrera."
        return (
            f"PackSense AI calibró esta recomendación para {food_trans} en función de su mecanismo primario de degradación. "
            f"{climate_note} "
            f"Al optimizar el espesor del film a {gauge_num} micrones, su empaque reduce el plástico en un {plastic_reduc}% y prolonga la vida útil en un {shelf_extension_pct}%."
        )

    # 8. French
    if lang == "fr":
        if clim_stress >= 75:
            climate_note = f"Étant donné que le corridor de {origin} à {destination} subit un stress climatique intense ({avg_rh}% HR, {season}), la barrière contre l'humidité a été renforcée de {int((1.0 - humidity_mult)*100)}% pour éviter toute dégradation en transit."
        else:
            climate_note = f"Le trajet de {origin} à {destination} bénéficie de conditions modérées, permettant une réduction sensible de l'épaisseur sans risque de rupture."
        return (
            f"PackSense AI a calibré cette recommandation pour {food_trans} selon son mécanisme principal de dégradation. "
            f"{climate_note} "
            f"En optimisant l'épaisseur du film à {gauge_num} microns, votre emballage réduit le plastique de {plastic_reduc}% tout en prolongeant la fraîcheur de {shelf_extension_pct}%."
        )

    # 9. German
    if lang == "de":
        if clim_stress >= 75:
            climate_note = f"Da die Route von {origin} nach {destination} extremen Klimabelastungen ausgesetzt ist ({avg_rh}% rF, {season}), wurde die Feuchtigkeitsbarriere um {int((1.0 - humidity_mult)*100)}% verstärkt, um vorzeitigem Verderb auf der Autobahn vorzubeugen."
        else:
            climate_note = f"Der Transitkorridor von {origin} nach {destination} weist moderate Umweltbedingungen auf, was eine gezielte Materialeinsparung ermöglicht."
        return (
            f"PackSense KI hat diese Empfehlung für {food_trans} basierend auf dem primären Verderbsmechanismus optimiert. "
            f"{climate_note} "
            f"Durch die Verringerung der Foliendicke auf {gauge_num} Mikrometer senkt Ihre Verpackung den Plastikverbrauch um {plastic_reduc}% bei einer Verlängerung der Haltbarkeit um {shelf_extension_pct}%."
        )

    # 10. Chinese
    if lang == "zh":
        if clim_stress >= 75:
            climate_note = f"由于从 {origin} 到 {destination} 的物流通道面临严峻的气候压力（相对湿度 {avg_rh}%，{season}），阻湿屏障已动态增强 {int((1.0 - humidity_mult)*100)}%，以防止公路运输期间发生霉变变质。"
        else:
            climate_note = f"从 {origin} 到 {destination} 的运输走廊环境温和，可在确保屏障安全的前提下显著降低材料厚度。"
        return (
            f"PackSense AI 根据 {food_trans} 的主要腐败变质机理精准定制了本包装方案。 "
            f"{climate_note} "
            f"通过将薄膜厚度优化至 {gauge_num} 微米，包装塑料使用量减少了 {plastic_reduc}%，同时将货架保质期延长了 {shelf_extension_pct}%。"
        )

    # 11. Arabic
    if lang == "ar":
        if clim_stress >= 75:
            climate_note = f"نظراً لأن مسار النقل من {origin} إلى {destination} يتعرض لإجهاد مناخي شديد ({avg_rh}% رطوبة نسبية، {season})، فقد تم تعزيز حاجز الرطوبة بنسبة {int((1.0 - humidity_mult)*100)}% لمنع التلف أثناء النقل."
        else:
            climate_note = f"يحافظ مسار النقل من {origin} إلى {destination} على ظروف مناخية معتدلة، مما يسمح بتقليل سماكة المواد دون المساس بالحماية."
        return (
            f"قام PackSense AI بضبط هذه التوصية لـ {food_trans} بناءً على آلية التلف الأساسية. "
            f"{climate_note} "
            f"من خلال تحسين سماكة الفيلم إلى {gauge_num} ميكرون، تستهلك عبوتك بلاستيكاً أقل بنسبة {plastic_reduc}% مع زيادة فترة الصلاحية بنسبة {shelf_extension_pct}%."
        )

    # 12. Portuguese
    if lang == "pt":
        if clim_stress >= 75:
            climate_note = f"Como o corredor logístico de {origin} até {destination} sofre severo estresse climático ({avg_rh}% UR, {season}), a barreira contra umidade foi reforçada em {int((1.0 - humidity_mult)*100)}% para evitar perdas no trajeto."
        else:
            climate_note = f"O trajeto de {origin} para {destination} mantém condições moderadas, possibilitando reduzir a espessura sem risco de quebra de barreira."
        return (
            f"O PackSense AI calibrou esta recomendação para {food_trans} com base no seu principal mecanismo de deterioração. "
            f"{climate_note} "
            f"Ao otimizar a espessura para {gauge_num} micrômetros, sua embalagem reduz {plastic_reduc}% do plástico e estende a validade em {shelf_extension_pct}%."
        )

    # 13. Russian
    if lang == "ru":
        if clim_stress >= 75:
            climate_note = f"Поскольку маршрут из {origin} в {destination} подвержен сильному климатическому стрессу ({avg_rh}% влажности, {season}), влагобарьер усилен на {int((1.0 - humidity_mult)*100)}% для защиты от порчи в пути."
        else:
            climate_note = f"Маршрут из {origin} в {destination} отличается умеренными условиями, что позволяет снизить толщину пленки без потери барьерных свойств."
        return (
            f"PackSense ИИ рассчитал эту рекомендацию для {food_trans} с учетом ключевых биохимических факторов порчи. "
            f"{climate_note} "
            f"Оптимизация толщины пленки до {gauge_num} микрон снижает расход пластика на {plastic_reduc}% и продлевает срок годности на {shelf_extension_pct}%."
        )

    # 14. Japanese
    if lang == "ja":
        if clim_stress >= 75:
            climate_note = f"{origin} から {destination} への輸送ルートは厳しい気候負荷（湿度 {avg_rh}%、{season}）にさらされるため、輸送中の腐敗を防ぐため防湿性能を {int((1.0 - humidity_mult)*100)}% 強化しました。"
        else:
            climate_note = f"{origin} から {destination} のルートは比較的安定した環境であるため、強度を維持しながら大幅な薄肉化が可能です。"
        return (
            f"PackSense AI は {food_trans} の品質劣化要因に基づいてこの推奨仕様を精密に算出しました。 "
            f"{climate_note} "
            f"フィルム厚を {gauge_num} ミクロンに最適化することで、プラスチック使用量を {plastic_reduc}% 削減し、賞味期限を {shelf_extension_pct}% 延長します。"
        )

    # 15. Italian
    if lang == "it":
        if clim_stress >= 75:
            climate_note = f"Poiché la rotta da {origin} a {destination} presenta elevato stress climatico ({avg_rh}% UR, {season}), la barriera anti-umidità è stata rinforzata del {int((1.0 - humidity_mult)*100)}%."
        else:
            climate_note = f"Il tragitto da {origin} a {destination} gode di condizioni miti, consentendo una decisa riduzione dello spessore del film."
        return (
            f"PackSense AI ha calibrato questa raccomandazione per {food_trans} sul suo profilo biologico. "
            f"{climate_note} "
            f"Portando lo spessore a {gauge_num} micron, si riduce la plastica del {plastic_reduc}% estendendo la conservazione del {shelf_extension_pct}%."
        )

    # 16. Turkish
    if lang == "tr":
        if clim_stress >= 75:
            climate_note = f"{origin} ile {destination} arasındaki taşıma hattı yüksek iklim stresi (%{avg_rh} bağıl nem, {season}) altında olduğundan, bozulmayı önlemek için nem bariyeri %{int((1.0 - humidity_mult)*100)} güçlendirildi."
        else:
            climate_note = f"{origin} - {destination} hattı ılıman koşullara sahip olduğundan film kalınlığı güvenle azaltılabilmiştir."
        return (
            f"PackSense AI, {food_trans} için bozulma dinamiklerini dikkate alarak bu öneriyi hazırladı. "
            f"{climate_note} "
            f"Film kalınlığını {gauge_num} mikrona optimize ederek plastik kullanımını %{plastic_reduc} azaltır ve tazeliği %{shelf_extension_pct} uzatır."
        )

    # 17. Korean
    if lang == "ko":
        if clim_stress >= 75:
            climate_note = f"{origin}에서 {destination}까지의 운송 구간은 높은 기후 스트레스(상대습도 {avg_rh}%, {season})가 발생하므로 수분 차단성을 {int((1.0 - humidity_mult)*100)}% 강화했습니다."
        else:
            climate_note = f"{origin}에서 {destination} 구간은 온화하여 품질 저하 없이 필름 두께를 경량화할 수 있습니다."
        return (
            f"PackSense AI는 {food_trans}의 고유한 부패 메커니즘을 고려하여 최적 포장 사양을 설계했습니다. "
            f"{climate_note} "
            f"필름 두께를 {gauge_num} 마이크론으로 최적화함으로써 플라스틱 사용량을 {plastic_reduc}% 절감하고 유통기한을 {shelf_extension_pct}% 연장합니다."
        )

    # 18. Dutch
    if lang == "nl":
        if clim_stress >= 75:
            climate_note = f"Omdat de route van {origin} naar {destination} te maken heeft met hoge klimaatstress ({avg_rh}% RV, {season}), is de vochtbarrière met {int((1.0 - humidity_mult)*100)}% aangescherpt."
        else:
            climate_note = f"Het transitnetwerk tussen {origin} en {destination} heeft milde condities, waardoor het materiaal veilig dunner gemaakt kan worden."
        return (
            f"PackSense AI heeft deze aanbeveling berekend voor {food_trans} op basis van biochemische bederffactoren. "
            f"{climate_note} "
            f"Door de foliedikte te optimaliseren naar {gauge_num} micron vermindert u plastic met {plastic_reduc}% en verlengt u de versheid met {shelf_extension_pct}%."
        )

    # 19. Vietnamese
    if lang == "vi":
        if clim_stress >= 75:
            climate_note = f"Do hành lang vận chuyển từ {origin} đến {destination} chịu áp lực thời tiết lớn ({avg_rh}% độ ẩm, {season}), lớp chắn ẩm đã được tăng cường thêm {int((1.0 - humidity_mult)*100)}% để chống úng thối."
        else:
            climate_note = f"Tuyến đường từ {origin} đến {destination} có điều kiện ổn định, cho phép giảm đáng kể độ dày màng bao bì."
        return (
            f"PackSense AI đã tối ưu hóa đề xuất này cho {food_trans} theo đặc tính hư hỏng sinh học. "
            f"{climate_note} "
            f"Bằng việc tối ưu độ dày màng còn {gauge_num} micron, bao bì tiết kiệm {plastic_reduc}% nhựa và kéo dài độ tươi ngon thêm {shelf_extension_pct}%."
        )

    # 20. Indonesian
    if lang == "id":
        if clim_stress >= 75:
            climate_note = f"Karena koridor logistik dari {origin} ke {destination} mengalami tekanan iklim tinggi ({avg_rh}% RH, {season}), pelindung kelembapan diperketat {int((1.0 - humidity_mult)*100)}% untuk mencegah kebusukan."
        else:
            climate_note = f"Jalur pengiriman dari {origin} ke {destination} beriklim sedang, memungkinkan pengurangan ketebalan bahan secara aman."
        return (
            f"PackSense AI mengkalibrasi rekomendasi ini untuk {food_trans} berdasarkan karakteristik degradasi alaminya. "
            f"{climate_note} "
            f"Dengan mengoptimalkan ketebalan film ke {gauge_num} mikron, kemasan menghemat {plastic_reduc}% plastik dan memperpanjang masa simpan {shelf_extension_pct}%."
        )

    # 21. Default: English
    if clim_stress >= 75:
        climate_note = f"Because the logistics corridor from {origin} to {destination} experiences severe climatic stress ({avg_rh}% RH, {season}), the moisture barrier was dynamically tightened by {int((1.0 - humidity_mult)*100)}% to prevent premature rotting during highway transit."
    else:
        climate_note = f"The transit corridor from {origin} to {destination} maintains moderate ambient profiles, enabling significant material down-gauging without risk of barrier failure."

    return (
        f"PackSense AI calibrated this recommendation for {food_name} based on its primary decay mechanism ({spoilage_mechanism}). "
        f"{climate_note} "
        f"By optimizing film thickness down to {gauge_num} microns, your packaging reduces plastic usage by {plastic_reduc}% while delivering a {shelf_extension_pct}% shelf-life extension."
    )


def generate_localized_comparison_table(primary_material, optimized_gauge, calibrated_otr, calibrated_wvtr, orig_shelf, shelf_ext_days, shelf_extension_pct, unit_cost, sust_rating, carbon_impact, destination, season, plastic_reduc, lang="en"):
    """Generates localized rows for the Current vs Recommended comparison table."""
    if not lang:
        lang = "en"

    table = []
    for row_meta in COMPARISON_ROWS_META:
        labels = row_meta["labels"].get(lang, row_meta["labels"].get("en"))
        param_title, curr_desc, imp_desc = labels

        if row_meta["id"] == "param_material":
            rec_val = primary_material.split("+")[0].strip()
        elif row_meta["id"] == "param_gauge":
            rec_val = optimized_gauge
            imp_desc = imp_desc.replace("{reduc}", str(plastic_reduc))
        elif row_meta["id"] == "param_otr":
            rec_val = f"{calibrated_otr} cc/m²/day"
        elif row_meta["id"] == "param_wvtr":
            rec_val = f"{calibrated_wvtr} g/m²/day"
        elif row_meta["id"] == "param_shelflife":
            curr_desc = curr_desc.replace("{orig}", str(orig_shelf))
            rec_val = f"{shelf_ext_days} " + ("Days" if lang == "en" else "d")
            imp_desc = imp_desc.replace("{pct}", str(shelf_extension_pct))
        else:
            rec_val = "Optimized"

        table.append({
            "parameter": param_title,
            "current": curr_desc,
            "recommended": rec_val,
            "improvement": imp_desc
        })

    # Unit cost row
    cost_labels = {
        "en": ("Estimated Unit Packaging Cost", "₹0.90 / unit", f"₹{unit_cost:.2f} / unit", "High ROI through massive food waste elimination"),
        "hi": ("अनुमानित पैकेजिंग लागत", "₹0.90 / इकाई", f"₹{unit_cost:.2f} / इकाई", "खाद्य अपव्यय रोकने से उच्च बचत"),
        "mr": ("अंदाजे पॅकेजिंग खर्च", "₹0.90 / नग", f"₹{unit_cost:.2f} / नग", "अन्नाची नासाडी टळून प्रचंड नफा"),
        "es": ("Coste Unitario Estimado", "₹0.90 / unidad", f"₹{unit_cost:.2f} / unidad", "Alto ROI por reducción de desperdicio"),
        "fr": ("Coût Unitaire Estimé", "₹0.90 / unité", f"₹{unit_cost:.2f} / unité", "Retour sur investissement élevé"),
        "de": ("Geschätzte Stückkosten", "₹0.90 / Stück", f"₹{unit_cost:.2f} / Stück", "Hohe Rentabilität durch weniger Verderb"),
        "zh": ("预估单件包装成本", "₹0.90 / 件", f"₹{unit_cost:.2f} / 件", "大幅减少食物浪费，投资回报率极高"),
        "ar": ("تكلفة العبوة المقدرة", "₹0.90 / وحدة", f"₹{unit_cost:.2f} / وحدة", "عائد استثماري مرتفع عبر منع الهدر"),
        "pt": ("Custo Unitário Estimado", "₹0.90 / unid.", f"₹{unit_cost:.2f} / unid.", "Alto retorno pela eliminação do desperdício"),
        "ru": ("Расчетная стоимость единицы", "₹0.90 / шт.", f"₹{unit_cost:.2f} / шт.", "Высокая окупаемость за счет снижения отходов"),
        "ja": ("推定ユニット包装コスト", "₹0.90 / 個", f"₹{unit_cost:.2f} / 個", "食品廃棄削減による高い投資回収効果"),
        "it": ("Costo Unitario Stimato", "₹0.90 / pezzo", f"₹{unit_cost:.2f} / pezzo", "Alto ROI eliminando gli sprechi alimentari"),
        "tr": ("Tahmini Birim Paket Maliyeti", "₹0.90 / adet", f"₹{unit_cost:.2f} / adet", "Gıda israfını önleyerek yüksek getiri"),
        "ko": ("예상 단위 포장 비용", "₹0.90 / 개", f"₹{unit_cost:.2f} / 개", "식품 폐기 감소로 높은 투자수익률"),
        "nl": ("Geschatte Stukkosten", "₹0.90 / eenheid", f"₹{unit_cost:.2f} / eenheid", "Hoge ROI door minder voedselverspilling"),
        "vi": ("Chi phí bao bì ước tính", "₹0.90 / đơn vị", f"₹{unit_cost:.2f} / đơn vị", "Hiệu quả đầu tư cao nhờ giảm hư hỏng"),
        "id": ("Estimasi Biaya Satuan", "₹0.90 / unit", f"₹{unit_cost:.2f} / unit", "ROI tinggi melalui pencegahan limbah pangan"),
        "bn": ("আনুমানিক প্যাকেজিং খরচ", "₹০.৯০ / ইউনিট", f"₹{unit_cost:.2f} / ইউনিট", "খাদ্য অপচয় রোধের মাধ্যমে উচ্চ মুনাফা"),
        "te": ("అంచనా యూనిట్ ప్యాకేజింగ్ ఖర్చు", "₹0.90 / యూనిట్", f"₹{unit_cost:.2f} / యూనిట్", "వ్యర్థాలు తగ్గి అధిక లాభం"),
        "ta": ("மதிப்பிடப்பட்ட பேக்கேஜிங் செலவு", "₹0.90 / அலகு", f"₹{unit_cost:.2f} / அலகு", "உணவு வீணாவதைத் தடுத்து அதிக லாபம்"),
        "gu": ("અંદાજિત પેકેજિંગ ખર્ચ", "₹0.90 / નંગ", f"₹{unit_cost:.2f} / નંગ", "ખોરાકનો બગાડ અટકાવી ઉત્તમ વળતર"),
    }
    c_labels = cost_labels.get(lang, cost_labels["en"])
    table.append({
        "parameter": c_labels[0],
        "current": c_labels[1],
        "recommended": c_labels[2],
        "improvement": c_labels[3]
    })

    # Sustainability Eco-Score row
    sust_labels = {
        "en": ("Sustainability Eco-Score", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "hi": ("पर्यावरणीय स्थिरता स्कोर", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "mr": ("पर्यावरण स्थिरता स्कोअर", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "es": ("Puntaje de Sostenibilidad", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "fr": ("Score d'Éco-durabilité", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "de": ("Nachhaltigkeits-Ökoscore", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "zh": ("绿色环保与可持续评分", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "ar": ("معدل الاستدامة البيئية", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "pt": ("Pontuação de Sustentabilidade", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "ru": ("Экологический рейтинг", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "ja": ("環境サステナビリティ評価", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "it": ("Punteggio di Sostenibilità", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "tr": ("Sürdürülebilirlik Puanı", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "ko": ("친환경 지속가능성 지수", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "nl": ("Duurzaamheidsscore", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "vi": ("Điểm bền vững môi trường", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "id": ("Skor Keberlanjutan", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "bn": ("পরিবেশগত স্থায়িত্ব স্কোর", "৩.৫ / ১০", f"{sust_rating} / 10", carbon_impact),
        "te": ("పర్యావరణ అనుకూలత స్కోరు", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "ta": ("சுற்றுச்சூழல் நிலைத்தன்மை மதிப்பீடு", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
        "gu": ("પર્યાવરણીય સ્થિરતા સ્કોર", "3.5 / 10", f"{sust_rating} / 10", carbon_impact),
    }
    s_labels = sust_labels.get(lang, sust_labels["en"])
    table.append({
        "parameter": s_labels[0],
        "current": s_labels[1],
        "recommended": s_labels[2],
        "improvement": s_labels[3]
    })

    return table
