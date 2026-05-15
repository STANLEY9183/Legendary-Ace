import datetime

# --- CONFIGURATION ---
SITE_NAME = "Legendary Ace"
TAGLINE = "legendary ace"

def get_current_date():
    return datetime.datetime.now().strftime("%B %d, 2026")

def generate_news_content():
    """Generates original news summaries for Page 1"""
    # In a real-world scenario, you could link this to a Football API.
    # For now, it creates high-quality, original news items for May 2026.
    news = [
        {
            "category": "Transfer Rumor",
            "title": "Arsenal's Bold Play for Julian Alvarez",
            "body": "Reports today suggest Mikel Arteta is looking to deploy Alvarez in a creative role rather than a traditional #9. PSG remains in the background with a €140m valuation."
        },
        {
            "category": "Premier League",
            "title": "Chelsea & Man Utd Battle for Barrenetxea",
            "body": "The Real Sociedad winger is the breakout star of the season. Scouts from London and Manchester were spotted at the Anoeta Stadium this week."
        }
    ]
    html = ""
    for item in news:
        html += f'''
        <div class="bg-zinc-900 p-8 rounded-2xl border-l-8 border-red-600 mb-6">
            <span class="text-xs text-red-500 font-bold uppercase tracking-widest">{get_current_date()} | {item['category']}</span>
            <h2 class="text-3xl font-bold mt-2">{item['title']}</h2>
            <p class="text-zinc-400 mt-3 text-lg">{item['body']}</p>
        </div>'''
    return html

def update_index_page():
    """Updates index.html with fresh news"""
    news_html = generate_news_content()
    
    # This reads your existing file and injects the new news
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        skip = False
        for line in lines:
            if 'id="news-container"' in line:
                new_lines.append(line)
                new_lines.append(news_html)
                skip = True
            elif 'id="end-news-container"' in line:
                skip = False
                new_lines.append(line)
            elif not skip:
                new_lines.append(line)

        with open("index.html", "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print("Successfully updated News on index.html")
    except Exception as e:
        print(f"Error updating index.html: {e}")

if __name__ == "__main__":
    update_index_page()
    # You can add similar functions for leagues.html and players.html here!
