import datetime
import os
from bs4 import BeautifulSoup

# --- CONFIGURATION ---
SITE_NAME = "Legendary Ace"
TAGLINE = "legendary ace"

# Unified structured database to scale content volume infinitely
FOOTBALL_DATABASE = {
    "index.html": [
        {
            "category": "rumor",  # Matches frontend filter logic
            "label": "Transfer Rumor",
            "border_color": "border-red-500",
            "badge_bg": "bg-red-100 dark:bg-red-950",
            "badge_text": "text-red-600 dark:text-red-400",
            "title": "Arsenal's Bold Play for Julian Alvarez",
            "body": "Reports today suggest Mikel Arteta is looking to deploy Alvarez in a creative role rather than a traditional #9. PSG remains in the background with a €140m valuation."
        },
        {
            "category": "done",
            "label": "Premier League",
            "border_color": "border-blue-500",
            "badge_bg": "bg-blue-100 dark:bg-blue-950",
            "badge_text": "text-blue-600 dark:text-blue-400",
            "title": "Chelsea & Man Utd Battle for Barrenetxea",
            "body": "The Real Sociedad winger is the breakout star of the season. Scouts from London and Manchester were spotted at the Anoeta Stadium this week."
        }
    ],
    "leagues.html": [],  # Add league structures here to scale automatically
    "players.html": []   # Add player structures here to scale automatically
}

def get_current_date():
    """Generates precise date format syncing with design parameters."""
    return datetime.datetime.now().strftime("%B %d, %Y")

def build_article_element(item, soup):
    """Creates fully structured HTML nodes safely matching the interactive components."""
    # Parent article container box
    card_classes = f"news-card bg-white dark:bg-zinc-800 p-8 rounded-2xl border-l-8 {item['border_color']} shadow-md hover:shadow-xl dark:hover:bg-zinc-750 border border-zinc-200 dark:border-transparent transition-all duration-300 transform hover:-translate-y-1"
    card = soup.new_tag("div", attrs={"class": card_classes, "data-category": item['category']})
    
    # Meta layout row header
    meta_row = soup.new_tag("div", attrs={"class": "flex justify-between items-center"})
    
    date_span = soup.new_tag("span", attrs={"class": f"text-xs font-bold uppercase tracking-widest {item['badge_text'].split()[0]}"})
    date_span.string = get_current_date()
    
    badge_span = soup.new_tag("span", attrs={"class": f"px-2.5 py-1 rounded {item['badge_bg']} {item['badge_text']} text-xs font-bold uppercase"})
    badge_span.string = item['label']
    
    meta_row.append(date_span)
    meta_row.append(badge_span)
    card.append(meta_row)
    
    # Article headline text
    h2 = soup.new_tag("h2", attrs={"class": "text-3xl font-extrabold mt-2 text-zinc-900 dark:text-white"})
    h2.string = item['title']
    card.append(h2)
    
    # Article summary text body block 
    p = soup.new_tag("p", attrs={"class": "text-zinc-600 dark:text-zinc-300 mt-3 text-lg leading-relaxed"})
    p.string = item['body']
    card.append(p)
    
    # Interactive Like mechanism integration
    like_div = soup.new_tag("div", attrs={"class": "mt-6 flex items-center space-x-4 border-t border-zinc-200 dark:border-zinc-700 pt-4"})
    like_btn = soup.new_tag("button", attrs={"onclick": "toggleLike(this)", "class": "flex items-center space-x-2 text-zinc-400 hover:text-red-500 transition-colors group"})
    
    # Complete raw verified svg injection matrix
    svg_soup = BeautifulSoup('<svg class="w-6 h-6 group-hover:scale-110 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>', "html.parser")
    count_span = soup.new_tag("span", attrs={"class": "text-sm font-semibold count text-zinc-600 dark:text-zinc-400"})
    count_span.string = "0"
    
    like_btn.append(svg_soup.svg)
    like_btn.append(count_span)
    like_div.append(like_btn)
    card.append(like_div)
    
    return card

def inject_page_content(target_page):
    """Reads target files safely and parses layouts without modifying template headers."""
    if not os.path.exists(target_page):
        print(f"Skipping execution: {target_page} file target not found.")
        return

    try:
        with open(target_page, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        # Finds target element ID block structural container cleanly 
        content_container = soup.find(id="news-feed")
        if not content_container:
            print(f"Error parsing layout: id='news-feed' block target absent in {target_page}")
            return

        # Safe programmatic tree node purging cleanup loop
        content_container.clear()

        # Build and append new element node lines cleanly
        for item in FOOTBALL_DATABASE[target_page]:
            article_node = build_article_element(item, soup)
            content_container.append(article_node)

        # Write clean formatted markup output back out to static disk records
        with open(target_page, "w", encoding="utf-8") as f:
            f.write(soup.prettify(formatter="html"))
        print(f"Successfully processed fresh content updates onto target asset: {target_page}")
        
    except Exception as error:
        print(f"Execution runtime tracking error inside target build pipeline stack: {error}")

if __name__ == "__main__":
    # Injects up-to-date data modules securely to the primary landing news view
    inject_page_content("index.html")
