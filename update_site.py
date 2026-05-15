import datetime
import os
from bs4 import BeautifulSoup

# --- EXTENDED DUAL-PAGE DATABASE COMPILER CONFIGURATION ---
FOOTBALL_DATABASE = {
    "index.html": [
        {
            "category": "happening",
            "label": "Happening Now",
            "border_color": "border-red-500",
            "badge_bg": "bg-red-100 dark:bg-red-950",
            "badge_text": "text-red-600 dark:text-red-400",
            "title": "Lewandowski in Active Talks with Al-Hilal",
            "body": "Live reports out of Barcelona indicate club board members are reviewing a structural €100m+ package submission."
        },
        {
            "category": "going-to-happen",
            "label": "Gonna Happen",
            "border_color": "border-blue-500",
            "badge_bg": "bg-blue-100 dark:bg-blue-950",
            "badge_text": "text-blue-600 dark:text-blue-400",
            "title": "Anthony Gordon to Bayern Munich Signed Next Week",
            "body": "The Newcastle winger has finalized personal terms. Medical documentation checks are booked in Munich."
        },
        {
            "category": "will-not-happen",
            "label": "Will Not Happen",
            "border_color": "border-zinc-500",
            "badge_bg": "bg-zinc-200 dark:bg-zinc-800",
            "badge_text": "text-zinc-600 dark:text-zinc-400",
            "title": "Erling Haaland to Barcelona Link Completely Dead",
            "body": "Financial compliance restrictions confirm Barcelona will not initiate any market contact for the forward."
        }
    ],
    
    "leagues.html": [
        {
            "flag": "🏴\u200d󠁢󠁥󠁮󠁧󠁿",
            "teams": "Arsenal, Man City, Man Utd",
            "status": "Confirmed",
            "status_color": "bg-green-100 dark:bg-green-950 text-green-600 dark:text-green-400",
            "tags": "england arsenal manchester city united"
        },
        {
            "flag": "🇪🇸",
            "teams": "Barcelona, Real Madrid, Atletico",
            "status": "In Progress",
            "status_color": "bg-orange-100 dark:bg-amber-950/70 text-amber-600 dark:text-amber-400",
            "tags": "spain barcelona real madrid atletico"
        },
        {
            "flag": "🇮🇹",
            "teams": "Inter Milan, Napoli, AC Milan",
            "status": "In Progress",
            "status_color": "bg-orange-100 dark:bg-amber-950/70 text-amber-600 dark:text-amber-400",
            "tags": "italy inter milan napoli ac milan"
        },
        {
            "flag": "🇩🇪",
            "teams": "Bayern, Dortmund, Leipzig",
            "status": "In Progress",
            "status_color": "bg-orange-100 dark:bg-amber-950/70 text-amber-600 dark:text-amber-400",
            "tags": "germany bayern munich dortmund leipzig"
        }
    ]
}

def get_current_date():
    return datetime.datetime.now().strftime("%B %d, %Y")

def generate_index_node(item, soup):
    card = soup.new_tag("div", attrs={"class": f"news-card bg-white dark:bg-zinc-800 p-8 rounded-2xl border-l-8 {item['border_color']} shadow-md tracking-tight", "data-category": item['category']})
    meta = soup.new_tag("div", attrs={"class": "flex justify-between items-center"})
    date_s = soup.new_tag("span", attrs={"class": "text-xs font-bold uppercase text-zinc-400"})
    date_s.string = get_current_date()
    badge = soup.new_tag("span", attrs={"class": f"px-2.5 py-1 rounded {item['badge_bg']} {item['badge_text']} text-xs font-bold uppercase"})
    badge.string = item['label']
    meta.append(date_s); meta.append(badge); card.append(meta)
    h2 = soup.new_tag("h2", attrs={"class": "text-3xl font-extrabold mt-2 text-zinc-900 dark:text-white"}); h2.string = item['title']; card.append(h2)
    p = soup.new_tag("p", attrs={"class": "text-zinc-600 dark:text-zinc-300 mt-3 text-lg leading-relaxed"}); p.string = item['body']; card.append(p)
    return card

def generate_leagues_node(item, soup):
    li = soup.new_tag("li", attrs={"class": "team-item flex items-center justify-between p-3 rounded-xl bg-zinc-50 dark:bg-zinc-900/50 border border-zinc-100 dark:border-zinc-800", "data-team": item['tags']})
    inner_div = soup.new_tag("div", attrs={"class": "flex items-center space-x-3"})
    flag_span = soup.new_tag("span", attrs={"class": "text-2xl"}); flag_span.string = item['flag']
    txt_span = soup.new_tag("span", attrs={"class": "font-bold text-zinc-800 dark:text-white"}); txt_span.string = item['teams']
    inner_div.append(flag_span); inner_div.append(txt_span); li.append(inner_div)
    status_span = soup.new_tag("span", attrs={"class": f"px-2.5 py-0.5 text-[11px] font-black uppercase tracking-wider rounded-md {item['status_color']}"})
    status_span.string = item['status']
    li.append(status_span)
    return li

def inject_page_content(target_page, container_id, node_generator_func):
    if not os.path.exists(target_page):
        return
    try:
        with open(target_page, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        container = soup.find(id=container_id)
        if not container:
            return
        container.clear()
        for item in FOOTBALL_DATABASE[target_page]:
            node = node_generator_func(item, soup)
            container.append(node)
        with open(target_page, "w", encoding="utf-8") as f:
            f.write(soup.prettify(formatter="html"))
        print(f"Compiled content successfully for file node link: {target_page}")
    except Exception as e:
        print(f"Error handling page injection pipeline: {e}")

if __name__ == "__main__":
    # Multi-page cloud compiler pipeline routing
    inject_page_content("index.html", "news-feed", generate_index_node)
    inject_page_content("leagues.html", "leagues-feed", generate_leagues_node)
