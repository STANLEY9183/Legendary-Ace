import datetime
import os
from bs4 import BeautifulSoup

# --- HIGH DENSITY CLOUD CONTENT DATABASE MODULE ---
FOOTBALL_DATABASE = {
    "index.html": [
        # --- CATEGORY 1: WHAT IS HAPPENING RIGHT NOW ---
        {
            "category": "happening",
            "label": "Happening Now",
            "border_color": "border-red-500",
            "badge_bg": "bg-red-100 dark:bg-red-950",
            "badge_text": "text-red-600 dark:text-red-400",
            "title": "Lewandowski in Active Talks with Al-Hilal",
            "body": "Live reports out of Barcelona indicate club board members are reviewing a structural €100m+ package submission. Direct contract terms are being assessed today."
        },
        {
            "category": "happening",
            "label": "Happening Now",
            "border_color": "border-red-500",
            "badge_bg": "bg-red-100 dark:bg-red-950",
            "badge_text": "text-red-600 dark:text-red-400",
            "title": "Arsenal Launching Record Bid for Julian Alvarez",
            "body": "Negotiations have advanced. Mikel Arteta has personally spoken with the player's camp regarding key deployment variations across the frontline layout."
        },
        # --- CATEGORY 2: WHAT IS GONNA HAPPEN NEXT ---
        {
            "category": "going-to-happen",
            "label": "Gonna Happen",
            "border_color": "border-blue-500",
            "badge_bg": "bg-blue-100 dark:bg-blue-950",
            "badge_text": "text-blue-600 dark:text-blue-400",
            "title": "Anthony Gordon to Bayern Munich Signed Next Week",
            "body": "The Newcastle winger has finalized personal terms. Internal tracking reveals the medical documentation checks are booked in Munich for the upcoming weekend."
        },
        {
            "category": "going-to-happen",
            "label": "Gonna Happen",
            "border_color": "border-blue-500",
            "badge_bg": "bg-blue-100 dark:bg-blue-950",
            "badge_text": "text-blue-600 dark:text-blue-400",
            "title": "Saliba Opening Real Madrid Proposal Prepared for June",
            "body": "Sources confirm Real Madrid will submit a formal opening offer testing Arsenal's position the second the international layout calendar concludes."
        },
        # --- CATEGORY 3: WHAT WILL NOT HAPPEN ---
        {
            "category": "will-not-happen",
            "label": "Will Not Happen",
            "border_color": "border-zinc-500",
            "badge_bg": "bg-zinc-200 dark:bg-zinc-800",
            "badge_text": "text-zinc-600 dark:text-zinc-400",
            "title": "Erling Haaland to Barcelona Link Completely Dead",
            "body": "Despite constant tracking rumors circulating online, financial compliance restrictions confirm Barcelona will not initiate any market contact for the forward."
        },
        {
            "category": "will-not-happen",
            "label": "Will Not Happen",
            "border_color": "border-zinc-500",
            "badge_bg": "bg-zinc-200 dark:bg-zinc-800",
            "badge_text": "text-zinc-600 dark:text-zinc-400",
            "title": "Neymar Return to Santos Ruled Out for 26/27",
            "body": "Medical staff evaluations and existing agreement extensions confirm a South American return is mathematically impossible before the winter window."
        }
    ]
}

def get_current_date():
    return datetime.datetime.now().strftime("%B %d, %Y")

def build_article_element(item, soup):
    card_classes = f"news-card bg-white dark:bg-zinc-800 p-8 rounded-2xl border-l-8 {item['border_color']} shadow-md hover:shadow-xl dark:hover:bg-zinc-750 border border-zinc-200 dark:border-transparent transition-all duration-300 transform hover:-translate-y-1"
    card = soup.new_tag("div", attrs={"class": card_classes, "data-category": item['category']})
    
    meta_row = soup.new_tag("div", attrs={"class": "flex justify-between items-center"})
    date_span = soup.new_tag("span", attrs={"class": "text-xs font-bold uppercase tracking-widest text-zinc-400"})
    date_span.string = f"{get_current_date()}"
    
    badge_span = soup.new_tag("span", attrs={"class": f"px-2.5 py-1 rounded {item['badge_bg']} {item['badge_text']} text-xs font-bold uppercase"})
    badge_span.string = item['label']
    
    meta_row.append(date_span)
    meta_row.append(badge_span)
    card.append(meta_row)
    
    h2 = soup.new_tag("h2", attrs={"class": "text-3xl font-extrabold mt-2 text-zinc-900 dark:text-white"})
    h2.string = item['title']
    card.append(h2)
    
    p = soup.new_tag("p", attrs={"class": "text-zinc-600 dark:text-zinc-300 mt-3 text-lg leading-relaxed"})
    p.string = item['body']
    card.append(p)
    
    like_div = soup.new_tag("div", attrs={"class": "mt-6 flex items-center space-x-4 border-t border-zinc-200 dark:border-zinc-700 pt-4"})
    like_btn = soup.new_tag("button", attrs={"onclick": "toggleLike(this)", "class": "flex items-center space-x-2 text-zinc-400 hover:text-red-500 transition-colors group"})
    
    svg_soup = BeautifulSoup('<svg class="w-6 h-6 group-hover:scale-110 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>', "html.parser")
    count_span = soup.new_tag("span", attrs={"class": "text-sm font-semibold count text-zinc-600 dark:text-zinc-400"})
    count_span.string = "0"
    
    like_btn.append(svg_soup.svg)
    like_btn.append(count_span)
    like_div.append(like_btn)
    card.append(like_div)
    
    return card

def inject_page_content(target_page):
    if not os.path.exists(target_page):
        return
    try:
        with open(target_page, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        content_container = soup.find(id="news-feed")
        if not content_container:
            return

        content_container.clear()

        for item in FOOTBALL_DATABASE[target_page]:
            article_node = build_article_element(item, soup)
            content_container.append(article_node)

        with open(target_page, "w", encoding="utf-8") as f:
            f.write(soup.prettify(formatter="html"))
        print(f"Successfully compiled high-volume metrics into {target_page}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inject_page_content("index.html")
