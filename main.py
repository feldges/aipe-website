from fasthtml.common import *
from monsterui.all import *  # Added MonsterUI import
import os
import frontmatter  # you'll need to install python-frontmatter

socials = Socials(title="AIPE Technology", description="Intelligent Deal Screening and Due Diligence for Private Markets", site_name='www.aipe.tech', image='https://www.aipe.tech/assets/images/aipe_technology_screen.png', url='https://www.aipe.tech')

tailwind_css = Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css")
headers =   (Meta(name="robots", content="noindex, nofollow"),
            MarkdownJS(),
            socials,
            Favicon('/assets/images/favicon.ico', '/assets/images/favicon.ico'),
            tailwind_css,
            picolink,
            )

app = FastHTML(hdrs=headers, title="AIPE Technology")

@app.get("/{fname:path}.{ext:static}")
def get(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

def app_header():
   return Div(
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
           Div(
               A('Home', href='/', cls='text-white hover:text-blue-200 mx-2 sm:mx-4'),
               A('Products', href='/#products', cls='text-white hover:text-blue-200 mx-2 sm:mx-4'),
               A('Services', href='/#services', cls='text-white hover:text-blue-200 mx-2 sm:mx-4'),
               A('About', href='/about', cls='text-white hover:text-blue-200 mx-2 sm:mx-4'),
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
    return Header(
        Div(
            H1(
                Span('AIPE Technology', cls='text-blue-800'),
                cls='text-4xl font-bold sm:text-5xl'
            ),
            P('Technology Solutions for Private Markets',
              cls='mt-4 text-2xl text-gray-800 font-semibold mb-2 max-w-2xl mx-auto'),
            P('Practical solutions that scale your operations',
              cls='text-xl text-gray-600 mb-4 max-w-2xl mx-auto'),
            Div(
                A(
                    'Schedule Demo ',
                    Span('→', cls='ml-2'),
                    href='/contact',
                    cls='bg-blue-800 text-white px-8 py-3 rounded-lg font-medium hover:bg-blue-900 transition-all transform hover:scale-105 inline-block'
                ),
                cls='mt-8'
            ),
            cls='max-w-5xl mx-auto px-6 text-center'
        ),
        cls="py-20 bg-gray-50"
    )

def challenge_category(title, points):
    return Div(
        H3(title, cls='text-xl font-semibold text-blue-800 mb-4'),
        Ul(
            *[Li(
                Div(
                    # Simple blue checkmark without circle
                    Div(
                        "✓",
                        cls='text-blue-500 text-lg mr-3 flex-shrink-0'  # Clean, elegant checkmark
                    ),
                    # Text in black
                    Div(
                        text,
                        cls='ml-4 text-gray-900 flex-grow'
                    ),
                    cls='flex items-center py-2'
                ),
                cls='transform transition-transform duration-200 hover:translate-x-2 list-none'
            ) for text in points],
            cls='space-y-2'
        ),
        cls='bg-white rounded-lg p-6 shadow-sm border border-gray-100 hover:shadow-md transition-shadow duration-200'
    )

def section_challenges():
    challenges = [
        {
            "title": "Investment Challenges",
            "points": [
                "AI revolution is disrupting traditional investment processes",
                "Risk of losing competitive edge to tech-enabled competitors",
                "Challenge of leveraging technology whil maintaining investment unique approach"
            ]
        },
        {
            "title": "Private Wealth Evolution",
            "points": [
                "Rising private wealth participation driving need for automation",
                "Increased frequency of valuations and reporting",
                "Need to serve more investors efficiently"
            ]
        },
        {
            "title": "Operational & Compliance",
            "points": [
                "Growing operational complexity and regulatory demands",
                "Need to scale operations without proportional team growth",
                "Complex compliance and oversight requirements"
            ]
        }
    ]

    return Section(
        Div(
            H2(
                'Key Challenges',
                cls='text-3xl font-semibold text-gray-900 mb-4 text-center'
            ),
            P(
                'The private markets industry faces transformative challenges that require innovative solutions.',
                cls='text-center text-gray-600 mb-8 max-w-2xl mx-auto'
            ),
            # Challenge categories in a grid
            Div(
                *[challenge_category(c["title"], c["points"]) for c in challenges],
                cls='grid md:grid-cols-3 gap-6'
            ),
            cls='max-w-6xl mx-auto px-4 sm:px-6 lg:px-8'
        ),
        cls='py-16'
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

def solution_card(title, description, benefits):
    return Div(
        H3(title, cls='text-xl font-semibold text-blue-800 mb-4'),
        Ul(
            *[Li(
                Div(
                    # Simple blue checkmark without circle
                    Div(
                        "✓",
                        cls='text-blue-500 text-lg mr-3 flex-shrink-0'
                    ),
                    # Benefit text
                    Div(
                        benefit,
                        cls='ml-4 text-gray-900 flex-grow'
                    ),
                    cls='flex items-center py-2'
                ),
                cls='transform transition-transform duration-200 hover:translate-x-2 list-none'
            ) for benefit in benefits],
            cls='space-y-2'
        ),
        cls='bg-white rounded-lg p-6 shadow-sm border border-gray-100 hover:shadow-md transition-shadow duration-200'
    )

def horizontal_scroll_container(items):
    """Create a container showing exactly three case studies"""
    return Div(
        # Heading for the case studies section
        Div(
            H3('Case Studies', cls='text-2xl font-semibold text-center mb-4'),
            P('Real examples of how our consulting expertise has helped clients', 
              cls='text-center text-gray-600'),
            cls='mb-6'
        ),
        
        # Grid container showing exactly 3 items
        Grid(
            *items[:3],  # Take first 3 items
            cols=3,      # 3 columns
            cols_md=2,   # 2 columns on medium screens
            cols_sm=1,   # 1 column on small screens
            gap=4,       # Gap between cards
            cls='max-w-6xl mx-auto'
        ),
        
        cls='max-w-6xl mx-auto mt-8 mb-8 px-4'
    )

def case_study_card(title, client_type, challenge, solution, results, image_path=None):
    """Create a case study card with consistent styling"""
    return Card(
        # Card content
        Div(
            # Optional image at top
            Div(
                Img(
                    src=image_path,
                    alt=f"{title} illustration",
                    cls='w-full h-24 object-cover rounded-t-lg'
                ),
                cls='w-full overflow-hidden'
            ) if image_path else None,
            
            # Content section
            Div(
                # Label/Client type
                Div(
                    client_type,
                    cls='text-xs font-medium text-blue-700 bg-blue-100 rounded-full px-3 py-1 inline-block mb-2'
                ),
                
                # Title
                H4(title, cls='text-lg font-semibold text-gray-900 mb-2'),
                
                # Challenge section
                Div(
                    P(Span('Challenge: ', cls='font-medium text-gray-800'), cls='text-sm mb-1'),
                    P(challenge, cls='text-sm text-gray-600 mb-2'),
                    cls='mb-2'
                ),
                
                # Solution section
                Div(
                    P(Span('Solution: ', cls='font-medium text-gray-800'), cls='text-sm mb-1'),
                    P(solution, cls='text-sm text-gray-600 mb-2'),
                    cls='mb-2'
                ),
                
                # Results section
                Div(
                    P(Span('Results: ', cls='font-medium text-gray-800'), cls='text-sm mb-1'),
                    P(results, cls='text-sm text-gray-600'),
                ),
                
                cls='p-4'
            ),
        ),
        # Using MonsterUI Card component with hover effect
        cls='h-full transform transition-all duration-200 hover:scale-[1.02] w-full'
    )

def section_products():
    return Section(
        Div(
            H2(
                'Our Products',
                cls='text-3xl font-semibold text-gray-900 mb-4 text-center'
            ),
            P(
                'AI-powered solutions that streamline your investment process while maintaining human oversight.',
                cls='text-center text-gray-600 mb-8 max-w-2xl mx-auto'
            ),
            # Product cards grid
            Div(
                solution_card(
                    title='Deal Screening',
                    description='Automated initial assessment of investment opportunities.',
                    benefits=[
                        "Process hundreds of web pages in minutes",
                        "Generate comprehensive IC memos",
                        "Quick go/no-go assessment capabilities"
                    ]
                ),
                solution_card(
                    title='Due Diligence',
                    description='Intelligent data room analysis and thesis development.',
                    benefits=[
                        "Automated data extraction from data rooms",
                        "Investment thesis development with AI",
                        "IC report generation in minutes"
                    ]
                ),
                cls='grid lg:grid-cols-2 gap-12 mt-8 max-w-6xl mx-auto'
            ),
            # Product CTA section
            Div(
                Div(
                    H3('Ready to See Our Products in Action?', 
                       cls='text-2xl font-semibold text-center mb-4'),
                    P('Schedule a demo to see how our AI-powered solutions can transform your investment process.',
                      cls='text-gray-600 text-center mb-6'),
                    Div(
                        A('Schedule Demo →',
                          href='/contact',
                          cls='bg-blue-800 text-white px-8 py-3 rounded-lg font-medium hover:bg-blue-900 transition-all transform hover:scale-105 inline-block'
                        ),
                        cls='text-center'
                    ),
                    cls='max-w-2xl mx-auto px-4'
                ),
                cls='border-t border-gray-200 pt-8 mt-8'
            ),
            cls='max-w-5xl mx-auto px-4 sm:px-6 lg:px-8'
        ),
        cls='py-16 bg-gray-50', id="products"
    )

def challenge_item(title, body, tag):
    """Template for a single challenge item with asset class tag"""
    return Div(
        Div(
            # Container for title and tag with minimal spacing
            Div(
                # Title container that can wrap
                Div(
                    H3(title, 
                       cls="text-xl font-semibold text-blue-800 pr-4"),
                    cls="flex-grow"
                ),
                # Tag display with more subtle styling
                Span(
                    tag,
                    cls="text-xs font-medium text-blue-600 bg-blue-50 rounded-full px-3 py-1 flex-shrink-0"
                ),
                cls="flex items-start justify-between"  # Removed mb-1 completely
            ),
            # Body with reduced top spacing
            P(body,
              cls="text-gray-600 mt-1 mb-4"),  # Added mt-1 for minimal space after title
        ),
        cls="relative hover:translate-x-1 transition-transform duration-200"
    )

def section_services():
    return Section(
        Div(
            H2(
                'Consulting Services',
                cls='text-3xl font-semibold text-gray-900 mb-4 text-center'
            ),
            P(
                'Drawing from successful implementations at leading private markets firms, '
                'we offer expert guidance in three key areas:',
                cls='text-center text-gray-600 mb-8 max-w-2xl mx-auto'
            ),
            # Services grid - three cards
            Div(
                solution_card(
                    title='Investment Process Automation',
                    description='Automate core investment activities.',
                    benefits=[
                        "Deal screening and due diligence automation",
                        "Comparables analysis automation",
                        "Asset-specific solutions (PE, Debt, RE)"
                    ]
                ),
                solution_card(
                    title='Operations Scaling & Efficiency',
                    description='Scale your operations effectively.',
                    benefits=[
                        "Private wealth readiness",
                        "Valuation process automation",
                        "Service provider oversight solution"
                    ]
                ),
                solution_card(
                    title='AI Transformation',
                    description='Navigate your AI journey.',
                    benefits=[
                        "Strategic AI roadmap and execution",
                        "Enterprise-wide AI adoption",
                        "Data science team hiring and development"
                    ]
                ),
                cls='grid md:grid-cols-3 gap-6 mt-8 max-w-6xl mx-auto'
            ),
            # Services CTA section
            Div(
                Div(
                    H3('Looking for Expert Guidance?', 
                       cls='text-2xl font-semibold text-center mb-4'),
                    P('Book a consultation to discuss how we can help optimize your investment process.',
                      cls='text-gray-600 text-center mb-6'),
                    Div(
                        A('Book a Consultation →',
                          href='/contact',
                          cls='bg-blue-800 text-white px-8 py-3 rounded-lg font-medium hover:bg-blue-900 transition-all transform hover:scale-105 inline-block'
                        ),
                        cls='text-center'
                    ),
                    cls='max-w-2xl mx-auto px-4'
                ),
                cls='border-t border-gray-200 pt-8 mt-8'
            ),
            cls='max-w-5xl mx-auto px-4 sm:px-6 lg:px-8'
        ),
        cls='py-16 bg-white', id="services"
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
                            Img(
                                src='/assets/images/linkedin_white.svg',
                                alt='LinkedIn',
                                cls='w-6 h-6'
                            ),
                            href='https://linkedin.com/company/aipe-technology-ag',
                            cls='text-gray-300 hover:text-white inline-flex items-center mt-3',
                            target='_blank',
                            rel='noopener noreferrer'
                        ),
                        cls='flex flex-col items-center md:items-center space-y-2'
                    ),
                    # Navigation section
                    Nav(
                        A('Home', href='/', cls='text-gray-300 hover:text-white'),
                        A('Products', href='/#products', cls='text-gray-300 hover:text-white'),
                        A('Services', href='/#services', cls='text-gray-300 hover:text-white'),
                        A('About', href='/about', cls='text-gray-300 hover:text-white'),
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
                        cls='text-gray-400 text-xs text-center md:text-left'  # Added text-xs
                    ),
                    Div(
                        A('Privacy Policy', href='/privacy_policy', cls='text-gray-500 hover:text-gray-300 text-xs'),  # Darker text, smaller size
                        Span('•', cls='mx-2 text-gray-600 text-xs'),  # Adjusted spacing and color
                        A('Terms of Service', href='/terms_of_service', cls='text-gray-500 hover:text-gray-300 text-xs'),
                        Span('•', cls='mx-2 text-gray-600 text-xs'),
                        Span('By using this website, you accept our terms and privacy policy.', 
                             cls='text-gray-500 text-xs'),  # Darker text, smaller size
                        cls='flex items-center justify-center md:justify-end flex-wrap gap-1'  # Reduced gap
                    ),
                    cls='flex flex-col md:flex-row justify-between items-center space-y-1 md:space-y-0'  # Reduced spacing
                ),
                cls='border-t border-gray-800 py-3'  # Reduced padding
            ),
            cls='max-w-6xl mx-auto px-4 sm:px-6 lg:px-8'
        ),
        cls='bg-black'
    )

def app_body():
    return H2(f"Welcome to the application")

def blog_card(title, date, description, image_url, url_path):
    return A(  # Wrap everything in an anchor tag
        Div(
            Div(
                # Image container with fixed aspect ratio
                Div(
                    Img(
                        src=image_url,
                        alt=title,
                        cls='w-full h-full object-cover'
                    ),
                    cls='w-full h-48 overflow-hidden'  # Fixed image height
                ),
                # Content container with fixed heights
                Div(
                    # Date at top
                    Span(date, cls='text-sm text-blue-600 font-medium block mb-2'),
                    # Title with increased height for three lines
                    H3(title,
                       cls='text-xl font-semibold text-gray-900 line-clamp-3 h-24 mb-3'),  # Height for 3 lines
                    # Description with fixed height and increased bottom margin
                    P(description,
                      cls='text-gray-600 line-clamp-2 h-12 mb-6'),  # Changed mb-4 to mb-6 for more space
                    # Read More at bottom
                    Div(
                        Span('Read More'),
                        Span('→', cls='ml-1'),
                        cls='text-blue-800 font-medium group-hover:text-blue-600 flex items-center'
                    ),
                    cls='p-6'
                ),
                cls='bg-white rounded-lg border border-gray-200'
            ),
            cls='p-[1px] bg-gradient-to-b from-blue-600/20 to-blue-800/20 rounded-lg'
        ),
        href=f'/blog/{url_path}',
        cls='block group transform transition-all duration-200 hover:scale-[1.02] hover:shadow-lg'
    )

def get_blog_posts():
    blog_posts = []
    blog_dir = "Blog"
    default_image = '/assets/images/blog/default.jpg'  # Create a default image

    for filename in os.listdir(blog_dir):
        if filename.endswith('.md'):
            with open(os.path.join(blog_dir, filename), 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                url_path = filename.replace('.md', '')
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
                cls='text-3xl font-semibold text-gray-900 mb-4 text-center'
            ),
            P(
                'Stay updated with our latest thoughts on AI in private markets, investment automation, and industry trends.',
                cls='text-center text-gray-600 mb-4 max-w-2xl mx-auto'
            ),
            Div(
                # Blog cards container with flex layout
                Div(
                    Div(
                        *[Div(
                            blog_card(
                                title=post['title'],
                                date=post['date'].strftime('%B %d, %Y') if hasattr(post['date'], 'strftime') else str(post['date']),
                                description=post['description'],
                                image_url=post['image_url'],
                                url_path=post['url_path']
                            ),
                            cls='w-full md:w-1/2 lg:w-1/3 px-4 mb-8'  # Changed to w-1/3 for large screens
                        ) for post in blog_posts[:3]],  # Still show 4 posts
                        cls='flex flex-wrap -mx-4'
                    ),
                    cls='max-w-6xl mx-auto'
                ),
                # View All Posts button
                Div(
                    A(
                        'View All Posts →',
                        href='/blog',
                        cls='inline-block mt-8 px-6 py-3 bg-blue-800 text-white rounded-lg hover:bg-blue-900 transition-all transform hover:scale-105'
                    ),
                    cls='text-center mt-8'
                ),
                cls='mt-8'
            ),
            cls='max-w-5xl mx-auto px-4 sm:px-6 lg:px-8'
        ),
        cls='py-16 bg-gray-50'  # Added bg-gray-50 to match Products section
    )

@app.get('/blog')
def blog_index():
    blog_posts = get_blog_posts()

    return Div(
        app_header(),
        Section(
            Div(
                H1('Blog', cls='text-4xl font-bold text-gray-900 mb-4 text-center'),
                P(
                    'Explore our latest insights on AI, AI in private markets, and investment automation.',
                    cls='text-center text-gray-600 mb-8 max-w-2xl mx-auto'
                ),
                # Using a container div with negative margin
                Div(
                    # Using flex with percentage-based widths for Tailwind v2.2.19
                    Div(
                        *[Div(
                            blog_card(
                                title=post['title'],
                                date=post['date'].strftime('%B %d, %Y') if hasattr(post['date'], 'strftime') else str(post['date']),
                                description=post['description'],
                                image_url=post['image_url'],
                                url_path=post['url_path']
                            ),
                            cls='w-full md:w-1/2 lg:w-1/3 px-4 mb-8'
                        ) for post in blog_posts],
                        cls='flex flex-wrap -mx-4'
                    ),
                    cls='max-w-6xl mx-auto'
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
        Section(
            Div(
                H1('About', cls='text-4xl font-bold text-gray-900 mb-8 text-center'),
                # Two-column layout for desktop
                Div(
                    # Left column with photo and quick facts
                    Div(
                        Img(
                            src='/assets/images/feldges.jpg',
                            alt='Dr. Claude Feldges',
                            cls='rounded-full w-48 h-48 object-cover mx-auto mb-6 shadow-lg border-2 border-blue-100'
                        ),
                        Div(
                            P(
                                Span('Dr. Claude Feldges', cls='font-medium block text-xl'),
                                cls='text-center text-gray-700 mb-6'
                            ),
                            Div(
                                A(
                                    Div(
                                        Img(
                                            src='/assets/images/linkedin.svg?v=2',
                                            alt='LinkedIn',
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
                        cls='w-full lg:w-1/3 px-6 mb-8 lg:mb-0 flex flex-col items-center'  # Updated classes
                    ),
                    # Right column with detailed bio
                    Div(
                        H3('Combining Technical Expertise with Industry Knowledge', cls='text-xl font-semibold text-blue-800 mb-4'),
                        P(
                            'As a leader in applying AI technologies to private markets, '
                            'I bridge the gap between technical implementation and '
                            'industry-specific knowledge. With over 15 years of experience '
                            'at Partners Group AG, a global leader and innovator in private '
                            'markets, I combine deep industry expertise with strong '
                            'quantitative skills from my PhD in Physics to bring a unique '
                            'perspective to digital transformation in the private markets industry.',
                            cls='text-gray-700 mb-4'
                        ),
                        P(
                            'My hands-on experience spans from building enterprise AI '
                            'solutions to optimizing investment processes. Throughout my '
                            'career, I\'ve successfully implemented GenAI strategies and '
                            'developed solutions that streamline investment processes.',
                            cls='text-gray-700 mb-4'
                        ),
                        P(
                            'Driven by a passion for innovation and a vision for the future '
                            'of private markets, I left my role at Partners Group to found '
                            'AIPE Technology. I believe in the transformative potential of '
                            'AI to enhance investment decision-making while maintaining the '
                            'crucial element of human judgment.',
                            cls='text-gray-700 mb-4'
                        ),
                        P(
                            'At AIPE Technology, I stay at the forefront of AI innovation '
                            'in private markets, creating solutions that generate real business value '
                            'for investment and operational teams while maintaining human oversight.',
                            cls='text-gray-700 mb-4'
                        ),
                        H3('Why Work With Me', cls='text-xl font-semibold text-blue-800 mt-6 mb-4'),
                        Div(
                            *[Div(
                                Div(
                                    # Simple blue checkmark without circle
                                    Div(
                                        "✓",
                                        cls='text-blue-500 text-lg mr-3 flex-shrink-0'
                                    ),
                                    # Point text
                                    Div(
                                        text,
                                        cls='ml-4 text-gray-900 flex-grow'
                                    ),
                                    cls='flex items-center py-2'
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
                        P('Ready to transform your investment processes with AI?', cls='text-xl font-medium text-center mb-5'),
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
        app_footer()
    )

@app.get('/')
def home():
    return Div(
        app_header(),
        section_hero(),
        section_challenges(),
        section_products(),
        section_services(),
        section_blog(),
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
            Div(
                Div(
                    # Fixed aspect ratio container for the featured image
                    Div(
                        Img(
                            src=post.metadata.get('image', ''),
                            alt=post.metadata['title'],
                            cls='w-full h-full object-cover'  # Same image handling as cards
                        ),
                        cls='w-full h-96 overflow-hidden mb-8'  # Taller height (24rem) for feature image
                    ) if post.metadata.get('image') else None,
                    H1(post.metadata['title'], cls='text-4xl font-bold mb-4'),
                    Div(
                        Span(post.metadata['date'].strftime('%B %d, %Y') if hasattr(post.metadata['date'], 'strftime') else str(post.metadata['date']), cls='text-gray-600'),
                        Span(' • ', cls='mx-2 text-gray-400'),
                        Span(f"{post.metadata['readTime']} min read", cls='text-gray-600'),
                        cls='mb-8'
                    ),
                    Div(post.content, cls='marked prose prose-lg max-w-none'),
                    cls='max-w-3xl mx-auto px-4 py-12'
                ),
                cls='bg-white'
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
                            H1('Contact Us', cls='text-3xl font-bold text-center mb-4'),
                            P('We\'d love to hear from you and discuss how we can help with your investment process.', 
                              cls='text-gray-600 mb-8 text-center max-w-xl mx-auto'),

                            # Divider
                            Div(cls='border-t border-gray-100 mb-8'),

                            # Email section
                            H2('Email Us', cls='font-medium mb-3 text-center text-lg text-gray-700'),
                            A('info@aipetech.com',
                              href='mailto:info@aipetech.com',
                              cls='text-blue-600 hover:text-blue-800 text-xl font-medium block text-center hover:scale-105 transition-transform'
                            ),
                            cls='text-center'
                        ),
                        cls='bg-white rounded-lg shadow-lg p-10 max-w-2xl mx-auto border border-gray-100'
                    ),
                    cls='max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-center h-full'  # Added flex and height
                ),
                cls='py-20 bg-gray-50 flex-grow flex items-center'  # Added flex and items-center
            ),
            app_footer(),
            cls='min-h-screen flex flex-col'
        )
    )

if __name__ == "__main__":
    serve(host='0.0.0.0', port=8080, reload=True)