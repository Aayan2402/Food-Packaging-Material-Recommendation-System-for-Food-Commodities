# build_translations.py
# Generates ai/translations.py containing all 21 major global and country languages
import json

SUPPORTED_LANGUAGES = {
    "en": {"code": "en", "name": "English", "native": "English", "country": "GB", "flag": "🇬🇧", "dir": "ltr"},
    "hi": {"code": "hi", "name": "Hindi", "native": "हिंदी", "country": "IN", "flag": "🇮🇳", "dir": "ltr"},
    "mr": {"code": "mr", "name": "Marathi", "native": "मराठी", "country": "IN", "flag": "🇮🇳", "dir": "ltr"},
    "es": {"code": "es", "name": "Spanish", "native": "Español", "country": "ES", "flag": "🇪🇸", "dir": "ltr"},
    "fr": {"code": "fr", "name": "French", "native": "Français", "country": "FR", "flag": "🇫🇷", "dir": "ltr"},
    "de": {"code": "de", "name": "German", "native": "Deutsch", "country": "DE", "flag": "🇩🇪", "dir": "ltr"},
    "zh": {"code": "zh", "name": "Chinese", "native": "中文", "country": "CN", "flag": "🇨🇳", "dir": "ltr"},
    "ar": {"code": "ar", "name": "Arabic", "native": "العربية", "country": "SA", "flag": "🇸🇦", "dir": "rtl"},
    "pt": {"code": "pt", "name": "Portuguese", "native": "Português", "country": "BR", "flag": "🇧🇷", "dir": "ltr"},
    "ru": {"code": "ru", "name": "Russian", "native": "Русский", "country": "RU", "flag": "🇷🇺", "dir": "ltr"},
    "ja": {"code": "ja", "name": "Japanese", "native": "日本語", "country": "JP", "flag": "🇯🇵", "dir": "ltr"},
    "it": {"code": "it", "name": "Italian", "native": "Italiano", "country": "IT", "flag": "🇮🇹", "dir": "ltr"},
    "tr": {"code": "tr", "name": "Turkish", "native": "Türkçe", "country": "TR", "flag": "🇹🇷", "dir": "ltr"},
    "ko": {"code": "ko", "name": "Korean", "native": "한국어", "country": "KR", "flag": "🇰🇷", "dir": "ltr"},
    "nl": {"code": "nl", "name": "Dutch", "native": "Nederlands", "country": "NL", "flag": "🇳🇱", "dir": "ltr"},
    "vi": {"code": "vi", "name": "Vietnamese", "native": "Tiếng Việt", "country": "VN", "flag": "🇻🇳", "dir": "ltr"},
    "id": {"code": "id", "name": "Indonesian", "native": "Bahasa Indonesia", "country": "ID", "flag": "🇮🇩", "dir": "ltr"},
    "bn": {"code": "bn", "name": "Bengali", "native": "বাংলা", "country": "IN/BD", "flag": "🇧🇩", "dir": "ltr"},
    "te": {"code": "te", "name": "Telugu", "native": "తెలుగు", "country": "IN", "flag": "🇮🇳", "dir": "ltr"},
    "ta": {"code": "ta", "name": "Tamil", "native": "தமிழ்", "country": "IN", "flag": "🇮🇳", "dir": "ltr"},
    "gu": {"code": "gu", "name": "Gujarati", "native": "ગુજરાતી", "country": "IN", "flag": "🇮🇳", "dir": "ltr"}
}

# We define translations for all 21 languages
TRANSLATIONS = {}

# Import existing knowledge base translations as baseline
import sys
sys.path.insert(0, ".")
from ai.knowledge_base import TRANSLATIONS as OLD_TRANSLATIONS

TRANSLATIONS["en"] = dict(OLD_TRANSLATIONS["en"])
TRANSLATIONS["hi"] = dict(OLD_TRANSLATIONS["hi"])
TRANSLATIONS["mr"] = dict(OLD_TRANSLATIONS["mr"])

# Additional universal keys
COMMON_EXTRAS = {
    "btn_save_pdf": "Save / Download PDF",
    "formulation_ready": "Formulation Ready",
    "extension_gain": "Extension",
    "open_full_report": "Open Full Technical Report",
    "ready_to_optimize": "Ready to Optimize",
    "ready_to_optimize_desc": "Configure your parameters in the left panel and click 'Run PackSense AI' to compute optimal barrier specifications."
}
for k, v in COMMON_EXTRAS.items():
    if k not in TRANSLATIONS["en"]:
        TRANSLATIONS["en"][k] = v

TRANSLATIONS["hi"]["btn_save_pdf"] = "पीडीएफ सहेजें / डाउनलोड करें"
TRANSLATIONS["hi"]["formulation_ready"] = "संरचना तैयार है"
TRANSLATIONS["hi"]["extension_gain"] = "विस्तार"
TRANSLATIONS["hi"]["open_full_report"] = "पूर्ण तकनीकी रिपोर्ट खोलें"
TRANSLATIONS["hi"]["ready_to_optimize"] = "ऑप्टिमाइज़ेशन के लिए तैयार"
TRANSLATIONS["hi"]["ready_to_optimize_desc"] = "बाएं पैनल में अपने पैरामीटर सेट करें और 'पाकसेंस एआई चलाएं' पर क्लिक करें।"

TRANSLATIONS["mr"]["btn_save_pdf"] = "पीडीएफ जतन / डाउनलोड करा"
TRANSLATIONS["mr"]["formulation_ready"] = "फॉर्म्युलेशन तयार आहे"
TRANSLATIONS["mr"]["extension_gain"] = "वाढ"
TRANSLATIONS["mr"]["open_full_report"] = "संपूर्ण तांत्रिक अहवाल उघडा"
TRANSLATIONS["mr"]["ready_to_optimize"] = "ऑप्टिमायझेशनसाठी सज्ज"
TRANSLATIONS["mr"]["ready_to_optimize_desc"] = "डाव्या पॅनेलमधील निकष निवडा आणि 'पॅकसेन्स एआय चालवा' बटणावर क्लिक करा."

print("Base en, hi, mr loaded successfully.")
