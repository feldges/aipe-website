from datetime import datetime
from starlette.responses import PlainTextResponse
from typing import List, Dict

def sitemap(blog_posts: List[Dict]) -> PlainTextResponse:
    """Generate sitemap XML response for the website.

    Args:
        blog_posts: List of blog post dictionaries containing url_path and date

    Returns:
        PlainTextResponse: XML response with proper content type
    """
    # Define your main routes with their properties
    main_routes = [
        {'url': '/', 'changefreq': 'weekly', 'priority': '1.0'},
        {'url': '/about', 'changefreq': 'monthly', 'priority': '0.8'},
        {'url': '/blog', 'changefreq': 'weekly', 'priority': '0.8'},
        {'url': '/contact', 'changefreq': 'monthly', 'priority': '0.7'},
        {'url': '/privacy_policy', 'changefreq': 'monthly', 'priority': '0.5'},
        {'url': '/terms_of_service', 'changefreq': 'monthly', 'priority': '0.5'}
    ]

    today = datetime.now().strftime('%Y-%m-%d')

    # Start XML content
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    # Add main routes
    for route in main_routes:
        xml_content += f"""    <url>
        <loc>https://www.aipe.tech{route['url']}</loc>
        <lastmod>{today}</lastmod>
        <changefreq>{route['changefreq']}</changefreq>
        <priority>{route['priority']}</priority>
    </url>\n"""

    # Add blog posts
    for post in blog_posts:
        post_date = post['date'].strftime('%Y-%m-%d') if hasattr(post['date'], 'strftime') else post['date']
        xml_content += f"""    <url>
        <loc>https://www.aipe.tech/blog/{post['url_path']}</loc>
        <lastmod>{post_date}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.6</priority>
    </url>\n"""

    xml_content += '</urlset>'
    return PlainTextResponse(content=xml_content, media_type="application/xml")