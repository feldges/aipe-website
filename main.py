from fasthtml.common import *
import os
import frontmatter  # you'll need to install python-frontmatter

tailwind_css = Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css")
headers =   (Meta(name="robots", content="noindex, nofollow"),
            MarkdownJS(),
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
               A('Solutions', href='/#practical-solutions', cls='text-white hover:text-blue-200 mx-2 sm:mx-4'),
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
        H1(Span('AIPE Technology', cls='text-blue-800'), cls='text-4xl font-bold sm:text-5xl'),
        P('Intelligent Deal Screening and Due Diligence for Private Markets', cls='mt-4 text-xl text-gray-600 mb-4 max-w-2xl mx-auto'),
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

def section_challenges():
    return Section(
        Div(
            H2(
                'The Challenge',
                cls='text-3xl font-semibold text-gray-900 mb-4 text-center'
            ),
            P(
                'In private markets, analysts and investment professionals dedicate significant time to searching and consolidating information, both from online sources and internal documents. This leaves limited time for their core expertise: analyzing investment opportunities and developing investment theses.',
                cls='text-center text-gray-600 mb-4 max-w-2xl mx-auto'
            ),
            Div(
                # Content grid could be added here later if needed
                cls='grid md:grid-cols-2 gap-8'
            ),
            cls='max-w-5xl mx-auto px-4 sm:px-6 lg:px-8'
        ),
        cls='py-16'
    )

def benefit_item(text):
    # Split the text into key term and description
    parts = text.split(' - ', 1)
    key_term = parts[0]
    description = parts[1] if len(parts) > 1 else ''

    return Li(
        Div(
            # Circle container with flex-shrink-0 to prevent squeezing
            Div(
                "✓",
                cls='w-8 h-8 rounded-full bg-gradient-to-r from-blue-600 to-blue-800 flex items-center justify-center shadow-md text-white text-lg flex-shrink-0'  # Added flex-shrink-0
            ),
            # Benefit text with highlighted key term
            Div(
                Span(key_term, cls='text-blue-900 font-semibold'),
                Span(f" - {description}" if description else ""),
                cls='ml-4 text-gray-700 flex-grow'  # Added flex-grow to allow text wrapping
            ),
            cls='flex items-center py-2'
        ),
        cls='transform transition-transform duration-200 hover:translate-x-2 list-none'
    )

def solution_card(title, description, benefits):
    return Div(
        Div(
            Div(  # Inner content
                H3(title, cls='text-2xl font-semibold text-gray-900 mb-3'),
                P(description, cls='text-gray-600 mb-4 leading-relaxed'),
                H4('Key Benefits:', cls='text-lg font-medium text-gray-800 mb-2'),
                Ul(
                    *[benefit_item(benefit) for benefit in benefits],
                    cls='space-y-2'
                ),
                cls='p-6 lg:p-8 bg-white rounded-lg h-full border border-gray-200'
            ),
            # Gradient border effect
            cls='p-[1px] bg-gradient-to-b from-blue-600/20 to-blue-800/20 rounded-lg h-full'
        ),
        cls='transform transition-all duration-200 hover:scale-[1.02] h-full'
    )

def section_solutions():
    return Section(
        Div(
            H2(
                'A Practical Solution',
                cls='text-3xl font-semibold text-gray-900 mb-4 text-center'
            ),
            P(
                'This does not have to be! Modern technologies allow for much more automation than what is today\'s norm. Our solutions help you streamline your investment process with AI-powered solutions that maintain human oversight.',
                cls='text-center text-gray-600 mb-4 max-w-2xl mx-auto'
            ),
            # Solution cards grid
            Div(
                solution_card(
                    title='Deal Screening',
                    description='Our system processes multiple sources simultaneously, delivering an IC memo within minutes. '
                               'When you enter a company name, agents run in parallel, searching the internet and analyzing '
                               '100+ web pages within minutes. Then a writing agents puts it together to generate an IC memo.',
                    benefits=[
                        "Fast process - it takes only 2-3 minutes",
                        "Web search - you have access to all web pages used",
                        "IC memo - the output is an IC memo"
                    ]
                ),
                solution_card(
                    title='Due Diligence',
                    description='Past the deal screening and entering the due diligence with access to a data room: '
                               'our solution extracts data from the dataroom, develops an investment thesis, and presents '
                               'this in a professional report for the investment committee.',
                    benefits=[
                        "Transparent - you see where the data comes from",
                        "Customizable - you can use your own company template",
                        "Full control - you can steer the process, fix any intermediate issues"
                    ]
                ),
                cls='grid lg:grid-cols-2 gap-12 mt-8 max-w-6xl mx-auto'
            ),
            # New CTA section with adjusted spacing
            Div(
                Div(
                    H3('Ready to Transform Your Investment Process?', 
                       cls='text-2xl font-semibold text-center mb-4'),
                    P('Get in touch to learn how our solutions can benefit your organization.',
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
        cls='py-16 bg-gray-50', id="practical-solutions"
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
                                src='/assets/images/linkedin.svg',
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
                        A('Solutions', href='/#practical-solutions', cls='text-gray-300 hover:text-white'),
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
        cls='py-16'
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

@app.get('/')
def home():
    return Div(
        app_header(),
        section_hero(),
        section_challenges(),
        section_solutions(),
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
    serve(host='0.0.0.0', port=8080, reload=False)