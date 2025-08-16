class News:

    def __init__(self, tit, des, img):

        self.tit = tit
        self.des = des
        self.img = img

news1 = News(
    "iPhone 16 Pro Max",
    "The iPhone 16 Pro Max is expected to feature a larger 6.9-inch display, the powerful A18 Pro chip, a significantly upgraded camera system with a new 48MP ultra-wide lens and 5x telephoto zoom, and support for Wi-Fi 7, all while being built with a durable titanium design. It will also come with iOS 18 pre-installed. ",
    "https://raw.githubusercontent.com/Sakina-programmer/images/refs/heads/main/16-Pro-Max-Desert-Titanium-1.webp"
)

news2 = News(
    "Airpods Pro 3",
    "AirPods Pro 3 are expected to launch in September 2025, potentially alongside the iPhone 17, and are rumored to feature several hardware and software enhancements. These include improvements to audio quality, active noise cancellation, and health tracking features. ",
    "https://raw.githubusercontent.com/Sakina-programmer/images/refs/heads/main/airpod.webp"
)

news3 = News(
    "Apple Watch Ultra 3",
    "The Apple Watch Ultra 3 is expected to maintain many of the key features of its predecessor, the Ultra 2, while introducing some notable upgrades. The design, including the 49mm titanium case and sapphire crystal display, is likely to remain consistent. However, rumors suggest potential improvements like a larger display thanks to slimmer bezels, a faster S11 chip, and satellite connectivity for off-grid communication. ",
    "https://github.com/Sakina-programmer/images/blob/main/apple%20watch.jpg?raw=true"   
)

news_list = [news1, news2, news3]