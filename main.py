from fasthtml.common import *
import os
import frontmatter  # you'll need to install python-frontmatter
from dotenv import load_dotenv
from sitemap import sitemap
# Load environment variables
load_dotenv()

# Get environment variables
ga_id = os.getenv('GOOGLE_ANALYTICS_ID')
cookiebot_id = os.getenv('COOKIEBOT_ID')

socials = Socials(title="AIPE Technology", description="Consulting firm turning AI potential into working business solutions", site_name='www.aipe.tech', image='https://www.aipe.tech/assets/images/aipe_technology_screen.png', url='https://www.aipe.tech')

tailwind_css = Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css")

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
""")

headers =   (Meta(name="robots", content="index, follow"),
            MarkdownJS(),
            socials,
            Favicon('/assets/images/favicon.ico', '/assets/images/favicon.ico'),
            tailwind_css,
            custom_css,
            #picolink,
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
  }, { threshold: 0.2 });
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
        // Only add animation if it doesn't already have a specific delay
        if (!el.classList.contains('animate-fade-in-delay-1') && 
            !el.classList.contains('animate-fade-in-delay-2') && 
            !el.classList.contains('animate-fade-in-delay-3') &&
            !el.classList.contains('animate-fade-in-delay-4') && 
            !el.classList.contains('animate-fade-in-delay-5') && 
            !el.classList.contains('animate-fade-in-delay-6') &&
            !el.classList.contains('animate-fade-in-delay-7') && 
            !el.classList.contains('animate-fade-in-delay-8')) {
          el.classList.add('animate-fade-in');
        }
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
""")
            )

app = FastHTML(hdrs=headers, title="AIPE Technology")

@app.get("/{fname:path}.xml")
def get_xml(fname: str):
    return FileResponse(f"{fname}.xml")

@app.get("/{fname:path}.{ext:static}")
def get(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

def app_header():
   return Header(
       Div(
           # Logo on the far left
           A(
               Img(
                   src='/assets/images/aipe_logo_white.svg',
                   alt='AIPE Logo',
                   cls='h-6 sm:h-7 w-auto'
               ),
               href='/',
               cls='no-underline ml-3 sm:ml-5'
           ),
           # Navigation items on the right
           Nav(
               A('Home', href='/', cls='text-white hover:text-blue-200 mx-2 sm:mx-4'),
               A('Services', href='/#services', cls='text-white hover:text-blue-200 mx-2 sm:mx-4'),
               A(
                   Span('About', cls='sm:hidden'),
                   Span('About us', cls='hidden sm:inline'),
                   href='/about', 
                   cls='text-white hover:text-blue-200 mx-2 sm:mx-4'
               ),
               A('Blog', href='/blog', cls='text-white hover:text-blue-200 mx-2 sm:mx-4'),
               A('Contact',
                 href='/contact',
                 cls='bg-white text-blue-800 px-3 sm:px-4 py-1.5 rounded-lg hover:bg-blue-100 ml-2 sm:ml-4 mr-3 sm:mr-5'
               ),
               cls='flex items-center text-sm sm:text-base'
           ),
           cls='flex justify-between items-center py-1.5 sm:py-2 w-full'
       ),
       cls='border-b border-blue-800 bg-blue-800 w-full'
   )

def section_hero():
    return Section(
        Div(
            H1(
                Span('Bridging the AI adoption gap.', cls='text-blue-800'),
                cls='text-4xl font-bold sm:text-5xl mb-8 animate-fade-in'
            ),
            P('At AIPE Technology, we show you what is possible and give you clear guidance on how to make AI part of your core business.',
              cls='mt-16 text-2xl text-gray-800 font-semibold mb-16 max-w-4xl animate-fade-in-delay-1'),
            P(
                Span('Why choose us ', cls='font-semibold'),
                'We don\'t just talk about AI possibilities - we build working proof. Here\'s how we turn your challenges into working solutions:',
                cls='text-xl text-gray-600 mb-24 max-w-4xl animate-fade-in-delay-2'
            ),
            # Three-step process cards
            Div(
                # Step 1: Discover (Left - appears first)
                Div(
                    Div(
                        Img(
                            src="/assets/images/oui--app-search-profiler.svg",
                            alt="Discover",
                            cls='w-16 h-16 mx-auto mb-4 text-blue-800'
                        ),
                        cls='text-center'
                    ),
                    H3(
                        'Discover',
                        cls='text-2xl font-semibold text-blue-800 mb-3'
                    ),
                    P(
                        'Identify where AI can create meaningful impact for your business.',
                        cls='text-gray-600 text-lg'
                    ),
                    cls='text-center p-8 bg-white rounded-xl shadow-sm border border-gray-200 hover:shadow-md transition-shadow duration-200 animate-fade-in-delay-3'
                ),
                # Step 2: Validate (Center - appears second)
                Div(
                    Div(
                        Img(
                            src="/assets/images/oui--check-in-circle-empty.svg",
                            alt="Validate",
                            cls='w-16 h-16 mx-auto mb-4 text-blue-800'
                        ),
                        cls='text-center'
                    ),
                    H3(
                        'Validate',
                        cls='text-2xl font-semibold text-blue-800 mb-3'
                    ),
                    P(
                        'Build a working proof of concept for your specific challenge.',
                        cls='text-gray-600 text-lg'
                    ),
                    cls='text-center p-8 bg-white rounded-xl shadow-sm border border-gray-200 hover:shadow-md transition-shadow duration-200 animate-fade-in-delay-4'
                ),
                # Step 3: Scale (Right - appears third)
                Div(
                    Div(
                        Img(
                            src="/assets/images/oui--rocket.svg",
                            alt="Scale",
                            cls='w-16 h-16 mx-auto mb-4 text-blue-800'
                        ),
                        cls='text-center'
                    ),
                    H3(
                        'Scale',
                        cls='text-2xl font-semibold text-blue-800 mb-3'
                    ),
                    P(
                        'Implement the validated solution across your organization.',
                        cls='text-gray-600 text-lg'
                    ),
                    cls='text-center p-8 bg-white rounded-xl shadow-sm border border-gray-200 hover:shadow-md transition-shadow duration-200 animate-fade-in-delay-5'
                ),
                cls='grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mb-24'
            ),
            Div(
                A(
                    'Book a consultation ',
                    Span('→', cls='ml-2'),
                    href='/contact',
                    cls='bg-blue-800 text-white px-8 py-3 rounded-lg font-medium hover:bg-blue-900 transition-all transform hover:scale-105 inline-block'
                ),
                cls='mt-20 text-center animate-fade-in-delay-6'
            ),
            cls='max-w-5xl mx-auto px-6'
        ),
        cls="py-20 bg-gray-50"
    )

def section_mission():
    return Section(
        Div(
            P(
                'Our Mission',
                cls='text-3xl text-gray-600 mb-6 max-w-2xl mx-auto text-center animate-on-scroll'
            ),
            H2(
                'We help clients scaling faster and smarter with AI.',
                cls='text-5xl font-semibold text-gray-900 mb-4 text-center animate-on-scroll'
            ),
        ),
        cls='py-32', id="mission-section"
    )

def portfolio_card(portfolio_element):
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
                    #cls='w-full h-full rounded-lg'
                ),
                #cls='w-full pb-[56.25%] relative border border-gray-300'  # Added border
                cls='w-full pb-[50%] relative border border-gray-300'  # Reduced from pb-[56.25%] to pb-[50%]
            )
        else:
            # No video - use PNG placeholder
            return Div(
                Img(
                    src="/assets/videos/placeholder.png",
                    alt="Project placeholder",
                    cls='w-full h-full object-cover rounded-lg'
                ),
                cls='w-full pb-[50%] relative border border-gray-300'  # Reduced from pb-[56.25%] to pb-[50%]
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
            H3(portfolio_element["title"], cls='text-xl font-semibold text-blue-800'),
            cls='mb-3'
        ),
        # Description
        Div(
            P(
                portfolio_element["description"],
                *link_buttons,
                cls='text-gray-600'
            ),
            cls='mb-4 flex-grow'  # flex-grow takes available space
        ),
        # Video element (fixed size)
        create_video_element(),
        cls='bg-white rounded-lg p-5 shadow-sm border border-gray-100 hover:shadow-md transition-shadow duration-200 h-full flex flex-col animate-on-scroll'  # Reduced padding from p-6 to p-5
    )

def section_portfolio():
    portfolio = [
    {
        "category": "Investment Tools",
        "title": "CIM Data Extraction Platform",
        "description": "Extract structured financial data from CIMs with intelligent copy-paste. Numbers automatically format for Excel, text stays clean.",
        "links": {
            "Video": "cim-data-extraction-platform.mp4",
            "GitHub": "https://github.com/feldges/data_extractor",
            "Demo": "tbd"
                }
    },
    {
        "category": "Investment Tools",
        "title": "Comprehensive PE Due Diligence Assistant",
        "description": "End-to-end due diligence automation: upload documents, extract data, run analysis, generate Word reports. Fully customizable with visual controls and user oversight at each step.",
        "links": {
            "Video": "comprehensive-pe-due-diligence-assistant.mp4",
            "GitHub": "tbd",
            "Demo": "tbd"
                }
    },
    {
        "category": "Investment Tools",
        "title": "M&A Target Research Intelligence",
        "description": "Automated LinkedIn research for target companies. Select roles, get curated profile lists, reorder by relevance, export to Excel. Simple interface, full user control.",
        "links": {
            "Video": "m-and-a-target-research-intelligence.mp4",
            "GitHub": "tbd",
            "Demo": "tbd"
                }
    },
        {
        "category": "Investment Tools",
        "title": "Investment Research Analyst",
        "description": "AI-Powered investment research analyst with access to the web. Generates an investment report. Based on Stanford's STORM framework.",
        "links": {
            "Video": "investment-research-analyst.mp4",
            "GitHub": "https://github.com/feldges/storm",
            "Demo": "https://storm.aipe.tech/"
                }
    },
    {
        "category": "Business Automation",
        "title": "Treasury Invoice Translation System",
        "description": "Upload non-English invoices, view original and translated versions side-by-side, extract key data (date, amount, bank details). For centralized payment teams.",
        "links": {
            "Video": "",
            "GitHub": "tbd",
            "Demo": "tbd"
                }
    },
    {
        "category": "Business Automation",
        "title": "Work Smarter AI - Document Intelligence",
        "description": "AI assistant seamlessly integrated into Microsoft Word for intelligent document tasks. Automates formatting, content generation, and document analysis. Brings powerful AI capabilities directly to where people work, enhancing productivity without disrupting existing workflows.",
        "links": {
            "Video": "work-smarter-ai-document-intelligence.mp4",
            "GitHub": "tbd",
            "Demo": "tbd"
                }
    },
    {
        "category": "Business Automation",
        "title": "Dynamic Pricing Intelligence Platform",
        "description": "Browser automation proof-of-concept using AI agents to extract hidden dynamic pricing. Demonstrates automated data collection capabilities for price transparency.",
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
                'Projects Portfolio',
                cls='text-5xl font-semibold text-gray-900 mb-6 text-center animate-on-scroll'
            ),
            P(
                'Real demonstrations of AI solving practical business problems.',
                cls='text-3xl text-gray-600 mb-8 max-w-3xl mx-auto text-center animate-on-scroll'
            ),
            # Create sections for each category
            *[Div(
                # Category section with frame only (no background)
                Div(
                    # Category header
                    H3(
                        category,
                        cls='text-2xl font-semibold text-blue-800 mb-8 animate-on-scroll'
                    ),
                    # Portfolio cards in a grid
                    Div(
                        *[portfolio_card(item) for item in items],
                        cls='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5 auto-rows-fr'  # Reduced gap from gap-6 to gap-5
                    ),
                    cls='p-6 rounded-lg border border-gray-200'  # Reduced padding from p-8 to p-6
                ),
                cls='mb-8 animate-on-scroll'
            ) for category, items in portfolio_by_category.items()],
            cls='max-w-6xl mx-auto px-4 sm:px-6 lg:px-8'
        ),
        cls='py-16 bg-gray-50', id="portfolio-section"
    )

def benefit_item(text):
    return Li(
        Div(
            # Simple blue checkmark without circle
            Div(
                "✓",
                cls='text-blue-500 text-lg mr-3 flex-shrink-0'  # Clean, elegant checkmark
            ),
            # Text content
            Div(
                text,
                cls='ml-4 text-gray-900 flex-grow'
            ),
            cls='flex items-center py-2'
        ),
        cls='transform transition-transform duration-200 hover:translate-x-2 list-none'
    )

def solution_card(title, description, animate_class=None):
    return Div(
        H3(title, cls='text-2xl font-semibold text-blue-800 mb-4 text-center'),
        P(description, cls='text-gray-600 text-lg mb-4 text-justify'),
        cls=f'bg-white rounded-lg p-8 shadow-sm border border-gray-200 hover:shadow-md transition-shadow duration-200 {animate_class if animate_class else ""}'
    )

def section_services():
    return Section(
        Div(
            H2(
                'Services',
                cls='text-5xl font-semibold text-gray-900 mb-6 text-center animate-on-scroll animate-fade-in-delay-1'
            ),
            P(
                'We follow a systematic approach to AI implementation, designed to minimize risk and maximize impact.',
                cls='text-3xl text-gray-600 mb-8 max-w-3xl mx-auto text-center animate-on-scroll animate-fade-in-delay-2'
            ),
            # Services grid - three cards
            Div(
                solution_card(
                    title='Discover',
                    description='We start by understanding your specific business challenges and operational bottlenecks. Through focused consultation, we identify where AI can create the most meaningful impact for your organization and define clear success criteria for moving forward.',
                    animate_class='animate-on-scroll animate-fade-in-delay-3'
                ),
                solution_card(
                    title='Validate',
                    description='We build a working proof of concept tailored to your identified challenge. In 2-4 weeks, you\'ll interact with a functional AI solution addressing your specific use case, allowing you to experience the potential impact before making larger commitments.',
                    animate_class='animate-on-scroll animate-fade-in-delay-4'
                ),
                solution_card(
                    title='Scale',
                    description='Once the proof of concept demonstrates clear value, we work with you to implement the validated solution across your organization. From solution refinement to full deployment, we ensure smooth integration with your existing processes and systems.',
                    animate_class='animate-on-scroll animate-fade-in-delay-5'
                ),
                cls='grid md:grid-cols-3 gap-8 mt-12 max-w-7xl mx-auto'
            ),
            # Services CTA section
            Div(
                Div(
                    H3('Looking for Expert Guidance?', 
                       cls='text-4xl font-semibold text-center mb-6 animate-on-scroll animate-fade-in-delay-6'),
                    P('Book a consultation to discuss how we can help automate your business processes.',
                      cls='text-gray-600 text-xl text-center mb-8 animate-on-scroll animate-fade-in-delay-7'),
                    Div(
                        A('Book a Consultation →',
                          href='/contact',
                          cls='bg-blue-800 text-white px-8 py-3 rounded-lg font-medium hover:bg-blue-900 transition-all transform hover:scale-105 inline-block animate-on-scroll animate-fade-in-delay-8'
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

def app_footer():
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
                            href='/',
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
                        A('Home', href='/', cls='text-gray-300 hover:text-white'),
                        A('Services', href='/#services', cls='text-gray-300 hover:text-white'),
                        A('About us', href='/about', cls='text-gray-300 hover:text-white'),
                        A('Blog', href='/blog', cls='text-gray-300 hover:text-white'),
                        A('Contact', href='/contact', cls='text-gray-300 hover:text-white'),
                        cls='space-y-2 flex flex-col items-center md:items-end'
                    ),
                    cls='grid grid-cols-1 md:grid-cols-3 gap-8 pt-12 pb-8'
                ),
            ),
            # Bottom footer with more subtle styling
            Div(
                Div(
                    P(
                        '© 2025 AIPE Technology. All rights reserved.',
                        cls='text-gray-400 text-sm text-center md:text-left'  # Changed from text-xs to text-sm
                    ),
                    Div(
                        A('Privacy Policy', 
                          href='/privacy_policy', 
                          cls='text-gray-300 hover:text-white text-sm font-medium'),
                        Span('•', cls='mx-2 text-gray-400 text-sm'),  # Updated dot styling
                        A('Terms of Service', 
                          href='/terms_of_service', 
                          cls='text-gray-300 hover:text-white text-sm font-medium'),
                        Span('•', cls='mx-2 text-gray-400 text-sm'),  # Updated dot styling
                        Span('By using this website, you accept our terms and privacy policy.', 
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

def app_body():
    return H2(f"Welcome to the application")

def blog_card(title, date, description, image_url, url_path, animate=False, animate_class=None):
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
                'Read more',
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

def section_blog():
    blog_posts = get_blog_posts()

    return Section(
        Div(
            H2(
                'Latest Insights',
                cls='text-5xl font-semibold text-gray-900 mb-6 text-center animate-on-scroll'
            ),
            P(
                'Stay updated with our latest thoughts on AI and its implementation, and industry trends.',
                cls='text-center text-gray-600 text-3xl mb-8 max-w-3xl mx-auto animate-on-scroll'
            ),
            # Blog cards container - each card gets a different animation class
            Div(
                *[blog_card(
                    title=post['title'],
                    date=post['date'],
                    description=post['description'],
                    image_url=post['image_url'],
                    url_path=post['url_path'],
                    animate_class=f'animate-on-scroll animate-fade-in-delay-{i+1}'  # Different delay for each card
                ) for i, post in enumerate(blog_posts[:3])],
                cls='grid grid-cols-1 md:grid-cols-3 gap-8 max-w-7xl mx-auto'
            ),
        ),
        cls='py-16 bg-gray-50', id="blog-section"
    )

@app.get('/blog')
def blog_index():
    blog_posts = get_blog_posts()

    return Div(
        app_header(),
        Section(
            Div(
                H1('Blog', cls='text-5xl font-semibold text-gray-900 mb-6 text-center'),
                P(
                    'Explore our latest insights on AI, AI implementation, and industry trends.',
                    cls='text-center text-gray-600 text-3xl mb-8 max-w-3xl mx-auto'
                ),
                # Change to grid layout like main page
                Div(
                    *[blog_card(
                        title=post['title'],
                        date=post['date'].strftime('%B %d, %Y') if hasattr(post['date'], 'strftime') else str(post['date']),
                        description=post['description'],
                        image_url=post['image_url'],
                        url_path=post['url_path']
                    ) for post in blog_posts],
                    cls='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-7xl mx-auto'
                ),
                cls='px-4 sm:px-6 lg:px-8'
            ),
            cls='py-16'
        ),
        app_footer()
    )

def privacy_policy_content():
    with open('assets/legal/privacy_policy.md', 'r') as file:
        PRIVACY_POLICY = file.read()
        return Div(
            Div(  # Added wrapper div for centering
                PRIVACY_POLICY,
                cls='marked prose prose-lg max-w-3xl mx-auto px-4'  # Added centering classes
            ),
            cls='py-12'  # Added vertical padding
        )

def terms_of_service_content():
    with open('assets/legal/terms_of_service.md', 'r') as file:
        TERMS_OF_SERVICE = file.read()
        return Div(
            Div(  # Added wrapper div for centering
                TERMS_OF_SERVICE,
                cls='marked prose prose-lg max-w-3xl mx-auto px-4'  # Added centering classes
            ),
            cls='py-12'  # Added vertical padding
        )

@app.get('/terms_of_service')
def terms_of_service():
    return Div(
        app_header(),
        terms_of_service_content(),
        app_footer()
    )

@app.get('/privacy_policy')
def privacy_policy():
    return Div(
        app_header(),
        privacy_policy_content(),
        app_footer()
    )

@app.get('/about')
def about():
    return Div(
        app_header(),
        Main(
        Section(
            Div(
                H1('About', cls='text-5xl font-semibold text-gray-900 mb-8 text-center'),  # Increased from text-4xl
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
                                Span('Dr. Claude Feldges', cls='font-medium block text-2xl'),  # Increased from text-xl
                                cls='text-center text-gray-700 mb-6'
                            ),
                            Div(
                                A(
                                    Div(
                                        Img(
                                            src='/assets/images/linkedin.svg?v=2',
                                            alt='Connect with Claude Feldges on LinkedIn',
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
                        H3('Combining Technical Expertise with Industry Knowledge', cls='text-2xl font-semibold text-blue-800 mb-6'),  # Increased from text-xl and mb-4
                        P(
                            'As a leader in applying AI technologies to private markets, '
                            'I bridge the gap between technical implementation and '
                            'industry-specific knowledge. With over 15 years of experience '
                            'at Partners Group AG, a global leader and innovator in private '
                            'markets, I combine deep industry expertise with strong '
                            'quantitative skills from my PhD in Physics to bring a unique '
                            'perspective to digital transformation in the private markets industry.',
                            cls='text-gray-700 mb-6 text-lg'  # Increased from mb-4 and added text-lg
                        ),
                        P(
                            'My hands-on experience spans from building enterprise AI '
                            'solutions to optimizing investment processes. Throughout my '
                            'career, I\'ve successfully implemented GenAI strategies and '
                            'developed solutions that streamline investment processes.',
                            cls='text-gray-700 mb-6 text-lg'  # Increased from mb-4 and added text-lg
                        ),
                        P(
                            'Driven by a passion for innovation and a vision for the future '
                            'of private markets, I left my role at Partners Group to found '
                            'AIPE Technology. I believe in the transformative potential of '
                            'AI to enhance investment decision-making while maintaining the '
                            'crucial element of human judgment.',
                            cls='text-gray-700 mb-6 text-lg'  # Increased from mb-4 and added text-lg
                        ),
                        P(
                            'At AIPE Technology, I stay at the forefront of AI innovation '
                            'in private markets, creating solutions that generate real business value '
                            'for investment and operational teams while maintaining human oversight.',
                            cls='text-gray-700 mb-6 text-lg'  # Increased from mb-4 and added text-lg
                        ),
                        H3('Why Work With Me', cls='text-2xl font-semibold text-blue-800 mt-8 mb-6'),  # Increased from text-xl, mt-6 to mt-8, mb-4 to mb-6
                        Div(
                            *[Div(
                                Div(
                                    # Simple blue checkmark without circle
                                    Div(
                                        "✓",
                                        cls='text-blue-500 text-xl mr-3 flex-shrink-0'  # Increased from text-lg
                                    ),
                                    # Point text
                                    Div(
                                        text,
                                        cls='ml-4 text-gray-900 flex-grow text-lg'  # Added text-lg
                                    ),
                                    cls='flex items-center py-3'  # Increased from py-2
                                ),
                                cls='transform transition-transform duration-200 hover:translate-x-2 list-none'
                            ) for text in [
                                "Practical Experience: From concept to implementation, I've built systems that drive real business value",
                                "Private Markets Expertise: Deep understanding of investment processes, challenges, and opportunities",
                                "Technical Depth: From data science to full-stack development, I speak both business and technology",
                                "Education Focus: Proven track record of training technical teams and driving AI adoption"
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
                        P('Ready to transform your investment processes with AI?', cls='text-2xl font-medium text-center mb-6'),  # Increased from text-xl and mb-5
                        Div(
                            A(
                                'Schedule a Consultation →',
                                href='/contact',
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
        app_footer()
    )

@app.get('/')
def home():
    return Div(
        app_header(),
        Main(
            section_hero(),
            section_mission(),
            section_portfolio(),
            section_services(),
            section_blog()
        ),
        app_footer()
        )

@app.get('/blog/{url_path}')
def blog_post(url_path: str):
    # Read the markdown file
    blog_dir = "Blog"
    file_path = os.path.join(blog_dir, f"{url_path}.md")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

        return Div(
            app_header(),
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
            app_footer()
        )
    except FileNotFoundError:
        return Div(
            app_header(),
            Div(
                H1("Blog Post Not Found", cls='text-4xl font-bold text-center my-12 text-gray-800'),
                P("We couldn't find the blog post you're looking for.", cls='text-center text-gray-600'),
                cls='max-w-3xl mx-auto px-4 py-12'
            ),
            app_footer()
        )

@app.get('/contact')
def contact():
    return Div(
        Div(  # Wrapper div with flex column
            app_header(),
            Section(
                Div(
                    # Contact card
                    Div(
                        Div(
                            # Title and description inside the card
                            H1('Contact Us', cls='text-5xl font-semibold text-center mb-6'),
                            P('We\'d love to hear from you and discuss how we can help with your investment process.', 
                              cls='text-gray-600 mb-8 text-center max-w-xl mx-auto text-2xl'),

                            # Divider
                            Div(cls='border-t border-gray-100 mb-8'),

                            # Email section
                            H2('Email Us', cls='font-medium mb-3 text-center text-2xl text-gray-700'),
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
            app_footer(),
            cls='min-h-screen flex flex-col'
        )
    )

if __name__ == "__main__":
    # Generate sitemap
    from sitemap import sitemap
    sitemap()

    # Start server
    serve(host='0.0.0.0', port=8080, reload=False)