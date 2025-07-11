from fasthtml.common import *
import os
import frontmatter  # you'll need to install python-frontmatter
from dotenv import load_dotenv
from sitemap import sitemap
import json
# Load environment variables
load_dotenv()

supported_locales = ["en", "de"]

def detect_locale(request, session):
    saved_locale = session.get('language')
    if saved_locale and saved_locale in supported_locales:
        return saved_locale
    else:
        browser_locale = request.headers.get('accept-language', 'en').split(',')[0].split('-')[0]
        if browser_locale and browser_locale in supported_locales:
            return browser_locale
        else:
            return "en" # fallback to English if no locale is detected

def modified_locale(locale):
    if locale == 'en':
        return ''
    else:
        return f'/{locale}'

def resolve_locale_and_redirect(request, session, lang, page_name):
    if lang:
        locale = lang
        if lang == 'en':
            return Redirect(f"{page_name}"), None
        if locale not in supported_locales:
            return Redirect(f"{page_name}"), None
    else:
        locale = detect_locale(request, session)
        if locale != 'en':
            return Redirect(f"/{locale}{page_name}"), None

    return None, locale  # No redirect, return locale

class Translator:
    def __init__(self, locale="en"):
        self.translations = self._load_locale(locale)
        self.english = self._load_locale("en")

    def _load_locale(self, locale):
        """Load localization strings from JSON file"""
        try:
            with open(f'locales/{locale}.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # Fallback to English if locale file doesn't exist
            with open('locales/en.json', 'r', encoding='utf-8') as f:
                return json.load(f)

    def t(self, key, default=""):
        """Get translated text with English fallback"""
        # Try current locale first
        result = self.translations.get(key)
        if result is not None:
            return result
        # Fallback to English
        result = self.english.get(key)
        if result is not None:
            return result
        # Final fallback
        return default

def locale_selector(current_page):
    # Build URLs that preserve current page
    if current_page == "home":
        en_href = "/"
        de_href = "/de/"
    else:
        en_href = f"/{current_page}"
        de_href = f"/de/{current_page}"

    return Div(
        A("EN", href=en_href,
          hx_post="/set-language",
          hx_vals='{"language": "en", "redirect": "' + en_href + '"}',
          hx_trigger="click",
          cls='text-white hover:text-blue-200 px-2 sm:px-3 py-1 sm:py-2 block text-sm sm:text-base'),
        A("DE", href=de_href,
          hx_post="/set-language",
          hx_vals='{"language": "de", "redirect": "' + de_href + '"}',
          hx_trigger="click",
          cls='text-white hover:text-blue-200 px-2 sm:px-3 py-1 sm:py-2 block text-sm sm:text-base'),
        cls='absolute top-full left-0 bg-blue-800 border border-blue-700 rounded shadow-lg hidden z-50 min-w-[50px] sm:min-w-[60px]'
    )

# Get environment variables
ga_id = os.getenv('GOOGLE_ANALYTICS_ID')
cookiebot_id = os.getenv('COOKIEBOT_ID')

socials = Socials(title="AIPE Technology", description="Consulting firm turning AI potential into working business solutions", site_name='www.aipe.tech', image='https://www.aipe.tech/assets/images/aipe_technology_screen.png', url='https://www.aipe.tech')

tailwind_css = Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css")

markdown_css = Style("""
    /* Custom markdown styles that work with TailwindCSS */
    .prose {
        color: #374151;
        max-width: none;
        line-height: 1.75;
    }
    
    .prose h1 {
        color: #111827;
        font-weight: 800;
        font-size: 2.25rem;
        line-height: 1.1111111;
        margin-top: 0;
        margin-bottom: 2rem;
    }
    
    .prose h2 {
        color: #111827;
        font-weight: 700;
        font-size: 1.875rem;
        line-height: 1.3333333;
        margin-top: 3rem;
        margin-bottom: 1.5rem;
    }
    
    .prose h3 {
        color: #111827;
        font-weight: 600;
        font-size: 1.5rem;
        line-height: 1.3333333;
        margin-top: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .prose h4 {
        color: #111827;
        font-weight: 600;
        font-size: 1.25rem;
        line-height: 1.4;
        margin-top: 2rem;
        margin-bottom: 0.75rem;
    }
    
    .prose p {
        margin-top: 0;
        margin-bottom: 1.25rem;
        line-height: 1.75;
    }
    
    .prose strong {
        color: #111827;
        font-weight: 600;
    }
    
    .prose em {
        font-style: italic;
    }
    
    .prose ul {
        list-style-type: disc;
        margin-top: 1.25rem;
        margin-bottom: 1.25rem;
        padding-left: 1.625rem;
    }
    
    .prose ol {
        list-style-type: decimal;
        margin-top: 1.25rem;
        margin-bottom: 1.25rem;
        padding-left: 1.625rem;
    }
    
    .prose li {
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    .prose li p {
        margin-top: 0.75rem;
        margin-bottom: 0.75rem;
    }
    
    .prose blockquote {
        font-weight: 500;
        font-style: italic;
        color: #111827;
        border-left: 0.25rem solid #d1d5db;
        quotes: "\\201C""\\201D""\\2018""\\2019";
        margin-top: 1.6rem;
        margin-bottom: 1.6rem;
        padding-left: 1rem;
    }
    
    .prose blockquote p:first-of-type::before {
        content: open-quote;
    }
    
    .prose blockquote p:last-of-type::after {
        content: close-quote;
    }
    
    .prose code {
        color: #111827;
        font-weight: 600;
        font-size: 0.875rem;
        background-color: #f3f4f6;
        padding: 0.125rem 0.25rem;
        border-radius: 0.25rem;
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, "Liberation Mono", Menlo, monospace;
    }
    
    .prose pre {
        color: #e5e7eb;
        background-color: #1f2937;
        overflow-x: auto;
        font-size: 0.875rem;
        line-height: 1.7142857;
        margin-top: 1.7142857em;
        margin-bottom: 1.7142857em;
        border-radius: 0.375rem;
        padding: 1rem;
    }
    
    .prose pre code {
        background-color: transparent;
        border-width: 0;
        border-radius: 0;
        padding: 0;
        font-weight: 400;
        color: inherit;
        font-size: inherit;
        font-family: inherit;
        line-height: inherit;
    }
    
    .prose pre code::before,
    .prose pre code::after {
        content: none;
    }
    
    .prose a {
        color: #1d4ed8;
        text-decoration: underline;
        font-weight: 500;
    }
    
    .prose a:hover {
        color: #1e40af;
    }
    
    .prose table {
        width: 100%;
        table-layout: auto;
        text-align: left;
        margin-top: 2em;
        margin-bottom: 2em;
        font-size: 0.875rem;
        line-height: 1.7142857;
        border-collapse: collapse;
    }
    
    .prose thead {
        border-bottom: 1px solid #d1d5db;
    }
    
    .prose thead th {
        color: #111827;
        font-weight: 600;
        vertical-align: bottom;
        padding-right: 0.5714286em;
        padding-bottom: 0.5714286em;
        padding-left: 0.5714286em;
    }
    
    .prose tbody tr {
        border-bottom: 1px solid #e5e7eb;
    }
    
    .prose tbody tr:last-child {
        border-bottom-width: 0;
    }
    
    .prose tbody td {
        vertical-align: baseline;
        padding: 0.5714286em;
    }
    
    .prose img {
        margin-top: 2em;
        margin-bottom: 2em;
        max-width: 100%;
        height: auto;
        border-radius: 0.5rem;
    }
    
    .prose hr {
        border-color: #d1d5db;
        border-top-width: 1px;
        margin-top: 3em;
        margin-bottom: 3em;
    }
    
    /* Responsive adjustments */
    .prose-lg {
        font-size: 1.125rem;
        line-height: 1.7777778;
    }
    
    .prose-lg h1 {
        font-size: 2.6666667rem;
        margin-bottom: 1.3333333rem;
        line-height: 1;
    }
    
    .prose-lg h2 {
        font-size: 2.2222222rem;
        margin-top: 2.2222222rem;
        margin-bottom: 1.1111111rem;
        line-height: 1.2;
    }
    
    .prose-lg h3 {
        font-size: 1.6666667rem;
        margin-top: 1.7777778rem;
        margin-bottom: 0.6666667rem;
        line-height: 1.3333333;
    }
    
    .prose-lg p {
        margin-top: 0;
        margin-bottom: 1.3333333rem;
    }
    
    .prose-lg blockquote {
        margin-top: 1.7777778rem;
        margin-bottom: 1.7777778rem;
        padding-left: 1.1111111rem;
    }
""")

# Add custom CSS for animations
custom_css = Style("""
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .animate-fade-in {
        animation: fadeInUp 0.8s ease-out forwards;
        opacity: 0;
    }
    
    .animate-fade-in-delay-1 {
        animation: fadeInUp 0.8s ease-out 0.2s forwards;
        opacity: 0;
    }
    
    .animate-fade-in-delay-2 {
        animation: fadeInUp 0.8s ease-out 0.4s forwards;
        opacity: 0;
    }
    
    .animate-fade-in-delay-3 {
        animation: fadeInUp 0.8s ease-out 0.6s forwards;
        opacity: 0;
    }
    
    .animate-fade-in-delay-4 {
        animation: fadeInUp 0.8s ease-out 0.8s forwards;
        opacity: 0;
    }
    
    .animate-fade-in-delay-5 {
        animation: fadeInUp 0.8s ease-out 1.0s forwards;
        opacity: 0;
    }
    
    .animate-fade-in-delay-6 {
        animation: fadeInUp 0.8s ease-out 1.2s forwards;
        opacity: 0;
    }
    
    .animate-fade-in-delay-7 {
        animation: fadeInUp 0.8s ease-out 1.4s forwards;
        opacity: 0;
    }
    
    /* Make animate-on-scroll elements start invisible */
    .animate-on-scroll {
        opacity: 0;
        transform: translateY(30px);
    }
    
    .animate-on-scroll.animate-fade-in {
        animation: fadeInUp 0.8s ease-out forwards;
    }
    
    .animate-on-scroll.animate-fade-in-delay-1 {
        animation: fadeInUp 0.8s ease-out 0.2s forwards;
    }
    
    .animate-on-scroll.animate-fade-in-delay-2 {
        animation: fadeInUp 0.8s ease-out 0.4s forwards;
    }
    
    .animate-on-scroll.animate-fade-in-delay-3 {
        animation: fadeInUp 0.8s ease-out 0.6s forwards;
    }
    
    .animate-on-scroll.animate-fade-in-delay-4 {
        animation: fadeInUp 0.8s ease-out 0.8s forwards;
    }
    
    .animate-on-scroll.animate-fade-in-delay-5 {
        animation: fadeInUp 0.8s ease-out 1.0s forwards;
    }
    
    .animate-on-scroll.animate-fade-in-delay-6 {
        animation: fadeInUp 0.8s ease-out 1.2s forwards;
    }

    .animate-on-scroll.animate-fade-in-delay-7 {
        animation: fadeInUp 0.8s ease-out 1.4s forwards;
    }
    
    
""")

headers =   (Meta(name="robots", content="index, follow"),
            MarkdownJS(),
            socials,
            Favicon('/assets/images/favicon.ico', '/assets/images/favicon.ico'),
            #picolink,
            tailwind_css,
            markdown_css,
            custom_css,
            # First set default consent settings to denied
            Script("""
                window.dataLayer = window.dataLayer || [];
                function gtag(){dataLayer.push(arguments);}
                gtag('consent', 'default', {
                'ad_storage': 'denied',
                'analytics_storage': 'denied',
                'wait_for_update': 500
                });
                """),
            # Add Cookiebot script second
            Script(src="https://consent.cookiebot.com/uc.js",
                  id="Cookiebot",
                  data_cbid=cookiebot_id,
                  data_blockingmode="auto",
                  type="text/javascript",
                  _async=True),
            # Add the Cookiebot callback function third
            Script("""
            window.addEventListener('CookiebotOnConsentReady', function () {
                if (Cookiebot.hasResponse) {
                    // User made an explicit choice
                    gtag('consent', 'update', {
                        'ad_storage': Cookiebot.consent.marketing ? 'granted' : 'denied',
                        'analytics_storage': Cookiebot.consent.statistics ? 'granted' : 'denied'
                    });
                } else if (Cookiebot.regulation === 'gdpr') {
                    // EU user who didn't respond - deny tracking
                    gtag('consent', 'update', {
                        'ad_storage': 'denied',
                        'analytics_storage': 'denied'
                    });
                }
                // Non-EU users keep the default 'granted' settings
            });
            """),
            # Then Google Analytics scripts fourth
            Script(src=f"https://www.googletagmanager.com/gtag/js?id={ga_id}", _async=True),
            Script(f"""
              window.dataLayer = window.dataLayer || [];
              function gtag(){{dataLayer.push(arguments);}}
              gtag('js', new Date());
              gtag('config', '{ga_id}');
            """),
            Script("""
            {
              "@context": "https://schema.org",
              "@type": "Organization",
              "name": "AIPE Technology",
              "url": "https://www.aipe.tech",
              "description": "Consulting firm turning AI potential into working business solutions",
              "email": "info@aipetech.com",
              "logo": "https://www.aipe.tech/assets/images/aipe_technology_screen.png",
              "sameAs": [
                "https://www.linkedin.com/company/aipe-technology-ag/"
              ]
            }
            """, type="application/ld+json"),
            Script("""
document.addEventListener('DOMContentLoaded', function() {
  var mission = document.getElementById('mission-section');
  if (!mission) return;
  var observer = new IntersectionObserver(function(entries) {
    if (entries[0].isIntersecting) {
      mission.querySelectorAll('.animate-on-scroll').forEach(function(el, i) {
        el.classList.add('animate-fade-in');
        if (i === 1) el.classList.add('animate-fade-in-delay-1');
      });
      observer.disconnect();
    }
  }, { threshold: 0.3 });
  observer.observe(mission);
});
"""),
            # Update the portfolio JavaScript to trigger earlier
            Script("""
document.addEventListener('DOMContentLoaded', function() {
  var portfolio = document.getElementById('portfolio-section');
  if (!portfolio) return;
  var observer = new IntersectionObserver(function(entries) {
    if (entries[0].isIntersecting) {
      portfolio.querySelectorAll('.animate-on-scroll').forEach(function(el, i) {
        el.classList.add('animate-fade-in');
        if (i === 1) el.classList.add('animate-fade-in-delay-1');
        if (i === 2) el.classList.add('animate-fade-in-delay-2');
        if (i === 3) el.classList.add('animate-fade-in-delay-3');
        if (i === 4) el.classList.add('animate-fade-in-delay-4');
        if (i === 5) el.classList.add('animate-fade-in-delay-5');
        if (i === 6) el.classList.add('animate-fade-in-delay-6');
      });
      observer.disconnect();
    }
  }, { threshold: 0.1 });
  observer.observe(portfolio);
});
"""),
            Script("""
document.addEventListener('DOMContentLoaded', function() {
  var services = document.getElementById('services');
  if (!services) return;
  var observer = new IntersectionObserver(function(entries) {
    if (entries[0].isIntersecting) {
      services.querySelectorAll('.animate-on-scroll').forEach(function(el, i) {
        el.classList.add('animate-fade-in');
        if (i === 1) el.classList.add('animate-fade-in-delay-1');
        if (i === 2) el.classList.add('animate-fade-in-delay-2');
        if (i === 3) el.classList.add('animate-fade-in-delay-3');
        if (i === 4) el.classList.add('animate-fade-in-delay-4');
        if (i === 5) el.classList.add('animate-fade-in-delay-5');
        if (i === 6) el.classList.add('animate-fade-in-delay-6');
        if (i === 7) el.classList.add('animate-fade-in-delay-7');
        if (i === 8) el.classList.add('animate-fade-in-delay-8');
      });
      observer.disconnect();
    }
  }, { threshold: 0.2 });
  observer.observe(services);
});
"""),
            Script("""
document.addEventListener('DOMContentLoaded', function() {
  var blog = document.getElementById('blog-section');
  if (!blog) return;
  var observer = new IntersectionObserver(function(entries) {
    if (entries[0].isIntersecting) {
      blog.querySelectorAll('.animate-on-scroll').forEach(function(el, i) {
        el.classList.add('animate-fade-in');
        if (i === 1) el.classList.add('animate-fade-in-delay-1');
        if (i === 2) el.classList.add('animate-fade-in-delay-2');
        if (i === 3) el.classList.add('animate-fade-in-delay-3');
        if (i === 4) el.classList.add('animate-fade-in-delay-4');
        if (i === 5) el.classList.add('animate-fade-in-delay-5');
      });
      observer.disconnect();
    }
  }, { threshold: 0.2 });
  observer.observe(blog);
});
"""),
            Script("""
window.addEventListener('load', function() {
  // Language dropdown functionality
  const languageIcon = document.querySelector('img[src="/assets/images/globe.svg"]');
  
  if (languageIcon) {
    const groupDiv = languageIcon.parentElement;
    const dropdown = groupDiv.querySelector('.absolute');
    
    if (dropdown) {
      let isOpen = false;
      
      languageIcon.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        
        if (!isOpen) {
          // Open dropdown
          dropdown.classList.remove('hidden');
          dropdown.style.display = 'block';
          dropdown.style.visibility = 'visible';
          dropdown.style.opacity = '1';
          dropdown.style.zIndex = '9999';
          isOpen = true;
        } else {
          // Close dropdown
          dropdown.classList.add('hidden');
          dropdown.style.display = 'none';
          isOpen = false;
        }
      });
      
      // Close dropdown when clicking outside
      document.addEventListener('click', function(e) {
        if (isOpen && !groupDiv.contains(e.target)) {
          dropdown.classList.add('hidden');
          dropdown.style.display = 'none';
          isOpen = false;
        }
      });
    }
  }
});
""")
            )

app = FastHTML(hdrs=headers, title="AIPE Technology")

@app.get("/{fname:path}.xml")
def get_xml(fname: str):
    return FileResponse(f"{fname}.xml")

@app.get("/{fname:path}.{ext:static}")
def get(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

def app_header(T, current_page, mod_locale):

   return Header(
       Div(
           # Logo on the far left
           A(
               Img(
                   src='/assets/images/aipe_logo_white.svg',
                   alt='AIPE Logo',
                   cls='h-6 sm:h-7 w-auto'
               ),
               href=f'{mod_locale}/',
               cls='no-underline ml-3 sm:ml-5'
           ),
           # Navigation items and language selector on the right
           Div(
               # Language selector (left of navigation) - smaller on mobile
               Div(
                   # Globe icon with dropdown
                   Div(
                       # Globe icon (using text symbol) - smaller on mobile
                       Img(
                           src='/assets/images/globe.svg',
                           alt='Language',
                           cls='w-5 h-5 text-white hover:text-blue-200 cursor-pointer'
                       ),
                       locale_selector(current_page),
                       cls='relative group'
                   ),
                   cls='flex items-center mr-1 sm:mr-4'  # Smaller margin on mobile
               ),
               # Navigation items
               Nav(
                   A(T.t("home"), href=f'{mod_locale}/', cls='text-white hover:text-blue-200 mx-1 sm:mx-2 md:mx-4'),
                   A(T.t("services"), href=f'{mod_locale}/#services', cls='text-white hover:text-blue-200 mx-1 sm:mx-2 md:mx-4'),
                   A(
                       Span(T.t("about"), cls='sm:hidden'),
                       Span(T.t("about_us"), cls='hidden sm:inline'),
                       href=f'{mod_locale}/about', 
                       cls='text-white hover:text-blue-200 mx-1 sm:mx-2 md:mx-4'
                   ),
                   A(T.t("blog"), href=f'{mod_locale}/blog', cls='text-white hover:text-blue-200 mx-1 sm:mx-2 md:mx-4'),
                   A(T.t("contact"),
                     href=f'{mod_locale}/contact',
                     cls='bg-white text-blue-800 px-2 sm:px-3 md:px-4 py-1.5 rounded-lg hover:bg-blue-100 ml-1 sm:ml-2 md:ml-4 mr-2 sm:mr-3 md:mr-5'
                   ),
                   cls='flex items-center text-xs sm:text-sm md:text-base'
               ),
               cls='flex items-center'
           ),
           cls='flex justify-between items-center py-1.5 sm:py-2 w-full'
       ),
       cls='border-b border-blue-800 bg-blue-800 w-full'
   )

def section_hero(T, mod_locale):
    return Section(
        Div(
            H1(
                Span(T.t("hero_title"), cls='text-blue-800'),
                cls='text-4xl font-bold sm:text-5xl mb-8 animate-fade-in'
            ),
            P(T.t("hero_subtitle"),
              cls='mt-16 text-2xl text-gray-800 font-semibold mb-16 max-w-4xl animate-fade-in-delay-1'),
            P(
                Span(T.t("why_choose_us") + ' ', cls='font-semibold'),
                T.t("why_choose_us_description"),
                cls='text-xl text-gray-600 mb-24 max-w-4xl animate-fade-in-delay-2'
            ),
            # Three-step process cards
            Div(
                # Step 1: Discover (Left - appears first)
                Div(
                    Div(
                        Img(
                            src="/assets/images/oui--app-search-profiler.svg",
                            alt=T.t("step_1_title"),
                            cls='w-16 h-16 mx-auto mb-4 text-blue-800'
                        ),
                        cls='text-center'
                    ),
                    H3(
                        T.t("step_1_title"),
                        cls='text-2xl font-semibold text-blue-800 mb-3'
                    ),
                    P(
                        T.t("step_1_description_short"),
                        cls='text-gray-600 text-lg'
                    ),
                    cls='text-center p-8 bg-white rounded-xl shadow-sm border border-gray-200 hover:shadow-md transition-shadow duration-200 animate-fade-in-delay-3'
                ),
                # Step 2: Validate (Center - appears second)
                Div(
                    Div(
                        Img(
                            src="/assets/images/oui--check-in-circle-empty.svg",
                            alt=T.t("step_2_title"),
                            cls='w-16 h-16 mx-auto mb-4 text-blue-800'
                        ),
                        cls='text-center'
                    ),
                    H3(
                        T.t("step_2_title"),
                        cls='text-2xl font-semibold text-blue-800 mb-3'
                    ),
                    P(
                        T.t("step_2_description_short"),
                        cls='text-gray-600 text-lg'
                    ),
                    cls='text-center p-8 bg-white rounded-xl shadow-sm border border-gray-200 hover:shadow-md transition-shadow duration-200 animate-fade-in-delay-4'
                ),
                # Step 3: Scale (Right - appears third)
                Div(
                    Div(
                        Img(
                            src="/assets/images/oui--rocket.svg",
                            alt=T.t("step_3_title"),
                            cls='w-16 h-16 mx-auto mb-4 text-blue-800'
                        ),
                        cls='text-center'
                    ),
                    H3(
                        T.t("step_3_title"),
                        cls='text-2xl font-semibold text-blue-800 mb-3'
                    ),
                    P(
                        T.t("step_3_description_short"),
                        cls='text-gray-600 text-lg'
                    ),
                    cls='text-center p-8 bg-white rounded-xl shadow-sm border border-gray-200 hover:shadow-md transition-shadow duration-200 animate-fade-in-delay-5'
                ),
                cls='grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mb-24'
            ),
            Div(
                A(
                    T.t("hero_cta"),
                    Span('→', cls='ml-2'),
                    href=f'{mod_locale}/contact',
                    cls='bg-blue-800 text-white px-8 py-3 rounded-lg font-medium hover:bg-blue-900 transition-all transform hover:scale-105 inline-block'
                ),
                cls='mt-20 text-center animate-fade-in-delay-6'
            ),
            cls='max-w-5xl mx-auto px-6'
        ),
        cls="py-20 bg-gray-50"
    )

def section_mission(T):
    return Section(
        Div(
            P(
                T.t("mission_title"),
                cls='text-2xl sm:text-3xl text-gray-600 mb-6 max-w-2xl mx-auto text-center animate-on-scroll'
            ),
            H2(
                T.t("mission_description"),
                cls='text-4xl sm:text-5xl font-semibold text-gray-900 mb-4 text-center animate-on-scroll'
            ),
            cls='px-4 sm:px-6 lg:px-8'  # Add horizontal padding for iPhone SE
        ),
        cls='py-16 sm:py-24 lg:py-32', id="mission-section"  # Make vertical padding responsive
    )

def portfolio_card(portfolio_element, T):
    # Create video element (either real video with thumbnail or placeholder)
    def create_video_element():
        video_filename = portfolio_element["links"]["Video"]

        if video_filename and video_filename != "":
            # Real video exists - create video player with thumbnail poster
            thumbnail_filename = video_filename.replace('.mp4', '.png')
            return Div(
                Video(
                    src=f"/assets/videos/{video_filename}",
                    poster=f"/assets/videos/{thumbnail_filename}",
                    controls=True,
                    preload="metadata",
                    muted=True,  # Start without sound
                    loading="lazy",
                    cls='w-full h-full rounded-lg object-contain bg-gray-900'
                ),
                cls='w-full pb-[30%] sm:pb-[35%] relative border border-gray-300'  # More reasonable height
            )
        else:
            # No video - use PNG placeholder
            return Div(
                Img(
                    src="/assets/videos/placeholder.png",
                    alt=T.t("project_placeholder"),
                    cls='w-full h-full object-cover rounded-lg'
                ),
                cls='w-full pb-[20%] relative border border-gray-300'  # Reduced from pb-[50%] to pb-[35%] for iPhone
            )

    # Create link buttons with SVG icons - only if URL is not "tbd"
    def create_link_button(link_type, url, icon_src):
        return A(
            Img(
                src=icon_src,
                alt=f"{link_type} link",
                cls='w-4 h-4 inline-block ml-2 bg-gray-100 hover:bg-blue-100 text-gray-600 hover:text-blue-600 rounded p-1 transition-colors duration-200'
            ),
            href=url if url != "tbd" else "#",
            cls='inline-block',
            **({"onclick": "return false;"} if url == "tbd" else {})
        )

    # Create the link buttons with SVG icons - only if URL is not "tbd"
    link_buttons = []

    # Add GitHub button only if GitHub URL is not "tbd"
    if portfolio_element["links"]["GitHub"] != "tbd":
        link_buttons.append(
            create_link_button("GitHub", portfolio_element["links"]["GitHub"], "/assets/images/github.svg")
        )

    # Add Demo button only if Demo URL is not "tbd"
    if portfolio_element["links"]["Demo"] != "tbd":
        link_buttons.append(
            create_link_button("Demo", portfolio_element["links"]["Demo"], "/assets/images/external-link.svg")
        )

    return Div(
        # Title
        Div(
            H3(portfolio_element["title"], cls='text-xl font-semibold text-blue-800 mb-0'),  # Reduced from text-2xl to text-xl
            cls='mb-2 sm:mb-3'
        ),
        # Description
        Div(
            P(
                portfolio_element["description"],
                *link_buttons,
                cls='text-gray-600 text-base mb-4 text-justify'  # Reduced from text-lg to text-base
            ),
            cls='mb-3 sm:mb-4 flex-grow'
        ),
        # Video element (responsive height)
        create_video_element(),
        cls='bg-white rounded-lg p-2 sm:p-3 lg:p-5 shadow-sm border border-gray-100 hover:shadow-md transition-shadow duration-200 h-full flex flex-col animate-on-scroll'
    )

def section_portfolio(T):
    portfolio = [
    {
        "category": T.t("portfolio_category_1"),
        "title": T.t("portfolio_title_1"),
        "description": T.t("portfolio_description_1"),
        "links": {
            "Video": "cim-data-extraction-platform.mp4",
            "GitHub": "https://github.com/feldges/data_extractor",
            "Demo": "tbd"
                }
    },
    {
        "category": T.t("portfolio_category_2"),
        "title": T.t("portfolio_title_2"),
        "description": T.t("portfolio_description_2"),
        "links": {
            "Video": "comprehensive-pe-due-diligence-assistant.mp4",
            "GitHub": "tbd",
            "Demo": "tbd"
                }
    },
    {
        "category": T.t("portfolio_category_3"),
        "title": T.t("portfolio_title_3"),
        "description": T.t("portfolio_description_3"),
        "links": {
            "Video": "m-and-a-target-research-intelligence.mp4",
            "GitHub": "tbd",
            "Demo": "tbd"
                }
    },
        {
        "category": T.t("portfolio_category_4"),
        "title": T.t("portfolio_title_4"),
        "description": T.t("portfolio_description_4"),
        "links": {
            "Video": "investment-research-analyst.mp4",
            "GitHub": "https://github.com/feldges/storm",
            "Demo": "https://storm.aipe.tech/"
                }
    },
    {
        "category": T.t("portfolio_category_5"),
        "title": T.t("portfolio_title_5"),
        "description": T.t("portfolio_description_5"),
        "links": {
            "Video": "",
            "GitHub": "tbd",
            "Demo": "tbd"
                }
    },
    {
        "category": T.t("portfolio_category_6"),
        "title": T.t("portfolio_title_6"),
        "description": T.t("portfolio_description_6"),
        "links": {
            "Video": "work-smarter-ai-document-intelligence.mp4",
            "GitHub": "tbd",
            "Demo": "tbd"
                }
    },
    {
        "category": T.t("portfolio_category_7"),
        "title": T.t("portfolio_title_7"),
        "description": T.t("portfolio_description_7"),
        "links": {
            "Video": "dynamic-pricing-intelligence-platform.mp4",
            "GitHub": "https://github.com/feldges/price_tracker",
            "Demo": "tbd"
                }
    }
    ]
    
    # Group portfolio items by category
    from collections import defaultdict
    portfolio_by_category = defaultdict(list)
    for item in portfolio:
        portfolio_by_category[item["category"]].append(item)

    return Section(
        Div(
            H2(
                T.t("portfolio_section_title"),
                cls='text-4xl sm:text-5xl font-semibold text-gray-900 mb-4 sm:mb-6 text-center animate-on-scroll'  # Aligned with mission section
            ),
            P(
                T.t("portfolio_section_description"),
                cls='text-2xl sm:text-3xl text-gray-600 mb-6 sm:mb-8 max-w-3xl mx-auto text-center animate-on-scroll'  # Aligned with mission section
            ),
            # Create sections for each category
            *[Div(
                # Category section with frame only (no background)
                Div(
                    # Category header
                    H3(
                        category,
                        cls='text-xl sm:text-2xl font-semibold text-blue-800 mb-4 sm:mb-8 animate-on-scroll'  # Aligned with other sections
                    ),
                    # Portfolio cards in a grid
                    Div(
                        *[portfolio_card(item, T) for item in items],
                        cls='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-3 sm:gap-5 auto-rows-fr'  # Back to normal gaps
                    ),
                    cls='p-3 sm:p-6 rounded-lg border border-gray-200'  # Back to normal padding
                ),
                cls='mb-6 sm:mb-8 animate-on-scroll'  # Back to normal margins
            ) for category, items in portfolio_by_category.items()],
            cls='max-w-4xl sm:max-w-6xl mx-auto px-2 sm:px-4 lg:px-8'  # Keep responsive max-width
        ),
        cls='py-12 sm:py-16 bg-gray-50', id="portfolio-section"  # Back to normal padding
    )

def solution_card(title, description, animate_class=None):
    return Div(
        H3(title, cls='text-2xl font-semibold text-blue-800 mb-4 text-center'),
        P(description, cls='text-gray-600 text-lg mb-4 text-justify'),
        cls=f'bg-white rounded-lg p-8 shadow-sm border border-gray-200 hover:shadow-md transition-shadow duration-200 {animate_class if animate_class else ""}'
    )

def section_services(T, mod_locale):
    return Section(
        Div(
            H2(
                T.t("services_section_title"),
                cls='text-4xl sm:text-5xl font-semibold text-gray-900 mb-6 text-center animate-on-scroll'  # Removed animate-fade-in-delay-1
            ),
            P(
                T.t("services_section_description"),
                cls='text-2xl sm:text-3xl text-gray-600 mb-8 max-w-3xl mx-auto text-center animate-on-scroll'  # Removed animate-fade-in-delay-2
            ),
            # Services grid - three cards
            Div(
                solution_card(
                    title=T.t("solution_card_1_title"),
                    description=T.t("solution_card_1_description"),
                    animate_class='animate-on-scroll'  # Removed animate-fade-in-delay-3
                ),
                solution_card(
                    title=T.t("solution_card_2_title"),
                    description=T.t("solution_card_2_description"),
                    animate_class='animate-on-scroll'  # Removed animate-fade-in-delay-4
                ),
                solution_card(
                    title=T.t("solution_card_3_title"),
                    description=T.t("solution_card_3_description"),
                    animate_class='animate-on-scroll'  # Removed animate-fade-in-delay-5
                ),
                cls='grid md:grid-cols-3 gap-8 mt-12 max-w-7xl mx-auto'
            ),
            # Services CTA section
            Div(
                Div(
                    H3(T.t("solution_cta_title"), 
                       cls='text-3xl sm:text-4xl font-semibold text-center mb-6 animate-on-scroll'),
                    P(T.t("solution_cta_description"),
                      cls='text-gray-600 text-lg sm:text-xl text-center mb-8 animate-on-scroll'),
                    Div(
                        A(T.t("solution_cta_button"),
                          href=f'{mod_locale}/contact',
                          cls='bg-blue-800 text-white px-8 py-3 rounded-lg font-medium hover:bg-blue-900 transition-all transform hover:scale-105 inline-block animate-on-scroll'
                        ),
                        cls='text-center'
                    ),
                    cls='max-w-2xl mx-auto px-4'
                ),
                cls='border-t border-gray-200 pt-12 mt-12'
            ),
            cls='max-w-7xl mx-auto px-4 sm:px-6 lg:px-8'
        ),
        cls='py-20 bg-white', id="services"
    )

def app_footer(T, mod_locale):
    return Footer(
        # Main footer content
        Div(
            Div(
                # Three column container for desktop
                Div(
                    # Logo section
                    Div(
                        A(
                            Img(
                                src='/assets/images/aipe_logo_white.svg',
                                alt='AIPE Logo',
                                cls='h-8 w-auto'
                            ),
                            href=f'{mod_locale}/',
                            cls='no-underline'
                        ),
                        cls='flex flex-col items-center md:items-start'
                    ),
                    # Contact and social section
                    Div(
                        A(
                            'info@aipetech.com',
                            href='mailto:info@aipetech.com',
                            cls='text-gray-300 hover:text-white block'
                        ),
                        A(
                            Div(
                                Img(
                                    src='/assets/images/linkedin.svg?v=2',
                                    alt='Connect with us on LinkedIn',
                                    cls='w-5 h-5'
                                ),
                                cls='text-gray-600'
                            ),
                            href='https://www.linkedin.com/company/aipe-technology-ag/',
                            cls='mx-2 group',
                            target='_blank',
                            rel='noopener noreferrer'
                        ),
                        cls='flex flex-col items-center md:items-center space-y-2'
                    ),
                    # Navigation section
                    Nav(
                        A(T.t("home"), href=f'{mod_locale}/', cls='text-gray-300 hover:text-white'),
                        A(T.t("services"), href=f'{mod_locale}/#services', cls='text-gray-300 hover:text-white'),
                        A(T.t("about_us"), href=f'{mod_locale}/about', cls='text-gray-300 hover:text-white'),
                        A(T.t("blog"), href=f'{mod_locale}/blog', cls='text-gray-300 hover:text-white'),
                        A(T.t("contact"), href=f'{mod_locale}/contact', cls='text-gray-300 hover:text-white'),
                        cls='space-y-2 flex flex-col items-center md:items-end'
                    ),
                    cls='grid grid-cols-1 md:grid-cols-3 gap-8 pt-12 pb-8'
                ),
            ),
            # Bottom footer with more subtle styling
            Div(
                Div(
                    P(
                        '© 2025 AIPE Technology. ' + T.t("rights_reserved") + '.',
                        cls='text-gray-400 text-sm text-center md:text-left'  # Changed from text-xs to text-sm
                    ),
                    Div(
                        A(T.t("privacy_policy_title"), 
                          href=f'{mod_locale}/privacy_policy', 
                          cls='text-gray-300 hover:text-white text-sm font-medium'),
                        Span('•', cls='mx-2 text-gray-400 text-sm'),  # Updated dot styling
                        A(T.t("terms_of_service_title"), 
                          href=f'{mod_locale}/terms_of_service', 
                          cls='text-gray-300 hover:text-white text-sm font-medium'),
                        Span('•', cls='mx-2 text-gray-400 text-sm'),  # Updated dot styling
                        Span(T.t("accept_terms"), 
                             cls='text-gray-400 text-sm'),  # Made consistent with other text
                        cls='flex items-center justify-center md:justify-end flex-wrap gap-1'
                    ),
                    cls='flex flex-col md:flex-row justify-between items-center space-y-1 md:space-y-0'
                ),
                cls='border-t border-gray-800 py-3'  # Reduced padding
            ),
            cls='max-w-6xl mx-auto px-4 sm:px-6 lg:px-8'
        ),
        cls='bg-black'
    )

def blog_card(T, title, date, description, image_url, url_path, animate=False, animate_class=None):
    return Div(
        Img(
            src=image_url,
            alt=title,
            cls='w-full h-48 object-cover rounded-t-lg'
        ),
        Div(
            P(
                date,
                cls='text-sm text-gray-500 mb-2'
            ),
            H3(
                title,
                cls='text-xl font-semibold text-gray-900 mb-2 line-clamp-2'
            ),
            P(
                description,
                cls='text-gray-600 text-base line-clamp-3'
            ),
            A(
                T.t("read_more"),
                href=url_path,
                cls='inline-block mt-4 text-blue-800 hover:text-blue-600 font-medium'
            ),
            cls='p-6'
        ),
        cls=f'bg-white rounded-lg shadow-sm border border-gray-200 hover:shadow-md transition-shadow duration-200 {animate_class if animate_class else ""}'
    )

def get_blog_posts():
    blog_posts = []
    blog_dir = "Blog"
    default_image = '/assets/images/blog/default.jpg'  # Create a default image

    for filename in os.listdir(blog_dir):
        if filename.endswith('.md'):
            with open(os.path.join(blog_dir, filename), 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                url_path = f"/blog/{filename.replace('.md', '')}"  # Add /blog/ prefix
                blog_posts.append({
                    'title': post.metadata.get('title', ''),
                    'date': post.metadata.get('date', ''),
                    'description': post.metadata.get('description', ''),
                    'read_time': post.metadata.get('readTime', ''),
                    'category': post.metadata.get('category', ''),
                    'url_path': url_path,
                    # Use image from frontmatter or fall back to default
                    'image_url': post.metadata.get('image', default_image)
                })

    # Sort by date, most recent first
    blog_posts.sort(key=lambda x: x['date'], reverse=True)
    return blog_posts

def section_blog(T, mod_locale):
    blog_posts = get_blog_posts()

    return Section(
        Div(
            H2(
                T.t("blog_section_title"),
                cls='text-4xl sm:text-5xl font-semibold text-gray-900 mb-6 text-center animate-on-scroll'
            ),
            P(
                T.t("blog_section_description"),
                cls='text-center text-gray-600 text-2xl sm:text-3xl mb-8 max-w-3xl mx-auto animate-on-scroll'
            ),
            # Blog cards container - use standardized approach
            Div(
                *[blog_card(
                    T=T,
                    title=post['title'],
                    date=post['date'],
                    description=post['description'],
                    image_url=post['image_url'],
                    url_path=f'{mod_locale}{post["url_path"]}',
                    animate_class='animate-on-scroll'
                ) for i, post in enumerate(blog_posts[:3])],
                cls='grid grid-cols-1 md:grid-cols-3 gap-8 max-w-7xl mx-auto'
            ),
            cls='px-4 sm:px-6 lg:px-8'  # Add responsive horizontal padding
        ),
        cls='py-16 bg-gray-50', id="blog-section"
    )

@app.get('/blog')
@app.get('/{lang}/blog')
def blog_index(request: Request, session, lang: str = None):

    redirect_response, locale = resolve_locale_and_redirect(request, session, lang, '/blog')
    if redirect_response:
        return redirect_response

    mod_locale = modified_locale(locale)

    T = Translator(locale)

    blog_posts = get_blog_posts()

    return Div(
        app_header(T, current_page="blog", mod_locale=mod_locale),
        Section(
            Div(
                H1(T.t("blog_page_title"), cls='text-5xl font-semibold text-gray-900 mb-6 text-center'),
                P(
                    T.t("blog_page_description"),
                    cls='text-center text-gray-600 text-3xl mb-8 max-w-3xl mx-auto'
                ),
                # Change to grid layout like main page
                Div(
                    *[blog_card(
                        T=T,
                        title=post['title'],
                        date=post['date'].strftime('%B %d, %Y') if hasattr(post['date'], 'strftime') else str(post['date']),
                        description=post['description'],
                        image_url=post['image_url'],
                        url_path=f'{mod_locale}{post["url_path"]}',
                    ) for post in blog_posts],
                    cls='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-7xl mx-auto'
                ),
                cls='px-4 sm:px-6 lg:px-8'
            ),
            cls='py-16'
        ),
        app_footer(T, mod_locale)
    )

def privacy_policy_content(T, locale):
    if locale == 'en':
        file_path = 'assets/legal/privacy_policy.md'
    else:
        file_path = f'assets/legal/privacy_policy_{locale}.md'
    with open(file_path, 'r') as file:
        PRIVACY_POLICY = file.read()
        return Div(
            Div(  # Added wrapper div for centering
                PRIVACY_POLICY,
                cls='marked prose prose-lg max-w-none'
            ),
            cls='max-w-3xl mx-auto px-4 py-12'
        )

def terms_of_service_content(T, locale):
    if locale == 'en':
        file_path = 'assets/legal/terms_of_service.md'
    else:
        file_path = f'assets/legal/terms_of_service_{locale}.md'
    with open(file_path, 'r') as file:
        TERMS_OF_SERVICE = file.read()
        return Div(
            Div(  # Added wrapper div for centering
                TERMS_OF_SERVICE,
                cls='marked prose prose-lg max-w-none'
            ),
            cls='max-w-3xl mx-auto px-4 py-12'
        )

@app.get('/terms_of_service')
@app.get('/{lang}/terms_of_service')
def terms_of_service(request: Request, session, lang: str = None):

    redirect_response, locale = resolve_locale_and_redirect(request, session, lang, '/terms_of_service')
    if redirect_response:
        return redirect_response

    mod_locale = modified_locale(locale)

    T = Translator(locale)
    return Div(
        app_header(T, current_page="terms_of_service", mod_locale=mod_locale),
        terms_of_service_content(T, locale),
        app_footer(T, mod_locale)
    )

@app.get('/privacy_policy')
@app.get('/{lang}/privacy_policy')
def privacy_policy(request: Request, session, lang: str = None):

    redirect_response, locale = resolve_locale_and_redirect(request, session, lang, '/privacy_policy')
    if redirect_response:
        return redirect_response

    mod_locale = modified_locale(locale)

    T = Translator(locale)
    return Div(
        app_header(T, current_page="privacy_policy", mod_locale=mod_locale),
        privacy_policy_content(T, locale),
        app_footer(T, mod_locale)
    )

@app.get('/about')
@app.get('/{lang}/about')
def about(request: Request, session, lang: str = None):

    redirect_response, locale = resolve_locale_and_redirect(request, session, lang, '/about')
    if redirect_response:
        return redirect_response

    mod_locale = modified_locale(locale)

    T = Translator(locale)
    return Div(
        app_header(T, current_page="about", mod_locale=mod_locale),
        Main(
        Section(
            Div(
                H1(T.t("about_page_title"), cls='text-5xl font-semibold text-gray-900 mb-8 text-center'),
                # Two-column layout for desktop
                Div(
                    # Left column with photo and quick facts
                    Div(
                        Img(
                            src='/assets/images/feldges.jpg',
                            alt='Claude Feldges',
                            cls='rounded-full w-48 h-48 object-cover mx-auto mb-6 shadow-lg border-2 border-blue-100'
                        ),
                        Div(
                            P(
                                Span('Dr. Claude Feldges', cls='font-medium block text-2xl'),
                                cls='text-center text-gray-700 mb-6'
                            ),
                            Div(
                                A(
                                    Div(
                                        Img(
                                            src='/assets/images/linkedin.svg?v=2',
                                            alt=T.t("connect_with_me_on_linkedin"),
                                            cls='w-5 h-5'
                                        ),
                                        cls='text-gray-600'
                                    ),
                                    href='https://www.linkedin.com/in/claude-feldges-plocek-78090a1/',
                                    cls='mx-2 group',
                                    target='_blank',
                                    rel='noopener noreferrer'
                                ),
                                cls='flex justify-center'
                            ),
                            cls='mb-6'
                        ),
                        cls='w-full lg:w-1/3 px-6 mb-8 lg:mb-0 flex flex-col items-center'
                    ),
                    # Right column with detailed bio
                    Div(
                        H3(T.t("about_page_subtitle"), cls='text-2xl font-semibold text-blue-800 mb-6'),
                        P(
                            T.t("about_page_paragraph_1"),
                            cls='text-gray-700 mb-6 text-lg text-justify'
                        ),
                        P(
                            T.t("about_page_paragraph_2"),
                            cls='text-gray-700 mb-6 text-lg text-justify'
                        ),
                        P(
                            T.t("about_page_paragraph_3"),
                            cls='text-gray-700 mb-6 text-lg text-justify'
                        ),
                        P(
                            T.t("about_page_paragraph_4"),
                            cls='text-gray-700 mb-6 text-lg text-justify'
                        ),
                        H3(T.t("why_work_with_me_title"), cls='text-2xl font-semibold text-blue-800 mt-8 mb-6'),
                        Div(
                            *[Div(
                                Div(
                                    # Simple blue checkmark without circle
                                    Div(
                                        "✓",
                                        cls='text-blue-500 text-xl mr-3 flex-shrink-0'
                                    ),
                                    # Point text
                                    Div(
                                        text,
                                        cls='ml-4 text-gray-900 flex-grow text-lg text-justify'
                                    ),
                                    cls='flex items-center py-3'
                                ),
                                cls='transform transition-transform duration-200 hover:translate-x-2 list-none'
                            ) for text in [
                                T.t("why_work_with_me_paragraph_1"),
                                T.t("why_work_with_me_paragraph_2"),
                                T.t("why_work_with_me_paragraph_3"),
                                T.t("why_work_with_me_paragraph_4")
                            ]],
                            cls='mt-2'
                        ),
                        cls='lg:w-2/3 px-6'
                    ),
                    cls='flex flex-wrap lg:flex-nowrap'
                ),
                # Call to action
                Div(
                    Div(
                        P(T.t("cta_title_about_us"), cls='text-2xl font-medium text-center mb-6'),
                        Div(
                            A(
                                T.t("cta_about_us"),
                                href=f'{mod_locale}/contact',
                                cls='bg-blue-800 text-white px-8 py-3 rounded-lg font-medium hover:bg-blue-900 transition-all transform hover:scale-105 inline-block'
                            ),
                            cls='text-center'
                        ),
                        cls='max-w-2xl mx-auto px-4'
                    ),
                    cls='border-t border-gray-200 pt-10 mt-10'
                ),
                cls='max-w-5xl mx-auto px-4 sm:px-6 lg:px-8'
            ),
            cls='py-16 bg-white'
        ),
        ),
        app_footer(T, mod_locale)
    )

@app.get('/')
@app.get("/{lang}/")
def home(request: Request, session, lang: str = None):

    redirect_response, locale = resolve_locale_and_redirect(request, session, lang, '/')
    if redirect_response:
        return redirect_response

    mod_locale = modified_locale(locale)

    # Dictionary of locale strings
    T = Translator(locale)

    return Div(
        app_header(T, current_page="home", mod_locale=mod_locale),
        Main(
            section_hero(T, mod_locale=mod_locale),
            section_mission(T),
            section_portfolio(T),
            section_services(T, mod_locale=mod_locale),
            section_blog(T, mod_locale=mod_locale)
        ),
        app_footer(T, mod_locale)
        )

@app.get('/blog/{url_path}')
@app.get('/{lang}/blog/{url_path}')
def blog_post(request: Request, session, url_path: str, lang: str = None):

    redirect_response, locale = resolve_locale_and_redirect(request, session, lang, f'/blog/{url_path}')
    if redirect_response:
        return redirect_response

    mod_locale = modified_locale(locale)

    # Read the markdown file
    T=Translator(locale)

    blog_dir = "Blog"
    file_path = os.path.join(blog_dir, f"{url_path}.md")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

        return Div(
            app_header(T, current_page=f"blog/{url_path}", mod_locale=mod_locale),
            Article(
                Div(  # Keep outer div for bg-white
                    Div(  # Keep inner div for max-width and padding
                        # Fixed aspect ratio container for the featured image
                        Div(  # Keep this div for image container styling
                            Img(
                                src=post.metadata.get('image', ''),
                                alt=post.metadata['title'],
                                cls='w-full h-full object-cover'  # Same image handling as cards
                            ),
                            cls='w-full h-96 overflow-hidden mb-8'  # Taller height (24rem) for feature image
                        ) if post.metadata.get('image') else None,
                        H1(post.metadata['title'], cls='text-4xl font-bold mb-4'),
                        Header(  # Changed from Div to Header for metadata
                            Time(  # Changed from Span to Time for date
                                post.metadata['date'].strftime('%B %d, %Y') if hasattr(post.metadata['date'], 'strftime') else str(post.metadata['date']),
                                datetime=post.metadata['date'].strftime('%Y-%m-%d') if hasattr(post.metadata['date'], 'strftime') else '',
                                cls='text-gray-600'
                            ),
                            Span(' • ', cls='mx-2 text-gray-400'),
                            Span(f"{post.metadata['readTime']} min read", cls='text-gray-600'),
                            cls='mb-8'
                        ),
                        Section(post.content, cls='marked prose prose-lg max-w-none'),  # Changed from Div to Section
                        cls='max-w-3xl mx-auto px-4 py-12'
                    ),
                    cls='bg-white'
                )
            ),
            app_footer(T, mod_locale)
        )
    except FileNotFoundError:
        return Div(
            app_header(T, current_page=f"blog/{url_path}", mod_locale=mod_locale),
            Div(
                H1("Blog Post Not Found", cls='text-4xl font-bold text-center my-12 text-gray-800'),
                P("We couldn't find the blog post you're looking for.", cls='text-center text-gray-600'),
                cls='max-w-3xl mx-auto px-4 py-12'
            ),
            app_footer(T, mod_locale)
        )

@app.get('/contact')
@app.get('/{lang}/contact')
def contact(request: Request, session, lang: str = None):

    redirect_response, locale = resolve_locale_and_redirect(request, session, lang, '/contact')
    if redirect_response:
        return redirect_response

    mod_locale = modified_locale(locale)

    T = Translator(locale)
    return Div(
        Div(  # Wrapper div with flex column
            app_header(T, current_page="contact", mod_locale=mod_locale),
            Section(
                Div(
                    # Contact card
                    Div(
                        Div(
                            # Title and description inside the card
                            H1(T.t("contact_us_title"), cls='text-5xl font-semibold text-center mb-6'),
                            P(T.t("contact_us_description"), 
                              cls='text-gray-600 mb-8 text-center max-w-xl mx-auto text-2xl'),

                            # Divider
                            Div(cls='border-t border-gray-100 mb-8'),

                            # Email section
                            H2(T.t("contact_us_email_title"), cls='font-medium mb-3 text-center text-2xl text-gray-700'),
                            A('info@aipetech.com',
                              href='mailto:info@aipetech.com',
                              cls='text-blue-600 hover:text-blue-800 text-2xl font-medium block text-center hover:scale-105 transition-transform'  # Reduced from text-3xl to text-2xl
                            ),
                            cls='text-center'
                        ),
                        cls='bg-white rounded-lg shadow-lg p-10 max-w-2xl mx-auto border border-gray-100'
                    ),
                    cls='max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-center h-full'
                ),
                cls='py-20 bg-gray-50 flex-grow flex items-center'
            ),
            app_footer(T, mod_locale),
            cls='min-h-screen flex flex-col'
        )
    )

# Handler for setting language in session
@app.post("/set-language")
def set_language(request: Request, language: str, redirect: str, session):
    session['language'] = language
    response = Response()
    response.headers["HX-Redirect"] = redirect
    return response

if __name__ == "__main__":
    # Generate sitemap
    from sitemap import sitemap
    sitemap()

    # Start server
    serve(host='0.0.0.0', port=8080, reload=False)