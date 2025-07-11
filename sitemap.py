from datetime import datetime
import os
import frontmatter

def get_legal_doc_date(filepath):
    """Extract the last updated date from legal documents."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if '*Last updated:' in content:
                # Find the line with the date
                for line in content.split('\n'):
                    if '*Last updated:' in line:
                        # Extract date string and convert to datetime
                        date_str = line.replace('*Last updated:', '').replace('*', '').strip()
                        return datetime.strptime(date_str, '%B %d, %Y').strftime('%Y-%m-%d')
    except Exception as e:
        print(f"Warning: Could not extract date from {filepath}: {str(e)}")
    return datetime.now().strftime('%Y-%m-%d')

def sitemap():
    """Generate a sitemap.xml file with both English and German pages."""
    
    # Static pages (without language prefix)
    static_pages = [
        {'url': '', 'changefreq': 'weekly', 'priority': '1.0'},  # Home page
        {'url': 'blog', 'changefreq': 'daily', 'priority': '0.9'},
        {'url': 'about', 'changefreq': 'monthly', 'priority': '0.8'},
        {'url': 'contact', 'changefreq': 'monthly', 'priority': '0.8'},
    ]

    # Legal pages with their file paths
    legal_pages = [
        {'url': 'privacy_policy', 'file': 'assets/legal/privacy_policy.md', 'changefreq': 'monthly', 'priority': '0.5'},
        {'url': 'terms_of_service', 'file': 'assets/legal/terms_of_service.md', 'changefreq': 'monthly', 'priority': '0.5'}
    ]

    today = datetime.now().strftime('%Y-%m-%d')

    # Start XML content with hreflang namespace
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'

    # Add static pages (both English and German)
    for page in static_pages:
        # English version
        en_url = f"/{page['url']}" if page['url'] else "/"
        de_url = f"/de/{page['url']}" if page['url'] else "/de/"
        
        xml_content += f"""    <url>
        <loc>https://www.aipe.tech{en_url}</loc>
        <lastmod>{today}</lastmod>
        <changefreq>{page['changefreq']}</changefreq>
        <priority>{page['priority']}</priority>
        <xhtml:link rel="alternate" hreflang="en" href="https://www.aipe.tech{en_url}" />
        <xhtml:link rel="alternate" hreflang="de" href="https://www.aipe.tech{de_url}" />
    </url>\n"""
        
        # German version
        xml_content += f"""    <url>
        <loc>https://www.aipe.tech{de_url}</loc>
        <lastmod>{today}</lastmod>
        <changefreq>{page['changefreq']}</changefreq>
        <priority>{page['priority']}</priority>
        <xhtml:link rel="alternate" hreflang="en" href="https://www.aipe.tech{en_url}" />
        <xhtml:link rel="alternate" hreflang="de" href="https://www.aipe.tech{de_url}" />
    </url>\n"""

    # Add legal pages (both languages)
    for page in legal_pages:
        lastmod = get_legal_doc_date(page['file'])
        en_url = f"/{page['url']}"
        de_url = f"/de/{page['url']}"
        
        # English version
        xml_content += f"""    <url>
        <loc>https://www.aipe.tech{en_url}</loc>
        <lastmod>{lastmod}</lastmod>
        <changefreq>{page['changefreq']}</changefreq>
        <priority>{page['priority']}</priority>
        <xhtml:link rel="alternate" hreflang="en" href="https://www.aipe.tech{en_url}" />
        <xhtml:link rel="alternate" hreflang="de" href="https://www.aipe.tech{de_url}" />
    </url>\n"""
        
        # German version
        xml_content += f"""    <url>
        <loc>https://www.aipe.tech{de_url}</loc>
        <lastmod>{lastmod}</lastmod>
        <changefreq>{page['changefreq']}</changefreq>
        <priority>{page['priority']}</priority>
        <xhtml:link rel="alternate" hreflang="en" href="https://www.aipe.tech{en_url}" />
        <xhtml:link rel="alternate" hreflang="de" href="https://www.aipe.tech{de_url}" />
    </url>\n"""

    # Add blog posts (both languages)
    blog_dir = "Blog"
    for filename in os.listdir(blog_dir):
        if filename.endswith('.md'):
            try:
                file_path = os.path.join(blog_dir, filename)
                post = frontmatter.load(file_path)
                post_date = post.get('date').strftime('%Y-%m-%d')
                
                url_path = filename.replace('.md', '')
                en_url = f"/blog/{url_path}"
                
                # Only English version - no German since content isn't translated
                xml_content += f"""    <url>
            <loc>https://www.aipe.tech{en_url}</loc>
            <lastmod>{post_date}</lastmod>
            <changefreq>monthly</changefreq>
            <priority>0.7</priority>
            <xhtml:link rel="alternate" hreflang="en" href="https://www.aipe.tech{en_url}" />
        </url>\n"""
                
            except Exception as e:
                print(f"Warning: Error processing {filename}: {str(e)}")
                continue

    xml_content += '</urlset>'

    # Write to file
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print(f"\nSitemap written with both English and German URLs")
    print(f"File size: {os.path.getsize('sitemap.xml')} bytes")

if __name__ == "__main__":
    sitemap()