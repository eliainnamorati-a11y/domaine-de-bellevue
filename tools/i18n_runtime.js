/* ---- Language switcher runtime (FR default, EN optional) ----
 * Priority: ?lang=en in URL  >  last choice (localStorage)  >  French.
 */
(function () {
  var STORAGE_KEY = 'ddb-lang';
  var dict = window.I18N || {};
  var current = 'fr';

  function t(key, lang) {
    lang = lang || current;
    if (dict[lang] && dict[lang][key] != null) return dict[lang][key];
    return (dict.fr && dict.fr[key] != null) ? dict.fr[key] : '';
  }

  function apply(lang) {
    if (!dict[lang]) lang = 'fr';
    current = lang;
    document.documentElement.lang = lang === 'fr' ? 'fr-CH' : 'en';

    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var v = t(el.getAttribute('data-i18n'), lang);
      if (v) el.innerHTML = v;
    });

    document.querySelectorAll('[data-i18n-attr]').forEach(function (el) {
      el.getAttribute('data-i18n-attr').split(';').forEach(function (pair) {
        var parts = pair.split(':');
        if (parts.length < 2) return;
        var v = t(parts[1].trim(), lang);
        if (v) el.setAttribute(parts[0].trim(), v);
      });
    });

    document.title = t('meta.title', lang).replace(/&amp;/g, '&');
    var md = document.querySelector('meta[name="description"]');
    if (md) md.setAttribute('content', t('meta.description', lang));

    document.querySelectorAll('.lang-btn').forEach(function (b) {
      var on = b.getAttribute('data-lang') === lang;
      b.classList.toggle('is-active', on);
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });

    try { localStorage.setItem(STORAGE_KEY, lang); } catch (e) {}
    try {
      var url = new URL(window.location.href);
      if (lang === 'fr') url.searchParams.delete('lang'); else url.searchParams.set('lang', lang);
      window.history.replaceState(null, '', url);
    } catch (e) {}
  }

  function initialLang() {
    try {
      var p = new URLSearchParams(window.location.search).get('lang');
      if (p && dict[p]) return p;
    } catch (e) {}
    try {
      var s = localStorage.getItem(STORAGE_KEY);
      if (s && dict[s]) return s;
    } catch (e) {}
    return 'fr';
  }

  document.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest('.lang-btn');
    if (btn) apply(btn.getAttribute('data-lang'));
  });

  window.i18n = { t: function (k) { return t(k); }, apply: apply, get lang() { return current; } };
  apply(initialLang());
})();
