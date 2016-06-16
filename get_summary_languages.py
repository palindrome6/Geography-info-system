from html import XHTML
import pycountry
import wikipedia
import gettext
import gettext
import os
names= []
wikipedia.set_rate_limiting(rate_limit=1)
done_languages = ['es', 'en', 'it', 'de', 'zh', 'fr', 'nl', 'aa', 'ab', 'af', 'ak', 'am', 'an', 'ar', 'as',  'av', 'ae', 'ay', 'az', 'ba', 'bm', 'be', 'bn', 'bi', 'bo', 'bs', 'br', 'bg', 'ca', 'cs', 'ch', 'ce', 'cu', 'cv', 'kw', 'co', 'cr', 'cy', 'da', 'de', 'dv', 'dz', 'el', 'en', 'eo', 'et', 'eu', 'ee', 'fo', 'fa', 'fj', 'fi', 'fr', 'fy', 'ff', 'gd', 'ga', 'gl', 'gv', 'gn', 'gu', 'ht', 'ha', 'sh', 'he', 'hz', 'hi', 'ho', 'hr', 'hu', 'hy', 'ig', 'io', 'ii', 'iu', 'ie', 'ia', 'id', 'ik', 'is', 'it', 'jv', 'ja', 'kl', 'kn', 'ks', 'ka', 'kr', 'kk', 'km', 'ki', 'rw', 'ky', 'kv', 'kg', 'ko', 'kj', 'ku', 'lo', 'la', 'lv', 'li', 'ln', 'lt', 'lb', 'lu', 'lg', 'mh', 'ml', 'mr', 'mk', 'mg', 'mt', 'mn', 'mi', 'ms']
# lang_list = wikipedia.languages()
# for key in lang_list.iteritems():
#     name = key[0].encode('utf-8')
#     names.append(name)
# print names
lang_list = [lang.iso639_1_code.encode('utf-8')
         for lang in pycountry.languages
         if hasattr(lang, 'iso639_1_code')]

print lang_list

for lang in lang_list:
    if lang in done_languages:
        continue
    else:
        newpath = "C:\Users\s158079\Downloads\Study_materials\Quartile 4\Adaptive web\Project\\final_lang\countries-" + str(lang).lower() + "\\"
        print str(lang).lower()
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        wikipedia.set_lang(lang)
        try:
            lg = gettext.translation('iso3166', pycountry.LOCALES_DIR,languages=[lang])
        except:
            continue
        lg.install()
        summary = []
        lists = []
        country_list = list(pycountry.countries)
        for country in country_list:
            country.name = _(country.name)

            try:
                summary1 = wikipedia.summary(country.name)
            except wikipedia.exceptions.PageError:
                lists.append(country.name)
                continue
            except wikipedia.exceptions.DisambiguationError:
                lists.append(country.name)
                continue

            print country.name
            summary1 = summary1.encode('utf-8')
            paras = summary1.split("\n")
            cname = (str(country.alpha2)).lower() + ".xhtml"
            direc = "C:\Users\s158079\Downloads\Study_materials\Quartile 4\Adaptive web\Project\\final_lang\countries-" + str(lang).lower() + "\\"
            with open(direc + str(cname), "w") as cfile:
                cfile.write("<div>\n")
                for item in paras:
                    cfile.write("<p>" + str(item) + "</p>\n")
                cfile.write("</div>")

        with open(direc + 'exceptions.txt', "w") as tfile:
            for item in lists:
                tfile.write(item + "\n")

