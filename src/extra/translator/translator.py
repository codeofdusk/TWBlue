# -*- coding: utf-8 -*-
from builtins import zip
from yandex_translate import YandexTranslate

def translate(text="", source="auto", target="en"):
	t = YandexTranslate("trnsl.1.1.20161012T134532Z.d01b9c75fc39aa74.7d1be75a5166a80583eeb020e10f584168da6bf7")
	return t.translate(text, target)["text"][0]


languages = {
  "af": _("Afrikaans"),
  "sq": _("Albanian"),
  "am": _("Amharic"),
  "ar": _("Arabic"),
  "hy": _("Armenian"),
  "az": _("Azerbaijani"),
  "eu": _("Basque"),
  "be": _("Belarusian"),
  "bn": _("Bengali"),
  "bh": _("Bihari"),
  "bg": _("Bulgarian"),
  "my": _("Burmese"),
  "ca": _("Catalan"),
  "chr": _("Cherokee"),
  "zh": _("Chinese"),
  "zh-CN": _("Chinese_simplified"),
  "zh-TW": _("Chinese_traditional"),
  "hr": _("Croatian"),
  "cs": _("Czech"),
  "da": _("Danish"),
  "dv": _("Dhivehi"),
  "nl": _("Dutch"),
  "en": _("English"),
  "eo": _("Esperanto"),
  "et": _("Estonian"),
  "tl": _("Filipino"),
  "fi": _("Finnish"),
  "fr": _("French"),
  "gl": _("Galician"),
  "ka": _("Georgian"),
  "de": _("German"),
  "el": _("Greek"),
  "gn": _("Guarani"),
  "gu": _("Gujarati"),
  "iw": _("Hebrew"),
  "hi": _("Hindi"),
  "hu": _("Hungarian"),
  "is": _("Icelandic"),
  "id": _("Indonesian"),
  "iu": _("Inuktitut"),
  "ga": _("Irish"),
  "it": _("Italian"),
  "ja": _("Japanese"),
  "kn": _("Kannada"),
  "kk": _("Kazakh"),
  "km": _("Khmer"),
  "ko": _("Korean"),
  "ku": _("Kurdish"),
  "ky": _("Kyrgyz"),
  "lo": _("Laothian"),
  "lv": _("Latvian"),
  "lt": _("Lithuanian"),
  "mk": _("Macedonian"),
  "ms": _("Malay"),
  "ml": _("Malayalam"),
  "mt": _("Maltese"),
  "mr": _("Marathi"),
  "mn": _("Mongolian"),
  "ne": _("Nepali"),
  "no": _("Norwegian"),
  "or": _("Oriya"),
  "ps": _("Pashto"),
  "fa": _("Persian"),
  "pl": _("Polish"),
  "pt-PT": _("Portuguese"),
  "pa": _("Punjabi"),
  "ro": _("Romanian"),
  "ru": _("Russian"),
  "sa": _("Sanskrit"),
  "sr": _("Serbian"),
  "sd": _("Sindhi"),
  "si": _("Sinhalese"),
  "sk": _("Slovak"),
  "sl": _("Slovenian"),
  "es": _("Spanish"),
  "sw": _("Swahili"),
  "sv": _("Swedish"),
  "tg": _("Tajik"),
  "ta": _("Tamil"),
  "tl": _("Tagalog"),
  "te": _("Telugu"),
  "th": _("Thai"),
  "bo": _("Tibetan"),
  "tr": _("Turkish"),
  "uk": _("Ukrainian"),
  "ur": _("Urdu"),
  "uz": _("Uzbek"),
  "ug": _("Uighur"),
  "vi": _("Vietnamese"),
  "cy": _("Welsh"),
  "yi": _("Yiddish")
}

def available_languages():
	l = list(languages.keys())
	d = list(languages.values())
	l.insert(0, '')
	d.insert(0, _("autodetect"))
	return sorted(zip(l, d))
